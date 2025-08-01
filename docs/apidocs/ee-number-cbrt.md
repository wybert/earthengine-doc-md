 
#  ee.Number.cbrt
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-cbrt#examples)


Computes the cubic root of the input.
Usage | Returns  
---|---  
`Number.cbrt()` | Number  
Argument | Type | Details  
---|---|---  
this: `input` | Number | The input value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-cbrt#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-cbrt#colab-python-sample) More
```
print('Cubic root of 27',ee.Number(27).cbrt());// 3
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print('Cubic root of 27:', ee.Number(27).cbrt().getInfo())  # 3
```

