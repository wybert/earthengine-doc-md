 
#  ee.Number.gammainc 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-gammainc#examples)


Calculates the regularized lower incomplete Gamma function γ(x,a). 
Usage| Returns  
---|---  
`Number.gammainc(right)`| Number  
Argument| Type| Details  
---|---|---  
this: `left`| Number| The left-hand value.  
`right`| Number| The right-hand value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-gammainc#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-gammainc#colab-python-sample) More
```
print('Lower incomplete gamma function for x = 0, a = 1',
ee.Number(0).gammainc(1));// 0
print('Lower incomplete gamma function for x = 1, a = 1',
ee.Number(1).gammainc(1));// 0.632120558
print('Lower incomplete gamma function for x = 10, a = 1',
ee.Number(10).gammainc(1));// 0.999954600
print('Lower incomplete gamma function for x = -1, a = 1',
ee.Number(-1).gammainc(1));// NaN
print('Lower incomplete gamma function for x = 10, a = -1',
ee.Number(10).gammainc(-1));// NaN
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print('Lower incomplete gamma function for x = 0, a = 1:',
   ee.Number(0).gammainc(1).getInfo()) # 0
print('Lower incomplete gamma function for x = 1, a = 1:',
   ee.Number(1).gammainc(1).getInfo()) # 0.632120558
print('Lower incomplete gamma function for x = 10, a = 1:',
   ee.Number(10).gammainc(1).getInfo()) # 0.999954600
print('Lower incomplete gamma function for x = -1, a = 1:',
   ee.Number(-1).gammainc(1).getInfo()) # NaN
print('Lower incomplete gamma function for x = 10, a = -1:',
   ee.Number(10).gammainc(-1).getInfo()) # NaN
```

