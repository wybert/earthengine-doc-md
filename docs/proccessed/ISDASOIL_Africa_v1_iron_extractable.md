 
#  iSDAsoil Extractable Iron 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![ISDASOIL/Africa/v1/iron_extractable](https://developers.google.com/earth-engine/datasets/images/ISDASOIL/ISDASOIL_Africa_v1_iron_extractable_sample.png) 

Dataset Availability
    2001-01-01T00:00:00Z–2017-01-01T00:00:00Z 

Dataset Provider
     [ iSDA ](https://isda-africa.com/) 

Earth Engine Snippet
     `    ee.Image("ISDASOIL/Africa/v1/iron_extractable")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/ISDASOIL/ISDASOIL_Africa_v1_iron_extractable) 

Tags
     [africa](https://developers.google.com/earth-engine/datasets/tags/africa) [isda](https://developers.google.com/earth-engine/datasets/tags/isda) [soil](https://developers.google.com/earth-engine/datasets/tags/soil)
iron
[Description](https://developers.google.com/earth-engine/datasets/catalog/ISDASOIL_Africa_v1_iron_extractable#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/ISDASOIL_Africa_v1_iron_extractable#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/ISDASOIL_Africa_v1_iron_extractable#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/ISDASOIL_Africa_v1_iron_extractable#citations) More
Extractable iron at soil depths of 0-20 cm and 20-50 cm, predicted mean and standard deviation.
Pixel values must be back-transformed with `exp(x/10)-1`.
In areas of dense jungle (generally over central Africa), model accuracy is low and therefore artifacts such as banding (striping) might be seen.
Soil property predictions were made by [Innovative Solutions for Decision Agriculture Ltd. (iSDA)](https://isda-africa.com/) at 30 m pixel size using machine learning coupled with remote sensing data and a training set of over 100,000 analyzed soil samples.
Further information can be found in the [FAQ](https://www.isda-africa.com/isdasoil/faq/) and [technical information documentation](https://www.isda-africa.com/isdasoil/technical-information/). To submit an issue or request support, please visit [the iSDAsoil site](https://isda-africa.com/isdasoil).
**Pixel Size** 30 meters 
**Bands**
Name | Units | Min | Max | Description  
---|---|---|---|---  
`mean_0_20` | ppm |  0  |  62  | Iron, extractable, predicted mean at 0-20 cm depth  
`mean_20_50` | ppm |  0  |  47  | Iron, extractable, predicted mean at 20-50 cm depth  
`stdev_0_20` | ppm |  0  |  39  | Iron, extractable, standard deviation at 0-20 cm depth  
`stdev_20_50` | ppm |  0  |  39  | Iron, extractable, standard deviation at 20-50 cm depth  
**Terms of Use**
[CC-BY-4.0](https://spdx.org/licenses/CC-BY-4.0.html)
Citations:
  * Hengl, T., Miller, M.A.E., Križan, J., et al. African soil properties and nutrients mapped at 30 m spatial resolution using two-scale ensemble machine learning. Sci Rep 11, 6130 (2021). [doi:10.1038/s41598-021-85639-y](https://doi.org/10.1038/s41598-021-85639-y)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/ISDASOIL_Africa_v1_iron_extractable#code-editor-javascript-sample) More
```
varmean_0_20=
'<RasterSymbolizer>'+
'<ColorMap type="ramp">'+
'<ColorMapEntry color="#0D0887" label="0-6.4" opacity="1" quantity="20"/>'+
'<ColorMapEntry color="#350498" label="6.4-13.9" opacity="1" quantity="27"/>'+
'<ColorMapEntry color="#5402A3" label="13.9-29" opacity="1" quantity="34"/>'+
'<ColorMapEntry color="#7000A8" label="29-35.6" opacity="1" quantity="36"/>'+
'<ColorMapEntry color="#8B0AA5" label="35.6-43.7" opacity="1" quantity="38"/>'+
'<ColorMapEntry color="#A31E9A" label="43.7-48.4" opacity="1" quantity="39"/>'+
'<ColorMapEntry color="#B93289" label="48.4-53.6" opacity="1" quantity="40"/>'+
'<ColorMapEntry color="#CC4678" label="53.6-59.3" opacity="1" quantity="41"/>'+
'<ColorMapEntry color="#DB5C68" label="59.3-65.7" opacity="1" quantity="42"/>'+
'<ColorMapEntry color="#E97158" label="65.7-72.7" opacity="1" quantity="43"/>'+
'<ColorMapEntry color="#F48849" label="72.7-80.5" opacity="1" quantity="44"/>'+
'<ColorMapEntry color="#FBA139" label="80.5-89" opacity="1" quantity="45"/>'+
'<ColorMapEntry color="#FEBC2A" label="89-98.5" opacity="1" quantity="46"/>'+
'<ColorMapEntry color="#FADA24" label="98.5-108.9" opacity="1" quantity="47"/>'+
'<ColorMapEntry color="#F0F921" label="108.9-1200" opacity="1" quantity="48"/>'+
'</ColorMap>'+
'<ContrastEnhancement/>'+
'</RasterSymbolizer>';
varmean_20_50=
'<RasterSymbolizer>'+
'<ColorMap type="ramp">'+
'<ColorMapEntry color="#0D0887" label="0-6.4" opacity="1" quantity="20"/>'+
'<ColorMapEntry color="#350498" label="6.4-13.9" opacity="1" quantity="27"/>'+
'<ColorMapEntry color="#5402A3" label="13.9-29" opacity="1" quantity="34"/>'+
'<ColorMapEntry color="#7000A8" label="29-35.6" opacity="1" quantity="36"/>'+
'<ColorMapEntry color="#8B0AA5" label="35.6-43.7" opacity="1" quantity="38"/>'+
'<ColorMapEntry color="#A31E9A" label="43.7-48.4" opacity="1" quantity="39"/>'+
'<ColorMapEntry color="#B93289" label="48.4-53.6" opacity="1" quantity="40"/>'+
'<ColorMapEntry color="#CC4678" label="53.6-59.3" opacity="1" quantity="41"/>'+
'<ColorMapEntry color="#DB5C68" label="59.3-65.7" opacity="1" quantity="42"/>'+
'<ColorMapEntry color="#E97158" label="65.7-72.7" opacity="1" quantity="43"/>'+
'<ColorMapEntry color="#F48849" label="72.7-80.5" opacity="1" quantity="44"/>'+
'<ColorMapEntry color="#FBA139" label="80.5-89" opacity="1" quantity="45"/>'+
'<ColorMapEntry color="#FEBC2A" label="89-98.5" opacity="1" quantity="46"/>'+
'<ColorMapEntry color="#FADA24" label="98.5-108.9" opacity="1" quantity="47"/>'+
'<ColorMapEntry color="#F0F921" label="108.9-1200" opacity="1" quantity="48"/>'+
'</ColorMap>'+
'<ContrastEnhancement/>'+
'</RasterSymbolizer>';
varstdev_0_20=
'<RasterSymbolizer>'+
'<ColorMap type="ramp">'+
'<ColorMapEntry color="#fde725" label="low" opacity="1" quantity="1"/>'+
'<ColorMapEntry color="#5dc962" label=" " opacity="1" quantity="2"/>'+
'<ColorMapEntry color="#20908d" label=" " opacity="1" quantity="3"/>'+
'<ColorMapEntry color="#3a528b" label=" " opacity="1" quantity="4"/>'+
'<ColorMapEntry color="#440154" label="high" opacity="1" quantity="6"/>'+
'</ColorMap>'+
'<ContrastEnhancement/>'+
'</RasterSymbolizer>';
varstdev_20_50=
'<RasterSymbolizer>'+
'<ColorMap type="ramp">'+
'<ColorMapEntry color="#fde725" label="low" opacity="1" quantity="1"/>'+
'<ColorMapEntry color="#5dc962" label=" " opacity="1" quantity="2"/>'+
'<ColorMapEntry color="#20908d" label=" " opacity="1" quantity="3"/>'+
'<ColorMapEntry color="#3a528b" label=" " opacity="1" quantity="4"/>'+
'<ColorMapEntry color="#440154" label="high" opacity="1" quantity="6"/>'+
'</ColorMap>'+
'<ContrastEnhancement/>'+
'</RasterSymbolizer>';
varraw=ee.Image("ISDASOIL/Africa/v1/iron_extractable");
Map.addLayer(
raw.select(0).sldStyle(mean_0_20),{},
"Iron, extractable, mean visualization, 0-20 cm");
Map.addLayer(
raw.select(1).sldStyle(mean_20_50),{},
"Iron, extractable, mean visualization, 20-50 cm");
Map.addLayer(
raw.select(2).sldStyle(stdev_0_20),{},
"Iron, extractable, stdev visualization, 0-20 cm");
Map.addLayer(
raw.select(3).sldStyle(stdev_20_50),{},
"Iron, extractable, stdev visualization, 20-50 cm");
varconverted=raw.divide(10).exp().subtract(1);
varvisualization={min:0,max:140};
Map.setCenter(25,-3,2);
Map.addLayer(converted.select(0),visualization,"Iron, extractable, mean, 0-20 cm");
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/ISDASOIL/ISDASOIL_Africa_v1_iron_extractable)
[ iSDAsoil Extractable Iron ](https://developers.google.com/earth-engine/datasets/catalog/ISDASOIL_Africa_v1_iron_extractable)
Extractable iron at soil depths of 0-20 cm and 20-50 cm, predicted mean and standard deviation. Pixel values must be back-transformed with exp(x/10)-1. In areas of dense jungle (generally over central Africa), model accuracy is low and therefore artifacts such as banding (striping) might be seen. Soil property predictions were …
ISDASOIL/Africa/v1/iron_extractable, africa,isda,soil 
2001-01-01T00:00:00Z/2017-01-01T00:00:00Z
-35.22 -31.46 37.98 57.08 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://isda-africa.com/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/ISDASOIL_Africa_v1_iron_extractable)


