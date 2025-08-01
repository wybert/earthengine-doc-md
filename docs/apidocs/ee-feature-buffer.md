 
#  ee.Feature.buffer
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-feature-buffer#examples)


Returns the input buffered by a given distance. If the distance is positive, the geometry is expanded, and if the distance is negative, the geometry is contracted.
Usage | Returns  
---|---  
`Feature.buffer(distance, _maxError_, _proj_)`|  Feature  
Argument | Type | Details  
---|---|---  
this: `feature` | Element | The feature the geometry of which is being buffered.  
`distance` | Float | The distance of the buffering, which may be negative. If no projection is specified, the unit is meters. Otherwise the unit is in the coordinate system of the projection.  
`maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when approximating the buffering circle and performing any necessary reprojection. If unspecified, defaults to 1% of the distance.  
`proj` | Projection, default: null | If specified, the buffering will be performed in this projection and the distance will be interpreted as units of the coordinate system of this projection. Otherwise the distance is interpereted as meters and the buffering is performed in a spherical coordinate system.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-feature-buffer#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-feature-buffer#colab-python-sample) More
```
// Polygon feature of Serengeti National Park.
varfeature=ee.FeatureCollection('WCMC/WDPA/202307/polygons')
.filter('ORIG_NAME == "Serengeti National Park"')
.first();

// Cast the resulting object as an ee.Feature so that the call to the buffer
// method is unambiguous (first() and buffer() are shared by multiple classes).
feature=ee.Feature(feature);

// Generate buffered features out and in from the original boundary.
varbufferOut=feature.buffer(10000);// 10 km out
varbufferIn=feature.buffer(-10000);// 10 km in

// Display the features on the map.
Map.addLayer(bufferOut,{color:'red'},'Buffer out');
Map.addLayer(feature,{color:'blue'},'No buffer');
Map.addLayer(bufferIn,{color:'yellow'},'Buffer in');
Map.setCenter(34.8407,-2.398,8);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Polygon feature of Serengeti National Park.
feature = (
    ee.FeatureCollection('WCMC/WDPA/202307/polygons')
    .filter('ORIG_NAME == "Serengeti National Park"')
    .first()
)

# Cast the resulting object as an ee.Feature so that the call to the buffer
# method is unambiguous (first() and buffer() are shared by multiple classes).
feature = ee.Feature(feature)

# Generate buffered features out and in from the original boundary.
buffer_out = feature.buffer(10000)  # 10 km out
buffer_in = feature.buffer(-10000)  # 10 km in

# Display the features on the map.
m = geemap.Map()
m.add_layer(buffer_out, {'color': 'red'}, 'Buffer out')
m.add_layer(feature, {'color': 'blue'}, 'No buffer')
m.add_layer(buffer_in, {'color': 'yellow'}, 'Buffer in')
m.set_center(34.8407, -2.398, 8)
m
```

