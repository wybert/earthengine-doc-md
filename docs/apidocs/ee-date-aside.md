 
#  ee.Date.aside 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-date-aside#examples)


Calls a function passing this object as the first argument, and returning itself. Convenient e.g. when debugging: 
var c = ee.ImageCollection('foo').aside(print)
.filterDate('2001-01-01', '2002-01-01').aside(print, 'In 2001')
.filterBounds(geom).aside(print, 'In region')
.aside(Map.addLayer, {min: 0, max: 142}, 'Filtered')
.select('a', 'b');
Returns the same object, for chaining.
Usage| Returns  
---|---  
`Date.aside(func, var_args)`| ComputedObject  
Argument| Type| Details  
---|---|---  
this: `computedobject`| ComputedObject| The ComputedObject instance.  
`func`| Function| The function to call.  
`var_args`| VarArgs| Any extra arguments to pass to the function.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-date-aside#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-date-aside#colab-python-sample) More
```
// Print a message when constructing the ee.Date.
vareeDict=ee.Date(Date.now()).aside(print,"Today's date (UTC)");
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
fromdatetimeimport datetime
defprint_date(ee_date, message):
"""Prints a formatted date, along with a descriptive message."""
 display(message, ee_date.format("YYYY-mm-dd"))
# Print a message when constructing the ee.Date.
ee_date = ee.Date(datetime.now()).aside(print_date, "Today's date (UTC):")
```

Was this helpful?
