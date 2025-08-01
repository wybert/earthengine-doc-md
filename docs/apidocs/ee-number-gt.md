 
#  ee.Number.gt
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-gt#examples)


Returns 1 if and only if the first value is greater than the second.
Usage | Returns  
---|---  
`Number.gt(right)` | Number  
Argument | Type | Details  
---|---|---  
this: `left` | Number | The left-hand value.  
`right` | Number | The right-hand value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-gt#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-gt#colab-python-sample) More
```
print('5 greater than 10?',ee.Number(5).gt(ee.Number(10)));// 0
print('10 greater than 5?',ee.Number(10).gt(ee.Number(5)));// 1
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print('5 greater than 10?', ee.Number(5).gt(ee.Number(10)).getInfo())  # 0
print('10 greater than 5?', ee.Number(10).gt(ee.Number(5)).getInfo())  # 1
```

