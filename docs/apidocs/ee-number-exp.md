 
#  ee.Number.exp
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-exp#examples)


Computes the Euler's number e raised to the power of the input. 
Usage| Returns  
---|---  
`Number.exp()`| Number  
Argument| Type| Details  
---|---|---  
this: `input`| Number| The input value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-exp#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-exp#colab-python-sample) More
```
print('e^-1',ee.Number(-1).exp());// 0.367879441
print('e^0',ee.Number(0).exp());// 1
print('e^1',ee.Number(1).exp());// 2.718281828
print('e^2',ee.Number(2).exp());// 7.389056098
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print('e^-1:', ee.Number(-1).exp().getInfo()) # 0.367879441
print('e^0:', ee.Number(0).exp().getInfo()) # 1
print('e^1:', ee.Number(1).exp().getInfo()) # 2.718281828
print('e^2:', ee.Number(2).exp().getInfo()) # 7.389056098
```

Was this helpful?
