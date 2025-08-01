 
#  ee.Number.add
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-add#examples)


Adds the first value to the second.
Usage | Returns  
---|---  
`Number.add(right)` | Number  
Argument | Type | Details  
---|---|---  
this: `left` | Number | The left-hand value.  
`right` | Number | The right-hand value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-add#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-add#colab-python-sample) More
```
print('5 + 10',ee.Number(5).add(ee.Number(10)));// 15
print('5 + 10.2',ee.Number(5).add(ee.Number(10.2)));// 15.2
print('5 + -10.2',ee.Number(5).add(ee.Number(-10.2)));// -5.199999999
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print('5 + 10:', ee.Number(5).add(ee.Number(10)).getInfo())  # 15
print('5 + 10.2:', ee.Number(5).add(ee.Number(10.2)).getInfo())  # 15.2
print('5 + -10.2:',
      ee.Number(5).add(ee.Number(-10.2)).getInfo())  # -5.199999999
```

Was this helpful?
