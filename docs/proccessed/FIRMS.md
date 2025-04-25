 
#  FIRMS: Fire Information for Resource Management System 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![FIRMS](https://developers.google.com/earth-engine/datasets/images/FIRMS/FIRMS_sample.png) 

Dataset Availability
    2000-11-01T00:00:00Z–2025-04-21T00:00:00Z 

Dataset Provider
     [ NASA / LANCE / EOSDIS ](https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms) 

Earth Engine Snippet
     `    ee.ImageCollection("FIRMS")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/FIRMS/FIRMS) 

Cadence
    1 Day 

Tags
     [eosdis](https://developers.google.com/earth-engine/datasets/tags/eosdis) [fire](https://developers.google.com/earth-engine/datasets/tags/fire) [firms](https://developers.google.com/earth-engine/datasets/tags/firms) [geophysical](https://developers.google.com/earth-engine/datasets/tags/geophysical) [hotspot](https://developers.google.com/earth-engine/datasets/tags/hotspot) [lance](https://developers.google.com/earth-engine/datasets/tags/lance) [modis](https://developers.google.com/earth-engine/datasets/tags/modis) [nasa](https://developers.google.com/earth-engine/datasets/tags/nasa) [thermal](https://developers.google.com/earth-engine/datasets/tags/thermal)
[Description](https://developers.google.com/earth-engine/datasets/catalog/FIRMS#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/FIRMS#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/FIRMS#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/FIRMS#citations) More
The Earth Engine version of the Fire Information for Resource Management System (FIRMS) dataset contains the LANCE fire detection product in rasterized form. The near real-time (NRT) active fire locations are processed by LANCE using the standard MODIS MOD14/MYD14 Fire and Thermal Anomalies product. Each active fire location represents the centroid of a 1km pixel that is flagged by the algorithm as containing one or more fires within the pixel. The data are rasterized as follows: for each FIRMS active fire point, a 1km bounding box (BB) is defined; pixels in the MODIS sinusoidal projection that intersect the FIRMS BB are identified; if multiple FIRMS BBs intersect the same pixel, the one with higher confidence is retained; in case of a tie, the brighter one is retained.
The data in the near-real-time dataset are not considered to be of science quality.
Additional information can be found [here](https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/about-firms).
NOTE: VIIRS FIRMS datasets from NOAA20 and SUOMI are also available:
  * [NASA/LANCE/NOAA20_VIIRS/C2](https://developers.google.com/earth-engine/datasets/catalog/NASA_LANCE_NOAA20_VIIRS_C2)
  * [NASA/LANCE/SNPP_VIIRS/C2](https://developers.google.com/earth-engine/datasets/catalog/NASA_LANCE_SNPP_VIIRS_C2)


**Pixel Size** 1000 meters 
**Bands**
Name | Units | Min | Max | Description  
---|---|---|---|---  
`T21` | K |  300*  |  509.29*  | The brightness temperature of a fire pixel using MODIS channels 21/22.  
`confidence` | % |  0  |  100  | A detection confidence intended to help users gauge the quality of individual active fire pixels. The confidence estimate ranges between 0% and 100% for all fire pixels within the fire mask. The confidence field should be used with caution; it is likely that it will vary in meaning in different parts of the world.  
`line_number` |  1*  |  35302*  | Line number in the FIRMS CSV file that the pixel came from.  
* estimated min or max value 
**Terms of Use**
NASA promotes the full and open sharing of all data with the research and applications communities, private industry, academia, and the general public. Read the [NASA Data and Information Policy](https://www.earthdata.nasa.gov/learn/use-data/data-use-policy).
If you provide the [Land, Atmosphere Near real-time Capability for EOS (LANCE) / Fire Information for Resource Management System (FIRMS)](https://earthdata.nasa.gov/earth-observation-data/near-real-time) data to a third party, follow the guidelines in the [LANCE Citation, Acknowledgements, and Disclaimer](https://earthdata.nasa.gov/earth-observation-data/near-real-time/citation#ed-lance-disclaimer) site and replicate or provide a link to the [disclaimer](https://earthdata.nasa.gov/earth-observation-data/near-real-time/citation#ed-lance-disclaimer).
Citations:
  * MODIS Collection 6 NRT Hotspot / Active Fire Detections MCD14DL. Available on-line <https://earthdata.nasa.gov/firms>. [doi:10.5067/FIRMS/MODIS/MCD14DL.NRT.006](https://doi.org/10.5067/FIRMS/MODIS/MCD14DL.NRT.006)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/FIRMS#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('FIRMS').filter(
ee.Filter.date('2018-08-01','2018-08-10'));
varfires=dataset.select('T21');
varfiresVis={
min:325.0,
max:400.0,
palette:['red','orange','yellow'],
};
Map.setCenter(-119.086,47.295,6);
Map.addLayer(fires,firesVis,'Fires');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/FIRMS/FIRMS)
[ FIRMS: Fire Information for Resource Management System ](https://developers.google.com/earth-engine/datasets/catalog/FIRMS)
The Earth Engine version of the Fire Information for Resource Management System (FIRMS) dataset contains the LANCE fire detection product in rasterized form. The near real-time (NRT) active fire locations are processed by LANCE using the standard MODIS MOD14/MYD14 Fire and Thermal Anomalies product. Each active fire location represents the …
FIRMS, eosdis,fire,firms,geophysical,hotspot,lance,modis,nasa,thermal 
2000-11-01T00:00:00Z/2025-04-21T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/FIRMS)


