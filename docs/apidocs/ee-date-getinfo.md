 
#  ee.Date.getInfo
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-date-getinfo#examples)


Retrieves the value of this object from the server. 
If no callback function is provided, the request is made synchronously. If a callback is provided, the request is made asynchronously.
The asynchronous mode is preferred because the synchronous mode stops all other code (for example, the EE Code Editor UI) while waiting for the server. To make an asynchronous request, evaluate() is preferred over getInfo().
Returns the computed value of this object.
Usage| Returns  
---|---  
`Date.getInfo( _callback_)`| Object  
Argument| Type| Details  
---|---|---  
this: `computedobject`| ComputedObject| The ComputedObject instance.  
`callback`| Function, optional| An optional callback. If not supplied, the call is made synchronously.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-date-getinfo#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-date-getinfo#colab-python-sample) More
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
// Use getInfo to transfer server-side date to the client. The result is
// an object with keys "type" and "value" where "value" is milliseconds since
// Unix epoch.
vardateClient=dateServer.getInfo();
print('Client-side date is an object',typeofdateClient);
print('Object keys include "type" and "value"',Object.keys(dateClient));
print('"value" is milliseconds since Unix epoch',dateClient.value);
print('Client-side date in JS Date constructor',newDate(dateClient.value));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
"""
WARNING: this function transfers data from Earth Engine servers to the
client. Doing so can negatively affect request processing and client
performance. Server-side options should be used whenever possible.
Learn more about the distinction between server and client:
https://developers.google.com/earth-engine/guides/client_server
"""
fromdatetimeimport datetime
# A server-side ee.Date object.
date_server = ee.Date('2021-4-30')
# Use getInfo to transfer server-side date to the client. The result is
# a dictionary with keys "type" and "value" where "value" is milliseconds since
# Unix epoch.
date_client = date_server.getInfo()
print('Client-side date is a dictionary:', type(date_client))
print('Dictionary keys include "type" and "value":', date_client.keys())
print('"value" is milliseconds since Unix epoch:', date_client['value'])
print('Client-side date in Python:',
   datetime.fromtimestamp(date_client['value'] / 1000))
```

Was this helpful?
