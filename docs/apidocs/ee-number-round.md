 
#  ee.Number.round 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-round#examples)


Computes the integer nearest to the input. 
Usage| Returns  
---|---  
`Number.round()`| Number  
Argument| Type| Details  
---|---|---  
this: `input`| Number| The input value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-round#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-round#colab-python-sample) More
```
print('10.4 rounds down',ee.Number(10.4).round());// 10
print('10.5 rounds up',ee.Number(10.5).round());// 11
print('10.9 rounds up',ee.Number(10.9).round());// 11
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print('10.4 rounds down:', ee.Number(10.4).round().getInfo()) # 10
print('10.5 rounds up:', ee.Number(10.5).round().getInfo()) # 11
print('10.9 rounds up:', ee.Number(10.9).round().getInfo()) # 11
```

Was this helpful?
