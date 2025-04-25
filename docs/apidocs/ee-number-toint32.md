 
#  ee.Number.toInt32 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-toint32#examples)


Casts the input value to a signed 32-bit integer. 
Usage| Returns  
---|---  
`Number.toInt32()`| Number  
Argument| Type| Details  
---|---|---  
this: `input`| Number| The input value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-toint32#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-toint32#colab-python-sample) More
```
// Cast a number to signed 32-bit integer: [-2147483648, 2147483647].
varnumber=ee.Number(100);
print('Number:',number);
varint32Number=number.toInt32();
print('Number cast to int32:',int32Number);

/**
 * Casting numbers to int32 that are outside of its range and precision can
 * modify the resulting value, note the behavior of the following scenarios.
 */
// A floating point number cast to int32 loses decimal precision.
varfloat=ee.Number(1.7);
print('Floating point value:',float);
varfloatToInt32=float.toInt32();
print('Floating point value cast to int32:',floatToInt32);
// A number greater than int32 range max cast to int32 becomes int32 range max.
varINT32_MAX=2147483647;
varoutOfRangeHi=ee.Number(INT32_MAX+12345);
print('Greater than int32 max:',outOfRangeHi);
varoutOfRangeHiToInt32=outOfRangeHi.toInt32();
print('Greater than int32 max cast to int32 becomes int32 max:',outOfRangeHiToInt32);
// A number greater than int32 range min cast to int32 becomes int32 range min.
varINT32_MIN=-2147483648;
varoutOfRangeLo=ee.Number(INT32_MIN-12345);
print('Less than int32 min:',outOfRangeLo);
varoutOfRangeLoToInt32=outOfRangeLo.toInt32();
print('Less than int32 min cast to int32 becomes int32 min:',outOfRangeLoToInt32);
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
int32_number = number.toInt32()
print('Number cast to int32:', int32_number.getInfo())

"""Casting numbers to int32 that are outside of its range and precision can
modify the resulting value, note the behavior of the following scenarios.
"""
# A floating point number cast to int32 loses decimal precision.
float_number = ee.Number(1.7)
print('Floating point value:', float_number.getInfo())
float_to_int32 = float_number.toInt32()
print('Floating point value cast to int32:', float_to_int32.getInfo())
# A number greater than int32 range max cast to int32 becomes int32 range max.
INT32_MAX = 2147483647
out_of_range_hi = ee.Number(INT32_MAX + 12345)
print('Greater than int32 max:', out_of_range_hi.getInfo())
out_of_range_hi_to_int32 = out_of_range_hi.toInt32()
print('Greater than int32 max cast to int32 becomes int32 max:',
   out_of_range_hi_to_int32.getInfo())
# A number greater than int32 range min cast to int32 becomes int32 range min.
INT32_MIN = -2147483648
out_of_range_lo = ee.Number(INT32_MIN - 12345)
print('Less than int32 min:', out_of_range_lo.getInfo())
out_of_range_lo_to_int32 = out_of_range_lo.toInt32()
print('Less than int32 min cast to int32 becomes int32 min:',
   out_of_range_lo_to_int32.getInfo())
```

Was this helpful?
