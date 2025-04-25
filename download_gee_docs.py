"""
Google Earth Engine Documentation Downloader

This script downloads documentation from Google Earth Engine's website and converts it to markdown format.
It creates a directory structure that mirrors the URL paths from the base Earth Engine documentation.
"""

import requests
from bs4 import BeautifulSoup
import asyncio
import os
import re
import json
from crawl4ai import AsyncWebCrawler
import numpy as np
from urllib.parse import urljoin, urlparse
from datetime import datetime
from typing import Dict, List, Tuple, NamedTuple
import aiohttp
from pathlib import Path

# Constants
DOCS_DIR = "docs"
BASE_URL = "https://developers.google.com/earth-engine"
BASE_URLS = [
    f"{BASE_URL}/apidocs",
    f"{BASE_URL}/guides",
    f"{BASE_URL}/tutorials"
]
PROGRESS_FILE = "download_progress.json"

# Concurrency settings
MAX_CONCURRENT_DOWNLOADS = 5
BATCH_SIZE = 10
RATE_LIMIT = 1.0

class PageTask(NamedTuple):
    """Represents a page download task."""
    url: str
    relative_path: str
    filename: str

class DownloadStats(NamedTuple):
    """Statistics for download progress."""
    total: int
    success: int
    errors: int
    elapsed_time: float
    remaining: int

def get_timestamp() -> str:
    """Get current timestamp in ISO format."""
    return datetime.now().isoformat()

def load_progress() -> Dict:
    """Load download progress from JSON file."""
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_progress(url: str, status: str, filename: str) -> None:
    """Save download progress to JSON file."""
    progress = load_progress()
    progress[url] = {
        "status": status,
        "filename": filename,
        "timestamp": get_timestamp()
    }
    with open(PROGRESS_FILE, 'w') as f:
        json.dump(progress, f, indent=2)

def get_relative_path(url: str) -> str:
    """
    Get the relative path from the base Earth Engine URL.
    Example: 
    https://developers.google.com/earth-engine/guides/image_visualization 
    becomes: guides/image_visualization
    """
    parsed = urlparse(url)
    path = parsed.path
    
    # Remove the base path
    base_path = urlparse(BASE_URL).path
    if path.startswith(base_path):
        path = path[len(base_path):].lstrip('/')
    
    return path

def create_file_path(url: str) -> Tuple[str, str]:
    """
    Create directory path and filename from URL.
    Returns (directory_path, filename)
    """
    relative_path = get_relative_path(url)
    path_parts = relative_path.split('/')
    
    # Last part becomes the filename, rest is the directory path
    if len(path_parts) > 1:
        dir_path = os.path.join(DOCS_DIR, *path_parts[:-1])
        filename = path_parts[-1]
    else:
        dir_path = DOCS_DIR
        filename = relative_path
    
    # Clean filename
    if not filename:
        filename = 'index'
    filename = re.sub(r'[^\w_.-]', '_', filename)
    if not filename.endswith('.md'):
        filename += '.md'
        
    return dir_path, filename

def ensure_directory(dir_path: str) -> None:
    """Ensure directory exists, create if it doesn't."""
    os.makedirs(dir_path, exist_ok=True)

def process_markdown_content(content: str) -> str:
    """Process the markdown content by removing unnecessary parts."""
    return content.split("Send feedback")[1]

def save_markdown_file(filepath: str, content: str) -> None:
    """Save markdown content to a file."""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

def print_batch_progress(stats: DownloadStats, batch_num: int, batch_size: int, batch_time: float) -> None:
    """Print progress information for the current batch."""
    print("\n=== Download Progress ===")
    print(f"Batch {batch_num}: Processed {batch_size} URLs")
    print(f"Total Progress: {stats.total} URLs processed ({stats.remaining} remaining)")
    print(f"Success: {stats.success}, Errors: {stats.errors}")
    print(f"Total Time: {stats.elapsed_time:.1f}s (This batch: {batch_time:.1f}s)")
    if stats.total > 0:
        print(f"Average Time per URL: {stats.elapsed_time/stats.total:.2f}s")
        print(f"Estimated time remaining: {(stats.elapsed_time/stats.total) * stats.remaining:.1f}s")
    print("=" * 25)

def print_final_statistics(stats: DownloadStats) -> None:
    """Print final download statistics."""
    print("\n=== Final Statistics ===")
    print(f"Total URLs Processed: {stats.total}")
    print(f"Successful Downloads: {stats.success}")
    print(f"Failed Downloads: {stats.errors}")
    print(f"Total Time: {stats.elapsed_time:.1f}s ({stats.elapsed_time/60:.1f}min)")
    if stats.success > 0:
        print(f"Average Time per Successful Download: {stats.elapsed_time/stats.success:.2f}s")
    print("=" * 25)

async def collect_urls(session: aiohttp.ClientSession, base_url: str) -> List[PageTask]:
    """
    Collect all URLs from a section that need to be processed.
    
    Args:
        session: aiohttp client session
        base_url: The base URL of the section
        
    Returns:
        List of PageTask objects
    """
    tasks = []
    try:
        print(f"\nCollecting URLs from: {base_url}")
        async with session.get(base_url) as response:
            response.raise_for_status()
            soup = BeautifulSoup(await response.text(), 'html.parser')

        nav = soup.find('nav', class_='devsite-book-nav devsite-nav nocontent')
        if not nav:
            print(f"Warning: Navigation not found for {base_url}")
            return tasks

        links = nav.find_all('a', {"class": "devsite-nav-title", "track-type": "bookNav"})
        print(f"Found {len(links)} links in section: {urlparse(base_url).path}")

        # Add the base URL itself as a task
        dir_path, filename = create_file_path(base_url)
        tasks.append(PageTask(base_url, dir_path, filename))

        for link in links:
            href = link.get('href')
            if not href or href.startswith(('http://', 'https://')):
                continue

            full_url = urljoin(base_url, href)
            dir_path, filename = create_file_path(full_url)
            tasks.append(PageTask(full_url, dir_path, filename))

    except Exception as e:
        print(f"Error collecting URLs from {base_url}: {str(e)}")

    return tasks

async def process_single_url(
    crawler: AsyncWebCrawler,
    task: PageTask,
    semaphore: asyncio.Semaphore,
    last_request_times: Dict[str, float],
    request_lock: asyncio.Lock
) -> bool:
    """Process a single URL and return whether it was successful."""
    async with semaphore:
        # Rate limiting
        domain = urlparse(task.url).netloc
        async with request_lock:
            now = datetime.now().timestamp()
            if domain in last_request_times:
                time_since_last = now - last_request_times[domain]
                if time_since_last < RATE_LIMIT:
                    await asyncio.sleep(RATE_LIMIT - time_since_last)
            last_request_times[domain] = now

        try:
            print(f"Downloading: {task.url}")
            result = await crawler.arun(url=task.url)
            
            markdown_content = process_markdown_content(result.markdown)
            
            # Ensure directory exists
            ensure_directory(task.relative_path)
            filepath = os.path.join(task.relative_path, task.filename)
            
            save_markdown_file(filepath, markdown_content)
            save_progress(task.url, "success", task.filename)
            print(f"Successfully saved: {filepath}")
            return True
            
        except Exception as e:
            print(f"Error processing {task.url}: {str(e)}")
            save_progress(task.url, "error", task.filename)
            return False

async def process_batch(
    tasks: List[PageTask],
    crawler: AsyncWebCrawler,
    batch_num: int,
    semaphore: asyncio.Semaphore,
    last_request_times: Dict[str, float],
    request_lock: asyncio.Lock,
    total_remaining: int
) -> Tuple[int, int, float]:
    """
    Process a batch of pages concurrently.
    Returns (success_count, error_count, batch_time)
    """
    print(f"\nStarting batch {batch_num} with {len(tasks)} tasks...")
    print(f"Total remaining URLs: {total_remaining}")
    batch_start = datetime.now()

    results = await asyncio.gather(*[
        process_single_url(crawler, task, semaphore, last_request_times, request_lock)
        for task in tasks
    ])
    
    success_count = sum(1 for r in results if r)
    error_count = sum(1 for r in results if not r)
    
    batch_time = (datetime.now() - batch_start).total_seconds()
    return success_count, error_count, batch_time

async def download_all_docs() -> None:
    """Main function to download all documentation."""
    print("Starting Google Earth Engine Documentation Downloader...")
    print(f"Base URL: {BASE_URL}")
    print("Files will be organized following the URL directory structure")
    
    start_time = datetime.now()
    
    # Initialize concurrency controls
    semaphore = asyncio.Semaphore(MAX_CONCURRENT_DOWNLOADS)
    last_request_times: Dict[str, float] = {}
    request_lock = asyncio.Lock()
    
    total_success = 0
    total_errors = 0
    
    async with aiohttp.ClientSession() as session:
        async with AsyncWebCrawler() as crawler:
            # Collect all URLs first
            all_tasks = []
            for base_url in BASE_URLS:
                tasks = await collect_urls(session, base_url)
                all_tasks.extend(tasks)

            total_urls = len(all_tasks)
            print(f"\nTotal URLs to process: {total_urls}")

            # Process URLs in batches
            for i in range(0, len(all_tasks), BATCH_SIZE):
                batch = all_tasks[i:i + BATCH_SIZE]
                batch_num = (i // BATCH_SIZE) + 1
                remaining = total_urls - (i + len(batch))
                
                success, errors, batch_time = await process_batch(
                    batch, crawler, batch_num, semaphore, last_request_times, request_lock, remaining
                )
                
                total_success += success
                total_errors += errors
                
                elapsed_time = (datetime.now() - start_time).total_seconds()
                stats = DownloadStats(
                    total=total_success + total_errors,
                    success=total_success,
                    errors=total_errors,
                    elapsed_time=elapsed_time,
                    remaining=remaining
                )
                
                print_batch_progress(stats, batch_num, len(batch), batch_time)
            
            # Print final statistics
            final_time = (datetime.now() - start_time).total_seconds()
            final_stats = DownloadStats(
                total=total_success + total_errors,
                success=total_success,
                errors=total_errors,
                elapsed_time=final_time,
                remaining=0
            )
            print_final_statistics(final_stats)

if __name__ == "__main__":
    # Create base directory
    os.makedirs(DOCS_DIR, exist_ok=True)
    asyncio.run(download_all_docs())
