 
#  ee.Number.atan2 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-atan2#examples)


Calculates the angle formed by the 2D vector [x, y]. 
Usage| Returns  
---|---  
`Number.atan2(right)`| Number  
Argument| Type| Details  
---|---|---  
this: `left`| Number| The left-hand value.  
`right`| Number| The right-hand value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-atan2#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-atan2#colab-python-sample) More
```
// Left input is x and right input is y, representing point (x,y).
print('Atan2 of point (0,0)',ee.Number(0).atan2(0));// 0
print('Atan2 of point (1,0)',ee.Number(1).atan2(0));// 0
print('Atan2 of point (0,1)',ee.Number(0).atan2(1));// 1.570796326 (π/2)
print('Atan2 of point (-1,0)',ee.Number(-1).atan2(0));// 3.141592653 (π)
print('Atan2 of point (0,-1)',ee.Number(0).atan2(-1));// -1.570796326 (-π/2)
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print('Atan2 of point (0,0):', ee.Number(0).atan2(0).getInfo()) # 0
print('Atan2 of point (1,0):', ee.Number(1).atan2(0).getInfo()) # 0
# 1.570796326 (π/2)
print('Atan2 of point (0,1):', ee.Number(0).atan2(1).getInfo())
# 3.141592653 (π)
print('Atan2 of point (-1,0):', ee.Number(-1).atan2(0).getInfo())
# -1.570796326 (-π/2)
print('Atan2 of point (0,-1):', ee.Number(0).atan2(-1).getInfo())
```

