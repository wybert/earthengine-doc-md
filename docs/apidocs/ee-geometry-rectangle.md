 
#  ee.Geometry.Rectangle 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-rectangle#examples)


Constructs an ee.Geometry describing a rectangular polygon. 
For convenience, varargs may be used when all arguments are numbers. This allows creating EPSG:4326 Polygons given exactly four coordinates, e.g. ee.Geometry.Rectangle(minLng, minLat, maxLng, maxLat).
Usage| Returns  
---|---  
`ee.Geometry.Rectangle(coords,  _proj_, _geodesic_, _evenOdd_)`| Geometry.Rectangle  
Argument| Type| Details  
---|---|---  
`coords`| List| The minimum and maximum corners of the rectangle, as a list of two points each in the format of GeoJSON 'Point' coordinates, or a list of two ee.Geometry objects describing a point, or a list of four numbers in the order xMin, yMin, xMax, yMax.  
`proj`| Projection, optional| The projection of this geometry. If unspecified, the default is the projection of the input ee.Geometry, or EPSG:4326 if there are no ee.Geometry inputs.  
`geodesic`| Boolean, optional| If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth. The default is the geodesic state of the inputs, or true if the inputs are numbers.  
`evenOdd`| Boolean, optional| If true, polygon interiors will be determined by the even/odd rule, where a point is inside if it crosses an odd number of edges to reach a point at infinity. Otherwise polygons use the left- inside rule, where interiors are on the left side of the shell's edges when walking the vertices in the given order. If unspecified, defaults to true.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-rectangle#code-editor-javascript-sample) More
```
// Coordinates for the bounds of a rectangle.
varxMin=-122.09;
varyMin=37.42;
varxMax=-122.08;
varyMax=37.43;
// Construct a rectangle from a list of GeoJSON 'point' formatted coordinates.
varrectangleGeoJSON=ee.Geometry.Rectangle(
[
[xMin,yMin],
[xMax,yMax]// max x and y
]
);
Map.addLayer(rectangleGeoJSON,{},'rectangleGeoJSON');
// Construct a rectangle from a list of ee.Geometry.Point objects.
varrectanglePoint=ee.Geometry.Rectangle(
[
ee.Geometry.Point(xMin,yMin),// min x and y
ee.Geometry.Point(xMax,yMax)// max x and y
]
);
Map.addLayer(rectanglePoint,{},'rectanglePoint');
// Construct a rectangle from a list of bounding coordinates.
varrectangleBounds=ee.Geometry.Rectangle(
[xMin,yMin,xMax,yMax]
);
Map.addLayer(rectangleBounds,{},'rectangleBounds');
Map.setCenter(-122.085,37.422,15);
```

Was this helpful?
