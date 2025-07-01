 
#  ee.Geometry
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry#examples)


Creates a geometry. 
Usage| Returns  
---|---  
`ee.Geometry(geoJson,  _proj_, _geodesic_, _evenOdd_)`| Geometry  
Argument| Type| Details  
---|---|---  
`geoJson`| Object| The GeoJSON object describing the geometry or a ComputedObject to be reinterpreted as a Geometry. Supports CRS specifications as per the GeoJSON spec, but only allows named (rather than "linked" CRSs). If this includes a 'geodesic' field, and opt_geodesic is not specified, it will be used as opt_geodesic.  
`proj`| Projection, optional| An optional projection specification, either as a CRS ID code or as a WKT string. If specified, overrides any CRS found in the geoJson parameter. If unspecified and the geoJson does not declare a CRS, defaults to "EPSG:4326" (x=longitude, y=latitude).  
`geodesic`| Boolean, optional| Whether line segments should be interpreted as spherical geodesics. If false, indicates that line segments should be interpreted as planar lines in the specified CRS. If absent, defaults to true if the CRS is geographic (including the default EPSG:4326), or to false if the CRS is projected.  
`evenOdd`| Boolean, optional| If true, polygon interiors will be determined by the even/odd rule, where a point is inside if it crosses an odd number of edges to reach a point at infinity. Otherwise polygons use the left- inside rule, where interiors are on the left side of the shell's edges when walking the vertices in the given order. If unspecified, defaults to true.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry#colab-python-sample) More
```
// A GeoJSON object for a triangular polygon.
vargeojsonObject={
"type":"Polygon",
"coordinates":[
[
[
-122.085,
37.423
],
[
-122.092,
37.424
],
[
-122.085,
37.418
],
[
-122.085,
37.423
]
]
]
};
print('ee.Geometry accepts a GeoJSON object',ee.Geometry(geojsonObject));
// GeoJSON strings need to be converted to an object.
vargeojsonString=JSON.stringify(geojsonObject);
print('A GeoJSON string needs to be converted to an object',
ee.Geometry(JSON.parse(geojsonString)));
// Use ee.Geometry to cast computed geometry objects into the ee.Geometry
// class to access their methods. In the following example an ee.Geometry
// object is stored as a ee.Feature property. When it is retrieved with the
// .get() function, a computed geometry object is returned. Cast the computed
// object as a ee.Geometry to get the geometry's bounds, for instance.
varfeature=ee.Feature(null,{geom:ee.Geometry(geojsonObject)});
print('Cast computed geometry objects to ee.Geometry class',
ee.Geometry(feature.get('geom')).bounds());
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
importjson
# A GeoJSON object for a triangular polygon.
geojson_object = {
  'type': 'Polygon',
  'coordinates': [
    [
      [
        -122.085,
        37.423
      ],
      [
        -122.092,
        37.424
      ],
      [
        -122.085,
        37.418
      ],
      [
        -122.085,
        37.423
        ]
      ]
    ]
}
print(
  'ee.Geometry accepts a GeoJSON object:',
  ee.Geometry(geojson_object).getInfo()
)
# GeoJSON strings need to be converted to an object.
geojson_string = json.dumps(geojson_object)
print('A GeoJSON string needs to be converted to an object:',
   ee.Geometry(json.loads(geojson_string)).getInfo())
# Use ee.Geometry to cast computed geometry objects into the ee.Geometry
# class to access their methods. In the following example an ee.Geometry
# object is stored as a ee.Feature property. When it is retrieved with the
# .get() function, a computed geometry object is returned. Cast the computed
# object as a ee.Geometry to get the geometry's bounds, for instance.
feature = ee.Feature(None, {'geom': ee.Geometry(geojson_object)})
print('Cast computed geometry objects to ee.Geometry class:',
   ee.Geometry(feature.get('geom')).bounds().getInfo())
```

Was this helpful?
