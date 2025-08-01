 
#  ee.Number.divide
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-divide#examples)


Divides the first value by the second, returning 0 for division by 0.
Usage | Returns  
---|---  
`Number.divide(right)` | Number  
Argument | Type | Details  
---|---|---  
this: `left` | Number | The left-hand value.  
`right` | Number | The right-hand value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-divide#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-divide#colab-python-sample) More
```
print('5 / 10',ee.Number(5).divide(ee.Number(10)));// 0.5
print('5 / 10.2',ee.Number(5).divide(ee.Number(10.2)));// 0.490196078
print('5 / -10.2',ee.Number(5).divide(ee.Number(-10.2)));// -0.490196078
print('-10.2 / 5',ee.Number(-10.2).divide(ee.Number(5)));// -2.04
print('-10.2 / -5',ee.Number(-10.2).divide(ee.Number(-5)));// 2.04
print('0 / 10',ee.Number(0).divide(ee.Number(10)));// 0
print('10 / 0',ee.Number(10).divide(ee.Number(0)));// 0
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print('5 / 10:', ee.Number(5).divide(ee.Number(10)).getInfo())  # 0.5
print('5 / 10.2:',
      ee.Number(5).divide(ee.Number(10.2)).getInfo())  # 0.490196078
print('5 / -10.2:',
      ee.Number(5).divide(ee.Number(-10.2)).getInfo()) # -0.490196078
print('-10.2 / 5:', ee.Number(-10.2).divide(ee.Number(5)).getInfo())  # -2.04
print('-10.2 / -5:', ee.Number(-10.2).divide(ee.Number(-5)).getInfo())  # 2.04
print('0 / 10:', ee.Number(0).divide(ee.Number(10)).getInfo())  # 0
print('10 / 0:', ee.Number(10).divide(ee.Number(0)).getInfo())  # 0
```

Was this helpful?
