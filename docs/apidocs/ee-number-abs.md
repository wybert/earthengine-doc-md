 
#  ee.Number.abs
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-abs#examples)


Computes the absolute value of the input. 
Usage| Returns  
---|---  
`Number.abs()`| Number  
Argument| Type| Details  
---|---|---  
this: `input`| Number| The input value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-abs#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-abs#colab-python-sample) More
```
print('Absolute value of -1',ee.Number(-1).abs());// 1
print('Absolute value of 0',ee.Number(0).abs());// 0
print('Absolute value of 2.3',ee.Number(2.3).abs());// 2.3
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print('Absolute value of -1:', ee.Number(-1).abs().getInfo()) # 1
print('Absolute value of 0:', ee.Number(0).abs().getInfo()) # 0
print('Absolute value of 2.3:', ee.Number(2.3).abs().getInfo()) # 2.3
```

Was this helpful?
