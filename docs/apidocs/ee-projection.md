 
#  ee.Projection
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-projection#examples)


Returns a Projection with the given base coordinate system and the given transform between projected coordinates and the base. If no transform is specified, the identity transform is assumed.
Usage | Returns  
---|---  
`ee.Projection(crs, _transform_, _transformWkt_)`|  Projection  
Argument | Type | Details  
---|---|---  
`crs` | Object | The base coordinate reference system of this Projection, given as a well-known authority code (e.g., 'EPSG:4326') or a WKT string.  
`transform` | List, default: null | The transform between projected coordinates and the base coordinate system, specified as a 2x3 affine transform matrix in row-major order: [xScale, xShearing, xTranslation, yShearing, yScale, yTranslation]. May not specify both this and 'transformWkt'.  
`transformWkt` | String, default: null | The transform between projected coordinates and the base coordinate system, specified as a WKT string. May not specify both this and 'transform'.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-projection#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-projection#colab-python-sample) More
```
// Construct projections.
// Printing the projection will show the EPSG code if it is a direct match.
//
// e.g. You will see this for the string 'EPSG:3857'
//   type: Projection
//   crs: EPSG:3857
//   transform: [1,0,0,0,1,0]

print(ee.Projection('EPSG:3857'));// https://epsg.io/3857
print(ee.Projection('EPSG:4326'));// https://epsg.io/4326

// WKT projection description for https://epsg.io/27572
varproj=ee.Projection(
'PROJCS["NTF (Paris) / Lambert zone II", '+
'  GEOGCS["NTF (Paris)", '+
'    DATUM["Nouvelle Triangulation Francaise (Paris)", '+
'      SPHEROID["Clarke 1880 (IGN)", 6378249.2, 293.4660212936269,'+
'               AUTHORITY["EPSG","7011"]], '+
'      AUTHORITY["EPSG","6807"]], '+
'    PRIMEM["Paris", 2.5969213, AUTHORITY["EPSG","8903"]], '+
'    UNIT["grade", 0.015707963267948967], '+
'    AXIS["Geodetic longitude", EAST], '+
'    AXIS["Geodetic latitude", NORTH], '+
'    AUTHORITY["EPSG","4807"]], '+
'  PROJECTION["Lambert_Conformal_Conic_1SP", AUTHORITY["EPSG","9801"]], '+
'  PARAMETER["central_meridian", 0.0], '+
'  PARAMETER["latitude_of_origin", 52.0], '+
'  PARAMETER["scale_factor", 0.99987742], '+
'  PARAMETER["false_easting", 600000.0], '+
'  PARAMETER["false_northing", 2200000.0], '+
'  UNIT["m", 1.0], '+
'  AXIS["Easting", EAST], '+
'  AXIS["Northing", NORTH], '+
'  AUTHORITY["EPSG","27572"]]');
print(proj);// crs: EPSG:27572
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Construct projections.
# Printing the projection will show the EPSG code if it is a direct match.
#
# e.g. You will see this for the string 'EPSG:3857'
#   type: Projection
#   crs: EPSG:3857
#   transform: [1,0,0,0,1,0]

print(ee.Projection('EPSG:3857').getInfo())  # https://epsg.io/3857
print(ee.Projection('EPSG:4326').getInfo())  # https://epsg.io/4326

# WKT projection description for https://epsg.io/27572
proj = ee.Projection(
    'PROJCS["NTF (Paris) / Lambert zone II", ' +
    '  GEOGCS["NTF (Paris)", ' +
    '    DATUM["Nouvelle Triangulation Francaise (Paris)", ' +
    '      SPHEROID["Clarke 1880 (IGN)", 6378249.2, 293.4660212936269,'+
    '               AUTHORITY["EPSG","7011"]], ' +
    '      AUTHORITY["EPSG","6807"]], ' +
    '    PRIMEM["Paris", 2.5969213, AUTHORITY["EPSG","8903"]], ' +
    '    UNIT["grade", 0.015707963267948967], ' +
    '    AXIS["Geodetic longitude", EAST], ' +
    '    AXIS["Geodetic latitude", NORTH], ' +
    '    AUTHORITY["EPSG","4807"]], ' +
    '  PROJECTION["Lambert_Conformal_Conic_1SP", AUTHORITY["EPSG","9801"]], ' +
    '  PARAMETER["central_meridian", 0.0], ' +
    '  PARAMETER["latitude_of_origin", 52.0], ' +
    '  PARAMETER["scale_factor", 0.99987742], ' +
    '  PARAMETER["false_easting", 600000.0], ' +
    '  PARAMETER["false_northing", 2200000.0], ' +
    '  UNIT["m", 1.0], ' +
    '  AXIS["Easting", EAST], ' +
    '  AXIS["Northing", NORTH], ' +
    '  AUTHORITY["EPSG","27572"]]')
print(proj.getInfo())  # crs: EPSG:27572
```

Was this helpful?
