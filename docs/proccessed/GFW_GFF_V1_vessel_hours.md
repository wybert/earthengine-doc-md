 
#  GFW (Global Fishing Watch) Daily Vessel Hours 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![GFW/GFF/V1/vessel_hours](https://developers.google.com/earth-engine/datasets/images/GFW/GFW_GFF_V1_vessel_hours_sample.png) 

Dataset Availability
    2012-01-01T00:00:00Z–2017-01-01T00:00:00Z 

Dataset Provider
     [ Global Fishing Watch ](https://globalfishingwatch.org/) 

Earth Engine Snippet
     `    ee.ImageCollection("GFW/GFF/V1/vessel_hours")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/GFW/GFW_GFF_V1_vessel_hours) 

Cadence
    1 Day 

Tags
     [fishing](https://developers.google.com/earth-engine/datasets/tags/fishing) [gfw](https://developers.google.com/earth-engine/datasets/tags/gfw) [marine](https://developers.google.com/earth-engine/datasets/tags/marine) [monthly](https://developers.google.com/earth-engine/datasets/tags/monthly) [ocean](https://developers.google.com/earth-engine/datasets/tags/ocean) [oceans](https://developers.google.com/earth-engine/datasets/tags/oceans)
[Description](https://developers.google.com/earth-engine/datasets/catalog/GFW_GFF_V1_vessel_hours#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/GFW_GFF_V1_vessel_hours#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/GFW_GFF_V1_vessel_hours#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/GFW_GFF_V1_vessel_hours#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/GFW_GFF_V1_vessel_hours#citations) More
Fishing vessel presence, measured in hours per square km. Each asset is the vessel presence for a given flag state and day, with one band for the presence of each gear type.
See [sample Earth Engine scripts](https://globalfishingwatch.org/research/global-footprint-of-fisheries/). Also see [the main GFW site](https://GlobalFishingWatch.org) for program information, fully interactive visualization maps, and impacts.
**Pixel Size** 1113.2 meters 
**Bands**
Name | Units | Description  
---|---|---  
`drifting_longlines` | h/km^2 | Hours per sq. km of fishing vessel presence with drifting longlines.  
`fixed_gear` | h/km^2 | Hours per sq. km of fishing vessel presence with fixed gear.  
`other_fishing` | h/km^2 | Hours per sq. km of fishing vessel presence with other gear types.  
`purse_seines` | h/km^2 | Hours per sq. km of fishing vessel presence with purse seines.  
`squid_jigger` | h/km^2 | Hours per sq. km of fishing vessel presence with squid jiggers.  
`trawlers` | h/km^2 | Hours per sq. km of fishing vessel presence with trawlers.  
**Image Properties**
Name | Type | Description  
---|---|---  
country | STRING | ISO3 country code of the vessel flag state. For all countries, use "WLD".  
**Terms of Use**
This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International license. (CC-BY-SA)
Citations:
  * Global Fishing Watch, "Tracking the Global Footprint of Fisheries." Science 361.6378 (2018).


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/GFW_GFF_V1_vessel_hours#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('GFW/GFF/V1/vessel_hours')
.filter(ee.Filter.date('2016-12-01','2017-01-01'));
vartrawlers=dataset.select('trawlers');
vartrawlersVis={
min:0.0,
max:5.0,
};
Map.setCenter(130.61,34.287,8);
Map.addLayer(trawlers.max(),trawlersVis,'Trawlers');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/GFW/GFW_GFF_V1_vessel_hours)
[ GFW (Global Fishing Watch) Daily Vessel Hours ](https://developers.google.com/earth-engine/datasets/catalog/GFW_GFF_V1_vessel_hours)
Fishing vessel presence, measured in hours per square km. Each asset is the vessel presence for a given flag state and day, with one band for the presence of each gear type. See sample Earth Engine scripts. Also see the main GFW site for program information, fully interactive visualization maps, …
GFW/GFF/V1/vessel_hours, fishing,gfw,marine,monthly,ocean,oceans 
2012-01-01T00:00:00Z/2017-01-01T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://globalfishingwatch.org/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/GFW_GFF_V1_vessel_hours)


