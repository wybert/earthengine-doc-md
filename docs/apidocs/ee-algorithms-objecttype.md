 
#  ee.Algorithms.ObjectType 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-algorithms-objecttype#examples)


Returns a string representing the type of the given object. 
Usage| Returns  
---|---  
`ee.Algorithms.ObjectType( _value_)`| String  
Argument| Type| Details  
---|---|---  
`value`| Object, default: null| The object to get the type of.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-algorithms-objecttype#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-algorithms-objecttype#colab-python-sample) More
```
print(ee.Algorithms.ObjectType(1));// The string "Integer"
print(ee.Algorithms.ObjectType(ee.Number(1)));// The string "Integer"
print(ee.Algorithms.ObjectType(ee.String('a string')));// The string "String"
print(ee.Algorithms.ObjectType(ee.List([1,'a string'])));// The string "List"
// ee.Algorithms.ObjectType can be used to get the type of properties
// of ee.Image or ee.Feature objects.
varfeature=ee.Feature(
null,// No need for geometry in this example.
{
'int':42,
'int8':ee.Number(-3).int8(),
});
// The string "Integer"
print('int:',ee.Algorithms.ObjectType(feature.get('int')));
// The string "Long"
print('int8:',ee.Algorithms.ObjectType(feature.get('int8')));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print(ee.Algorithms.ObjectType(ee.Number(1)).getInfo()) # The string "Integer"
print(
  ee.Algorithms.ObjectType(ee.String('a string')).getInfo()
) # The string "String"
print(
  ee.Algorithms.ObjectType(ee.List([1, 'a string'])).getInfo()
) # The string "List"
# ee.Algorithms.ObjectType can be used to get the type of properties
# of ee.Image or ee.Feature objects.
feature = ee.Feature(
  None, # No need for geometry in this example.
  {
    'int': 42,
    'int8': ee.Number(-3).int8(),
  }
)
# The string "Integer"
print('int:', ee.Algorithms.ObjectType(feature.get('int')).getInfo())
# The string "Long"
print('int8:', ee.Algorithms.ObjectType(feature.get('int8')).getInfo())
```

Was this helpful?
