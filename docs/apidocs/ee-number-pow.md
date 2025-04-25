 
#  ee.Number.pow 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-pow#examples)


Raises the first value to the power of the second. 
Usage| Returns  
---|---  
`Number.pow(right)`| Number  
Argument| Type| Details  
---|---|---  
this: `left`| Number| The left-hand value.  
`right`| Number| The right-hand value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-pow#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-pow#colab-python-sample) More
```
print('5 ** 2',ee.Number(5).pow(ee.Number(2)));// 25
print('-5 ** 2',ee.Number(-5).pow(ee.Number(2)));// 25
print('5 ** -2',ee.Number(5).pow(ee.Number(-2)));// 0.04
print('5 ** 2.2',ee.Number(5).pow(ee.Number(2.2)));// 34.493241536
print('5.2 ** 2',ee.Number(5.2).pow(ee.Number(2)));// 27.040000000
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print('5 ** 2', ee.Number(5).pow(ee.Number(2)).getInfo()) # 25
print('-5 ** 2', ee.Number(-5).pow(ee.Number(2)).getInfo()) # 25
print('5 ** -2', ee.Number(5).pow(ee.Number(-2)).getInfo()) # 0.04
print('5 ** 2.2', ee.Number(5).pow(ee.Number(2.2)).getInfo()) # 34.493241536
print('5.2 ** 2', ee.Number(5.2).pow(ee.Number(2)).getInfo()) # 27.040000000
```

