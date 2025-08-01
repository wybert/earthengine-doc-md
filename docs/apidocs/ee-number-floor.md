 
#  ee.Number.floor
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-floor#examples)


Computes the largest integer less than or equal to the input.
Usage | Returns  
---|---  
`Number.floor()` | Number  
Argument | Type | Details  
---|---|---  
this: `input` | Number | The input value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-floor#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-floor#colab-python-sample) More
```
// Positive numbers.
print('Floor for 2.1',ee.Number(2.1).floor());// 2
print('Floor for 2.5',ee.Number(2.5).floor());// 2
print('Floor for 2.9',ee.Number(2.9).floor());// 2

// Negative numbers.
print('Floor for -2.1',ee.Number(-2.1).floor());// -3
print('Floor for -2.5',ee.Number(-2.5).floor());// -3
print('Floor for -2.9',ee.Number(-2.9).floor());// -3
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Positive numbers.
print('Floor for 2.1:', ee.Number(2.1).floor().getInfo())  # 2
print('Floor for 2.5:', ee.Number(2.5).floor().getInfo())  # 2
print('Floor for 2.9:', ee.Number(2.9).floor().getInfo())  # 2

# Negative numbers.
print('Floor for -2.1:', ee.Number(-2.1).floor().getInfo())  # -3
print('Floor for -2.5:', ee.Number(-2.5).floor().getInfo())  # -3
print('Floor for -2.9:', ee.Number(-2.9).floor().getInfo())  # -3
```

Was this helpful?
