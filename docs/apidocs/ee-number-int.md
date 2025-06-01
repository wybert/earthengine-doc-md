 
#  ee.Number.int 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-int#examples)


Casts the input value to a signed 32-bit integer. 
Usage| Returns  
---|---  
`Number.int()`| Number  
Argument| Type| Details  
---|---|---  
this: `input`| Number| The input value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-int#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-int#colab-python-sample) More
```
// Cast a number to signed 32-bit integer: [-2147483648, 2147483647].
varnumber=ee.Number(100);
print('Number:',number);
varintNumber=number.int();
print('Number cast to int:',intNumber);

/**
 * Casting numbers to int that are outside of its range and precision can
 * modify the resulting value, note the behavior of the following scenarios.
 */
// A floating point number cast to int loses decimal precision.
varfloat=ee.Number(1.7);
print('Floating point value:',float);
varfloatToInt=float.int();
print('Floating point value cast to int:',floatToInt);
// A number greater than int range max cast to int becomes int range max.
varINT_MAX=2147483647;
varoutOfRangeHi=ee.Number(INT_MAX+12345);
print('Greater than int max:',outOfRangeHi);
varoutOfRangeHiToInt=outOfRangeHi.int();
print('Greater than int max cast to int becomes int max:',outOfRangeHiToInt);
// A number greater than int range min cast to int becomes int range min.
varINT_MIN=-2147483648;
varoutOfRangeLo=ee.Number(INT_MIN-12345);
print('Less than int min:',outOfRangeLo);
varoutOfRangeLoToInt=outOfRangeLo.int();
print('Less than int min cast to int becomes int min:',outOfRangeLoToInt);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Cast a number to signed 32-bit integer: [-2147483648, 2147483647].
number = ee.Number(100)
print('Number:', number.getInfo())
int_number = number.int()
print('Number cast to int:', int_number.getInfo())

"""Casting numbers to int that are outside of its range and precision can
modify the resulting value, note the behavior of the following scenarios.
"""
# A floating point number cast to int loses decimal precision.
float_number = ee.Number(1.7)
print('Floating point value:', float_number.getInfo())
float_to_int = float_number.int()
print('Floating point value cast to int:', float_to_int.getInfo())
# A number greater than int range max cast to int becomes int range max.
INT_MAX = 2147483647
out_of_range_hi = ee.Number(INT_MAX + 12345)
print('Greater than int max:', out_of_range_hi.getInfo())
out_of_range_hi_to_int = out_of_range_hi.int()
print('Greater than int max cast to int becomes int max:',
   out_of_range_hi_to_int.getInfo())
# A number greater than int range min cast to int becomes int range min.
INT_MIN = -2147483648
out_of_range_lo = ee.Number(INT_MIN - 12345)
print('Less than int min:', out_of_range_lo.getInfo())
out_of_range_lo_to_int = out_of_range_lo.int()
print('Less than int min cast to int becomes int min:',
   out_of_range_lo_to_int.getInfo())
```

