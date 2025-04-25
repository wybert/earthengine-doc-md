 
#  GOES-19 FDCC Series ABI Level 2 Fire/Hot Spot Characterization CONUS 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![NOAA/GOES/19/FDCC](https://developers.google.com/earth-engine/datasets/images/NOAA/NOAA_GOES_19_FDCC_sample.png) 

Dataset Availability
    2025-04-07T00:00:00Z–2025-04-22T15:56:17.700000Z 

Dataset Provider
     [ NOAA ](https://data.noaa.gov/onestop/collections/details/d9303237-8672-4917-a251-29c3f7640684) 

Earth Engine Snippet
     `    ee.ImageCollection("NOAA/GOES/19/FDCC")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NOAA/NOAA_GOES_19_FDCC) 

Cadence
    10 Minutes 

Tags
     [abi](https://developers.google.com/earth-engine/datasets/tags/abi) [fdc](https://developers.google.com/earth-engine/datasets/tags/fdc) [fire](https://developers.google.com/earth-engine/datasets/tags/fire) [goes](https://developers.google.com/earth-engine/datasets/tags/goes) [goes-19](https://developers.google.com/earth-engine/datasets/tags/goes-19) [goes-east](https://developers.google.com/earth-engine/datasets/tags/goes-east) [goes-u](https://developers.google.com/earth-engine/datasets/tags/goes-u) [hotspot](https://developers.google.com/earth-engine/datasets/tags/hotspot) [nesdis](https://developers.google.com/earth-engine/datasets/tags/nesdis) [noaa](https://developers.google.com/earth-engine/datasets/tags/noaa) [ospo](https://developers.google.com/earth-engine/datasets/tags/ospo) [wildfire](https://developers.google.com/earth-engine/datasets/tags/wildfire)
[Description](https://developers.google.com/earth-engine/datasets/catalog/NOAA_GOES_19_FDCC#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/NOAA_GOES_19_FDCC#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/NOAA_GOES_19_FDCC#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/NOAA_GOES_19_FDCC#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/NOAA_GOES_19_FDCC#dois) More
[GOES](https://www.goes.noaa.gov) satellites are geostationary weather satellites run by NOAA.
The Fire (HSC) product contains four images: one in the form of a fire mask and the other three with pixel values identifying fire temperature, fire area, and fire radiative power.
The ABI L2+ FHS metadata mask assigns a flag to every earth-navigated pixel that indicates its disposition with respect to the FHS algorithm. Operational users who have the lowest tolerance for false alarms should focus on the "processed" and "saturated" categories (mask codes 10, 11, 30, and 31), but within these categories there can still be false alarms.
Operational data production for GOES-19 began April 7, 2025. Any data prior to this date is provisional only.
[README](https://www.ncei.noaa.gov/products/satellite/goes-r)
NOAA provides the following scripts for suggested categories, color maps, and visualizations:
  * [GOES-16-17_FireDetection.js](https://github.com/google/earthengine-community/blob/master/datasets/scripts/GOES-16-17_FireDetection.js)
  * [GOES-16-17_FireReclassification.js](https://github.com/google/earthengine-community/blob/master/datasets/scripts/GOES-16-17_FireReclassification.js)


NOAA's Office of Satellite and Product Operations has a [General Satellite Messages](https://www.ospo.noaa.gov/Operations/messages.html) channel with status updates.
**Pixel Size** 2000 meters 
**Bands**
Name | Units | Min | Max | Scale | Offset | Description  
---|---|---|---|---|---|---  
`Area` | m^2 |  0*  |  16723*  | 60.98 | 4000 | Fire area  
`Temp` | K |  0*  |  32642*  | 0.0549367 | 400 | Fire temperature  
`Mask` | Fire mask categories. Pixel values in the fire mask image identify a fire category and diagnostic information associated with algorithm execution. The six fire categories include: Good quality or temporally filtered good quality fire pixel; Saturated fire pixel or temporally filtered saturated fire pixel; Cloud contaminated or temporally filtered cloud contaminated fire pixel; High probability or temporally filtered high probability fire pixel; Medium probability or temporally filtered high probability fire pixel; Low probability or temporally filtered high probability fire. Temporally filtered fire pixels are those resulting from fire pixels that are in close proximity in both space and time.  
`Power` | MW |  0  |  200000  | Fire radiative power  
`DQF` |  0  |  5  | Data quality flags  
* estimated min or max value 
**Mask Class Table**
Value | Color | Description  
---|---|---  
10 | red | Processed fire  
11 | white | Saturated fire  
12 | slategray | Cloud contaminated fire  
13 | orange | High probability fire  
14 | violet | Medium probability fire  
15 | blue | Low probability fire  
30 | darkred | Processed fire, filtered  
31 | ghostwhite | Saturated fire, filtered  
32 | darkslategray | Cloud contaminated fire, filtered  
33 | darkorange | High probability fire, filtered  
34 | darkviolet | Medium probability fire, filtered  
35 | darkblue | Low probability fire, filtered  
**DQF Class Table**
Value | Color | Description  
---|---|---  
0 | #ffffff | Good quality fire  
1 | #ff00ff | Good quality fire-free land  
2 | #0000ff | Invalid due to opaque cloud  
3 | #00ffff | Invalid due to surface type or sunglint or LZA threshold exceeded or off earth or missing input data  
4 | #ffff00 | Invalid due to bad input data  
5 | #ff0000 | Invalid due to algorithm failure  
**Terms of Use**
NOAA data, information, and products, regardless of the method of delivery, are not subject to copyright and carry no restrictions on their subsequent use by the public. Once obtained, they may be put to any lawful use.
Citations:
  * Early characterization of the active fire detection products derived from the next generation NPOESS/VIIRS and GOES-R/ABI instruments. Schroeder, W., Csiszar, I., et al, (2010), Early characterization of the active fire detection products derived from the next generation NPOESS/VIIRS and GOES-R/ABI instruments, paper presented at 2010 IEEE International Geoscience and Remote Sensing Symposium (IGARSS), Honolulu, HI. [doi:10.1109/IGARSS.2010.5650863](https://doi.org/10.1109/IGARSS.2010.5650863)
  * Schmit, T., Griffith, P., et al, (2016), A closer look at the ABI on the GOES-R series, Bull. Amer. Meteor. Soc., 98(4), 681-698. [doi:10.1175/BAMS-D-15-00230.1](https://doi.org/10.1175/BAMS-D-15-00230.1)


  * [ https://doi.org/10.1175/BAMS-D-15-00230.1 ](https://doi.org/10.1175/BAMS-D-15-00230.1)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/NOAA_GOES_19_FDCC#code-editor-javascript-sample) More
```
// NOAA GOES-19 conterminous fire product for a single time slice.
varimage=ee.Image('NOAA/GOES/19/FDCC/2025097000117300000');
vararea=image.select('Area');
vartemp=image.select('Temp');
vardqf=image.select('DQF');
Map.centerObject(image,3);
varxMin=-145;
varyMin=15;
varxMax=-55;
varyMax=54;
Map.setCenter((xMin+xMax)/2,15,3);
vargeometry=ee.Geometry.Rectangle([xMin,yMin,xMax,yMax],null,true);

varDQFVis={
min:0,
max:5,
palette:[
'blanchedalmond',// Good quality fire pixel
'olive',// Good quality fire free land
'teal',// Opaque cloud
// Bad surface type, sunglint, LZA threshold exceeded,
'darkslateblue',// off Earth, or missing input data
'lemonchiffon',// Bad input data
'burlywood'// Algorithm failure
]};
Map.addLayer(dqf,DQFVis,'DQF');
// Fires are small enough that they are difficult to see at the scale of
// an entire GOES image. Buffer fires based on area to make them stand out.
vararea=area.reduceToVectors({
geometry:geometry,
scale:2000,
geometryType:'centroid',
labelProperty:'area',
maxPixels:1e10,
}).map(function(feature){
returnfeature.buffer(ee.Number(feature.get('area')).add(1).pow(1.4));
});
Map.addLayer(area,{color:'orange'},'area');
// Buffer fires based on temperature to make them stand out.
vartemp=temp.reduceToVectors({
geometry:geometry,
scale:2000,
geometryType:'centroid',
labelProperty:'temp',
maxPixels:1e10,
}).map(function(feature){
returnfeature.buffer(ee.Number(feature.get('temp')).add(2).pow(1.2));
});
Map.addLayer(temp,{color:'red'},'temp');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NOAA/NOAA_GOES_19_FDCC)
[ GOES-19 FDCC Series ABI Level 2 Fire/Hot Spot Characterization CONUS ](https://developers.google.com/earth-engine/datasets/catalog/NOAA_GOES_19_FDCC)
GOES satellites are geostationary weather satellites run by NOAA. The Fire (HSC) product contains four images: one in the form of a fire mask and the other three with pixel values identifying fire temperature, fire area, and fire radiative power. The ABI L2+ FHS metadata mask assigns a flag to …
NOAA/GOES/19/FDCC, abi,fdc,fire,goes,goes-19,goes-east,goes-u,hotspot,nesdis,noaa,ospo,wildfire 
2025-04-07T00:00:00Z/2025-04-22T15:56:17.700000Z
14.57 -180 53.51 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.1175/BAMS-D-15-00230.1 ](https://doi.org/https://data.noaa.gov/onestop/collections/details/d9303237-8672-4917-a251-29c3f7640684)
  * [ https://doi.org/10.1175/BAMS-D-15-00230.1 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/NOAA_GOES_19_FDCC)


