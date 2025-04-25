 
#  SBTN Natural Lands Map v1.1 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![WRI/SBTN/naturalLands/v1_1/2020](https://developers.google.com/earth-engine/datasets/images/WRI/WRI_SBTN_naturalLands_v1_1_2020_sample.png) 

Dataset Availability
    2020-01-01T00:00:00Z–2020-12-31T23:59:59Z 

Dataset Provider
     [ WRI ](https://github.com/wri/natural-lands-map/tree/main) 

Earth Engine Snippet
     `    ee.Image("WRI/SBTN/naturalLands/v1_1/2020")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/WRI/WRI_SBTN_naturalLands_v1_1_2020) 

Tags
     [ecosystems](https://developers.google.com/earth-engine/datasets/tags/ecosystems) [landcover](https://developers.google.com/earth-engine/datasets/tags/landcover) [landuse-landcover](https://developers.google.com/earth-engine/datasets/tags/landuse-landcover) [wri](https://developers.google.com/earth-engine/datasets/tags/wri)
[Description](https://developers.google.com/earth-engine/datasets/catalog/WRI_SBTN_naturalLands_v1_1_2020#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/WRI_SBTN_naturalLands_v1_1_2020#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/WRI_SBTN_naturalLands_v1_1_2020#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/WRI_SBTN_naturalLands_v1_1_2020#citations) More
The SBTN Natural Lands Map v1.1 is a 2020 baseline map of natural and non-natural land covers intended for use by companies setting [science-based targets for nature](https://sciencebasedtargetsnetwork.org/companies/take-action/), specifically the SBTN Land target #1: no conversion of natural ecosystems.
"Natural" and "non-natural" definitions were adapted from the [Accountability Framework initiative's definition of a natural ecosystem](https://accountability-framework.org/use-the-accountability-framework/definitions/natural-ecosystem/) as "one that substantially resembles - in terms of species composition, structure, and ecological function - what would be found in a given area in the absence of major human impacts" and can include managed ecosystems as well as degraded ecosystems that are expected to regenerate either naturally or through management (AFi 2024). The SBTN Natural Lands Map operationalizes this definition by using proxies based on available data that align with AFi guidance to the extent possible.
This map was made by compiling existing global and regional data.You can find the full technical note explaining the methodology linked on the [Natural Lands GitHub](https://github.com/wri/natural-lands-map). This work was a collaboration between Land & Carbon Lab at the World Resources Institute, World Wildlife Fund US, Systemiq, and SBTN.
**Pixel Size** 30 meters 
**Bands**
Name | Min | Max | Description  
---|---|---|---  
`classification` |  2  |  21  | Land cover classification.  
`natural` |  0  |  1  | Land cover classification.  
**classification Class Table**
Value | Color | Description  
---|---|---  
2 | #246E24 | natural forests  
3 | #B9B91E | natural short vegetation  
4 | #6BAED6 | natural water  
5 | #06A285 | mangroves  
6 | #FEFECC | bare  
7 | #ACD1E8 | snow  
8 | #589558 | wet natural forests  
9 | #093D09 | natural peat forests  
10 | #DBDB7B | wet natural short vegetation  
11 | #99991A | natural peat short vegetation  
12 | #D3D3D3 | crop  
13 | #D3D3D3 | built  
14 | #D3D3D3 | non-natural tree cover  
15 | #D3D3D3 | non-natural short vegetation  
16 | #D3D3D3 | non-natural water  
17 | #D3D3D3 | wet non-natural tree cover  
18 | #D3D3D3 | non-natural peat tree cover  
19 | #D3D3D3 | wet non-natural short vegetation  
20 | #D3D3D3 | non-natural peat short vegetation  
21 | #D3D3D3 | non-natural bare  
**natural Class Table**
Value | Color | Description  
---|---|---  
0 | #969696 | Non-natural land  
1 | #a8ddb5 | Natural land  
**Terms of Use**
[CC-BY-SA-4.0](https://spdx.org/licenses/CC-BY-SA-4.0.html)
Citations:
  * Mazur, E., M. Sims, E. Goldman, M. Schneider, M.D. Pirri, C.R. Beatty, F. Stolle, M. Stevenson. 2025. "SBTN Natural Lands Map v1.1: Technical Documentation". Science Based Targets for Land Version 1 - Supplementary Material. Science Based Targets Network. <https://sciencebasedtargetsnetwork.org/wp-content/uploads/2025/02/Technical-Guidance-2025-Step3-Land-v1_1-Natural-Lands-Map.pdf>


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/WRI_SBTN_naturalLands_v1_1_2020#code-editor-javascript-sample) More
```
vardataset=ee.Image('WRI/SBTN/naturalLands/v1_1/2020').select('natural');
varlon=0;
varlat=0;
Map.setCenter(lon,lat,2);
Map.addLayer(dataset,{},'Natural Lands');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/WRI/WRI_SBTN_naturalLands_v1_1_2020)
[ SBTN Natural Lands Map v1.1 ](https://developers.google.com/earth-engine/datasets/catalog/WRI_SBTN_naturalLands_v1_1_2020)
The SBTN Natural Lands Map v1.1 is a 2020 baseline map of natural and non-natural land covers intended for use by companies setting science-based targets for nature, specifically the SBTN Land target #1: no conversion of natural ecosystems. "Natural" and "non-natural" definitions were adapted from the Accountability Framework initiative's definition …
WRI/SBTN/naturalLands/v1_1/2020, ecosystems,landcover,landuse-landcover,wri 
2020-01-01T00:00:00Z/2020-12-31T23:59:59Z
-60 -180 75 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://github.com/wri/natural-lands-map/tree/main)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/WRI_SBTN_naturalLands_v1_1_2020)


