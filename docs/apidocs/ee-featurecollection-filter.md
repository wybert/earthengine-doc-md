 
#  ee.FeatureCollection.filter
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-filter#examples)


Apply a filter to this collection. 
Returns the filtered collection.
Usage| Returns  
---|---  
`FeatureCollection.filter(filter)`| Collection  
Argument| Type| Details  
---|---|---  
this: `collection`| Collection| The Collection instance.  
`filter`| Filter| A filter to apply to this collection.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-filter#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-filter#colab-python-sample) More
```
// Get Denver county polygon.
vardenver=ee.FeatureCollection('FAO/GAUL_SIMPLIFIED_500m/2015/level2')
.filter("ADM2_NAME == 'Denver'")
.filter(ee.Filter.eq('ADM2_NAME','Denver'))// Exactly the same as above.
.first()
.geometry();
Map.centerObject(denver,9);
Map.addLayer(denver,null,'Denver');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Get Denver county polygon.
denver = (
  ee.FeatureCollection('FAO/GAUL_SIMPLIFIED_500m/2015/level2')
  .filter("ADM2_NAME == 'Denver'")
  .filter(ee.Filter.eq('ADM2_NAME', 'Denver')) # Exactly the same as above.
  .first()
  .geometry()
)
m = geemap.Map()
m.center_object(denver, 9)
m.add_layer(denver, None, 'Denver')
m
```

Was this helpful?
