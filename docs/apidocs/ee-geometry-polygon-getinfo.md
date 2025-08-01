 
#  ee.Geometry.Polygon.getInfo
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-polygon-getinfo#examples)


If no callback function is provided, the request is made synchronously. If a callback is provided, the request is made asynchronously.
The asynchronous mode is preferred because the synchronous mode stops all other code (for example, the EE Code Editor UI) while waiting for the server. To make an asynchronous request, evaluate() is preferred over getInfo().
Returns the computed value of this object.
Usage | Returns  
---|---  
`Polygon.getInfo(_callback_)`|  Object  
Argument | Type | Details  
---|---|---  
this: `computedobject` | ComputedObject | The ComputedObject instance.  
`callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-polygon-getinfo#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-polygon-getinfo#colab-python-sample) More
```
// Define a Polygon object.
varpolygon=ee.Geometry.Polygon(
[[[-122.092,37.424],
[-122.086,37.418],
[-122.079,37.425],
[-122.085,37.423]]]);

// Apply the getInfo method to the Polygon object.
varpolygonGetInfo=polygon.getInfo();

// Print the result to the console.
print('polygon.getInfo(...) =',polygonGetInfo);

// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(polygon,
{'color':'black'},
'Geometry [black]: polygon');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Define a Polygon object.
polygon = ee.Geometry.Polygon([[
    [-122.092, 37.424],
    [-122.086, 37.418],
    [-122.079, 37.425],
    [-122.085, 37.423],
]])

# Apply the getInfo method to the Polygon object.
polygon_get_info = polygon.getInfo()

# Print the result.
display('polygon.getInfo(...) =', polygon_get_info)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(polygon, {'color': 'black'}, 'Geometry [black]: polygon')
m
```

