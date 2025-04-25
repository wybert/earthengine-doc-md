 
#  ee.Number.log 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-log#examples)


Computes the natural logarithm of the input. 
Usage| Returns  
---|---  
`Number.log()`| Number  
Argument| Type| Details  
---|---|---  
this: `input`| Number| The input value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-log#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-log#colab-python-sample) More
```
print(ee.Number(Math.pow(Math.E,-1)).log());// -1
print(ee.Number(1).log());// 0
print(ee.Number(Math.E).log());// 1
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
importmath
print(ee.Number(pow(math.e, -1)).log().getInfo()) # -1
print(ee.Number(1).log().getInfo()) # 0
print(ee.Number(math.e).log().getInfo()) # 1
```

Was this helpful?
