 
#  ee.Number.gamma
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-gamma#examples)


Computes the gamma function of the input.
Usage | Returns  
---|---  
`Number.gamma()` | Number  
Argument | Type | Details  
---|---|---  
this: `input` | Number | The input value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-gamma#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-gamma#colab-python-sample) More
```
// Values less than or equal to 0 are invalid.
print('Gamma for 0.001',ee.Number(0.001).gamma());// 999.423772484
print('Gamma for 0.5',ee.Number(0.5).gamma());// 1.772453850
print('Gamma for 1',ee.Number(1).gamma());// 1
print('Gamma for 100',ee.Number(100).gamma());// 9.332621544e+155
print('Gamma for 200',ee.Number(200).gamma());// Infinity
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Values less than or equal to 0 are invalid.
print('Gamma for 0.001:', ee.Number(0.001).gamma().getInfo())  # 999.423772484
print('Gamma for 0.5:', ee.Number(0.5).gamma().getInfo())  # 1.772453850
print('Gamma for 1:', ee.Number(1).gamma().getInfo())  # 1
print('Gamma for 100:', ee.Number(100).gamma().getInfo())  # 9.332621544e+155
print('Gamma for 200:', ee.Number(200).gamma().getInfo())  # Infinity
```

Was this helpful?
