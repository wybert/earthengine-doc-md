 
#  GCOM-C/SGLI L3 Leaf Area Index (V1) 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![JAXA/GCOM-C/L3/LAND/LAI/V1](https://developers.google.com/earth-engine/datasets/images/JAXA/JAXA_GCOM-C_L3_LAND_LAI_V1_sample.png) 

Dataset Availability
    2018-01-01T00:00:00Z–2020-06-28T00:00:00Z 

Dataset Provider
     [ Global Change Observation Mission (GCOM) ](https://suzaku.eorc.jaxa.jp/GCOM/index.html) 

Earth Engine Snippet
     `    ee.ImageCollection("JAXA/GCOM-C/L3/LAND/LAI/V1")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/JAXA/JAXA_GCOM-C_L3_LAND_LAI_V1) 

Cadence
    1 Day 

Tags
     [g-portal](https://developers.google.com/earth-engine/datasets/tags/g-portal) [gcom](https://developers.google.com/earth-engine/datasets/tags/gcom) [gcom-c](https://developers.google.com/earth-engine/datasets/tags/gcom-c) [jaxa](https://developers.google.com/earth-engine/datasets/tags/jaxa) [lai](https://developers.google.com/earth-engine/datasets/tags/lai) [land](https://developers.google.com/earth-engine/datasets/tags/land) [leaf-area-index](https://developers.google.com/earth-engine/datasets/tags/leaf-area-index) [vegetation-indices](https://developers.google.com/earth-engine/datasets/tags/vegetation-indices)
[Description](https://developers.google.com/earth-engine/datasets/catalog/JAXA_GCOM-C_L3_LAND_LAI_V1#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/JAXA_GCOM-C_L3_LAND_LAI_V1#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/JAXA_GCOM-C_L3_LAND_LAI_V1#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/JAXA_GCOM-C_L3_LAND_LAI_V1#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/JAXA_GCOM-C_L3_LAND_LAI_V1#citations) More
This product is the sum of the one-sided green leaf area per unit ground area.
A newer version [JAXA/GCOM-C/L3/LAND/LAI/V3](https://developers.google.com/earth-engine/datasets/catalog/JAXA_GCOM-C_L3_LAND_LAI_V3) is also available for this dataset which uses this [algorithm](https://suzaku.eorc.jaxa.jp/GCOM_C/data/product_std.html) for processing.
GCOM-C conducts long-term and continuous global observation and data collection to elucidate the mechanism behind fluctuations in radiation budget and carbon cycle needed to make accurate projections regarding future temperature rise. At the same time, cooperating with research institutions having a climate numerical model, it contributes to reduction of errors in temperature rise prediction derived from the climate numerical model and improvement of accuracy of prediction of various environmental changes. SGLI mounted on GCOM-C is the succession sensor of the Global Imager (GLI) mounted on ADEOS-II (MIDORI II) and is the Imaging Radiometer which measures the radiation from near-ultraviolet to thermal infrared region (380 nm-12 um) in 19 channels. Global observation of once for approximately every two days is possible at mid-latitude near Japan by observation width at ground greater than 1,000 km. In addition, SGLI realizes high resolution than the similar global sensor and has a polarized observation function and a multi-angle observation function.
**Pixel Size** 4638.3 meters 
**Bands**
Name | Min | Max | Description  
---|---|---|---  
`LAI_AVE` |  0*  |  65531*  | The sum of the one-sided green leaf area per unit ground area.  
`LAI_QA_flag` | LAI QA  
Bitmask for LAI_QA_flag
  * Bits 0-1: Terrain type 
    * 0: water (land fraction = 0%)
    * 1: mostly water (0% < land fraction < 50%)
    * 2: mostly coastal (50% < land fraction < 100%)
    * 3: land (land fraction = 100%)

  
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

  
LAI_AVE_OFFSET | STRING | Offset  
LAI_AVE_SLOPE | STRING | Slope  
**Terms of Use**
This dataset is free to use without any restrictions (including commercial use). Anyone wishing to publish analyzed results or value added data products should properly credit the original G-Portal data, e.g., "PR data by Japan Aerospace Exploration Agency". For value added data products, please indicate the credit of the original G-Portal data, e.g., "Original data for this value added data product was provided by Japan Aerospace Exploration Agency."
See [G-Portal's terms of service (Article 7)](https://gportal.jaxa.jp/gpr/index/eula?lang=en) for additional information.
Citations:
  * Ono, Y. (Nov. 2011). GCOM-C1 / SGLI LAI Product Algorithm Theoretical Basis Document (Version 1). Retrieved from <https://suzaku.eorc.jaxa.jp/GCOM_C/data/ATBD/ver1/Ono_Y_ATBD.pdf>


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/JAXA_GCOM-C_L3_LAND_LAI_V1#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('JAXA/GCOM-C/L3/LAND/LAI/V1')
.filterDate('2020-01-01','2020-02-01')
// filter to daytime data only
.filter(ee.Filter.eq('SATELLITE_DIRECTION','D'));
// Multiply with slope coefficient
vardataset=dataset.mean().multiply(0.001);
varvisualization={
bands:['LAI_AVE'],
min:-7,
max:7,
palette:[
'040274','040281','0502a3','0502b8','0502ce','0502e6',
'0602ff','235cb1','307ef3','269db1','30c8e2','32d3ef',
'3be285','3ff38f','86e26f','3ae237','b5e22e','d6e21f',
'fff705','ffd611','ffb613','ff8b13','ff6e08','ff500d',
'ff0000','de0101','c21301','a71001','911003',
]
};
Map.setCenter(128.45,33.33,5);
Map.addLayer(dataset,visualization,'Leaf Area Index');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/JAXA/JAXA_GCOM-C_L3_LAND_LAI_V1)
[ GCOM-C/SGLI L3 Leaf Area Index (V1) ](https://developers.google.com/earth-engine/datasets/catalog/JAXA_GCOM-C_L3_LAND_LAI_V1)
This product is the sum of the one-sided green leaf area per unit ground area. A newer version JAXA/GCOM-C/L3/LAND/LAI/V3 is also available for this dataset which uses this algorithm for processing. GCOM-C conducts long-term and continuous global observation and data collection to elucidate the mechanism behind fluctuations in radiation budget …
JAXA/GCOM-C/L3/LAND/LAI/V1, g-portal,gcom,gcom-c,jaxa,lai,land,leaf-area-index,vegetation-indices 
2018-01-01T00:00:00Z/2020-06-28T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://suzaku.eorc.jaxa.jp/GCOM/index.html)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/JAXA_GCOM-C_L3_LAND_LAI_V1)


