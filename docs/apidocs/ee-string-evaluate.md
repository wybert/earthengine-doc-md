 
#  ee.String.evaluate 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-string-evaluate#examples)


Asynchronously retrieves the value of this object from the server and passes it to the provided callback function. 
Usage| Returns  
---|---  
`String.evaluate(callback)`|   
Argument| Type| Details  
---|---|---  
this: `computedobject`| ComputedObject| The ComputedObject instance.  
`callback`| Function| A function of the form function(success, failure), called when the server returns an answer. If the request succeeded, the success argument contains the evaluated result. If the request failed, the failure argument will contains an error message.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-string-evaluate#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-string-evaluate#colab-python-sample) More
```
/**
 * WARNING: this function transfers data from Earth Engine servers to the
 * client. Doing so can negatively affect request processing and client
 * performance. Server-side options should be used whenever possible.
 * Learn more about the distinction between server and client:
 * https://developers.google.com/earth-engine/guides/client_server
 */
// A server-side ee.String object fetched from a feature property.
varstringServer=ee.Feature(null,{lc:'grassland'}).getString('lc');
// Use evaluate to transfer server-side string to client for use in ui.Label.
stringServer.evaluate(function(stringClient){
print('Client-side primitive data type',typeofstringClient);// string
print('Client-side string',stringClient);// grassland
print('Client-side string used in ui.Label',
ui.Label('Land cover: '+stringClient));// Land cover: grassland
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
# asynchronous evaluation of ee.String objects.
# Use ee.String.getInfo() instead.
```

Was this helpful?
