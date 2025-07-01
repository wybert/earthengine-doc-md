 
#  ee.String.getInfo
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-string-getinfo#examples)


Retrieves the value of this object from the server. 
If no callback function is provided, the request is made synchronously. If a callback is provided, the request is made asynchronously.
The asynchronous mode is preferred because the synchronous mode stops all other code (for example, the EE Code Editor UI) while waiting for the server. To make an asynchronous request, evaluate() is preferred over getInfo().
Returns the computed value of this object.
Usage| Returns  
---|---  
`String.getInfo( _callback_)`| Object  
Argument| Type| Details  
---|---|---  
this: `computedobject`| ComputedObject| The ComputedObject instance.  
`callback`| Function, optional| An optional callback. If not supplied, the call is made synchronously.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-string-getinfo#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-string-getinfo#colab-python-sample) More
```
// After getInfo(), the instance is a local JavaScript string.
// Regular JavaScript string manipulations are then available.
//
// Note: getInfo() fetches results from Earth Engine immediately, and may freeze
// the browser or lead to poor performance. Use evaluate() to avoid this.
print(ee.String('abc').getInfo().charAt(1));// b
print(ee.String('abc').getInfo()[2]);// c
// Using + with ee.String has unexpected results
print(ee.String('abc')+'def');// ee.String("abc")def
// Fetch string using getInfo
print(ee.String('abc').getInfo()+'def');// abcdef
// Improved solution: cat is available on ee.String
print(ee.String('abc').cat('def'));// abcdef
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# After getInfo(), the instance is a local Python string.
# Regular Python string manipulations are then available.
# Note: getInfo() fetches results from Earth Engine synchronously;
# later expressions will not be evaluated until it completes.
print(ee.String('abc').getInfo()[-2]) # b
print(ee.String('abc').getInfo()[2]) # c
# Fetch string using getInfo
print(ee.String('abc').getInfo() + 'def') # abcdef
```

