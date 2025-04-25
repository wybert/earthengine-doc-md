 
#  ETOPO1: Global 1 Arc-Minute Elevation 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![NOAA/NGDC/ETOPO1](https://developers.google.com/earth-engine/datasets/images/NOAA/NOAA_NGDC_ETOPO1_sample.png) 

Dataset Availability
    2008-08-01T00:00:00Z–2008-08-01T00:00:00Z 

Dataset Provider
     [ NOAA ](https://www.ngdc.noaa.gov/mgg/global/global.html) 

Earth Engine Snippet
     `    ee.Image("NOAA/NGDC/ETOPO1")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NOAA/NOAA_NGDC_ETOPO1) 

Tags
     [bedrock](https://developers.google.com/earth-engine/datasets/tags/bedrock) [dem](https://developers.google.com/earth-engine/datasets/tags/dem) [elevation](https://developers.google.com/earth-engine/datasets/tags/elevation) [elevation-topography](https://developers.google.com/earth-engine/datasets/tags/elevation-topography) [geophysical](https://developers.google.com/earth-engine/datasets/tags/geophysical) [ice](https://developers.google.com/earth-engine/datasets/tags/ice) [noaa](https://developers.google.com/earth-engine/datasets/tags/noaa) [topography](https://developers.google.com/earth-engine/datasets/tags/topography)
[Description](https://developers.google.com/earth-engine/datasets/catalog/NOAA_NGDC_ETOPO1#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/NOAA_NGDC_ETOPO1#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/NOAA_NGDC_ETOPO1#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/NOAA_NGDC_ETOPO1#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/NOAA_NGDC_ETOPO1#dois) More
ETOPO1 is a 1 arc-minute global relief model of Earth''s surface that integrates land topography and ocean bathymetry. It was built from numerous global and regional data sets. It contains two elevation bands: ice_surface and bedrock.
**Pixel Size** 1855 meters 
**Bands**
Name | Units | Min | Max | Description  
---|---|---|---|---  
`bedrock` | m |  -10898*  |  8271*  | Elevation at ground level and at the base of the Antarctic and Greenland ice sheets  
`ice_surface` | m |  -10898*  |  8271*  | Elevation at ground level and at the top of the Antarctic and Greenland ice sheets  
* estimated min or max value 
**Terms of Use**
It is not necessary to obtain written permission to use ETOPO1 or other NOAA products that are in the public domain, nor are there any fees for using them. We ask only that you cite NCEI as source.
Citations:
  * Amante, C. and B. W. Eakins, ETOPO1 1 Arc-Minute Global Relief Model: Procedures, Data Sources and Analysis. NOAA Technical Memorandum NESDIS NGDC-24, 19 pp, March 2009.


  * [ https://doi.org/10.7289/V5C8276M ](https://doi.org/10.7289/V5C8276M)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/NOAA_NGDC_ETOPO1#code-editor-javascript-sample) More
```
vardataset=ee.Image('NOAA/NGDC/ETOPO1');
varelevation=dataset.select('bedrock');
varelevationVis={
min:-7000.0,
max:3000.0,
palette:['011de2','afafaf','3603ff','fff477','b42109'],
};
Map.setCenter(-37.62,25.8,2);
Map.addLayer(elevation,elevationVis,'Elevation');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NOAA/NOAA_NGDC_ETOPO1)
[ ETOPO1: Global 1 Arc-Minute Elevation ](https://developers.google.com/earth-engine/datasets/catalog/NOAA_NGDC_ETOPO1)
ETOPO1 is a 1 arc-minute global relief model of Earth''s surface that integrates land topography and ocean bathymetry. It was built from numerous global and regional data sets. It contains two elevation bands: ice_surface and bedrock.
NOAA/NGDC/ETOPO1, bedrock,dem,elevation,elevation-topography,geophysical,ice,noaa,topography 
2008-08-01T00:00:00Z/2008-08-01T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.7289/V5C8276M ](https://doi.org/https://www.ngdc.noaa.gov/mgg/global/global.html)
  * [ https://doi.org/10.7289/V5C8276M ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/NOAA_NGDC_ETOPO1)


