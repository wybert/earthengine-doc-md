 
#  ee.FeatureCollection.bounds 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-bounds#examples)


Constructs a bounding box around the geometries in a collection. 
Usage| Returns  
---|---  
`FeatureCollection.bounds( _maxError_, _proj_)`| Geometry  
Argument| Type| Details  
---|---|---  
this: `collection`| FeatureCollection| The collection whose bounds will be constructed.  
`maxError`| ErrorMargin, optional| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, optional| If specified, the result will be in this projection. Otherwise it will be in EPSG:4326.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-bounds#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-bounds#colab-python-sample) More
```
// FeatureCollection of power plants in Belgium.
varfc=ee.FeatureCollection('WRI/GPPD/power_plants')
.filter('country_lg == "Belgium"');
print('Bounds of Belgium power plants:',fc.bounds());// ee.Geometry
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# FeatureCollection of power plants in Belgium.
fc = ee.FeatureCollection('WRI/GPPD/power_plants').filter(
  'country_lg == "Belgium"')
print('Bounds of Belgium power plants:', fc.bounds().getInfo()) # ee.Geometry
```

