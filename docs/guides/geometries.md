 
#  Geometry Overview 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Creating Geometry objects](https://developers.google.com/earth-engine/guides/geometries#creating-geometry-objects)


Earth Engine handles vector data with the `Geometry` type. The [GeoJSON spec](http://geojson.org/geojson-spec.html) describes in detail the type of geometries supported by Earth Engine, including `Point` (a list of coordinates in some projection), `LineString` (a list of points), `LinearRing` (a closed `LineString`), and `Polygon` (a list of `LinearRing`s where the first is a shell and subsequent rings are holes). Earth Engine also supports `MultiPoint`, `MultiLineString`, and `MultiPolygon`. The GeoJSON GeometryCollection is also supported, although it has the name `MultiGeometry` within Earth Engine.
## Creating Geometry objects
You can create geometries interactively using the Code Editor geometry tools. See the [Earth Engine Code Editor page](https://developers.google.com/earth-engine/guides/playground#geometry-tools) for more information. To create a `Geometry` programmatically, provide the constructor with the proper list(s) of coordinates. For example:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/geometries#code-editor-javascript-sample) More
```
varpoint=ee.Geometry.Point([1.5,1.5]);
varlineString=ee.Geometry.LineString(
[[-35,-10],[35,-10],[35,10],[-35,10]]);
varlinearRing=ee.Geometry.LinearRing(
[[-35,-10],[35,-10],[35,10],[-35,10],[-35,-10]]);
varrectangle=ee.Geometry.Rectangle([-40,-20,40,20]);
varpolygon=ee.Geometry.Polygon([
[[-5,40],[65,40],[65,60],[-5,60],[-5,60]]
]);
```

In the previous examples, note that the distinction between a `LineString` and a `LinearRing` is that the `LinearRing` is “closed” by having the same coordinate at both the start and end of the list.
An individual `Geometry` may consist of multiple geometries. To break a multi-part `Geometry` into its constituent geometries, use `geometry.geometries()`. For example:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/geometries#code-editor-javascript-sample) More
```
// Create a multi-part feature.
varmultiPoint=ee.Geometry.MultiPoint([[-121.68,39.91],[-97.38,40.34]]);
// Get the individual geometries as a list.
vargeometries=multiPoint.geometries();
// Get each individual geometry from the list and print it.
varpt1=geometries.get(0);
varpt2=geometries.get(1);
print('Point 1',pt1);
print('Point 2',pt2);
```

