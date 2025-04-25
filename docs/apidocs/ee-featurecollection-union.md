 
#  ee.FeatureCollection.union 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-union#examples)


Merges all geometries in a given collection into one and returns a collection containing a single feature with only an ID of 'union_result' and a geometry. 
Usage| Returns  
---|---  
`FeatureCollection.union( _maxError_)`| FeatureCollection  
Argument| Type| Details  
---|---|---  
this: `collection`| FeatureCollection| The collection being merged.  
`maxError`| ErrorMargin, default: null| The maximum error allowed when performing any necessary reprojections. If not specified, defaults to the error margin requested from the output.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-union#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-union#colab-python-sample) More
```
// FeatureCollection of power plants in Belgium.
varfc=ee.FeatureCollection('WRI/GPPD/power_plants')
.filter('country_lg == "Belgium"');
print('Original FeatureCollection',fc);
// Merge all geometries into one. A FeatureCollection with a single feature
// with no properties is returned.
print('All geometries merged into one',fc.union(1));
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
print('Original FeatureCollection:', fc.getInfo())
# Merge all geometries into one. A FeatureCollection with a single feature
# with no properties is returned.
print('All geometries merged into one:', fc.union(1).getInfo())
```

