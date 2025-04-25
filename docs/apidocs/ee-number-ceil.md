 
#  ee.Number.ceil 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-ceil#examples)


Computes the smallest integer greater than or equal to the input. 
Usage| Returns  
---|---  
`Number.ceil()`| Number  
Argument| Type| Details  
---|---|---  
this: `input`| Number| The input value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-ceil#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-ceil#colab-python-sample) More
```
// Positive numbers.
print('Ceiling for 2.1',ee.Number(2.1).ceil());// 3
print('Ceiling for 2.5',ee.Number(2.5).ceil());// 3
print('Ceiling for 2.9',ee.Number(2.9).ceil());// 3
// Negative numbers.
print('Ceiling for 2.1',ee.Number(-2.1).ceil());// -2
print('Ceiling for 2.5',ee.Number(-2.5).ceil());// -2
print('Ceiling for 2.9',ee.Number(-2.9).ceil());// -2
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Positive numbers.
print('Ceiling for 2.1:', ee.Number(2.1).ceil().getInfo()) # 3
print('Ceiling for 2.5:', ee.Number(2.5).ceil().getInfo()) # 3
print('Ceiling for 2.9:', ee.Number(2.9).ceil().getInfo()) # 3
# Negative numbers.
print('Ceiling for 2.1:', ee.Number(-2.1).ceil().getInfo()) # -2
print('Ceiling for 2.5:', ee.Number(-2.5).ceil().getInfo()) # -2
print('Ceiling for 2.9:', ee.Number(-2.9).ceil().getInfo()) # -2
```

Was this helpful?
