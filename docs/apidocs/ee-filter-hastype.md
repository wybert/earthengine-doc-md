 
#  ee.Filter.hasType
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-filter-hastype#examples)


Creates a unary or binary filter that passes if the left operand has the type, or is a subtype of the type named in the right operand. 
Usage| Returns  
---|---  
`ee.Filter.hasType( _leftField_, _rightValue_, _rightField_, _leftValue_)`| Filter  
Argument| Type| Details  
---|---|---  
`leftField`| String, default: null| A selector for the left operand. Should not be specified if leftValue is specified.  
`rightValue`| Object, default: null| The value of the right operand. Should not be specified if rightField is specified.  
`rightField`| String, default: null| A selector for the right operand. Should not be specified if rightValue is specified.  
`leftValue`| Object, default: null| The value of the left operand. Should not be specified if leftField is specified.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-filter-hastype#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-filter-hastype#colab-python-sample) More
```
varfc=ee.FeatureCollection([
ee.Feature(ee.Geometry.Rectangle([0,0,1,1]),{'x':0}),
ee.Feature(ee.Geometry.Rectangle(0,0,3,3),{'x':'foo'}),
ee.Feature(ee.Geometry.Point(0,0))]);
// The third feature has a Point geometry.
print(fc.filter(ee.Filter.hasType({leftField:'.geo',rightValue:'Point'})));
// The first two features have a Polygon geometry.
print(fc.filter(ee.Filter.hasType({leftField:'.geo',rightValue:'Polygon'})));
// The first feature has property x with type Number.
print(fc.filter(ee.Filter.hasType({leftField:'x',rightValue:'Number'})));
// The second feature has property x with type String.
print(fc.filter(ee.Filter.hasType({leftField:'x',rightValue:'String'})));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
fc = ee.FeatureCollection([
  ee.Feature(ee.Geometry.Rectangle([0, 0, 1, 1]), {'x': 0}),
  ee.Feature(ee.Geometry.Rectangle(0, 0, 3, 3), {'x': 'foo'}),
  ee.Feature(ee.Geometry.Point(0, 0)),
])
# The third feature has a Point geometry.
display(
  fc.filter(ee.Filter.hasType(leftField='.geo', rightValue='Point')).getInfo()
)
# The first two features have a Polygon geometry.
display(
  fc.filter(
    ee.Filter.hasType(leftField='.geo', rightValue='Polygon')
  ).getInfo()
)
# The first feature has property x with type Number.
display(
  fc.filter(ee.Filter.hasType(leftField='x', rightValue='Number')).getInfo()
)
# The second feature has property x with type String.
display(
  fc.filter(ee.Filter.hasType(leftField='x', rightValue='String')).getInfo()
)
```

Was this helpful?
