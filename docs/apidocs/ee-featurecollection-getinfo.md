 
#  ee.FeatureCollection.getInfo
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-getinfo#examples)


Returns a collection description whose fields include:
- features: a list containing metadata about the features in the collection.
- properties: an optional dictionary containing the collection's metadata properties.
Usage | Returns  
---|---  
`FeatureCollection.getInfo(_callback_)`|  FeatureCollectionDescription  
Argument | Type | Details  
---|---|---  
this: `featurecollection` | FeatureCollection | The FeatureCollection instance.  
`callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. If supplied, will be called with the first parameter if successful and the second if unsuccessful.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-getinfo#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-getinfo#colab-python-sample) More
```
/**
 * WARNING: this function transfers data from Earth Engine servers to the
 * client. Doing so can negatively affect request processing and client
 * performance. Server-side options should be used whenever possible.
 * Learn more about the distinction between server and client:
 * https://developers.google.com/earth-engine/guides/client_server
 */

// A server-side ee.FeatureCollection of power plants in Belgium.
varfcServer=ee.FeatureCollection('WRI/GPPD/power_plants')
.filter('country_lg == "Belgium"');

// Use getInfo to transfer server-side feature collection to the client. The
// result is an object.
varfcClient=fcServer.getInfo();
print('Client-side feature collection is an object',typeoffcClient);
print('Feature collection object keys',Object.keys(fcClient));
print('Array of features',fcClient.features);
print('Properties of first feature',fcClient.features[0].properties);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
"""WARNING: this function transfers data from Earth Engine servers to the
client. Doing so can negatively affect request processing and client
performance. Server-side options should be used whenever possible.
Learn more about the distinction between server and client:
https://developers.google.com/earth-engine/guides/client_server
"""

# A server-side ee.FeatureCollection of power plants in Belgium.
fc_server = ee.FeatureCollection('WRI/GPPD/power_plants').filter(
    'country_lg == "Belgium"')

# Use getInfo to transfer server-side feature collection to the client. The
# result is an object.
fc_client = fc_server.getInfo()
print('Client-side feature collection is a dictionary:', type(fc_client))
print('Feature collection dictionary keys:', fc_client.keys())
print('Array of features:', fc_client['features'])
print('Properties of first feature:', fc_client['features'][0]['properties'])
```

Was this helpful?
