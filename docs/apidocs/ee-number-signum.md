 
#  ee.Number.signum 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-signum#examples)


Computes the signum function (sign) of the input; 0 if the input is 0, 1 if the input is greater than 0, -1 if the input is less than 0. 
Usage| Returns  
---|---  
`Number.signum()`| Number  
Argument| Type| Details  
---|---|---  
this: `input`| Number| The input value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-signum#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-signum#colab-python-sample) More
```
print('Sign of -5',ee.Number(-5).signum());// -1
print('Sign of 0',ee.Number(0).signum());// 0
print('Sign of 5',ee.Number(5).signum());// 1
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print('Sign of -5:', ee.Number(-5).signum().getInfo()) # -1
print('Sign of 0:', ee.Number(0).signum().getInfo()) # 0
print('Sign of 5:', ee.Number(5).signum().getInfo()) # 1
```

Was this helpful?
