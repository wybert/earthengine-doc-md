 
#  ee.Date.evaluate 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-date-evaluate#examples)


Asynchronously retrieves the value of this object from the server and passes it to the provided callback function. 
Usage| Returns  
---|---  
`Date.evaluate(callback)`|   
Argument| Type| Details  
---|---|---  
this: `computedobject`| ComputedObject| The ComputedObject instance.  
`callback`| Function| A function of the form function(success, failure), called when the server returns an answer. If the request succeeded, the success argument contains the evaluated result. If the request failed, the failure argument will contains an error message.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-date-evaluate#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-date-evaluate#colab-python-sample) More
```
/**
 * WARNING: this function transfers data from Earth Engine servers to the
 * client. Doing so can negatively affect request processing and client
 * performance. Server-side options should be used whenever possible.
 * Learn more about the distinction between server and client:
 * https://developers.google.com/earth-engine/guides/client_server
 */
// A server-side ee.Date object.
vardateServer=ee.Date('2021-4-30');
// Use evaluate to transfer server-side date to the client. The result is
// an object with keys "type" and "value" where "value" is milliseconds since
// Unix epoch.
dateServer.evaluate(function(dateClient){
print('Client-side date is an object',typeofdateClient);
print('Object keys include "type" and "value"',Object.keys(dateClient));
print('"value" is milliseconds since Unix epoch',dateClient.value);
print('Client-side date in JS Date constructor',newDate(dateClient.value));
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
# asynchronous evaluation of ee.Date objects.
# Use ee.Date.getInfo() instead.
```

Was this helpful?
