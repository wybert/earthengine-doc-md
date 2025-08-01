 
#  Processing Environments
Stay organized with collections  Save and categorize content based on your preferences. 
Earth Engine has different environments for processing data: _interactive_ and _batch_. These two environments (or "realms") handle different types of queries and have very different performance characteristics, so it's important to understand when and how to use each.
**Note:** Project-level request limits apply to both interactive and batch processing requests. See the [Earth Engine quotas](https://developers.google.com/earth-engine/guides/usage) page.
## Interactive environment
**Key Term:** _Interactive_ - run computations synchronously and include the output directly in the response.
Also called the "synchronous" or "online" stack, this environment is optimized for answering small requests which finish quickly (responses are limited to tens of megabytes of data and must finish processing within five minutes). Many requests can be made in parallel up to the [quota limits](https://developers.google.com/earth-engine/guides/usage).
### Endpoints
The interactive environment is composed of different API endpoints: _standard_ and _high volume_.
#### Standard endpoint
The standard endpoint is appropriate for most human-driven usage, and it's what powers the Code Editor and Earth Engine Apps. Specifically, this endpoint is best suited for latency-sensitive applications which involve a low volume of concurrent, non-programmatic requests.
#### High-volume endpoint
The high-volume endpoint is designed to handle a higher volume of requests in parallel than the standard endpoint. Key differences include:
  * **Higher latency** : The high-volume endpoint has higher average latency per request.
  * **Less caching** : It provides less caching of intermediate results, so complex queries may require more compute time.
  * **Best for automated, small queries** : The high-volume endpoint excels at handling many programmatic requests, but is most suitable for simple queries that don't require aggregation (like fetching tiles from prebuilt images).


For complex analyses that need efficient caching, the standard API endpoint may be preferable. The high-volume endpoint is optimized for high-throughput, low-computation tasks. Complex queries typically require more [EECU-time](https://developers.google.com/earth-engine/guides/computation_overview#eecus) when using the high-volume endpoint than they do in the regular online endpoint.
##### Use of the high-volume endpoint
### Python client
When initializing the `earthengine` library, pass in an `opt_url` parameter and set it to `https://earthengine-highvolume.googleapis.com`. As always, be sure to also pass in proper credentials and specify the Cloud project. For example:
```
ee.Initialize(
    credentials=credentials,
    project='my-project',
    opt_url='https://earthengine-highvolume.googleapis.com'
)

```

### JavaScript client
When initializing the `earthengine` library using [`ee.initialize()`](https://developers.google.com/earth-engine/apidocs/ee-initialize), pass `https://earthengine-highvolume.googleapis.com` for the first parameter.
### REST API
Direct your REST requests to `https://earthengine-highvolume.googleapis.com` (instead of `https://earthengine.googleapis.com`, as shown in the [REST API Quickstart](https://developers.google.com/earth-engine/reference/Quickstart#accessing-and-testing-your-credentials), for example).
## Batch environment
**Key Term:** _Batch_ - run computations asynchronously and output results for later access (in Google Cloud Storage, the Earth Engine asset store, etc.).
Also called the "asynchronous" or "offline" stack, this environment is optimized for high-latency parallel processing of large amounts of data. Requests are submitted as tasks to batch processing endpoints, usually by calling data [import](https://developers.google.com/earth-engine/guides/image_upload) or [export](https://developers.google.com/earth-engine/guides/exporting) functions (e.g., `Export.*` and `ee.batch.*`) from the Earth Engine client libraries. Each batch task has a maximum lifetime of ten days. Each project supports [up to 3000 pending tasks](https://developers.google.com/earth-engine/guides/usage#task_queue_length), but each individual user is limited to a small number of [concurrently running tasks](https://developers.google.com/earth-engine/guides/usage#concurrent_batch_tasks).
### Task lifecycle
Tasks are submitted to a queue and ordered by their priority (highest first) and submission time (earliest first). Tasks change from the `SUBMITTED` (queued) state to the `RUNNING` state when they're assigned to a _batch processor_. Each processor is responsible for orchestrating a varying number of _batch workers_ to run the computation and produce the task's results. The number of workers for a task is determined by the EE service's ability to parallelize the job and is not user-configurable.
When using a Cloud project, tasks are visible to anyone with the project-level permission to list tasks. If the project is [registered](https://developers.google.com/earth-engine/guides/access#a-role-in-a-cloud-project) for paid Earth Engine access, tasks are organized in a project-wide queue; if the project is registered for unpaid (research) access, tasks are scheduled independently for each individual but still visible across users of the project.
Tasks complete successfully when they create the necessary artifacts (Earth Engine assets, files in Google Cloud Storage, etc.).
### Task management
Tasks can be viewed and cancelled using the following interfaces:
  * [Tasks page in the Cloud Console](https://console.cloud.google.com/earth-engine/tasks)
    * Enables task management at the Cloud project level. Going forward, this is the main user interface for managing tasks.
  * [Task Manager page](https://code.earthengine.google.com/tasks)
    * This interface shows tasks at the user and project level, and supports filtering by task name.
  * [Code Editor Tasks Tab](https://developers.google.com/earth-engine/guides/playground#tasks-tab)
    * Allows for monitoring tasks alongside a Code Editor script.
  * [`ListOperations` endpoint](https://developers.google.com/earth-engine/apidocs/ee-data-listoperations) and [`task` command](https://developers.google.com/earth-engine/guides/command_line#task)
    * Best for programmatically viewing and managing tasks.


### Task failures
If a task fails for a reason which won't be fixed by retrying (e.g., the data are invalid), the task will be marked as `FAILED` and won't be run again.
If a task fails for a reason which could be intermittent (e.g., it timed out when running a computation), Earth Engine will automatically attempt to retry it and populate the `retries` field. Tasks can fail up to five times, and the final failure will cause the entire task to be marked as `FAILED`.
### Task ID
Each task has an alphanumeric ID of the form `3DNU363IM57LNU4SDTMB6I33`. These can be viewed or obtained through our [task management](https://developers.google.com/earth-engine/guides/processing_environments#task_management) interfaces. If you are starting tasks programmatically, you get the task ID from [`ee.data.newTaskId`](https://developers.google.com/earth-engine/apidocs/ee-data-newtaskid). When requesting help to debug an export or ingestion task, provide this task ID as a copyable string (not a screenshot).
### List of task states
Tasks can have the following `state` values:
  * `UNSUBMITTED`, still pending on the client
  * `READY`, queued on the server
  * `RUNNING`, currently running
  * `COMPLETED`, completed successfully
  * `FAILED`, completed unsuccessfully
  * `CANCEL_REQUESTED`, still running but has been requested to be cancelled (i.e., not a guarantee that the task will be cancelled)
  * `CANCELLED`, cancelled by the owner


### Task priority
Task priority is a mechanism for controlling the order of tasks in the queue. Higher priority tasks get scheduled before other pending tasks with lower priorities, regardless of their submission time. The default task priority is 100.
The ability to set other priorities (higher or lower) on export tasks is only available for users of [projects that are registered for paid Earth Engine access](https://developers.google.com/earth-engine/guides/access#a-role-in-a-cloud-project). Changing the priority of an export task doesn't affect how it's scheduled relative to any import tasks, since the two types of tasks are scheduled separately.
#### Example: using task priorities
Consider the following task list, where tasks 1-5 are submitted in their natural order with the default priority. They run in the order they were submitted, since the priorities are all the same, and, since [two batch processing slots](https://developers.google.com/earth-engine/guides/usage#concurrent_batch_tasks) are available for this project, two run concurrently (the first and second submitted).
```
Task name           State      Priority
---------------------------------------
MyDefaultTask5      READY      100
MyDefaultTask4      READY      100
MyDefaultTask3      READY      100
MyDefaultTask2      RUNNING    100
MyDefaultTask1      RUNNING    100

```

Submitting a new task, `MyHighPriorityTask1`, won't affect the running tasks:
```
Task name           State      Priority
---------------------------------------
MyHighPriorityTask    READY      500
MyDefaultTask5        READY      100
MyDefaultTask4        READY      100
MyDefaultTask3        READY      100
MyDefaultTask2        RUNNING    100
MyDefaultTask1        RUNNING    100

```

After one of the running tasks completes, the pending task with the highest priority will run (in this case, our high-priority task):
```
Task name             State      Priority
-----------------------------------------
MyHighPriorityTask    RUNNING    500
MyDefaultTask5        READY      100
MyDefaultTask4        READY      100
MyDefaultTask3        READY      100
MyDefaultTask2        COMPLETED  100
MyDefaultTask1        RUNNING    100

```

