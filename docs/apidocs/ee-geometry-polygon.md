 
#  ee.Geometry.Polygon 
Stay organized with collections  Save and categorize content based on your preferences. 
Constructs an ee.Geometry describing a polygon. 
For convenience, varargs may be used when all arguments are numbers. This allows creating geodesic EPSG:4326 Polygons with a single LinearRing given an even number of arguments, e.g. ee.Geometry.Polygon(aLng, aLat, bLng, bLat, ..., aLng, aLat).
Usage| Returns  
---|---  
`ee.Geometry.Polygon(coords,  _proj_, _geodesic_, _maxError_, _evenOdd_)`| Geometry.Polygon  
Argument| Type| Details  
---|---|---  
`coords`| List| A list of rings defining the boundaries of the polygon. May be a list of coordinates in the GeoJSON 'Polygon' format, a list of ee.Geometry objects describing a LinearRing, or a list of numbers defining a single polygon boundary.  
`proj`| Projection, optional| The projection of this geometry. The default is the projection of the inputs, where Numbers are assumed to be EPSG:4326.  
`geodesic`| Boolean, optional| If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth. The default is the geodesic state of the inputs, or true if the inputs are numbers.  
`maxError`| ErrorMargin, optional| Max error when input geometry must be reprojected to an explicitly requested result projection or geodesic state.  
`evenOdd`| Boolean, optional| If true, polygon interiors will be determined by the even/odd rule, where a point is inside if it crosses an odd number of edges to reach a point at infinity. Otherwise polygons use the left- inside rule, where interiors are on the left side of the shell's edges when walking the vertices in the given order. If unspecified, defaults to true.  
## Examples
### Code Editor (JavaScript)
```
// Construct a polygon from a list of GeoJSON 'Polygon' formatted coordinates.
varpolygonGeoJSON=ee.Geometry.Polygon(
[
[// exterior ring
[100.0,0.0],
[103.0,0.0],
[103.0,3.0],
[100.0,3.0],
[100.0,0.0]// matching the first vertex is optional
],
[// interior ring
[101.0,1.0],
[102.0,2.0],
[102.0,1.0]
]
]
);
Map.addLayer(polygonGeoJSON,{},'polygonGeoJSON');
// Construct a polygon from an ee.Geometry.LinearRing.
varpolygonLinearRing=ee.Geometry.Polygon(
[
ee.Geometry.LinearRing(
[
[105.0,0.0],
[108.0,0.0],
[108.0,3.0]
]
)
]
);
Map.addLayer(polygonLinearRing,{},'polygonLinearRing');
// Construct a polygon from a list of x,y coordinate pairs defining a boundary.
varpolygonCoordList=ee.Geometry.Polygon(
[110.0,0.0,113.0,0.0,110.0,3.0]
);
Map.addLayer(polygonCoordList,{},'polygonCoordList');
Map.centerObject(polygonLinearRing);
```

