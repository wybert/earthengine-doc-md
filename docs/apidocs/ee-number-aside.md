 
#  ee.Number.aside 
Stay organized with collections  Save and categorize content based on your preferences. 
Calls a function passing this object as the first argument, and returning itself. Convenient e.g. when debugging: 
var c = ee.ImageCollection('foo').aside(print)
.filterDate('2001-01-01', '2002-01-01').aside(print, 'In 2001')
.filterBounds(geom).aside(print, 'In region')
.aside(Map.addLayer, {min: 0, max: 142}, 'Filtered')
.select('a', 'b');
Returns the same object, for chaining.
Usage| Returns  
---|---  
`Number.aside(func, var_args)`| ComputedObject  
Argument| Type| Details  
---|---|---  
this: `computedobject`| ComputedObject| The ComputedObject instance.  
`func`| Function| The function to call.  
`var_args`| VarArgs| Any extra arguments to pass to the function.  
## Examples
### Code Editor (JavaScript)
```
// Print a message when constructing an ee.Number.
vareeNum=ee.Number(10).aside(print,'An ee.Number was defined');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
defprint_result(val, message):
"""A print function to invoke with the aside method."""
 print(val.getInfo())
 print(message)
# Print a message when constructing an ee.Number.
ee_num = ee.Number(10).aside(print_result, 'An ee.Number was defined')
```

