 
#  ee.Number.sqrt
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-sqrt#examples)


Computes the square root of the input.
Usage | Returns  
---|---  
`Number.sqrt()` | Number  
Argument | Type | Details  
---|---|---  
this: `input` | Number | The input value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-sqrt#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-sqrt#colab-python-sample) More
```
// Values less than 0 are invalid.
print('Square root of 100',ee.Number(100).sqrt());// 10
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Values less than 0 are invalid.
print('Square root of 100:', ee.Number(100).sqrt().getInfo())  # 10
```

