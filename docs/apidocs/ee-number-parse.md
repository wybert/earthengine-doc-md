 
#  ee.Number.parse
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-parse#examples)


Convert a string to a number. 
Usage| Returns  
---|---  
`ee.Number.parse(input,  _radix_)`| Number  
Argument| Type| Details  
---|---|---  
`input`| String| The string to convert to a number.  
`radix`| Integer, default: 10| An integer representing the base number system from which to convert. If input is not an integer, radix must equal 10 or not be specified.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-parse#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-parse#colab-python-sample) More
```
print('Client-side string converted to ee.Number',
ee.Number.parse('10'));// 10
print('ee.String converted to ee.Number',
ee.Number.parse(ee.String('100')));// 100
print('Ambiguous string object converted to ee.Number',
ee.Number.parse(ee.Feature(null,{id:'1000'}).get('id')));// 1000
print('Ambiguous number object converted to ee.Number',
ee.Number.parse(ee.Feature(null,{id:1000}).get('id')));// 1000
print('Leading zeros are removed',
ee.Number.parse('0001'));// 1
print('Radix 16',
ee.Number.parse('3E8',16));// 1000
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print('Client-side string converted to ee.Number:',
   ee.Number.parse('10').getInfo()) # 10
print('ee.String converted to ee.Number:',
   ee.Number.parse(ee.String('100')).getInfo()) # 100
# 1000
print('Ambiguous string object converted to ee.Number:',
   ee.Number.parse(ee.Feature(None, {'id': '1000'}).get('id')).getInfo())
print('Leading zeros are removed:',
   ee.Number.parse('0001').getInfo()) # 1
print('Radix 16:', ee.Number.parse('3E8', 16).getInfo()) # 1000
```

Was this helpful?
