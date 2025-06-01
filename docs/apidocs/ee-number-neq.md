 
#  ee.Number.neq 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-neq#examples)


Returns 1 if and only if the first value is not equal to the second. 
Usage| Returns  
---|---  
`Number.neq(right)`| Number  
Argument| Type| Details  
---|---|---  
this: `left`| Number| The left-hand value.  
`right`| Number| The right-hand value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-neq#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-neq#colab-python-sample) More
```
print('5 is not equal to 10',ee.Number(5).neq(ee.Number(10)));// 1
print('5 is not equal to 5',ee.Number(5).neq(ee.Number(5)));// 0
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print('5 is not equal to 10:', ee.Number(5).neq(ee.Number(10)).getInfo()) # 1
print('5 is not equal to 5:', ee.Number(5).neq(ee.Number(5)).getInfo()) # 0
```

Was this helpful?
