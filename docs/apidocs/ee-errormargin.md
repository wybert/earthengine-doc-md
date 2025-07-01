 
#  ee.ErrorMargin
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-errormargin#examples)


Returns an ErrorMargin of the given type with the given value. 
Usage| Returns  
---|---  
`ee.ErrorMargin( _value_, _unit_)`| ErrorMargin  
Argument| Type| Details  
---|---|---  
`value`| Float, default: null| The maximum error value allowed by the margin. Ignored if the unit is 'infinite'.  
`unit`| String, default: "meters"| The unit of this margin: 'meters', 'projected' or 'infinite'.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-errormargin#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-errormargin#colab-python-sample) More
```
// Construct a variety of error margins.
print(ee.ErrorMargin(0));// unit: meters value: 0
print(ee.ErrorMargin(1));// unit: meters value: 1
// Negative margin yields a positive value.
print(ee.ErrorMargin(-1));// unit: meters value: 1
// Large values are turned into an 'infinite'
print(ee.ErrorMargin(1e8));// unit: infinite
// A very large error margin does not quite trigger infinite, which is 2.0e7.
print(ee.ErrorMargin(1e7));// unit: meters value: 10000000
// Being explicit about the units of the error margin.
print(ee.ErrorMargin(1,'meters'));// unit: meters value: 1
print(ee.ErrorMargin(1,'projected'));// unit: projected value: 1
print(ee.ErrorMargin(1,'infinite'));// unit: infinite
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Construct a variety of error margins.
print(ee.ErrorMargin(0).getInfo()) # unit: meters value: 0
print(ee.ErrorMargin(1).getInfo()) # unit: meters value: 1
# Negative margin yields a positive value.
print(ee.ErrorMargin(-1).getInfo()) # unit: meters value: 1
# Large values are turned into an 'infinite'
print(ee.ErrorMargin(1e8).getInfo()) # unit: infinite
# A very large error margin does not quite trigger infinite, which is 2.0e7.
print(ee.ErrorMargin(1e7).getInfo()) # unit: meters value: 10000000
# Being explicit about the units of the error margin.
print(ee.ErrorMargin(1, 'meters').getInfo()) # unit: meters value: 1
print(ee.ErrorMargin(1, 'projected').getInfo()) # unit: projected value: 1
print(ee.ErrorMargin(1, 'infinite').getInfo()) # unit: infinite
```

Was this helpful?
