 
#  ee.Geometry.Point.aside
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-point-aside#examples)


Calls a function passing this object as the first argument, and returning itself. Convenient e.g. when debugging: 
var c = ee.ImageCollection('foo').aside(print)
.filterDate('2001-01-01', '2002-01-01').aside(print, 'In 2001')
.filterBounds(geom).aside(print, 'In region')
.aside(Map.addLayer, {min: 0, max: 142}, 'Filtered')
.select('a', 'b');
Returns the same object, for chaining.
Usage| Returns  
---|---  
`Point.aside(func, var_args)`| ComputedObject  
Argument| Type| Details  
---|---|---  
this: `computedobject`| ComputedObject| The ComputedObject instance.  
`func`| Function| The function to call.  
`var_args`| VarArgs| Any extra arguments to pass to the function.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-point-aside#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-point-aside#colab-python-sample) More
```
varpoint=ee.Geometry.Point([-122.08412,37.42189]);
point.aside(print);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
defprint_result(val, message):
"""A print function to invoke with the aside method."""
 print(val.getInfo())
 print(message)

point = ee.Geometry.Point([-122.08412, 37.42189]).aside(
  print_result, "An ee.Geometry.Point was defined."
)
```

Was this helpful?
