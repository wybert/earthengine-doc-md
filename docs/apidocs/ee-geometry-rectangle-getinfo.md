 
#  ee.Geometry.Rectangle.getInfo 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-rectangle-getinfo#examples)


Retrieves the value of this object from the server. 
If no callback function is provided, the request is made synchronously. If a callback is provided, the request is made asynchronously.
The asynchronous mode is preferred because the synchronous mode stops all other code (for example, the EE Code Editor UI) while waiting for the server. To make an asynchronous request, evaluate() is preferred over getInfo().
Returns the computed value of this object.
Usage| Returns  
---|---  
`Rectangle.getInfo( _callback_)`| Object  
Argument| Type| Details  
---|---|---  
this: `computedobject`| ComputedObject| The ComputedObject instance.  
`callback`| Function, optional| An optional callback. If not supplied, the call is made synchronously.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-rectangle-getinfo#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-rectangle-getinfo#colab-python-sample) More
```
// Define a Rectangle object.
varrectangle=ee.Geometry.Rectangle(-122.09,37.42,-122.08,37.43);
// Apply the getInfo method to the Rectangle object.
varrectangleGetInfo=rectangle.getInfo();
// Print the result to the console.
print('rectangle.getInfo(...) =',rectangleGetInfo);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(rectangle,
{'color':'black'},
'Geometry [black]: rectangle');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Define a Rectangle object.
rectangle = ee.Geometry.Rectangle(-122.09, 37.42, -122.08, 37.43)
# Apply the getInfo method to the Rectangle object.
rectangle_get_info = rectangle.getInfo()
# Print the result.
display('rectangle.getInfo(...) =', rectangle_get_info)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(rectangle, {'color': 'black'}, 'Geometry [black]: rectangle')
m
```

Was this helpful?
