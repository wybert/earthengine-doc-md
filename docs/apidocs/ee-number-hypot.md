 
#  ee.Number.hypot
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-hypot#examples)


Calculates the magnitude of the 2D vector [x, y]. 
Usage| Returns  
---|---  
`Number.hypot(right)`| Number  
Argument| Type| Details  
---|---|---  
this: `left`| Number| The left-hand value.  
`right`| Number| The right-hand value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-hypot#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-hypot#colab-python-sample) More
```
// Left input is x and right input is y, representing point (x,y).
print('Length from origin to point (0,0)',ee.Number(0).hypot(0));// 0
print('Length from origin to point (3,0)',ee.Number(3).hypot(0));// 3
print('Length from origin to point (3,4)',ee.Number(3).hypot(4));// 5
print('Length from origin to point (-3,4)',ee.Number(-3).hypot(4));// 5
print('Length from origin to point (-3,-4)',ee.Number(-3).hypot(-4));// 5
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Left input is x and right input is y, representing point (x,y).
# 0
print('Length from origin to point (0,0):', ee.Number(0).hypot(0).getInfo())
# 3
print('Length from origin to point (3,0):', ee.Number(3).hypot(0).getInfo())
# 5
print('Length from origin to point (3,4):', ee.Number(3).hypot(4).getInfo())
# 5
print('Length from origin to point (-3,4):', ee.Number(-3).hypot(4).getInfo())
# 5
print('Length from origin to point (-3,-4):', ee.Number(-3).hypot(-4).getInfo())
```

Was this helpful?
