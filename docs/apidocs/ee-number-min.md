 
#  ee.Number.min
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-min#examples)


Selects the minimum of the first and second values.
Usage | Returns  
---|---  
`Number.min(right)` | Number  
Argument | Type | Details  
---|---|---  
this: `left` | Number | The left-hand value.  
`right` | Number | The right-hand value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-min#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-min#colab-python-sample) More
```
print('Given 5 and 10, min is 5',ee.Number(5).min(ee.Number(10)));// 5
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print('Given 5 and 10, min is 5:',
      ee.Number(5).min(ee.Number(10)).getInfo())  # 5
```

