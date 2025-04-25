 
#  ee.Number.getInfo 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-getinfo#examples)


Retrieves the value of this object from the server. 
If no callback function is provided, the request is made synchronously. If a callback is provided, the request is made asynchronously.
The asynchronous mode is preferred because the synchronous mode stops all other code (for example, the EE Code Editor UI) while waiting for the server. To make an asynchronous request, evaluate() is preferred over getInfo().
Returns the computed value of this object.
Usage| Returns  
---|---  
`Number.getInfo( _callback_)`| Object  
Argument| Type| Details  
---|---|---  
this: `computedobject`| ComputedObject| The ComputedObject instance.  
`callback`| Function, optional| An optional callback. If not supplied, the call is made synchronously.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-getinfo#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-getinfo#colab-python-sample) More
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
varnumberClient=numberServer.getInfo();
print('Client-side primitive data type',typeofnumberClient);// number
print('Client-side number',numberClient);// 10.3
print('Client-side number used in expression',numberClient+10);// 20.3
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
# A server-side ee.Number object.
number_server = ee.Number(10.3)
number_client = number_server.getInfo()
print('Client-side primitive data type:', type(number_client)) # float
print('Client-side number:', number_client) # 10.3
print('Client-side number used in expression:', number_client + 10) # 20.3
```

