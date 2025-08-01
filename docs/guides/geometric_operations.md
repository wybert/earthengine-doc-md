 
#  Geometric Operations
Stay organized with collections  Save and categorize content based on your preferences. 
Earth Engine supports a wide variety of operations on `Geometry` objects. These include operations on individual geometries such as computing a buffer, centroid, bounding box, perimeter, convex hull, etc. For example:
### Code Editor (JavaScript)
```
// Create a geodesic polygon.
varpolygon=ee.Geometry.Polygon([
[[-5,40],[65,40],[65,60],[-5,60],[-5,60]]
]);

// Compute a buffer of the polygon.
varbuffer=polygon.buffer(1000000);

// Compute the centroid of the polygon.
varcentroid=polygon.centroid();
Map.addLayer(buffer,{},'buffer');
Map.addLayer(centroid,{},'centroid');
```

Observe from the previous example that the buffer distance is specified in meters.
Supported geometric operations also include relational computations between geometries such as intersection, union, difference, distance, contains, etc. To test some of these relations, geometries use the “even-odd” rule by default. By the even-odd rule, a point is inside the polygon if a line from that point to some point known to be outside the polygon crosses an odd number of other edges. The inside of a polygon is everything inside the shell and not inside a hole. As a simple example, a point within a circular polygon must cross exactly one edge to escape the polygon. Geometries can optionally use the "left-inside" rule, if necessary. Imagine walking the points of a ring in the order given; the inside will be on the left.
To demonstrate the difference between geometries created with the "left-inside" rule (`evenOdd: **false**`) and those created with the "even-odd" rule, the following example compares a point to two different polygons:
### Code Editor (JavaScript)
```
// Create a left-inside polygon.
varholePoly=ee.Geometry.Polygon({
coords:[
[[-35,-10],[-35,10],[35,10],[35,-10],[-35,-10]]
],
evenOdd:false
});

// Create an even-odd version of the polygon.
varevenOddPoly=ee.Geometry({
geoJson:holePoly,
evenOdd:true
});

// Create a point to test the insideness of the polygon.
varpt=ee.Geometry.Point([1.5,1.5]);

// Check insideness with a contains operator.
print(holePoly.contains(pt));// false
print(evenOddPoly.contains(pt));// true
```

The previous example demonstrates how the order of coordinates provided to the `Polygon` constructor affects the result when a left-inside polygon is constructed. Specifically, the point is outside the left-inside polygon but inside the even-odd polygon.
The following example computes and visualizes derived geometries based on the relationship between two polygons:
### Code Editor (JavaScript)
```
// Create two circular geometries.
varpoly1=ee.Geometry.Point([-50,30]).buffer(1e6);
varpoly2=ee.Geometry.Point([-40,30]).buffer(1e6);

// Display polygon 1 in red and polygon 2 in blue.
Map.setCenter(-45,30);
Map.addLayer(poly1,{color:'FF0000'},'poly1');
Map.addLayer(poly2,{color:'0000FF'},'poly2');

// Compute the intersection, display it in green.
varintersection=poly1.intersection(poly2,ee.ErrorMargin(1));
Map.addLayer(intersection,{color:'00FF00'},'intersection');

// Compute the union, display it in magenta.
varunion=poly1.union(poly2,ee.ErrorMargin(1));
Map.addLayer(union,{color:'FF00FF'},'union');

// Compute the difference, display in yellow.
vardiff1=poly1.difference(poly2,ee.ErrorMargin(1));
Map.addLayer(diff1,{color:'FFFF00'},'diff1');

// Compute symmetric difference, display in black.
varsymDiff=poly1.symmetricDifference(poly2,ee.ErrorMargin(1));
Map.addLayer(symDiff,{color:'000000'},'symmetric difference');
```

In these examples, note that that `maxError` parameter is set to one meter for the geometry operations. The `maxError` is the maximum allowable error, in meters, from transformations (such as projection or reprojection) that may alter the geometry. If one of the geometries is in a different projection from the other, Earth Engine will do the computation in a spherical coordinate system, with a projection precision given by `maxError`. You can also specify a specific projection in which to do the computation, if necessary.
