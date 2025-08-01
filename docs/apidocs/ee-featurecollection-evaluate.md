 
#  ee.FeatureCollection.evaluate
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-evaluate#examples)


Usage | Returns  
---|---  
`FeatureCollection.evaluate(callback)` |   
Argument | Type | Details  
---|---|---  
this: `computedobject` | ComputedObject | The ComputedObject instance.  
`callback` | Function | A function of the form function(success, failure), called when the server returns an answer. If the request succeeded, the success argument contains the evaluated result. If the request failed, the failure argument will contains an error message.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-evaluate#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-evaluate#colab-python-sample) More
```
/**
 * WARNING: this function transfers data from Earth Engine servers to the
 * client. Doing so can negatively affect request processing and client
 * performance. Server-side options should be used whenever possible.
 * Learn more about the distinction between server and client:
 * https://developers.google.com/earth-engine/guides/client_server
 */

// FeatureCollection of power plants in Belgium.
varfcServer=ee.FeatureCollection('WRI/GPPD/power_plants')
.filter('country_lg == "Belgium"');

fcServer.evaluate(function(fcClient){
print('Client-side feature collection is an object',typeoffcClient);
print('Feature collection object keys',Object.keys(fcClient));
print('Array of features',fcClient.features);
print('Properties for first feature',fcClient.features[0].properties);
});
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# The Earth Engine Python client library does not have an evaluate method for
# asynchronous evaluation of ee.FeatureCollection objects.
# Use ee.FeatureCollection.getInfo() instead.
```

Was this helpful?
