 
#  MOD17A3HGF.061: Terra Net Primary Production Gap-Filled Yearly Global 500m 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![MODIS/061/MOD17A3HGF](https://developers.google.com/earth-engine/datasets/images/MODIS/MODIS_061_MOD17A3HGF_sample.png) 

Dataset Availability
    2001-01-01T00:00:00Z–2024-01-01T00:00:00Z 

Dataset Provider
     [ NASA LP DAAC at the USGS EROS Center ](https://doi.org/10.5067/MODIS/MOD17A3HGF.061) 

Earth Engine Snippet
     `    ee.ImageCollection("MODIS/061/MOD17A3HGF")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_061_MOD17A3HGF) 

Cadence
    1 Year 

Tags
     [global](https://developers.google.com/earth-engine/datasets/tags/global) [gpp](https://developers.google.com/earth-engine/datasets/tags/gpp) [nasa](https://developers.google.com/earth-engine/datasets/tags/nasa) [npp](https://developers.google.com/earth-engine/datasets/tags/npp) [photosynthesis](https://developers.google.com/earth-engine/datasets/tags/photosynthesis) [plant-productivity](https://developers.google.com/earth-engine/datasets/tags/plant-productivity) [productivity](https://developers.google.com/earth-engine/datasets/tags/productivity) [psn](https://developers.google.com/earth-engine/datasets/tags/psn) [terra](https://developers.google.com/earth-engine/datasets/tags/terra) [usgs](https://developers.google.com/earth-engine/datasets/tags/usgs) [yearly](https://developers.google.com/earth-engine/datasets/tags/yearly)
[Description](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD17A3HGF#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD17A3HGF#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD17A3HGF#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD17A3HGF#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD17A3HGF#dois) More
The MOD17A3HGF V6.1 product provides information about annual Gross and Net Primary Productivity (GPP and NPP) at 500m pixel resolution. Annual NPP is derived from the sum of all 8-day Net Photosynthesis(PSN) products (MOD17A2H) from the given year. The PSN value is the difference of the Gross Primary Productivity (GPP) and the Maintenance Respiration (MR) (GPP-MR).
**Pixel Size** 500 meters 
**Bands**
Name | Units | Min | Max | Scale | Description  
---|---|---|---|---|---  
`Gpp` | kg*C/m^2 |  0  |  65500  | 0.0001 | Gross primary productivity  
`Npp` | kg*C/m^2 |  -30000  |  32700  | 0.0001 | Net primary productivity  
`Npp_QC` | % |  0  |  100  | Quality control percentage  
**Terms of Use**
MODIS data and products acquired through the LP DAAC have no restrictions on subsequent use, sale, or redistribution.
Citations:
  * Please visit [LP DAAC 'Citing Our Data' page](https://lpdaac.usgs.gov/citing_our_data) for information on citing LP DAAC datasets.


  * [ https://doi.org/10.5067/MODIS/MOD17A3HGF.061 ](https://doi.org/10.5067/MODIS/MOD17A3HGF.061)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD17A3HGF#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('MODIS/061/MOD17A3HGF');
varvisualization={
bands:['Npp'],
min:0,
max:19000,
palette:['bbe029','0a9501','074b03']
};
Map.setCenter(6.746,46.529,3);
Map.addLayer(dataset,visualization,'NPP');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_061_MOD17A3HGF)
[ MOD17A3HGF.061: Terra Net Primary Production Gap-Filled Yearly Global 500m ](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD17A3HGF)
The MOD17A3HGF V6.1 product provides information about annual Gross and Net Primary Productivity (GPP and NPP) at 500m pixel resolution. Annual NPP is derived from the sum of all 8-day Net Photosynthesis(PSN) products (MOD17A2H) from the given year. The PSN value is the difference of the Gross Primary Productivity (GPP) …
MODIS/061/MOD17A3HGF, global,gpp,nasa,npp,photosynthesis,plant-productivity,productivity,psn,terra,usgs,yearly 
2001-01-01T00:00:00Z/2024-01-01T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.5067/MODIS/MOD17A3HGF.061 ](https://doi.org/https://doi.org/10.5067/MODIS/MOD17A3HGF.061)
  * [ https://doi.org/10.5067/MODIS/MOD17A3HGF.061 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD17A3HGF)


