 
#  GCOM-C/SGLI L3 Sea Surface Temperature (V3) 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![JAXA/GCOM-C/L3/OCEAN/SST/V3](https://developers.google.com/earth-engine/datasets/images/JAXA/JAXA_GCOM-C_L3_OCEAN_SST_V3_sample.png) 

Dataset Availability
    2018-01-22T00:00:00Z–2025-04-19T00:00:00Z 

Dataset Provider
     [ Global Change Observation Mission (GCOM) ](https://suzaku.eorc.jaxa.jp/GCOM/index.html) 

Earth Engine Snippet
     `    ee.ImageCollection("JAXA/GCOM-C/L3/OCEAN/SST/V3")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/JAXA/JAXA_GCOM-C_L3_OCEAN_SST_V3) 

Cadence
    1 Day 

Tags
     [climate](https://developers.google.com/earth-engine/datasets/tags/climate) [g-portal](https://developers.google.com/earth-engine/datasets/tags/g-portal) [gcom](https://developers.google.com/earth-engine/datasets/tags/gcom) [gcom-c](https://developers.google.com/earth-engine/datasets/tags/gcom-c) [jaxa](https://developers.google.com/earth-engine/datasets/tags/jaxa) [ocean](https://developers.google.com/earth-engine/datasets/tags/ocean) [oceans](https://developers.google.com/earth-engine/datasets/tags/oceans) [sea-surface-temperature](https://developers.google.com/earth-engine/datasets/tags/sea-surface-temperature) [sst](https://developers.google.com/earth-engine/datasets/tags/sst)
[Description](https://developers.google.com/earth-engine/datasets/catalog/JAXA_GCOM-C_L3_OCEAN_SST_V3#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/JAXA_GCOM-C_L3_OCEAN_SST_V3#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/JAXA_GCOM-C_L3_OCEAN_SST_V3#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/JAXA_GCOM-C_L3_OCEAN_SST_V3#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/JAXA_GCOM-C_L3_OCEAN_SST_V3#citations) More
This product is the temperature of sea surface.
This is an ongoing dataset with a latency of 3-4 days.
GCOM-C conducts long-term and continuous global observation and data collection to elucidate the mechanism behind fluctuations in radiation budget and carbon cycle needed to make accurate projections regarding future temperature rise. At the same time, cooperating with research institutions having a climate numerical model, it contributes to reduction of errors in temperature rise prediction derived from the climate numerical model and improvement of accuracy of prediction of various environmental changes. SGLI mounted on GCOM-C is the succession sensor of the Global Imager (GLI) mounted on ADEOS-II (MIDORI II) and is the Imaging Radiometer which measures the radiation from near-ultraviolet to thermal infrared region (380 nm-12 um) in 19 channels. Global observation of once for approximately every two days is possible at mid-latitude near Japan by observation width at ground greater than 1,000 km. In addition, SGLI realizes high resolution than the similar global sensor and has a polarized observation function and a multi-angle observation function.
**Pixel Size** 4638.3 meters 
**Bands**
Name | Units | Min | Max | Description  
---|---|---|---|---  
`SST_AVE` | °C |  0*  |  65531*  | Temperature of sea surface.  
`SST_QA_flag` | SST QA  
Bitmask for SST_QA_flag
  * Bits 0-1: Terrain type 
    * 0: water(land fraction = 0%)
    * 1: mostly water(0% < land fraction < 50%)
    * 2: mostly coastal(50% < land fraction < 100%)
    * 3: land(land fraction = 100%)
  * Bits 2-3: Terrain type 
    * 0: day (night fraction = 0%)
    * 1: mostly day (0% < night fraction < 50%)
    * 2: mostly night (50% < night fraction < 100%)
    * 3: night (night fraction = 100%)

  
* estimated min or max value 
**Image Properties**
Name | Type | Description  
---|---|---  
ALGORITHM_VERSION | STRING | Algorithm version  
GRID_INTERVAL | STRING | Spatial resolution  
GRID_INTERVAL_UNIT | STRING | Unit of GRID_INTERVAL  
IMAGE_END_TIME | STRING | Image acquisition end time  
IMAGE_START_TIME | STRING | Image acquisition start time  
PROCESSING_RESULT | STRING | Good, Fair, Poor, NG  
PROCESSING_UT | STRING | Processing time  
PRODUCT_FILENAME | STRING | Source filename  
PRODUCT_VERSION | STRING | Product version  
SATELLITE_DIRECTION | STRING | Satellite orbit direction
  * A: Nighttime data
  * D: Daytime data

  
SST_AVE_OFFSET | STRING | Offset  
SST_AVE_SLOPE | STRING | Slope  
**Terms of Use**
This dataset is free to use without any restrictions (including commercial use). Anyone wishing to publish analyzed results or value added data products should properly credit the original G-Portal data, e.g., "PR data by Japan Aerospace Exploration Agency". For value added data products, please indicate the credit of the original G-Portal data, e.g., "Original data for this value added data product was provided by Japan Aerospace Exploration Agency."
See [G-Portal's terms of service (Article 7)](https://gportal.jaxa.jp/gpr/index/eula?lang=en) for additional information.
Citations:
  * Kurihara, Y. (Jun. 2020). GCOM-C/SGLI Sea Surface Temperature (SST) ATBD (Version 2). Retrieved from <https://suzaku.eorc.jaxa.jp/GCOM_C/data/ATBD/ver2/V2ATBD_O1AB_SST_Kurihara_r1.pdf>


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/JAXA_GCOM-C_L3_OCEAN_SST_V3#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('JAXA/GCOM-C/L3/OCEAN/SST/V3')
.filterDate('2021-12-01','2022-01-01')
// filter to daytime data only
.filter(ee.Filter.eq('SATELLITE_DIRECTION','D'));
// Multiply with slope coefficient and add offset
vardataset=dataset.mean().multiply(0.0012).add(-10);
varvis={
bands:['SST_AVE'],
min:0,
max:30,
palette:['000000','005aff','43c8c8','fff700','ff0000'],
};
Map.setCenter(128.45,33.33,5);
Map.addLayer(dataset,vis,'Sea Surface Temperature');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/JAXA/JAXA_GCOM-C_L3_OCEAN_SST_V3)
[ GCOM-C/SGLI L3 Sea Surface Temperature (V3) ](https://developers.google.com/earth-engine/datasets/catalog/JAXA_GCOM-C_L3_OCEAN_SST_V3)
This product is the temperature of sea surface. This is an ongoing dataset with a latency of 3-4 days. GCOM-C conducts long-term and continuous global observation and data collection to elucidate the mechanism behind fluctuations in radiation budget and carbon cycle needed to make accurate projections regarding future temperature rise. …
JAXA/GCOM-C/L3/OCEAN/SST/V3, climate,g-portal,gcom,gcom-c,jaxa,ocean,oceans,sea-surface-temperature,sst 
2018-01-22T00:00:00Z/2025-04-19T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://suzaku.eorc.jaxa.jp/GCOM/index.html)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/JAXA_GCOM-C_L3_OCEAN_SST_V3)


