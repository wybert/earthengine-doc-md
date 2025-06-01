 
#  ee.Geometry.BBox.cutLines 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-bbox-cutlines#examples)


Converts LineString, MultiLineString, and LinearRing geometries into a MultiLineString by cutting them into parts no longer than the given distance along their length. All other geometry types will be converted to an empty MultiLineString. 
Usage| Returns  
---|---  
`BBox.cutLines(distances,  _maxError_, _proj_)`| Geometry  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry| Cuts the lines of this geometry.  
`distances`| List| Distances along each LineString to cut the line into separate pieces, measured in units of the given proj, or meters if proj is unspecified.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| Projection of the result and distance measurements, or EPSG:4326 if unspecified.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-bbox-cutlines#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-bbox-cutlines#colab-python-sample) More
```
// Notice: the cutLines geometry method applies only to LineString,
// MultiLineString, and LinearRing geometries. All other geometry types result
// in an empty MultiLineString.
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Notice: the cutLines geometry method applies only to LineString,
# MultiLineString, and LinearRing geometries. All other geometry types result
# in an empty MultiLineString.
```

