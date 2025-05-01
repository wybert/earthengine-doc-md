 
#  ee.Number.lanczos 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-lanczos#examples)


Computes the Lanczos approximation of the input. 
Usage| Returns  
---|---  
`Number.lanczos()`| Number  
Argument| Type| Details  
---|---|---  
this: `input`| Number| The input value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-lanczos#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-lanczos#colab-python-sample) More
```
print('Lanczos approx. of -1',ee.Number(-1).lanczos());// Infinity
print('Lanczos approx. of -0.9',ee.Number(-0.9).lanczos());// 524.955196990
print('Lanczos approx. of 0',ee.Number(0).lanczos());// 32.946318679
print('Lanczos approx. of 10',ee.Number(10).lanczos());// 2.281783181
print('Lanczos approx. of 1e10',ee.Number(1e10).lanczos());// 1.000000001
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print('Lanczos approx. of -1:', ee.Number(-1).lanczos().getInfo()) # Infinity
print('Lanczos approx. of -0.9:',
   ee.Number(-0.9).lanczos().getInfo()) # 524.955196990
print('Lanczos approx. of 0:', ee.Number(0).lanczos().getInfo()) # 32.946318679
print('Lanczos approx. of 10:',
   ee.Number(10).lanczos().getInfo()) # 2.281783181
print('Lanczos approx. of 1e10:',
   ee.Number(1e10).lanczos().getInfo()) # 1.000000001
```

