 
#  MOD10A2.061 Terra Snow Cover 8-Day L3 Global 500m 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![MODIS/061/MOD10A2](https://developers.google.com/earth-engine/datasets/images/MODIS/MODIS_061_MOD10A2_sample.png) 

Dataset Availability
    2000-02-18T00:00:00Z–2025-04-07T00:00:00Z 

Dataset Provider
     [ NASA NSIDC DAAC at CIRES ](https://doi.org/10.5067/MODIS/MOD10A2.061) 

Earth Engine Snippet
     `    ee.ImageCollection("MODIS/061/MOD10A2")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_061_MOD10A2) 

Cadence
    1 Day 

Tags
     [cryosphere](https://developers.google.com/earth-engine/datasets/tags/cryosphere) [daily](https://developers.google.com/earth-engine/datasets/tags/daily) [geophysical](https://developers.google.com/earth-engine/datasets/tags/geophysical) [global](https://developers.google.com/earth-engine/datasets/tags/global) [modis](https://developers.google.com/earth-engine/datasets/tags/modis) [nasa](https://developers.google.com/earth-engine/datasets/tags/nasa) [nsidc](https://developers.google.com/earth-engine/datasets/tags/nsidc) [snow](https://developers.google.com/earth-engine/datasets/tags/snow) [terra](https://developers.google.com/earth-engine/datasets/tags/terra)
[Description](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD10A2#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD10A2#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD10A2#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD10A2#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD10A2#dois) More
MOD10A2 is a snow cover dataset from the MODIS on the Terra satellite. The dataset reports the maximum snow cover extent during an eight-day period at the resolution of 500 m.
An eight-day compositing period was chosen because that is the exact ground track repeat period of the Terra and Aqua platforms. Snow cover over eight days is mapped as maximum snow extent in one SDS and as a chronology of observations in the other SDS. Eight-day periods begin on the first day of the year and extend into the next year. The product can be produced with two to eight days of input. There may not always be eight days of input, because of various reasons, so the user should check the attributes to determine on what days observations were obtained.
  * [General documentation](https://doi.org/10.5067/MODIS/MOD10A2.061)
  * [User's Guide](https://modis-snow-ice.gsfc.nasa.gov/uploads/snow_user_guide_C6.1_final_revised_april.pdf),


**Pixel Size** 500 meters 
**Bands**
Name | Min | Max | Description  
---|---|---|---  
`Maximum_Snow_Extent` |  0  |  255  | Maximum snow extent observed over an eight-day period.  
`Eight_Day_Snow_Cover` | Snow chronology bit flags for each day in the eight-day observation period.  
Bitmask for Eight_Day_Snow_Cover
  * Bit 0: day 1 
  * Bit 1: day 2 
  * Bit 2: day 3 
  * Bit 3: day 4 
  * Bit 4: day 5 
  * Bit 5: day 6 
  * Bit 6: day 7 
  * Bit 7: day 8 

  
**Maximum_Snow_Extent Class Table**
Value | Color | Description  
---|---|---  
0 | Missing data  
1 | No decision  
11 | Night  
25 | No snow  
37 | Lake  
39 | Ocean  
50 | Cloud  
100 | Lake ice  
200 | Snow  
254 | Detector saturated  
**Terms of Use**
You may download and use photographs, imagery, or text from the NSIDC web site, unless limitations for its use are specifically stated. For more information on usage and citing NSIDC datasets, please visit the [NSIDC 'Use and Copyright' page](https://nsidc.org/about/data-use-and-copyright).
Citations:
  * Hall, D. K., V. V. Salomonson, and G. A. Riggs. 2016. MODIS/Terra Snow Cover Daily L3 Global 500m Grid. Version 6. Boulder, Colorado USA: NASA National Snow and Ice Data Center Distributed Active Archive Center.


  * [ https://doi.org/10.5067/MODIS/MOD10A1.061 ](https://doi.org/10.5067/MODIS/MOD10A1.061)
  * [ https://doi.org/10.5067/MODIS/MOD10A2.061 ](https://doi.org/10.5067/MODIS/MOD10A2.061)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD10A2#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('MODIS/061/MOD10A2')
.filter(ee.Filter.date('2023-01-01','2023-12-01'))
.select('Maximum_Snow_Extent');
varvisualization={
min:50.0,
max:200.0,
palette:[
'000000',
'0dffff',
'0524ff',
'ffffff'
]
};

Map.setCenter(-3.69,65.99,4);
Map.addLayer(dataset.mean(),visualization,'Maximum_Snow_Extent');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_061_MOD10A2)
[ MOD10A2.061 Terra Snow Cover 8-Day L3 Global 500m ](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD10A2)
MOD10A2 is a snow cover dataset from the MODIS on the Terra satellite. The dataset reports the maximum snow cover extent during an eight-day period at the resolution of 500 m. An eight-day compositing period was chosen because that is the exact ground track repeat period of the Terra and …
MODIS/061/MOD10A2, cryosphere,daily,geophysical,global,modis,nasa,nsidc,snow,terra 
2000-02-18T00:00:00Z/2025-04-07T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.5067/MODIS/MOD10A2.061 ](https://doi.org/https://doi.org/10.5067/MODIS/MOD10A2.061)
  * [ https://doi.org/10.5067/MODIS/MOD10A2.061 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD10A2)


