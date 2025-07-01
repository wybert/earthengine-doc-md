 
#  ee.Geometry.evaluate
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-evaluate#examples)


Asynchronously retrieves the value of this object from the server and passes it to the provided callback function. 
Usage| Returns  
---|---  
`Geometry.evaluate(callback)`|   
Argument| Type| Details  
---|---|---  
this: `computedobject`| ComputedObject| The ComputedObject instance.  
`callback`| Function| A function of the form function(success, failure), called when the server returns an answer. If the request succeeded, the success argument contains the evaluated result. If the request failed, the failure argument will contains an error message.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-evaluate#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-evaluate#colab-python-sample) More
```
// Define a callback function that prints a GeoJSON string.
varprintGeoJSONString=function(geometry){
geometry=ee.Geometry(geometry);
print(geometry.toGeoJSONString());
};
// Create a simple computed geometry.
varcomputedGeometry=ee.Geometry.Point(0,0).buffer(10);
// Evaluate the callback function that asynchronously retrieves and prints
// the GeoJSON string representation of computed geometry.
computedGeometry.evaluate(printGeoJSONString);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# The Earth Engine Python client library does not have an evaluate method for
# asynchronous evaluation of ee.Geometry objects.
# Use ee.Geometry.getInfo() instead.
```

Was this helpful?
