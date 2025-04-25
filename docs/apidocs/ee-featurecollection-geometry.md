 
#  ee.FeatureCollection.geometry 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-geometry#examples)


Extracts and merges the geometries of a collection. Requires that all the geometries in the collection share the projection and edge interpretation. **Caution:** providing a large or complex collection as input can result in poor performance. Collating the geometry of collections does not scale well; use the smallest collection that is required to achieve the desired outcome.**Note:** If only a bounding box around the collection is needed, consider using Collection.bounds instead.
Usage| Returns  
---|---  
`FeatureCollection.geometry( _maxError_)`| Geometry  
Argument| Type| Details  
---|---|---  
this: `collection`| FeatureCollection| The collection whose geometries will be extracted.  
`maxError`| ErrorMargin, optional| An error margin to use when merging geometries.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-geometry#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-geometry#colab-python-sample) More
```
// FeatureCollection of power plants in Belgium.
varfc=ee.FeatureCollection('WRI/GPPD/power_plants')
.filter('country_lg == "Belgium"');
print("Point FeatureCollection's geometry",fc.geometry());
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
frompprintimport pprint
# FeatureCollection of power plants in Belgium.
fc = ee.FeatureCollection('WRI/GPPD/power_plants').filter(
  'country_lg == "Belgium"')
print("Point FeatureCollection's geometry:")
pprint(fc.geometry().getInfo())
```

Was this helpful?
