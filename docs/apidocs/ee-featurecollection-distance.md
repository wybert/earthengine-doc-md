 
#  ee.FeatureCollection.distance 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-distance#examples)


Produces a DOUBLE image where each pixel is the distance in meters from the pixel center to the nearest Point, LineString, or polygonal boundary in the collection. Note distance is also measured within interiors of polygons. Pixels that are not within 'searchRadius' meters of a geometry will be masked out. 
Distances are computed on a sphere, so there is a small error proportional to the latitude difference between each pixel and the nearest geometry.
Usage| Returns  
---|---  
`FeatureCollection.distance( _searchRadius_, _maxError_)`| Image  
Argument| Type| Details  
---|---|---  
this: `features`| FeatureCollection| Feature collection from which to get features used to compute pixel distances.  
`searchRadius`| Float, default: 100000| Maximum distance in meters from each pixel to look for edges. Pixels will be masked unless there are edges within this distance.  
`maxError`| Float, default: 100| Maximum reprojection error in meters, only used if the input polylines require reprojection. If '0' is provided, then this operation will fail if projection is required.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-distance#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-distance#colab-python-sample) More
```
// FeatureCollection of power plants in Belgium.
varfc=ee.FeatureCollection('WRI/GPPD/power_plants')
.filter('country_lg == "Belgium"');
// Generate an image of distance to nearest power plant.
vardistance=fc.distance({searchRadius:50000,maxError:50});
// Display the image and FeatureCollection on the map.
Map.setCenter(4.56,50.78,7);
Map.addLayer(distance,{max:50000},'Distance to power plants');
Map.addLayer(fc,{color:'red'},'Power plants');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# FeatureCollection of power plants in Belgium.
fc = ee.FeatureCollection('WRI/GPPD/power_plants').filter(
  'country_lg == "Belgium"'
)
# Generate an image of distance to nearest power plant.
distance = fc.distance(searchRadius=50000, maxError=50)
# Display the image and FeatureCollection on the map.
m = geemap.Map()
m.set_center(4.56, 50.78, 7)
m.add_layer(distance, {'max': 50000}, 'Distance to power plants')
m.add_layer(fc, {'color': 'red'}, 'Power plants')
m
```

Was this helpful?
