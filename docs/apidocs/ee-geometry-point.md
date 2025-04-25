 
#  ee.Geometry.Point 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-point#examples)


Constructs an ee.Geometry describing a point. 
For convenience, varargs may be used when all arguments are numbers. This allows creating EPSG:4326 points, e.g. ee.Geometry.Point(lng, lat).
Usage| Returns  
---|---  
`ee.Geometry.Point(coords,  _proj_)`| Geometry.Point  
Argument| Type| Details  
---|---|---  
`coords`| List| A list of two [x,y] coordinates in the given projection.  
`proj`| Projection, optional| The projection of this geometry, or EPSG:4326 if unspecified.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-point#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-point#colab-python-sample) More
```
// Construct a point from coordinates.
varpoint=ee.Geometry.Point([-122.08412,37.42189]);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Construct a point from coordinates.
point = ee.Geometry.Point([-122.08412, 37.42189])
```

Was this helpful?
