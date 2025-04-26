 
#  ee.String.aside 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-string-aside#examples)


Calls a function passing this object as the first argument, and returning itself. Convenient e.g. when debugging: 
var c = ee.ImageCollection('foo').aside(print)
.filterDate('2001-01-01', '2002-01-01').aside(print, 'In 2001')
.filterBounds(geom).aside(print, 'In region')
.aside(Map.addLayer, {min: 0, max: 142}, 'Filtered')
.select('a', 'b');
Returns the same object, for chaining.
Usage| Returns  
---|---  
`String.aside(func, var_args)`| ComputedObject  
Argument| Type| Details  
---|---|---  
this: `computedobject`| ComputedObject| The ComputedObject instance.  
`func`| Function| The function to call.  
`var_args`| VarArgs| Any extra arguments to pass to the function.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-string-aside#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-string-aside#colab-python-sample) More
```
// aside with no var_args.
// a
ee.String('a').aside(print);
// foo
// bar
ee.String('foo').aside(print,'bar');
// foo
// bar
//
// foo
print(ee.String('foo').aside(print,'bar'));
// aside in the middle of a chain of calls.
// a
// b
//
// ac
print(ee.String('a').aside(print,'b').cat('c'));
// aside with more than one var_args.
// a
// 1
// 2
ee.String('a').aside(print,1,2);
// Print a empty JSON string.
// ''
ee.String('').aside(print);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
defprint_result(val, *params):
"""A print function to invoke with the aside method."""
 print(val.getInfo())
 for param in params:
  print(param)

# aside with no var_args.
# a
ee.String('a').aside(print_result)
# foo
# bar
ee.String('foo').aside(print_result, 'bar')
# foo
# bar
#
# foo
print(ee.String('foo').aside(print_result, 'bar').getInfo())
# aside in the middle of a chain of calls.
# a
# b
#
# ac
print(ee.String('a').aside(print_result, 'b').cat('c').getInfo())
# aside with more than one var_args.
# a
# 1
# 2
ee.String('a').aside(print_result, 1, 2)
# Print a empty JSON string.
# ''
ee.String('').aside(print_result)
```

Was this helpful?
