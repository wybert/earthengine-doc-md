 
#  ee.Number.unitScale 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-unitscale#examples)


Scales the input so that the range of input values [min, max] becomes [0, 1]. Values outside the range are NOT clamped. If min == max, 0 is returned. 
Usage| Returns  
---|---  
`Number.unitScale(min, max)`| Number  
Argument| Type| Details  
---|---|---  
this: `number`| Number|   
`min`| Float|   
`max`| Float|   
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-unitscale#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-unitscale#colab-python-sample) More
```
print('-10 scaled between [0, 100]',ee.Number(-10).unitScale(0,100));// -0.1
print('10 scaled between [0, 100]',ee.Number(10).unitScale(0,100));// 0.1
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print('-10 scaled between [0, 100]:',
   ee.Number(-10).unitScale(0, 100).getInfo()) # -0.1
print('10 scaled between [0, 100]:',
   ee.Number(10).unitScale(0, 100).getInfo()) # 0.1
```

Was this helpful?
