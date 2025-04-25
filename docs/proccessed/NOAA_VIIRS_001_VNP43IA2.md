 
#  VNP43IA2: BRDF/Albedo Quality Daily L3 Global 500m SIN Grid 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![NOAA/VIIRS/001/VNP43IA2](https://developers.google.com/earth-engine/datasets/images/NOAA/NOAA_VIIRS_001_VNP43IA2_sample.png) 

Dataset Availability
    2012-01-17T00:00:00Z–2024-06-09T00:00:00Z 

Dataset Provider
     [ NASA LP DAAC at the USGS EROS Center ](https://doi.org/10.5067/VIIRS/VNP43IA2.001) 

Earth Engine Snippet
     `    ee.ImageCollection("NOAA/VIIRS/001/VNP43IA2")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NOAA/NOAA_VIIRS_001_VNP43IA2) 

Cadence
    1 Day 

Tags
     [land](https://developers.google.com/earth-engine/datasets/tags/land) [nasa](https://developers.google.com/earth-engine/datasets/tags/nasa) [noaa](https://developers.google.com/earth-engine/datasets/tags/noaa) [satellite-imagery](https://developers.google.com/earth-engine/datasets/tags/satellite-imagery) [surface](https://developers.google.com/earth-engine/datasets/tags/surface) [viirs](https://developers.google.com/earth-engine/datasets/tags/viirs)
[Description](https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_001_VNP43IA2#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_001_VNP43IA2#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_001_VNP43IA2#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_001_VNP43IA2#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_001_VNP43IA2#dois) More
The Suomi National Polar-Orbiting Partnership (Suomi NPP) NASA Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Quality (VNP43IA2) Version 1 product provides BRDF and Albedo quality at 500m resolution. The VNP43IA2 product is produced daily using 16 days of VIIRS data and is weighted temporally to the ninth day, which is reflected in the file name. The VNP43IA2 product provides information regarding band quality and days of valid observation within a 16-day period for the VIIRS imagery bands. The VNP43 data products are designed to promote the continuity of NASA's Moderate Resolution Imaging Spectroradiometer (MODIS) BRDF/Albedo data product suite.
Documentation:
  * [User's Guide](https://www.umb.edu/spectralmass/viirs_user_guide/vnp43ia2_and_vnp43ma2_brdf_albedo_quality_product)
  * [Algorithm Theoretical Basis Document (ATBD)](https://lpdaac.usgs.gov/documents/194/VNP43_ATBD_V1.pdf)
  * [General Documentation](https://lpdaac.usgs.gov/products/vnp43ia2v001/)
  * [Land Product Quality Assessment website](https://landweb.modaps.eosdis.nasa.gov/browse?sensor=VIIRS&sat=SNPP)


**Pixel Size** 500 meters 
**Bands**
Name | Units | Description  
---|---|---  
`BRDF_Albedo_Band_Quality_I1` | BRDF inversion information I1  
`BRDF_Albedo_Band_Quality_I2` | BRDF inversion information I2  
`BRDF_Albedo_Band_Quality_I3` | BRDF inversion information I3  
`BRDF_Albedo_LandWaterType` | Land/Water type  
`BRDF_Albedo_LocalSolarNoon` | deg | Solar zenith angle at local solar noon  
`BRDF_Albedo_Platform` | Platform name  
`BRDF_Albedo_Uncertainty` | Weight of Determination (WoD) of WSA  
`BRDF_Albedo_ValidObs_I1` | d | Days of valid observation within 16-day period for band I1  
`BRDF_Albedo_ValidObs_I2` | d | Days of valid observation within 16-day period for band I2  
`BRDF_Albedo_ValidObs_I3` | d | Days of valid observation within 16-day period for band I3  
`Snow_BRDF_Albedo` | Snow flag  
**BRDF_Albedo_Band_Quality_I1 Class Table**
Value | Color | Description  
---|---|---  
0 | best quality, full inversion (WoDs, RMSE majority good)   
1 | good quality, full inversion  
2 | Magnitude inversion (numobs ≥ 7)  
3 | Magnitude inversion (numobs ≥ 2 & 7)  
**BRDF_Albedo_Band_Quality_I2 Class Table**
Value | Color | Description  
---|---|---  
0 | best quality, full inversion (WoDs, RMSE majority good)   
1 | good quality, full inversion  
2 | Magnitude inversion (numobs ≥ 7)  
3 | Magnitude inversion (numobs ≥ 2 & 7)  
**BRDF_Albedo_Band_Quality_I3 Class Table**
Value | Color | Description  
---|---|---  
0 | best quality, full inversion (WoDs, RMSE majority good)   
1 | good quality, full inversion  
2 | Magnitude inversion (numobs ≥ 7)  
3 | Magnitude inversion (numobs ≥ 2 & 7)  
**BRDF_Albedo_LandWaterType Class Table**
Value | Color | Description  
---|---|---  
0 | Shallow ocean  
1 | Land (Nothing else but land)  
2 | Ocean and lake shorelines  
3 | Shallow inland water  
4 | Ephemeral water  
5 | Deep inland water  
6 | Moderate or continental ocean  
7 | Deep ocean  
**Snow_BRDF_Albedo Class Table**
Value | Color | Description  
---|---|---  
0 | snow-free albedo retrieved  
1 | snow albedo retrieved  
**Terms of Use**
LP DAAC NASA data are freely accessible; however, when an author publishes these data or works based on the data, it is requested that the author cite the datasets within the text of the publication and include a reference to them in the reference list.
Citations:
  * Please visit [LP DAAC 'Citing Our Data' page](https://lpdaac.usgs.gov/citing_our_data) for information on citing LP DAAC datasets.


  * [ https://doi.org/10.5067/VIIRS/VNP43IA2.001 ](https://doi.org/10.5067/VIIRS/VNP43IA2.001)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_001_VNP43IA2#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('NOAA/VIIRS/001/VNP43IA2')
.filter(ee.Filter.date('2021-06-01','2021-06-03'));
varvisualization={
bands:['BRDF_Albedo_ValidObs_I1'],
min:35550,
max:45535,
palette:[
'000080','0000d9','4000ff','8000ff','0080ff','00ffff',
'00ff80','80ff00','daff00','ffff00','fff500','ffda00',
'ffb000','ffa400','ff4f00','ff2500','ff0a00','ff00ff',
]
};
Map.setCenter(89,58,6);
Map.addLayer(dataset,visualization,'Days of valid observation for band I1');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NOAA/NOAA_VIIRS_001_VNP43IA2)
[ VNP43IA2: BRDF/Albedo Quality Daily L3 Global 500m SIN Grid ](https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_001_VNP43IA2)
The Suomi National Polar-Orbiting Partnership (Suomi NPP) NASA Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Quality (VNP43IA2) Version 1 product provides BRDF and Albedo quality at 500m resolution. The VNP43IA2 product is produced daily using 16 days of VIIRS data and is weighted temporally …
NOAA/VIIRS/001/VNP43IA2, land,nasa,noaa,satellite-imagery,surface,viirs 
2012-01-17T00:00:00Z/2024-06-09T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.5067/VIIRS/VNP43IA2.001 ](https://doi.org/https://doi.org/10.5067/VIIRS/VNP43IA2.001)
  * [ https://doi.org/10.5067/VIIRS/VNP43IA2.001 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_001_VNP43IA2)


