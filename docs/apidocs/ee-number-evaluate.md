 
#  ee.Number.evaluate
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-evaluate#examples)


Usage | Returns  
---|---  
`Number.evaluate(callback)` |   
Argument | Type | Details  
---|---|---  
this: `computedobject` | ComputedObject | The ComputedObject instance.  
`callback` | Function | A function of the form function(success, failure), called when the server returns an answer. If the request succeeded, the success argument contains the evaluated result. If the request failed, the failure argument will contains an error message.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-evaluate#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-evaluate#colab-python-sample) More
```
/**
 * WARNING: this function transfers data from Earth Engine servers to the
 * client. Doing so can negatively affect request processing and client
 * performance. Server-side options should be used whenever possible.
 * Learn more about the distinction between server and client:
 * https://developers.google.com/earth-engine/guides/client_server
 */

// A server-side ee.Number object.
varnumberServer=ee.Number(10.3);

// Use evaluate to transfer server-side number to the client.
numberServer.evaluate(function(numberClient){
print('Client-side primitive data type',typeofnumberClient);// number
print('Client-side number',numberClient);// 10.3
print('Client-side number used in expression',numberClient+10);// 20.3
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
# asynchronous evaluation of ee.Number objects.
# Use ee.Number.getInfo() instead.
```

