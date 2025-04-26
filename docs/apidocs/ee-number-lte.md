 
#  ee.Number.lte 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-lte#examples)


Returns 1 if and only if the first value is less than or equal to the second. 
Usage| Returns  
---|---  
`Number.lte(right)`| Number  
Argument| Type| Details  
---|---|---  
this: `left`| Number| The left-hand value.  
`right`| Number| The right-hand value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-lte#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-lte#colab-python-sample) More
```
print('5 less than or equal to 10?',ee.Number(5).lte(ee.Number(10)));// 1
print('10 less than or equal to 5?',ee.Number(10).lte(ee.Number(5)));// 0
print('5 less than or equal to 5?',ee.Number(5).lte(ee.Number(5)));// 1
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print('5 less than or equal to 10?',
   ee.Number(5).lte(ee.Number(10)).getInfo()) # 1
print('10 less than or equal to 5?',
   ee.Number(10).lte(ee.Number(5)).getInfo()) # 0
print('5 less than or equal to 5?',
   ee.Number(5).lte(ee.Number(5)).getInfo()) # 1
```

