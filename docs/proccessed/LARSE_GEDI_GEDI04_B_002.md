 
#  GEDI L4B Gridded Aboveground Biomass Density (Version 2) 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![LARSE/GEDI/GEDI04_B_002](https://developers.google.com/earth-engine/datasets/images/LARSE/LARSE_GEDI_GEDI04_B_002_sample.png) 

Dataset Availability
    2019-04-18T00:00:00Z–2021-08-04T00:00:00Z 

Dataset Provider
     [ USFS Laboratory for Applications of Remote Sensing in Ecology (LARSE) ](https://www.fs.usda.gov/) [ NASA GEDI mission, accessed through the USGS LP DAAC ](https://lpdaac.usgs.gov/products/gedi02_av002/) 

Earth Engine Snippet
     `    ee.Image("LARSE/GEDI/GEDI04_B_002")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/LARSE/LARSE_GEDI_GEDI04_B_002) 

Tags
     [elevation](https://developers.google.com/earth-engine/datasets/tags/elevation) [forest-biomass](https://developers.google.com/earth-engine/datasets/tags/forest-biomass) [gedi](https://developers.google.com/earth-engine/datasets/tags/gedi) [larse](https://developers.google.com/earth-engine/datasets/tags/larse) [nasa](https://developers.google.com/earth-engine/datasets/tags/nasa) [tree-cover](https://developers.google.com/earth-engine/datasets/tags/tree-cover) [usgs](https://developers.google.com/earth-engine/datasets/tags/usgs)
[Description](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI04_B_002#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI04_B_002#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI04_B_002#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI04_B_002#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI04_B_002#dois) More
This Global Ecosystem Dynamics Investigation (GEDI) L4B product provides 1 km x 1 km estimates of mean aboveground biomass density (AGBD) based on observations from mission week 19 starting on 2019-04-18 to mission week 138 ending on 2021-08-04. The GEDI L4A Footprint Biomass product converts each high-quality waveform to an AGBD prediction, and the L4B product uses the sample present within the borders of each 1 km cell to statistically infer mean AGBD.
Please see [User Guide](https://daac.ornl.gov/GEDI/guides/GEDI_L4B_Gridded_Biomass.html) for more information.
The Global Ecosystem Dynamics Investigation [GEDI](https://gedi.umd.edu/) mission aims to characterize ecosystem structure and dynamics to enable radically improved quantification and understanding of the Earth's carbon cycle and biodiversity. The GEDI instrument, attached to the International Space Station (ISS), collects data globally between 51.6° N and 51.6° S latitudes at the highest resolution and densest sampling of the 3-dimensional structure of the Earth. The GEDI instrument consists of three lasers producing a total of eight beam ground transects, which instantaneously sample eight ~25 m footprints spaced approximately every 60 m along-track.
Product | Description  
---|---  
L2A Vector | [LARSE/GEDI/GEDI02_A_002](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI02_A_002)  
L2A Monthly raster | [LARSE/GEDI/GEDI02_A_002_MONTHLY](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI02_A_002_MONTHLY)  
L2A table index | [LARSE/GEDI/GEDI02_A_002_INDEX](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI02_A_002_INDEX)  
L2B Vector | [LARSE/GEDI/GEDI02_B_002](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI02_B_002)  
L2B Monthly raster | [LARSE/GEDI/GEDI02_B_002_MONTHLY](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI02_B_002_MONTHLY)  
L2B table index | [LARSE/GEDI/GEDI02_B_002_INDEX](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI02_B_002_INDEX)  
L4A Biomass Vector | [LARSE/GEDI/GEDI04_A_002](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI04_A_002)  
L4A Monthly raster | [LARSE/GEDI/GEDI04_A_002_MONTHLY](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI04_A_002_MONTHLY)  
L4A table index | [LARSE/GEDI/GEDI04_A_002_INDEX](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI04_A_002_INDEX)  
L4B Biomass | [LARSE/GEDI/GEDI04_B_002](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI04_B_002)  
**Pixel Size** 1000 meters 
**Bands**
Name | Units | Description  
---|---|---  
`MU` | Mg/ha | Mean aboveground biomass density (MU): Estimated mean AGBD for the 1 km grid cell, including forest and non-forest.  
`V1` | Variance component 1 (V1): Uncertainty in the estimate of mean biomass due to the field-to-GEDI model used in L4A.  
`V2` | Variance component 2 (V2)
  * If Mode of Inference = 1, this is the uncertainty due to GEDI's sampling of the 1 km cell.
  * If Mode of Inference = 2, this is uncertainty owing to the model predicting biomass using wall-to-wall data, calibrated with the L4A footprint product.

  
`SE` | Mg/ha | Mean aboveground biomass density standard error (SE): Standard Error of the mean estimate, combining sampling and modeling uncertainty.  
`PE` | % | Standard error as a fraction of the estimated mean AGBD (PE). If >100%, the cell values are truncated to 100.  
`NC` | Number of clusters (NC): Number of unique GEDI ground tracks with at least one high-quality waveform intersecting the grid cell.  
`NS` | Number of samples (NS): Total number of high-quality waveforms across all ground tracks within the grid cell.  
`QF` | Quality flag (QF)
  * 0=Outside the GEDI domain
  * 1=Land surface
  * 2=Land surface and meets GEDI mission L1 requirement (Percent standard error <20% or Standard Error < 20 Mg ha-1)

  
`PS` | Prediction stratum (PS) determined by plant functional type and continent. PS is associated with an L4A model parameter covariance matrix that contributes to the Model Error Variance (Table 2).  
`MI` | Mode of interference (MI): Method used for a particular cell. Until mission completion, only those cells where hybrid inference is possible will be populated with a mean biomass value.
  * 0=None applied
  * 1=Hybrid Model-Based
  * 2=Generalized Hierarchical Model-Based

  
**Terms of Use**
This dataset is in the public domain and is available without restriction on use and distribution. See [NASA's Earth Science Data & Information Policy](https://www.earthdata.nasa.gov/engage/open-data-services-and-software/data-and-information-policy) for additional information.
Citations:
  * Dubayah, R.O., J. Armston, S.P. Healey, Z. Yang, P.L. Patterson, S. Saarela, G. Stahl, L. Duncanson, and J.R. Kellner. 2022. GEDI L4B Gridded Aboveground Biomass Density, Version 2. ORNL DAAC, Oak Ridge, Tennessee, USA. [doi:10.3334/ORNLDAAC/2056](https://doi.org/10.3334/ORNLDAAC/2056)


  * [ https://doi.org/10.3334/ORNLDAAC/2056 ](https://doi.org/10.3334/ORNLDAAC/2056)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI04_B_002#code-editor-javascript-sample) More
```
varl4b=ee.Image('LARSE/GEDI/GEDI04_B_002')
Map.addLayer(
l4b.select('MU'),
{min:10,max:250,palette:'440154,414387,2a788e,23a884,7ad151,fde725'},
'Mean Biomass');
Map.addLayer(
l4b.select('SE'),
{min:10,max:50,palette:'000004,3b0f6f,8c2981,dd4a69,fe9f6d,fcfdbf'},
'Standard Error');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/LARSE/LARSE_GEDI_GEDI04_B_002)
[ GEDI L4B Gridded Aboveground Biomass Density (Version 2) ](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI04_B_002)
This Global Ecosystem Dynamics Investigation (GEDI) L4B product provides 1 km x 1 km estimates of mean aboveground biomass density (AGBD) based on observations from mission week 19 starting on 2019-04-18 to mission week 138 ending on 2021-08-04. The GEDI L4A Footprint Biomass product converts each high-quality waveform to an …
LARSE/GEDI/GEDI04_B_002, elevation,forest-biomass,gedi,larse,nasa,tree-cover,usgs 
2019-04-18T00:00:00Z/2021-08-04T00:00:00Z
-52 -180 52 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.3334/ORNLDAAC/2056 ](https://doi.org/https://www.fs.usda.gov/)
  * [ https://doi.org/10.3334/ORNLDAAC/2056 ](https://doi.org/https://lpdaac.usgs.gov/products/gedi02_av002/)
  * [ https://doi.org/10.3334/ORNLDAAC/2056 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI04_B_002)


