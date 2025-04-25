 
#  NOAA NHC HURDAT2 Atlantic Hurricane Catalog 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![NOAA/NHC/HURDAT2/atlantic](https://developers.google.com/earth-engine/datasets/images/NOAA/NOAA_NHC_HURDAT2_atlantic_sample.png) 

Dataset Availability
    1851-06-25T00:00:00Z–2018-11-04T12:00:00Z 

Dataset Provider
     [ NOAA NHC ](https://www.nhc.noaa.gov/data/) 

Earth Engine Snippet
     FeatureCollection `    ee.FeatureCollection("NOAA/NHC/HURDAT2/atlantic")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NOAA/NOAA_NHC_HURDAT2_atlantic)      FeatureView  `    ui.Map.FeatureViewLayer("NOAA/NHC/HURDAT2/atlantic_FeatureView")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NOAA/NOAA_NHC_HURDAT2_atlantic_FeatureView) 

Tags
     [climate](https://developers.google.com/earth-engine/datasets/tags/climate) [hurricane](https://developers.google.com/earth-engine/datasets/tags/hurricane) [nhc](https://developers.google.com/earth-engine/datasets/tags/nhc) [noaa](https://developers.google.com/earth-engine/datasets/tags/noaa) [table](https://developers.google.com/earth-engine/datasets/tags/table) [weather](https://developers.google.com/earth-engine/datasets/tags/weather)
[Description](https://developers.google.com/earth-engine/datasets/catalog/NOAA_NHC_HURDAT2_atlantic#description)[Table Schema](https://developers.google.com/earth-engine/datasets/catalog/NOAA_NHC_HURDAT2_atlantic#table-schema)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/NOAA_NHC_HURDAT2_atlantic#terms-of-use) More
Hurricane best track database (HURDAT2).
Atlantic basin 1851-2018.
**Table Schema**
Name | Type | Description  
---|---|---  
seq | DOUBLE | ATCF cyclone number for that year  
name | STRING | Hurricane name. e.g. "ALEX"  
datetime | STRING | Observation time in UTC. Format is YYYY-MM-DDTHH:MM:SS.  
record_id | STRING | Single letter desinating a specific event in a hurricane track. An empty string if no code.
  * C - Closest approach to a coast not followed by a landfall
  * G - Genesis
  * I - An intensity peak in terms of both pressure and wind
  * L - Landfall (center of system crossing a coastline)
  * P - Minimum in central pressure
  * R - Provides additional detail on the intensity of the cyclone when rapid changes are underway
  * S - Change of status of the system
  * T - Provides additional detail on the track (position) of the cyclone
  * W - Maximum sustained wind speed

  
status | STRING | Status of system:
  * DB - Disturbance (of any intensity)
  * ET - Unknown. The only occurrence is in HARVEY.
  * EX - Extratropical cyclone (of any intensity)
  * HU - Tropical cyclone of hurricane intensity (> 64 knots)
  * LO - A low that is neither a tropical cyclone, a subtropical cyclone, nor an extratropical cyclone (of any intensity)
  * SD - Subtropical cyclone of subtropical depression intensity (< 34 knots)
  * SS - Subtropical cyclone of subtropical storm intensity (> 34 knots)
  * TD - Tropical cyclone of tropical depression intensity (< 34 knots)
  * TS - Tropical cyclone of tropical storm intensity (34-63 knots)
  * WV - Tropical Wave (of any intensity)

  
max_wind_kts | DOUBLE | Maximum wind speed  
min_pressure | DOUBLE | Minimum pressure  
numEntries | DOUBLE | Number of points for a particular hurricane  
radii_ne_34kt | DOUBLE | 34 kt wind radii maximum extent in northeastern quadrant  
radii_se_34kt | DOUBLE | 34 kt wind radii maximum extent in southeastern quadrant  
radii_sw_34kt | DOUBLE | 34 kt wind radii maximum extent in southwestern quadrant  
radii_nw_34kt | DOUBLE | 34 kt wind radii maximum extent in northwestern quadrant  
radii_ne_50kt | DOUBLE | 50 kt wind radii maximum extent in northeastern quadrant  
radii_se_50kt | DOUBLE | 50 kt wind radii maximum extent in southeastern quadrant  
radii_sw_50kt | DOUBLE | 50 kt wind radii maximum extent in southwestern quadrant  
radii_nw_50kt | DOUBLE | 50 kt wind radii maximum extent in northwestern quadrant  
radii_ne_64kt | DOUBLE | 64 kt wind radii maximum extent in northeastern quadrant  
radii_se_64kt | DOUBLE | 64 kt wind radii maximum extent in southeastern quadrant  
radii_sw_64kt | DOUBLE | 64 kt wind radii maximum extent in southwestern quadrant  
radii_nw_64kt | DOUBLE | 64 kt wind radii maximum extent in northwestern quadrant  
basin | STRING | Ocean basin. Always "AL" for Atlantic.  
id | STRING | Code for a particular hurricane. "AL" followed by a 2 digit cyclone number followed by a 4-digit year. e.g. "AL162018"  
year | DOUBLE | Year in which the hurricane occurred  
**Terms of Use**
NOAA data, information, and products, regardless of the method of delivery, are not subject to copyright and carry no restrictions on their subsequent use by the public. Once obtained, they may be put to any lawful use.
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/NOAA_NHC_HURDAT2_atlantic#code-editor-javascript-sample) More
```
// Show hurricane tracks and points for 2017.
varhurricanes=ee.FeatureCollection('NOAA/NHC/HURDAT2/atlantic');
varyear='2017';
varpoints=hurricanes.filter(ee.Filter.date(ee.Date(year).getRange('year')));
// Find all of the hurricane ids.
varGetId=function(point){
returnee.Feature(point).get('id');
};
varstorm_ids=points.toList(1000).map(GetId).distinct();
// Create a line for each hurricane.
varlines=ee.FeatureCollection(storm_ids.map(function(storm_id){
varpts=points.filter(ee.Filter.eq('id',ee.String(storm_id)));
pts=pts.sort('system:time_start');
varline=ee.Geometry.LineString(pts.geometry().coordinates());
varfeature=ee.Feature(line);
returnfeature.set('id',storm_id);
}));
Map.addLayer(lines,{color:'red'},'tracks');
Map.addLayer(points,{color:'black'},'points');
Map.setCenter(-53,36,3);
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NOAA/NOAA_NHC_HURDAT2_atlantic)
### Visualize as a FeatureView
A `FeatureView` is a view-only, accelerated representation of a `FeatureCollection`. For more details, visit the [ `FeatureView` documentation. ](https://developers.google.com/earth-engine/guides/featureview_overview)
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/NOAA_NHC_HURDAT2_atlantic#code-editor-javascript-sample) More
```
varfvLayer=ui.Map.FeatureViewLayer('NOAA/NHC/HURDAT2/atlantic_FeatureView');
varvisParams={
isVisible:false,
pointSize:20,
rules:[
{
filter:ee.Filter.eq('year',2018),
isVisible:true,
pointFillColor:{
property:'max_wind_kts',
mode:'linear',
palette:['f1eef6','d7b5d8','df65b0','ce1256'],
min:15,
max:115
}
}
]
};
fvLayer.setVisParams(visParams);
fvLayer.setName('2018 hurricane max wind speed');
Map.setLocked(false,4);
Map.setCenter(-62.25,32.19,4);
Map.add(fvLayer);
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NOAA/NOAA_NHC_HURDAT2_atlantic_FeatureView)
[ NOAA NHC HURDAT2 Atlantic Hurricane Catalog ](https://developers.google.com/earth-engine/datasets/catalog/NOAA_NHC_HURDAT2_atlantic)
Hurricane best track database (HURDAT2). Atlantic basin 1851-2018.
NOAA/NHC/HURDAT2/atlantic, climate,hurricane,nhc,noaa,table,weather 
1851-06-25T00:00:00Z/2018-11-04T12:00:00Z
7.2 -109.5 81 63 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.nhc.noaa.gov/data/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/NOAA_NHC_HURDAT2_atlantic)


