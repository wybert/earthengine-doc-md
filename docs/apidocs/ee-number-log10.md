 
#  ee.Number.log10 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-log10#examples)


Computes the base-10 logarithm of the input. 
Usage| Returns  
---|---  
`Number.log10()`| Number  
Argument| Type| Details  
---|---|---  
this: `input`| Number| The input value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-log10#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-log10#colab-python-sample) More
```
print(ee.Number(0.1).log10());// -1
print(ee.Number(1).log10());// 0
print(ee.Number(10).log10());// 1
print(ee.Number(100).log10());// 2
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print(ee.Number(0.1).log10().getInfo()) # -1
print(ee.Number(1).log10().getInfo()) # 0
print(ee.Number(10).log10().getInfo()) # 1
print(ee.Number(100).log10().getInfo()) # 2
```

Was this helpful?
