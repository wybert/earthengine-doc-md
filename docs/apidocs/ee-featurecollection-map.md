 
#  ee.FeatureCollection.map
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-map#examples)


Maps an algorithm over a collection. 
Returns the mapped collection.
Usage| Returns  
---|---  
`FeatureCollection.map(algorithm,  _dropNulls_)`| Collection  
Argument| Type| Details  
---|---|---  
this: `collection`| Collection| The Collection instance.  
`algorithm`| Function| The operation to map over the images or features of the collection. A JavaScript function that receives an image or features and returns one. The function is called only once and the result is captured as a description, so it cannot perform imperative operations or rely on external state.  
`dropNulls`| Boolean, optional| If true, the mapped algorithm is allowed to return nulls, and the elements for which it returns nulls will be dropped.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-map#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-map#colab-python-sample) More
```
// FeatureCollection of power plants in Belgium.
varfc=ee.FeatureCollection('WRI/GPPD/power_plants')
.filter('country_lg == "Belgium"');
// Function to convert power plant capacity from megawatts to gigawatts and
// add the value as a new feature property.
varmwToGw=function(feature){
varmegawatt=feature.getNumber('capacitymw');
vargigawatt=megawatt.divide(1000);
returnfeature.set('capacitygw',gigawatt);
};
// Apply the function to each feature in the collection.
fc=fc.map(mwToGw);
print('Note the new "capacitygw" property in each feature',fc);
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
# Function to convert power plant capacity from megawatts to gigawatts and
# add the value as a new feature property.
defmw_to_gw(feature):
 megawatt = feature.getNumber('capacitymw')
 gigawatt = megawatt.divide(1000)
 return feature.set('capacitygw', gigawatt)
# Apply the function to each feature in the collection.
fc = fc.map(mw_to_gw)
print('Note the new "capacitygw" property in each feature:', fc.getInfo())
```

Was this helpful?
