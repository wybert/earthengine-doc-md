 
#  ee.Number.not
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-not#examples)


Returns 0 if the input is non-zero, and 1 otherwise. 
Usage| Returns  
---|---  
`Number.not()`| Number  
Argument| Type| Details  
---|---|---  
this: `input`| Number| The input value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-not#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-not#colab-python-sample) More
```
print('Value is not 0',ee.Number(5).not());// 0
print('Value is 0',ee.Number(0).not());// 1
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print('Value is not 0:', ee.Number(5).Not().getInfo()) # 0
print('Value is 0:', ee.Number(0).Not().getInfo()) # 1
```

Was this helpful?
