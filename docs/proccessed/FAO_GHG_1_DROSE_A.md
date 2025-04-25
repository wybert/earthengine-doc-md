 
#  Drained Organic Soils Emissions (Annual) 1.0 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![FAO/GHG/1/DROSE_A](https://developers.google.com/earth-engine/datasets/images/FAO/FAO_GHG_1_DROSE_A_sample.png) 

Dataset Availability
    1992-01-01T00:00:00Z–2018-01-01T00:00:00Z 

Dataset Provider
     [ FAO UN ](http://fao.org/economic/ess/environment/data/organic-soils/la/) 

Earth Engine Snippet
     `    ee.ImageCollection("FAO/GHG/1/DROSE_A")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/FAO/FAO_GHG_1_DROSE_A) 

Cadence
    1 Year 

Tags
     [agriculture](https://developers.google.com/earth-engine/datasets/tags/agriculture) [climate](https://developers.google.com/earth-engine/datasets/tags/climate) [climate-change](https://developers.google.com/earth-engine/datasets/tags/climate-change) [emissions](https://developers.google.com/earth-engine/datasets/tags/emissions) [fao](https://developers.google.com/earth-engine/datasets/tags/fao) [ghg](https://developers.google.com/earth-engine/datasets/tags/ghg) [organic-soils](https://developers.google.com/earth-engine/datasets/tags/organic-soils)
[Description](https://developers.google.com/earth-engine/datasets/catalog/FAO_GHG_1_DROSE_A#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/FAO_GHG_1_DROSE_A#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/FAO_GHG_1_DROSE_A#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/FAO_GHG_1_DROSE_A#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/FAO_GHG_1_DROSE_A#dois) More
The two related FAO datasets on Drained Organic Soils provide estimates of:
  1. DROSA-A: area of Organic Soils (in hectares) drained for agricultural activities (cropland and grazed grassland)
  2. DROSE-A: carbon (C) and nitrous oxide (N2O) estimates (in gigagrams) from the agricultural drainage of organic soils under these land uses.


Annual data are available at 0.0083333 X 0.0083333 resolution (~1 km at the equator), with global coverage for the period 1992 - 2018.
FAOSTAT estimates follow the Intergovernmental Panel on Climate Change Guidelines (IPCC) and use histosols as proxy for the presence of organic soils and annual land cover maps as time- dependent component. Additionally, soils characteristics, land use, and climate information are applied in the analysis. The carbon emissions can be converted to CO2, multiplying pixel values by the ratio of the molecular weight of carbon dioxide (CO2) to that of C (44/12).
Organic soils develop in wet soil ecosystems. They include tropical and boreal peatlands, high-latitude bogs, ferns, and mires. Organic soils cover globally a mere 3 percent of the terrestrial land area but represent up to 30 percent of the total soil carbon, thus playing an important role in maintaining the earth's carbon balance. Agriculture is a major cause of drainage of organic soils around the world. Drainage exposes to aerobic conditions the organic matter of organic soils that oxidizes releasing large amounts of harmful greenhouse gases (GHG) to the atmosphere.
DROSA-A and DROSE-A are the basis for country and regional statistics on drained organic soils disseminated in three FAOSTAT datasets (Cultivation of Organic Soils; Cropland; and Grassland).
**Pixel Size** 927.67 meters 
**Bands**
Name | Units | Description  
---|---|---  
`croplandc` | Gg | C emissions from cropland organic soils  
`croplandn2o` | Gg | N2O emissions from cropland organic soils  
`grasslandc` | Gg | C emissions from grassland organic soils  
`grasslandn2o` | Gg | N2O emissions from grassland organic soils  
**Terms of Use**
The Food and Agriculture Organization of the United Nations (FAO) is mandated to collect, analyze, interpret, and disseminate information related to nutrition, food, and agriculture. In this regard, it publishes a number of databases on topics related to FAO's mandate, and encourages the use of them for scientific and research purposes. Consistent with the principles of openness and sharing envisioned under the Open Data Licensing For Statistical Databases, and consistent with the mandate of FAO, data on GHG emissions from agriculture activities on organic soils as part of FAOSTAT - FAO's database on Food and Agriculture data, is available free to the user community.
Citations:
  * FAO 2020. Drained organic soils 1990 - 2019. Global, regional and country trends. FAOSTAT Analytical Brief Series No 4, FAO, Rome. <http://www.fao.org/3/cb0489en/cb0489en.pdf>
  * Conchedda, G. and Tubiello, F. N.: Drainage of organic soils and GHG emissions: Validation with country data, Earth Syst. Sci. Data Discuss. [doi:10.5194/essd-12-3113-2020](https://doi.org/10.5194/essd-12-3113-2020), 2020


  * [ https://doi.org/10.5194/essd-12-3113-2020 ](https://doi.org/10.5194/essd-12-3113-2020)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/FAO_GHG_1_DROSE_A#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('FAO/GHG/1/DROSE_A');
varvisualization={
bands:['croplandc'],
min:0,
max:1,
palette:['yellow','red']
};
Map.setCenter(108.0,-0.4,6);
Map.addLayer(dataset,visualization,'Cropland C emissions (Annual)');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/FAO/FAO_GHG_1_DROSE_A)
[ Drained Organic Soils Emissions (Annual) 1.0 ](https://developers.google.com/earth-engine/datasets/catalog/FAO_GHG_1_DROSE_A)
The two related FAO datasets on Drained Organic Soils provide estimates of: DROSA-A: area of Organic Soils (in hectares) drained for agricultural activities (cropland and grazed grassland) DROSE-A: carbon (C) and nitrous oxide (N2O) estimates (in gigagrams) from the agricultural drainage of organic soils under these land uses. Annual data …
FAO/GHG/1/DROSE_A, agriculture,climate,climate-change,emissions,fao,ghg,organic-soils 
1992-01-01T00:00:00Z/2018-01-01T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.5194/essd-12-3113-2020 ](https://doi.org/http://fao.org/economic/ess/environment/data/organic-soils/la/)
  * [ https://doi.org/10.5194/essd-12-3113-2020 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/FAO_GHG_1_DROSE_A)


