 
#  Greenland Ice & Ocean Mask - Greenland Mapping Project (GIMP) 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
![OSU/GIMP/2000_ICE_OCEAN_MASK](https://developers.google.com/earth-engine/datasets/images/OSU/OSU_GIMP_2000_ICE_OCEAN_MASK_sample.png) 

Dataset Availability
    1999-06-30T00:00:00Z–2002-09-04T00:00:00Z 

Dataset Provider
     [ NASA NSIDC DAAC at CIRES ](https://doi.org/10.5067/B8X58MQBFUPA) 

Earth Engine Snippet
     `    ee.Image("OSU/GIMP/2000_ICE_OCEAN_MASK")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/OSU/OSU_GIMP_2000_ICE_OCEAN_MASK) 

Tags
     [arctic](https://developers.google.com/earth-engine/datasets/tags/arctic) [cryosphere](https://developers.google.com/earth-engine/datasets/tags/cryosphere) [gimp](https://developers.google.com/earth-engine/datasets/tags/gimp) [greenland](https://developers.google.com/earth-engine/datasets/tags/greenland) [ice](https://developers.google.com/earth-engine/datasets/tags/ice) [nasa](https://developers.google.com/earth-engine/datasets/tags/nasa) [polar](https://developers.google.com/earth-engine/datasets/tags/polar)
mask
[Description](https://developers.google.com/earth-engine/datasets/catalog/OSU_GIMP_2000_ICE_OCEAN_MASK#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/OSU_GIMP_2000_ICE_OCEAN_MASK#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/OSU_GIMP_2000_ICE_OCEAN_MASK#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/OSU_GIMP_2000_ICE_OCEAN_MASK#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/OSU_GIMP_2000_ICE_OCEAN_MASK#dois) More
This dataset provides complete land ice and ocean classification masks at 15 m for the Greenland ice sheet. Ice cover was mapped using a combination of orthorectified panchromatic (band 8) imagery from the Landsat 7 Enhanced Thematic Mapper Plus (ETM+), distributed by the USGS, and RADARSAT-1 Synthetic Amplitude Radar (SAR) amplitude images produced and distributed by I. Joughin at the Applied Physics Laboratory, University of Washington.
The Landsat imagery was acquired for the months of July through September in 1999, 2000 and 2001 (mostly 2000) and the RADARSAT imagery was acquired in fall of 2000.
**Pixel Size** 15 meters 
**Bands**
Name | Description  
---|---  
`ocean_mask` | Ocean mask  
`ice_mask` | Ice mask  
**ocean_mask Class Table**
Value | Color | Description  
---|---|---  
0 | #000000 | all other terrain  
1 | #0000ff | ocean  
**ice_mask Class Table**
Value | Color | Description  
---|---|---  
0 | #000000 | not glacier ice  
1 | #ffffff | glacier ice  
**Terms of Use**
As a condition of using these data, you must cite the use of this data set using the given citation.
Citations:
  * Howat, I.M., A. Negrete, B.E. Smith, 2014, The Greenland Ice Mapping Project (GIMP) land classification and surface elevation datasets, The Cryosphere, 8, 1509-1518, [doi:10.5194/tc-8-1509-2014](https://doi.org/10.5194/tc-8-1509-2014) [article pdf](https://www.the-cryosphere.net/8/1509/2014/tc-8-1509-2014.pdf)


  * [ https://doi.org/10.5067/B8X58MQBFUPA ](https://doi.org/10.5067/B8X58MQBFUPA)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/OSU_GIMP_2000_ICE_OCEAN_MASK#code-editor-javascript-sample) More
```
vardataset=ee.Image('OSU/GIMP/2000_ICE_OCEAN_MASK');
varoceanAndIceMaskVis={
min:0.0,
max:1.0,
bands:['ice_mask','ice_mask','ocean_mask'],
};
Map.setCenter(-41.0,74.0,4);
Map.addLayer(dataset,oceanAndIceMaskVis,'Ocean and Ice Mask');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/OSU/OSU_GIMP_2000_ICE_OCEAN_MASK)
[ Greenland Ice & Ocean Mask - Greenland Mapping Project (GIMP) ](https://developers.google.com/earth-engine/datasets/catalog/OSU_GIMP_2000_ICE_OCEAN_MASK)
This dataset provides complete land ice and ocean classification masks at 15 m for the Greenland ice sheet. Ice cover was mapped using a combination of orthorectified panchromatic (band 8) imagery from the Landsat 7 Enhanced Thematic Mapper Plus (ETM+), distributed by the USGS, and RADARSAT-1 Synthetic Amplitude Radar (SAR) …
OSU/GIMP/2000_ICE_OCEAN_MASK, arctic,cryosphere,gimp,greenland,ice,nasa,polar 
1999-06-30T00:00:00Z/2002-09-04T00:00:00Z
58.79601275381146 -89.3211593425295 83.95386175580668 7.555941634834938 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.5067/B8X58MQBFUPA ](https://doi.org/https://doi.org/10.5067/B8X58MQBFUPA)
  * [ https://doi.org/10.5067/B8X58MQBFUPA ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/OSU_GIMP_2000_ICE_OCEAN_MASK)


