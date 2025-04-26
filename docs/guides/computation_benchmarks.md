 
#  Computation Benchmarks 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Methodology](https://developers.google.com/earth-engine/guides/computation_benchmarks#methodology)
    * [Notebooks](https://developers.google.com/earth-engine/guides/computation_benchmarks#notebooks)
    * [Operation](https://developers.google.com/earth-engine/guides/computation_benchmarks#operation)
    * [Processing](https://developers.google.com/earth-engine/guides/computation_benchmarks#processing)
    * [Region](https://developers.google.com/earth-engine/guides/computation_benchmarks#region)
    * [Scale](https://developers.google.com/earth-engine/guides/computation_benchmarks#scale)
    * [Timeframe](https://developers.google.com/earth-engine/guides/computation_benchmarks#timeframe)
    * [Samples](https://developers.google.com/earth-engine/guides/computation_benchmarks#samples)
  * [How to use these data](https://developers.google.com/earth-engine/guides/computation_benchmarks#how_to_use_these_data)
    * [Caveats](https://developers.google.com/earth-engine/guides/computation_benchmarks#caveats)
  * [Benchmark data](https://developers.google.com/earth-engine/guides/computation_benchmarks#benchmark_data)


To help model potential Earth Engine compute costs, we've run a number of benchmark operations and logged their corresponding compute footprint. These data may be useful for modeling compute costs for your own processing, based on similar criteria (see ["how to use these data"](https://developers.google.com/earth-engine/guides/computation_benchmarks#how_to_use_these_data)).
## Methodology
### Notebooks
We use a [Colab notebook to generate these measurements](https://github.com/google/earthengine-community/blob/master/guides/linked/Earth_Engine_benchmarking_toolkit.ipynb), and another to [parse the results from Cloud Monitoring](https://github.com/google/earthengine-community/tree/master/guides/linked/cloud-monitoring).
### Operation
Included here are a set of common Earth Engine operations.
  * **Export image** is a raster image export using the `Export.image.toCloudStorage()` batch processing function. This is often used to export large numbers of pixels to Cloud Storage.
  * **Export to BigQuery** samples points from a raster and writes it to Google BigQuery using the `Export.table.toBigQuery()` batch processing function. Writing to BigQuery enables both analysis in BigQuery as well as use in other tools and services that integrate with BigQuery (like [Looker Studio](https://lookerstudio.google.com/)).
  * **High-volume extraction** downloads 256x256 patches of imagery around a number of points. This is common for machine learning workflows that use training and inference on small patches of pixels.


### Processing
This field shows which pixel-processing pipeline was used to generate a given result. All of these operations fundamentally involve a raster image (either exporting it directly, sampling it with geometries, or extracting patches), and the 'processing' option describes the mechanism for generating the pixels in that raster.
The only option is "Sentinel-2 mosaic", though this page may be updated to show benchmarks involving different processing options in the future. The Sentinel-2 mosaic is constructed using a filtering and compositing algorithm on top of Sentinel-2 data for the relevant timeframe, resolution, etc. - the specific parameters and operations are described in [the measurement notebook](https://github.com/google/earthengine-community/blob/master/guides/linked/Earth_Engine_benchmarking_toolkit.ipynb). Sentinel-2 compositing is a very common first step or intermediate data product, though the specific parameters (like cloud cover percentage) vary.
### Region
The regions used here are:
  * **Bay Area** : a simple `ee.Geometry.Rectangle` around the San Francisco Bay area. This is interesting because it contains both land and ocean pixels, so not all areas are covered by Sentinel-2 imagery. 
Area (approx) | Dimensions at 10 m/pixel | Dimensions at 30 m/pixel | Dimensions at 120 m/pixel  
---|---|---|---  
22779 km² | [21342,13554]2.9E8 pixels | [7114x4518]3.2E7 pixels | [1779x1130]2010270 pixels  
  * **Nigeria** : The bounds of Nigeria from the [simplified LSIB dataset](https://developers.google.com/earth-engine/datasets/catalog/USDOS_LSIB_SIMPLE_2017). This is the largest region, and is interesting because it's both a cloudy region (meaning that there are fewer cloud-free pixels) and it's close to the equator (meaning that it gets relatively fewer visits from polar-orbit satellites like Sentinel-2). 
Area (approx) | Dimensions at 10 m/pixel | Dimensions at 30 m/pixel | Dimensions at 120 m/pixel  
---|---|---|---  
912554 km² | [133595x107035]1.4E10 pixels | [44532x35679]1.6E9 pixels | [11133x8920]9.9E7 pixels  
  * **Germany** : The bounds of Germany from the [simplified LISB dataset](https://developers.google.com/earth-engine/datasets/catalog/USDOS_LSIB_SIMPLE_2017). It's more affected by seasonality than the other regions. 
Area (approx) | Dimensions at 10 m/pixel | Dimensions at 30 m/pixel | Dimensions at 120 m/pixel  
---|---|---|---  
356077 km² | [102130x86666]8.9E9 pixels | [34044x28889]9.8E8 pixels | [8511x7223]6.1E7 pixels  


For more info about the regions, see [a view of the regions in the Code Editor](https://code.earthengine.google.com/5c92dff15500c1c541fe7e944fc31aae).
### Scale
All pixel computation happens within a grid (for example, when creating a mosaic to sample). The scale set here controls the size of the pixels in meters at the projection's point of true scale.
Using larger values of 'scale' corresponds to lower resolution, so, for example, increasing 'scale' reduces the number of pixels in an image export for a region.
### Timeframe
Each of the operations performs a compositing step on the underlying dataset. The timeframe listed here is the total calendar time that's considered when filtering the dataset (more time typically means more data).
The specific times here are the three-month, six-month and one-year periods before 2024-01-01.
### Samples
The number of samples has different interpretations based on the operation.
  * When exporting tabular data to BigQuery, it's the number of random points that are sampled from the dataset and exported. Framed another way, this is the number of rows in the final BigQuery dataset.
  * When exporting TFRecord patches using the high-volume API endpoint, it's the total number of 256x256 pixel regions that are sampled from random points within the region of interest. Note that patches can overlap with this methodology.
  * For image exports, the sample count is listed as "N/A" here, since they don't really "sample" in the typical sense (every pixel value is computed). One can think of image exports as a grid of samples, where the sample count is the number of pixels in the result.


## How to use these data
These example measurements are provided for illustration only. They're intended to provide real-world examples of Earth Engine performance and EECU-time costs, but they're not guarantees - see the ["Caveats" section](https://developers.google.com/earth-engine/guides/computation_benchmarks#caveats) for more details.
To generate samples using your own processing workflows, use the two notebooks in the ["Notebooks" section](https://developers.google.com/earth-engine/guides/computation_benchmarks#notebooks). With those, it's possible to generate a number of measurements for any custom code and read and aggregate the results from Cloud Monitoring.
**Caution:** Depending on the operation, it may be expensive to run. Always try with small regions and trimmed-down examples first!
### Caveats
Caching affects these results, but using a random seed (the `RANDOM_SEED` in the [Measurement notebook](https://github.com/google/earthengine-community/blob/master/guides/linked/Earth_Engine_benchmarking_toolkit.ipynb)) helps to skip cached results as much as possible, making the values more consistent between runs. This technique isn't perfect, however, since there are some caches that are outside of direct user control (e.g., caches for image tiles).
The state of the data catalog also affects these results, since the underlying collections can change, get reprocessed, or have new data backfilled, among other changes.
Additionally, the level of activity from all users of the Earth Engine serving infrastructure can also play a part. More system-wide usage of the cache or other users running similar computations may affect the EECU-time for your results.
## Benchmark data
These are real benchmarks (the actual cost to run as of 2024-03-08), but they provide no guarantee - actual compute costs can [vary significantly](https://developers.google.com/earth-engine/guides/computation_overview#stability_and_predictability).
The cost of an EECU-hour of processing can have different costs (in USD or EUR, for example) depending on the specific [pricing plan](https://cloud.google.com/earth-engine/pricing) and currency conversion in Google Cloud Billing.
Export image Export to BigQuery High-volume extraction
Select one or more optionsOperation
  * Export image
  * Export to BigQuery
  * High-volume extraction


Sentinel-2 composite
Select one or more optionsProcessing
  * Sentinel-2 composite


Bay Area Germany Nigeria
Select one or more optionsLocation
  * Bay Area
  * Germany
  * Nigeria


10 meter 30 meter 120 meter
Select one or more optionsProcessing scale
  * 10 meter
  * 30 meter
  * 120 meter


3 months 6 months 12 months
Select one or more optionsTimeframe
  * 3 months
  * 6 months
  * 12 months


N/A 100 samples 500 samples 1000 samples
Select one or more optionsSamples
  * N/A
  * 100 samples
  * 500 samples
  * 1000 samples


A note about Earth Engine benchmarks.
Operation | Processing | Region | Scale | Timeframe | Samples | Compute benchmark  
---|---|---|---|---|---|---  
Export image | Sentinel-2 composite | Bay Area | 10 meters | 12 months | N/A | 105.09 [EECU-hours](https://developers.google.com/earth-engine/guides/computation_overview#eecus)  
Export image | Sentinel-2 composite | Bay Area | 10 meters | 6 months | N/A | 41.53 [EECU-hours](https://developers.google.com/earth-engine/guides/computation_overview#eecus)  
Export image | Sentinel-2 composite | Bay Area | 10 meters | 3 months | N/A | 29.95 [EECU-hours](https://developers.google.com/earth-engine/guides/computation_overview#eecus)  
