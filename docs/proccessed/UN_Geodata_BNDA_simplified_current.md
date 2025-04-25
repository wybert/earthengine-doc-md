 
#  United Nations Geospatial Data: BNDA_simplified 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![UN/Geodata/BNDA_simplified/current](https://developers.google.com/earth-engine/datasets/images/UN/UN_Geodata_BNDA_simplified_current_sample.png) 

Dataset Availability
    2023-02-11T00:00:00Z–2023-02-12T00:00:00Z 

Dataset Provider
     [ United Nations Geospatial ](https://geoportal.un.org/arcgis/home/user.html?user=United_Nations_Geospatial) 

Earth Engine Snippet
     FeatureCollection `    ee.FeatureCollection("UN/Geodata/BNDA_simplified/current")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/UN/UN_Geodata_BNDA_simplified_current)      FeatureView  `    ui.Map.FeatureViewLayer("UN/Geodata/BNDA_simplified/current_FeatureView")   ` 

Tags
     [borders](https://developers.google.com/earth-engine/datasets/tags/borders) [countries](https://developers.google.com/earth-engine/datasets/tags/countries) [infrastructure-boundaries](https://developers.google.com/earth-engine/datasets/tags/infrastructure-boundaries) [table](https://developers.google.com/earth-engine/datasets/tags/table)
[Description](https://developers.google.com/earth-engine/datasets/catalog/UN_Geodata_BNDA_simplified_current#description)[Table Schema](https://developers.google.com/earth-engine/datasets/catalog/UN_Geodata_BNDA_simplified_current#table-schema)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/UN_Geodata_BNDA_simplified_current#terms-of-use) More
The United Nations Geospatial Data, or Geodata, is a worldwide geospatial dataset of the United Nations.
The United Nations Geodata is provided to facilitate the preparation of cartographic materials in the United Nations includes geometry, attributes and labels to facilitate the adequate depiction and naming of geographic features for the preparation of maps in accordance with United Nations policies and practices.
The geospatial dataset include polygons/areas of countries (BNDA_simplified). Please refer this [page](https://geoportal.un.org/arcgis/home/item.html?id=e4ee80edac9d4e08b8303522dd4a5fc1) for more information.
**Table Schema**
Name | Type | Description  
---|---|---  
admiso | STRING | ISO-3166 alpha-3 code of the area's administrator.  
geo_cd | INT | UN M49 geographical region code  
georeg | STRING | UN M49 geographic region  
globalid | STRING | GlobalID  
globalid_1 | STRING | GlobalID_1  
int_cd | STRING | UN M49 intermediary region code; 0 if unset  
intreg | STRING | UN M49 intermediary region; empty if "int_cd" is 0  
iso2cd | STRING | ISO-3166 alpha-2 code  
iso3cd | STRING | ISO-3166 alpha-3 code  
lbl_en | STRING | Cartographic label (English)  
lbl_fr | STRING | Cartographic label (French)  
m49_cd | STRING | UN M49 country or area code  
nam_en | STRING | Name (English)  
name_fr | STRING | Name (French)  
objectid | STRING | Internal object ID number  
st_area_sh | DOUBLE | Total area of the geometry  
stscod | INT | Sovereignty status code:
  * 0: Antarctica
  * 1: State
  * 2: Occupied Palestinian Territory
  * 3: Non-Self Governing Territory
  * 4: Territory
  * 5: Special Region or Province
  * 99: Undetermined

  
sub_cd | INT | UN M49 sub-region code  
subreg | STRING | UN M49 sub-region  
**Terms of Use**
The UN Geodata is a global geospatial database available for use by the UN Secretariat and external users. It can be used for various purposes, but commercial use is prohibited. The UN retains ownership of the data, and users must credit the UN as the source in their creations. The data is provided "as is" without warranties, and the UN is not liable for any damages or losses arising from its use. Please refer this [page](https://developers.google.com/earth-engine/datasets/papers/BNDA_terms_of_use.pdf) for more information.
**Note:** Users of the Data that are not subject to the administrative instruction ("Outside Users") may only use the Data for the purpose for which the Data is suitable, as identified by the Geospatial Information Section upon transmission of or granting access to the Data. Intellectual property over the Data shall at all times vest with the United Nations. Intellectual property over the products created using the Data shall vest with the Outside User. The United Nations shall be recognized as the source of the Data in any products created by Outside Users using the Data, unless the Outside Users alter the Data or combine the Data with other data sets. In case of doubt regarding crediting the United Nations as the Data source, please contact: geospatial@un.org. Outside Users acknowledge that any right to access and use the Data is revocable and non-transferable. Under no circumstances may the Data be used for commercial purposes.
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/UN_Geodata_BNDA_simplified_current#code-editor-javascript-sample) More
```
vardataset=ee.FeatureCollection('UN/Geodata/BNDA_simplified/current');
varstyleParams={
fillColor:'b5ffb4',
color:'00909F',
width:1.0,
};
dataset=dataset.style(styleParams);
Map.centerObject(dataset);
Map.addLayer(dataset,{},'BNDA simplified');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/UN/UN_Geodata_BNDA_simplified_current)
[ United Nations Geospatial Data: BNDA_simplified ](https://developers.google.com/earth-engine/datasets/catalog/UN_Geodata_BNDA_simplified_current)
The United Nations Geospatial Data, or Geodata, is a worldwide geospatial dataset of the United Nations. The United Nations Geodata is provided to facilitate the preparation of cartographic materials in the United Nations includes geometry, attributes and labels to facilitate the adequate depiction and naming of geographic features for the …
UN/Geodata/BNDA_simplified/current, borders,countries,infrastructure-boundaries,table 
2023-02-11T00:00:00Z/2023-02-12T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://geoportal.un.org/arcgis/home/user.html?user=United_Nations_Geospatial)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/UN_Geodata_BNDA_simplified_current)


