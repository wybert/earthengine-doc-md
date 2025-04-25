 
#  Global map of forest types 2020 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![JRC/GFC2020_subtypes/V0](https://developers.google.com/earth-engine/datasets/images/JRC/JRC_GFC2020_subtypes_V0_sample.png) 

Dataset Availability
    2020-01-01T00:00:00Z–2020-12-31T23:59:59Z 

Dataset Provider
     [ Joint Research Centre, European Commission ](https://forest-observatory.ec.europa.eu/forest/) 

Earth Engine Snippet
     `    ee.ImageCollection("JRC/GFC2020_subtypes/V0")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/JRC/JRC_GFC2020_subtypes_V0) 

Cadence
    1 Year 

Tags
     [eudr](https://developers.google.com/earth-engine/datasets/tags/eudr) [forest](https://developers.google.com/earth-engine/datasets/tags/forest) [forest-biomass](https://developers.google.com/earth-engine/datasets/tags/forest-biomass) [jrc](https://developers.google.com/earth-engine/datasets/tags/jrc) [landcover](https://developers.google.com/earth-engine/datasets/tags/landcover) [primary-forest](https://developers.google.com/earth-engine/datasets/tags/primary-forest)
[Description](https://developers.google.com/earth-engine/datasets/catalog/JRC_GFC2020_subtypes_V0#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/JRC_GFC2020_subtypes_V0#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/JRC_GFC2020_subtypes_V0#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/JRC_GFC2020_subtypes_V0#citations) More
The global map of forest types provides a spatially explicit representation of primary forest, naturally regenerating forest and planted forest (including plantation forest) for the year 2020 at 10m spatial resolution. The base layer for mapping these forest types is the extent of forest cover of version 1 of the Global Forest Cover map for year 2020 (JRC GFC 2020). The definitions of the forest types follow the definitions of the Regulation from the European Union "on the making available on the Union market and the export from the Union of certain commodities and products associated with deforestation and forest degradation" (EUDR, Regulation (EU) 2023/1115), which are similar to characteristics and specific forest categories from the FAO Global Forest Resources Assessment. The year 2020 corresponds to the cut-off date of the EUDR.
In the context of the EUDR, the global forest types map can be used as a non-mandatory, non-exclusive and not legally binding source of information, namely in the phase of risk assessment by operators and traders. Further information about the map and its use can be found on the EU Observatory on Deforestation and Forest Degradation. The definition of forest degradation under the EUDR implies that for year 2020 it is only necessary to assess the presence of primary forests and naturally regenerating forests; all other forests, including plantation forests, were mapped under class "planted forests". Class "other wooded land" exists only outside the extent of forest cover in the Global Forest Cover map for year 2020 and is therefore not mapped in GFT 2020.
Data for deriving a harmonized, globally consistent representation of forest types are scarce, and mapping of the respective forest types from Earth Observation data is challenging. This map of global forest types is released as a preliminary version (version 0) for feedback by the user community that is concerned or interested in the issue of forest degradation under the EUDR. Based on expected feedback and future additional or improved data sets, the JRC aims to produce a consolidated map during year 2025.
The global map of forest types v0 combines available global datasets (wall-to-wall or global in their scope) that indicate or are proxies for the four main forest types The main data layers that are used to delineate primary forests in GFT 2020 are:
  1. The Forest Landscape Integrity Index in 2019
  2. Map of undisturbed tropical mangroves in 2020 and degradation and deforestation in tropical moist forests from 1990 to 2020 (from JRC-TMF)
  3. Map of Intact Forest Landscapes 2020
  4. World Database on Protected Areas
  5. The European Primary Forest Dataset from Sabatini et al. 2021
  6. Global tree cover loss from 2001 to 2020 in combination with the map of drivers of global forest loss
  7. A map on global mining land use.


The main layers to map planted forests (including plantation forests) are:
  1. The WRI Spatial Database on Planted Trees (version 2.1)
  2. IIASA Forest Management classes on planted/plantation forest
  3. The Global Forest Canopy Height dataset in 2019
  4. global tree cover in 2000 and loss from 2001 to 2020.


The global input layers and mapping approach are described in [this technical report](https://op.europa.eu/en/publication-detail/-/publication/e2c286ac-14e9-11f0-b1a3-01aa75ed71a1/language-en).
For a list of known issues please refer to [this website](https://forobs.jrc.ec.europa.eu/GFC).
**Pixel Size** 10 meters 
**Bands**
Name | Description  
---|---  
`Map` | Global forest types 2020  
**Map Class Table**
Value | Color | Description  
---|---|---  
1 | #78c679 | Naturally regenerating forest  
10 | #006837 | Primary forest  
20 | #cc6600 | Planted/Plantation forest  
**Terms of Use**
The data may be used by anyone, anywhere, anytime without permission, license or royalty payment. Attribution using the recommended citation is requested.
Citations:
  * Bourgoin, Clement; Verhegghen, Astrid; Carboni, Silvia; Ameztoy, Iban; Ceccherini, Guido; Colditz, Rene; Achard, Frederic (2024): Global map of forest types 2020 - version 0. European Commission, Joint Research Centre (JRC) [Dataset] PID: <http://data.europa.eu/89h/037ca376-ba92-49db-a8f7-0c277c1e5436>.
  * Bourgoin, C., Verhegghen, A., Carboni, S., Degreve, L., Ameztoy Aramendi, I., Ceccherini, G., Colditz, R. and Achard, F., Global Forest Maps for the Year 2020 to Support the EU Regulation on Deforestation-free Supply Chains, Publications Office of the European Union, Luxembourg, 2025, <https://data.europa.eu/doi/10.2760/1975879>, JRC141702.


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/JRC_GFC2020_subtypes_V0#code-editor-javascript-sample) More
```
functionrgb(r,g,b){
varbin=r << 16|g << 8|b;
return(function(h){
returnnewArray(7-h.length).join('0')+h;
})(bin.toString(16).toUpperCase());
}
varPALETTE=
[
rgb(255,255,255),rgb(120,198,121),rgb(0,0,0),rgb(0,0,0),
rgb(0,0,0),rgb(0,0,0),rgb(0,0,0),rgb(0,0,0),
rgb(0,0,0),rgb(0,0,0),rgb(0,104,55),rgb(0,0,0),
rgb(0,0,0),rgb(0,0,0),rgb(0,0,0),rgb(0,0,0),
rgb(0,0,0),rgb(0,0,0),rgb(0,0,0),rgb(0,0,0),
rgb(204,102,0)
]
//**Legend
// value 1 - Naturally regenerating forest
// value 10 - Primary forest
// value 20 - Planted/Plantation forest
varGFT2020=ee.ImageCollection('JRC/GFC2020_subtypes/V0').mosaic()
Map.addLayer(
GFT2020,{min:0,max:20,palette:PALETTE},
'EC JRC Global forest types 2020 – V0')
Map.setOptions('SATELLITE')
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/JRC/JRC_GFC2020_subtypes_V0)
[ Global map of forest types 2020 ](https://developers.google.com/earth-engine/datasets/catalog/JRC_GFC2020_subtypes_V0)
The global map of forest types provides a spatially explicit representation of primary forest, naturally regenerating forest and planted forest (including plantation forest) for the year 2020 at 10m spatial resolution. The base layer for mapping these forest types is the extent of forest cover of version 1 of the …
JRC/GFC2020_subtypes/V0, eudr,forest,forest-biomass,jrc,landcover,primary-forest 
2020-01-01T00:00:00Z/2020-12-31T23:59:59Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://forest-observatory.ec.europa.eu/forest/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/JRC_GFC2020_subtypes_V0)


