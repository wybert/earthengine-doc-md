 
#  ee.Number.gte
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-gte#examples)


Returns 1 if and only if the first value is greater than or equal to the second. 
Usage| Returns  
---|---  
`Number.gte(right)`| Number  
Argument| Type| Details  
---|---|---  
this: `left`| Number| The left-hand value.  
`right`| Number| The right-hand value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-gte#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-gte#colab-python-sample) More
```
print('5 greater than or equal to 10?',ee.Number(5).gte(ee.Number(10)));// 0
print('10 greater than or equal to 5?',ee.Number(10).gte(ee.Number(5)));// 1
print('5 greater than or equal to 5?',ee.Number(5).gte(ee.Number(5)));// 1
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# 0
print('5 greater than or equal to 10?',
   ee.Number(5).gte(ee.Number(10)).getInfo())
# 1
print('10 greater than or equal to 5?',
   ee.Number(10).gte(ee.Number(5)).getInfo())
# 1
print('5 greater than or equal to 5?',
   ee.Number(5).gte(ee.Number(5)).getInfo())
```

Was this helpful?
