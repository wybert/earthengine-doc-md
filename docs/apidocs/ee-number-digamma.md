 
#  ee.Number.digamma
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-digamma#examples)


Computes the digamma function of the input.
Usage | Returns  
---|---  
`Number.digamma()` | Number  
Argument | Type | Details  
---|---|---  
this: `input` | Number | The input value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-digamma#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-digamma#colab-python-sample) More
```
print('Digamma for -1.5',ee.Number(-1.5).digamma());// 0.703156637
print('Digamma for -1',ee.Number(-1).digamma());// -Infinity
print('Digamma for 0',ee.Number(0).digamma());// -Infinity
print('Digamma for 0.5',ee.Number(0.5).digamma());// -1.963510028
print('Digamma for 1',ee.Number(1).digamma());// -0.577215667
print('Digamma for 100',ee.Number(100).digamma());// 4.600161852
print('Digamma for 1e13',ee.Number(1e13).digamma());// 29.933606208
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print('Digamma for -1.5:', ee.Number(-1.5).digamma().getInfo())  # 0.703156637
print('Digamma for -1:', ee.Number(-1).digamma().getInfo())  # -Infinity
print('Digamma for 0:', ee.Number(0).digamma().getInfo())  # -Infinity
print('Digamma for 0.5:', ee.Number(0.5).digamma().getInfo())  # -1.963510028
print('Digamma for 1:', ee.Number(1).digamma().getInfo())  # -0.577215667
print('Digamma for 100:', ee.Number(100).digamma().getInfo())  # 4.600161852
print('Digamma for 1e13:', ee.Number(1e13).digamma().getInfo())  # 29.933606208
```

