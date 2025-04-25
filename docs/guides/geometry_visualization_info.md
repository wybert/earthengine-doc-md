 
#  Geometry Visualization and Information 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Visualizing geometries](https://developers.google.com/earth-engine/guides/geometry_visualization_info#visualizing-geometries)
  * [Geometry information and metadata](https://developers.google.com/earth-engine/guides/geometry_visualization_info#geometry-information-and-metadata)


## Visualizing geometries
To visualize a geometry, add it to the map. For example:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/geometry_visualization_info#code-editor-javascript-sample) More
```
// Create a geodesic polygon.
varpolygon=ee.Geometry.Polygon([
[[-5,40],[65,40],[65,60],[-5,60],[-5,60]]
]);
// Create a planar polygon.
varplanarPolygon=ee.Geometry(polygon,null,false);
// Display the polygons by adding them to the map.
Map.centerObject(polygon);
Map.addLayer(polygon,{color:'FF0000'},'geodesic polygon');
Map.addLayer(planarPolygon,{color:'000000'},'planar polygon');
```

For more on visualizing, see [Feature and FeatureCollection Visualization](https://developers.google.com/earth-engine/guides/feature_collections_visualizing).
## Geometry information and metadata
To view information about a geometry, print it. To access the information programmatically, Earth Engine provides several methods. For example, to get information about the polygon created previously, use:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/geometry_visualization_info#code-editor-javascript-sample) More
```
print('Polygon printout: ',polygon);
// Print polygon area in square kilometers.
print('Polygon area: ',polygon.area().divide(1000*1000));
// Print polygon perimeter length in kilometers.
print('Polygon perimeter: ',polygon.perimeter().divide(1000));
// Print the geometry as a GeoJSON string.
print('Polygon GeoJSON: ',polygon.toGeoJSONString());
// Print the GeoJSON 'type'.
print('Geometry type: ',polygon.type());
// Print the coordinates as lists.
print('Polygon coordinates: ',polygon.coordinates());
// Print whether the geometry is geodesic.
print('Geodesic? ',polygon.geodesic());
```

Observe that the perimeter (or length) of a geometry is returned in meters and the area is returned in square meters unless a projection is specified. By default, the computation is performed on the WGS84 spheroid and the result is computed in meters or square meters.
