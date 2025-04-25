 
#  ee.Dictionary.aside 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-dictionary-aside#examples)


Calls a function passing this object as the first argument, and returning itself. Convenient e.g. when debugging: 
var c = ee.ImageCollection('foo').aside(print)
.filterDate('2001-01-01', '2002-01-01').aside(print, 'In 2001')
.filterBounds(geom).aside(print, 'In region')
.aside(Map.addLayer, {min: 0, max: 142}, 'Filtered')
.select('a', 'b');
Returns the same object, for chaining.
Usage| Returns  
---|---  
`Dictionary.aside(func, var_args)`| ComputedObject  
Argument| Type| Details  
---|---|---  
this: `computedobject`| ComputedObject| The ComputedObject instance.  
`func`| Function| The function to call.  
`var_args`| VarArgs| Any extra arguments to pass to the function.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-dictionary-aside#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-dictionary-aside#colab-python-sample) More
```
// A dictionary (e.g. results of ee.Image.reduceRegion of an S2 image).
vardict={
B1:182,
B2:219,
B3:443
};
// Print a message when constructing the ee.Dictionary.
vareeDict=ee.Dictionary(dict).aside(print,'ee.Dictionary from an object');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# A dictionary (e.g. results of ee.Image.reduceRegion of an S2 image).
dic = {
  'B1': 182,
  'B2': 219,
  'B3': 443
}

defprint_dic(dic):
"""Prints the dictionary."""
 print('ee.Dictionary from client-side dictionary:', dic.getInfo())
# Print a message when constructing the ee.Dictionary.
ee_dic = ee.Dictionary(dic).aside(print_dic)
```

