 
#  ee.Geometry.closestPoint 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-closestpoint#examples)


Returns the point on the right input that is nearest to the left input. If either input is empty, null is returned. If both inputs are unbounded, an arbitrary point is returned. If one input is unbounded, an arbitrary point in the bounded input is returned. 
Usage| Returns  
---|---  
`Geometry.closestPoint(right,  _maxError_, _proj_)`| Object  
Argument| Type| Details  
---|---|---  
this: `left`| Geometry| The geometry used as the left operand of the operation.  
`right`| Geometry| The geometry used as the right operand of the operation.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-closestpoint#code-editor-javascript-sample) More
```
// Define a Geometry object.
vargeometry=ee.Geometry({
'type':'Polygon',
'coordinates':
[[[-122.081,37.417],
[-122.086,37.421],
[-122.084,37.418],
[-122.089,37.416]]]
});
// Define other inputs.
varinputGeom=ee.Geometry.Polygon(
[[[-122.068,37.418],
[-122.068,37.416],
[-122.064,37.416],
[-122.064,37.418]]]);
// Apply the closestPoints method to the Geometry objects.
varclosestPoints=ee.Dictionary(geometry.closestPoints({'right':inputGeom,'maxError':1}));
// Print the result to the console.
print('geometry.closestPoints(...) =',closestPoints);
// There is also a one-sided API for convenience.
varclosestPointOnInputGeom=geometry.closestPoint({'right':inputGeom,'maxError':1});
print('geometry.closestPoint(...) =',closestPointOnInputGeom);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(geometry,
{'color':'black'},
'Geometry [black]: geometry');
Map.addLayer(inputGeom,
{'color':'blue'},
'Parameter [blue]: inputGeom');
Map.addLayer(closestPoints.getGeometry('left'),
{'color':'red'},
'Result [red]: closestPointOnLeft');
Map.addLayer(closestPoints.getGeometry('right'),
{'color':'red'},
'Result [red]: closestPointOnRight');
```

Was this helpful?
