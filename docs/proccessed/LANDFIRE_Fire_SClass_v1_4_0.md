 
#  LANDFIRE SClass (Succession Classes) v1.4.0 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![LANDFIRE/Fire/SClass/v1_4_0](https://developers.google.com/earth-engine/datasets/images/LANDFIRE/LANDFIRE_Fire_SClass_v1_4_0_sample.png) 

Dataset Availability
    2014-09-01T00:00:00Z–2014-09-01T00:00:00Z 

Dataset Provider
     [ U.S. Department of Agriculture's (USDA), U.S. Forest Service (USFS), U.S. Department of the Interior's Geological Survey (USGS), and The Nature Conservancy. ](https://landfire.gov/) 

Earth Engine Snippet
     `    ee.ImageCollection("LANDFIRE/Fire/SClass/v1_4_0")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/LANDFIRE/LANDFIRE_Fire_SClass_v1_4_0) 

Tags
     [doi](https://developers.google.com/earth-engine/datasets/tags/doi) [fire](https://developers.google.com/earth-engine/datasets/tags/fire) [landfire](https://developers.google.com/earth-engine/datasets/tags/landfire) [nature-conservancy](https://developers.google.com/earth-engine/datasets/tags/nature-conservancy) [usda](https://developers.google.com/earth-engine/datasets/tags/usda) [usgs](https://developers.google.com/earth-engine/datasets/tags/usgs) [vegetation](https://developers.google.com/earth-engine/datasets/tags/vegetation) [wildfire](https://developers.google.com/earth-engine/datasets/tags/wildfire)
[Description](https://developers.google.com/earth-engine/datasets/catalog/LANDFIRE_Fire_SClass_v1_4_0#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/LANDFIRE_Fire_SClass_v1_4_0#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/LANDFIRE_Fire_SClass_v1_4_0#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/LANDFIRE_Fire_SClass_v1_4_0#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/LANDFIRE_Fire_SClass_v1_4_0#citations) More
LANDFIRE (LF), Landscape Fire and Resource Management Planning Tools, is a shared program between the wildland fire management programs of the U.S. Department of Agriculture's Forest Service, U.S. Department of the Interior's Geological Survey, and The Nature Conservancy.
Landfire (LF) Historical fire regimes, intervals, and vegetation conditions are mapped using the Vegetation Dynamics Development Tool (VDDT). These data support fire and landscape management planning goals in the National Cohesive Wildland Fire Management Strategy, the Federal Wildland Fire Management Policy, and the Healthy Forests Restoration Act.
The Succession Classes (SClass) layer characterizes current vegetation conditions with respect to the vegetation species composition, cover, and height ranges of successional states that occur within each biophysical setting. SClass can also represent uncharacteristic vegetation components, such as exotic species, that are not found within the compositional or structural variability of successional states defined for a biophysical setting. Succession classes do not directly quantify fuel characteristics of the current vegetation, but rather represent vegetative states with unique succession or disturbance-related dynamics, such as structural development or fire frequency. To produce SClass, the historical reference conditions of these successional states were derived from the vegetation and disturbance dynamics model VDDT (Vegetation Dynamics Development Tool) (LF_1.0.0 CONUS only used the vegetation and disturbance dynamics model LANDSUM). The area contained in succession classes is compared to the simulated historical reference conditions to calculate measurements of vegetation departure, such as fire regime condition class. SClass is used in landscape assessments.
The LANDIFRE Fire datasets include:
  * Fire Regime Groups (FRG) is intended to characterize presumed historical fire regimes within landscapes based on interactions between vegetation dynamics, fire spread, fire effects, and spatial context
  * Mean Fire Return Interval (MFRI) quantifies the average period between fires under the presumed historical fire regime
  * Percent of Low-severity Fire (PLS) image quantifies the amount of low-severity fires relative to mixed- and replacement-severity fires under the presumed historical fire regime and is defined as less than 25 percent average top-kill within a typical fire perimeter for a given vegetation type
  * Percent of Mixed-severity Fire (PMS) layer quantifies the amount of mixed-severity fires relative to low- and replacement-severity fires under the presumed historical fire regime, and is defined as between 25 and 75 percent average top-kill within a typical fire perimeter for a given vegetation type
  * Percent of Replacement-severity Fire (PRS) layer quantifies the amount of replacement-severity fires relative to low- and mixed-severity fires under the presumed historical fire regime, and is defined as greater than 75 percent average top-kill within a typical fire perimeter for a given vegetation type
  * Succession Classes (SClass) layer characterizes current vegetation conditions with respect to the vegetation species composition, cover, and height ranges of successional states that occur within each biophysical setting
  * Vegetation Condition Class (VCC) represents a simple categorization of the associated Vegetation Departure (VDEP) layer and indicates the general level to which current vegetation is different from the simulated historical vegetation reference conditions
  * Vegetation Departure (VDep) indicates how different current vegetation on a landscape is from estimated historical conditions. VDep is based on changes to species composition, structural stage, and canopy closure.


**Pixel Size** 30 meters 
**Bands**
Name | Description  
---|---  
`SClass` | Succession Classes  
**SClass Class Table**
Value | Color | Description  
---|---|---  
1 | #a16333 | Succession Class A  
2 | #38a800 | Succession Class B  
3 | #c9deab | Succession Class C  
4 | #fff8a6 | Succession Class D  
5 | #004a4d | Succession Class E  
6 | #a00000 | Uncharacteristic Native Vegetation Cover / Structure / Composition  
7 | #ff0000 | Uncharacteristic Exotic Vegetation  
111 | #0000ff | Water  
112 | #c8ffff | Snow / Ice  
120 | #8400a8 | Non-burnable Urban  
121 | #e8beff | Burnable Urban  
131 | #4e4e4e | Barren  
132 | #b2b2b2 | Sparsely Vegetated  
180 | #ffff00 | Non-burnable Agriculture  
181 | #ffaa00 | Burnable Agriculture  
**Image Properties**
Name | Type | Description  
---|---|---  
SClass_classes | DOUBLE | Class values of the Succession Classes.  
SClass_names | STRING | Descriptive names of Succession Classes.  
**Terms of Use**
LANDFIRE data are public domain data with no use restrictions, though if modifications or derivatives of the product(s) are created, then please add some descriptive modifier to the data set to avoid confusion.
Citations:
  * The suggested way to cite LANDFIRE products is specific to each product, so the model for citation is provided, with an example for a particular product. Producer. Year released. Product xxxxx:
    * Individual model name.
    * BpS Models and Descriptions, Online. LANDFIRE. Washington, DC. U.S. Department of Agriculture, Forest Service
    * U.S. Department of the Interior; U.S. Geological Survey; Arlington, VA
    * The Nature Conservancy (Producers). Available- URL. Access date.
Example Citation: LANDFIRE Biophysical Settings. 2018. Biophysical setting 14420: South Texas sand sheet grassland. In: LANDFIRE Biophysical Setting Model: Map zone 36, [Online]. In: BpS Models and Descriptions. In: LANDFIRE. Washington, DC: U.S. Department of Agriculture, Forest Service; U.S. Department of the Interior; U.S. Geological Survey; Arlington, VA: The Nature Conservancy (Producers). Available: <https://www.landfire.gov/bps-models.php> [2018, June 27]. Additional guidance on citation of LANDFIRE products can be found [here](https://landfire.gov/data/citation)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/LANDFIRE_Fire_SClass_v1_4_0#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('LANDFIRE/Fire/SClass/v1_4_0');
varvisualization={
bands:['SClass'],
};
Map.setCenter(-121.671,40.699,5);
Map.addLayer(dataset,visualization,'SClass');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/LANDFIRE/LANDFIRE_Fire_SClass_v1_4_0)
[ LANDFIRE SClass (Succession Classes) v1.4.0 ](https://developers.google.com/earth-engine/datasets/catalog/LANDFIRE_Fire_SClass_v1_4_0)
LANDFIRE (LF), Landscape Fire and Resource Management Planning Tools, is a shared program between the wildland fire management programs of the U.S. Department of Agriculture's Forest Service, U.S. Department of the Interior's Geological Survey, and The Nature Conservancy. Landfire (LF) Historical fire regimes, intervals, and vegetation conditions are mapped using …
LANDFIRE/Fire/SClass/v1_4_0, doi,fire,landfire,nature-conservancy,usda,usgs,vegetation,wildfire 
2014-09-01T00:00:00Z/2014-09-01T00:00:00Z
17.52 -175.1 71.48 -63.66 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://landfire.gov/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/LANDFIRE_Fire_SClass_v1_4_0)


