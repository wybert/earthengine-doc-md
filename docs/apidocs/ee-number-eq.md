 
#  ee.Number.eq
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-eq#examples)


Returns 1 if and only if the first value is equal to the second. 
Usage| Returns  
---|---  
`Number.eq(right)`| Number  
Argument| Type| Details  
---|---|---  
this: `left`| Number| The left-hand value.  
`right`| Number| The right-hand value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-eq#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-eq#colab-python-sample) More
```
print('1 equal to 1?',ee.Number(1).eq(ee.Number(1)));// 1
print('1.001 equal to 1?',ee.Number(1.001).eq(ee.Number(1)));// 0
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print('1 equal to 1?', ee.Number(1).eq(ee.Number(1)).getInfo()) # 1
print('1.001 equal to 1?', ee.Number(1.001).eq(ee.Number(1)).getInfo()) # 0
```

