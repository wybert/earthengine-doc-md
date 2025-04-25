 
#  WCMC Above and Below Ground Biomass Carbon Density 
Stay organized with collections  Save and categorize content based on your preferences. 
![WCMC/biomass_carbon_density/v1_0](https://developers.google.com/earth-engine/datasets/images/WCMC/WCMC_biomass_carbon_density_v1_0_sample.png) 

Dataset Availability
    2010-01-01T00:00:00Z–2010-12-31T00:00:00Z 

Dataset Provider
     [ UNEP-WCMC (UN Environment Programme World Conservation Monitoring Centre) ](https://doi.org/10.34892/rh7v-hg80) 

Earth Engine Snippet
     `    ee.ImageCollection("WCMC/biomass_carbon_density/v1_0")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/WCMC/WCMC_biomass_carbon_density_v1_0) 

Tags
     [biomass](https://developers.google.com/earth-engine/datasets/tags/biomass) [carbon](https://developers.google.com/earth-engine/datasets/tags/carbon) [forest-biomass](https://developers.google.com/earth-engine/datasets/tags/forest-biomass) [wcmc](https://developers.google.com/earth-engine/datasets/tags/wcmc)
unep
#### Description
This dataset represents above- and below-ground terrestrial carbon storage (tonnes (t) of C per hectare (ha)) for circa 2010. The dataset was constructed by combining the most reliable publicly available datasets and overlaying them with the ESA CCI landcover map for the year 2010 (ESA, 2017), assigning to each grid cell the corresponding above-ground biomass value from the biomass map that was most appropriate for the grid cell's landcover type. Input carbon datasets were identified through a literature review of existing datasets on biomass carbon in terrestrial ecosystems published in peer-reviewed literature. To determine which datasets to combine to produce the global carbon density map, identified datasets were evaluated based on resolution, accuracy, biomass definition and reference date (see Table 1 in paper cited for further information on datasets selected). After aggregating each selected dataset to a nominal scale of 300 m resolution, forest categories in the CCI ESA 2010 landcover dataset were used to extract above-ground biomass from Santoro et al. 2018 for forest areas. Woodland and savanna biomass were then incorporated for Africa from Bouvet et al. 2018., and from Santoro et al. 2018 for areas outside of Africa and outside of forest. Biomass from croplands, sparse vegetation and grassland landcover classes from CCI ESA, in addition to shrubland areas outside Africa missing from Santoro et al. 2018, were extracted from were extracted from Xia et al. 2014. and Spawn et al. 2017 averaged by ecological zone for each landcover type. Below-ground biomass were added using root-to-shoot ratios from the 2006 IPCC guidelines for National Greenhouse Gas Inventories (IPCC, 2006). No below-ground values were assigned to croplands as ratios were unavailable. Above-and-below-ground biomass were then summed together and multiplied by 0.5 to convert to carbon, generating a single above-and-below-ground biomass carbon layer. This dataset has not been validated.
References:
  * Bouvet, A. et al. 2018. An above-ground biomass map of African savannahs and woodlands at 25 m resolution derived from ALOS PALSAR. Remote Sensing of the Environment 206, 156-173.
  * ESA (2017) [Land Cover CCI Product User Guide Version 2. Tech. Rep.](https://maps.elie.ucl.ac.be/CCI/viewer/download/ESACCI-LC-Ph2-PUGv2_2.0.pdf).
  * IPCC (2006) 2006 IPCC guidelines for national greenhouse gas inventories (eds HS Eggleston, L Buendia, K Miwa, T Ngara, K Tanabe.) Kanagawa, Japan: IGES.
  * Santoro, M. et al. (2018). A detailed portrait of the forest aboveground biomass pool for the year 2010 obtained from multiple remote sensing observations. Geophysical Research Abstracts 20, EGU2018-EG18932.
  * Spawn SA et al. (2017) New global biomass map for the year 2010. New Orleans, LA: American Geophysical Union.
  * Xia, J. et al. (2014) Spatio-temporal patterns and climate variables controlling of biomass carbon stock of global grassland ecosystems from 1982 to 2006. Remote Sensing 6, 1783-1802.


Provider's note: The UN Environment Programme World Conservation Monitoring Centre (UNEP-WCMC) carbon biomass dataset represents conditions between 1982 and 2010 depending on land cover type. The relative patterns of carbon stocks are well represented with this dataset. The [NASA/ORNL carbon biomass dataset](https://daac.ornl.gov/VEGETATION/guides/Global_Maps_C_Density_2010.html) represents biomass conditions for 2010, with uncertainty estimates at the pixel-level. Additional biomass of non-dominant land cover types are represented within each pixel. For more detailed information, please refer to the papers describing each dataset: WCMC [(Soto-Navarro et al. 2020)](https://royalsocietypublishing.org/doi/full/10.1098/rstb.2019.0128) and [NASA/ORNL](https://developers.google.com/earth-engine/datasets/catalog/NASA_ORNL_biomass_carbon_density_v1) [(Spawn et al. 2020)](https://www.nature.com/articles/s41597-020-0444-4).
### Bands
**Bands**
Name | Min | Max | Pixel Size | Description  
---|---|---|---|---  
`carbon_tonnes_per_ha` |  0  |  445.5  |  300 meters  | Tonnes of above and below ground biomass carbon per hectare  
### Terms of Use
**Terms of Use**
These data are subject to Attribution-ShareAlike 4.0 International (CC BY-SA 4.0). Details can be found [here.](https://creativecommons.org/licenses/by-sa/4.0/)
### Citations
Citations:
  * Soto-Navarro C., Ravilious C., Arnell A., de Lamo X., Harfoot M., Hill S. L. L., Wearn O. R., Santoro M., Bouvet A., Mermoz S., Le Toan T., Xia J., Liu S., Yuan W., Spawn S. A., Gibbs H. K., Ferrier S., Harwood T., Alkemade R., Schipper A. M., Schmidt-Traub G., Strassburg B., Miles L., Burgess N. D. and Kapos V. (2020) Mapping co-benefits for carbon storage and biodiversity to inform conservation policy and action. Philosophical Transactions of the Royal Society B. 375 [Link](https://doi.org/10.1098/rstb.2019.0128)


### DOIs
  * [ https://doi.org/10.34892/rh7v-hg80 ](https://doi.org/10.34892/rh7v-hg80)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
### Code Editor (JavaScript)
```
varimage=ee.Image('WCMC/biomass_carbon_density/v1_0/2010');
Map.addLayer(ee.Image(1),{min:0,max:1},'base_map');
Map.addLayer(
image,{
min:1,
max:180,
palette:['d9f0a3','addd8e','78c679','41ab5d','238443','005a32']
},
'carbon_tonnes_per_ha');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/WCMC/WCMC_biomass_carbon_density_v1_0)
[ WCMC Above and Below Ground Biomass Carbon Density ](https://developers.google.com/earth-engine/datasets/catalog/WCMC_biomass_carbon_density_v1_0)
This dataset represents above- and below-ground terrestrial carbon storage (tonnes (t) of C per hectare (ha)) for circa 2010. The dataset was constructed by combining the most reliable publicly available datasets and overlaying them with the ESA CCI landcover map for the year 2010 (ESA, 2017), assigning to each grid …
WCMC/biomass_carbon_density/v1_0, biomass,carbon,forest-biomass,wcmc 
2010-01-01T00:00:00Z/2010-12-31T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.34892/rh7v-hg80 ](https://doi.org/https://doi.org/10.34892/rh7v-hg80)
  * [ https://doi.org/10.34892/rh7v-hg80 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/WCMC_biomass_carbon_density_v1_0)


