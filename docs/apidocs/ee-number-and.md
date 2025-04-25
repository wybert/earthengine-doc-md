 
#  ee.Number.and 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-and#examples)


Returns 1 if and only if both values are non-zero. 
Usage| Returns  
---|---  
`Number.and(right)`| Number  
Argument| Type| Details  
---|---|---  
this: `left`| Number| The left-hand value.  
`right`| Number| The right-hand value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-and#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-and#colab-python-sample) More
```
print('Both 5 and 10 are not 0?',ee.Number(5).and(ee.Number(10)));// 1
print('Both 5 and 0 are not 0?',ee.Number(5).and(ee.Number(0)));// 0
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# 1
print('Both 5 and 10 are not 0?', ee.Number(5).And(ee.Number(10)).getInfo())
# 0
print('Both 5 and 0 are not 0?', ee.Number(5).And(ee.Number(0)).getInfo())
```

Was this helpful?
