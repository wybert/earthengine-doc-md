 
#  ee.Number.long
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-long#examples)


Casts the input value to a signed 64-bit integer. 
Usage| Returns  
---|---  
`Number.long()`| Number  
Argument| Type| Details  
---|---|---  
this: `input`| Number| The input value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-long#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-long#colab-python-sample) More
```
// Declare an ee.Number.
varnumber=ee.Number(100);
print('ee.Number:',number);
// Cast a number to signed 64-bit integer.
varlongNumber=number.long();
print('ee.Number cast to long:',longNumber);

/**
* Casting numbers to long that are outside of its range and precision can
* modify the resulting value, note the behavior of the following scenarios.
*/
// A floating point number cast to long loses decimal precision.
varfloat=ee.Number(1.7);
print('Floating point value:',float);
varfloatToLong=float.long();
print('Floating point value cast to long:',floatToLong);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Declare an ee.Number.
number = ee.Number(100)
print('ee.Number:', number.getInfo())
# Cast a number to signed 64-bit integer.
long_number = number.long()
print('ee.Number cast to long:', long_number.getInfo())

"""Casting numbers to long that are outside of its range and precision can
modify the resulting value, note the behavior of the following scenarios.
"""
# A floating point number cast to long loses decimal precision.
float_number = ee.Number(1.7)
print('Floating point value:', float_number.getInfo())
float_to_long = float_number.long()
print('Floating point value cast to long:', float_to_long.getInfo())
```

Was this helpful?
