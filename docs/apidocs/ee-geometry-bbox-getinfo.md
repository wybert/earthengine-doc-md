 
#  ee.Geometry.BBox.getInfo 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Retrieves the value of this object from the server. 
If no callback function is provided, the request is made synchronously. If a callback is provided, the request is made asynchronously.
The asynchronous mode is preferred because the synchronous mode stops all other code (for example, the EE Code Editor UI) while waiting for the server. To make an asynchronous request, evaluate() is preferred over getInfo().
Returns the computed value of this object.
Usage| Returns  
---|---  
`BBox.getInfo( _callback_)`| Object  
Argument| Type| Details  
---|---|---  
this: `computedobject`| ComputedObject| The ComputedObject instance.  
`callback`| Function, optional| An optional callback. If not supplied, the call is made synchronously.  
## Examples
### Code Editor (JavaScript)
```
// Define a BBox object.
varbBox=ee.Geometry.BBox(-122.09,37.42,-122.08,37.43);
// Apply the getInfo method to the BBox object.
varbBoxGetInfo=bBox.getInfo();
// Print the result to the console.
print('bBox.getInfo(...) =',bBoxGetInfo);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(bBox,
{'color':'black'},
'Geometry [black]: bBox');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Define a BBox object.
bbox = ee.Geometry.BBox(-122.09, 37.42, -122.08, 37.43)
# Apply the getInfo method to the BBox object.
bbox_get_info = bbox.getInfo()
# Print the result.
display('bbox.getInfo(...) =', bbox_get_info)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(bbox, {'color': 'black'}, 'Geometry [black]: bbox')
m
```

