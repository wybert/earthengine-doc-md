 
#  ee.Number.or 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-or#examples)


Returns 1 if and only if either input value is non-zero. 
Usage| Returns  
---|---  
`Number.or(right)`| Number  
Argument| Type| Details  
---|---|---  
this: `left`| Number| The left-hand value.  
`right`| Number| The right-hand value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-or#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-or#colab-python-sample) More
```
print('Either 0 or 5 non-zero?',ee.Number(0).or(ee.Number(5)));// 1
print('Either 0 or 0 non-zero?',ee.Number(0).or(ee.Number(0)));// 0
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print('Either 0 or 5 non-zero?', ee.Number(0).Or(ee.Number(5)).getInfo()) # 1
print('Either 0 or 0 non-zero?', ee.Number(0).Or(ee.Number(0)).getInfo()) # 0
```

Was this helpful?
