 
#  ee.Number.int8
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-int8#examples)


Casts the input value to a signed 8-bit integer.
Usage | Returns  
---|---  
`Number.int8()` | Number  
Argument | Type | Details  
---|---|---  
this: `input` | Number | The input value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-int8#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-int8#colab-python-sample) More
```
// Cast a number to signed 8-bit integer: [-128, 127].
varnumber=ee.Number(100);
print('Number:',number);

varint8Number=number.int8();
print('Number cast to int8:',int8Number);


/**
 * Casting numbers to int8 that are outside of its range and precision can
 * modify the resulting value, note the behavior of the following scenarios.
 */

// A floating point number cast to int8 loses decimal precision.
varfloat=ee.Number(1.7);
print('Floating point value:',float);

varfloatToInt8=float.int8();
print('Floating point value cast to int8:',floatToInt8);

// A number greater than int8 range max cast to int8 becomes int8 range max.
varINT8_MAX=127;
varoutOfRangeHi=ee.Number(INT8_MAX+12345);
print('Greater than int8 max:',outOfRangeHi);

varoutOfRangeHiToInt8=outOfRangeHi.int8();
print('Greater than int8 max cast to int8 becomes int8 max:',outOfRangeHiToInt8);

// A number greater than int8 range min cast to int8 becomes int8 range min.
varINT8_MIN=-128;
varoutOfRangeLo=ee.Number(INT8_MIN-12345);
print('Less than int8 min:',outOfRangeLo);

varoutOfRangeLoToInt8=outOfRangeLo.int8();
print('Less than int8 min cast to int8 becomes int8 min:',outOfRangeLoToInt8);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Cast a number to signed 8-bit integer: [-128, 127].
number = ee.Number(100)
print('Number:', number.getInfo())

int8_number = number.int8()
print('Number cast to int8:', int8_number.getInfo())


"""Casting numbers to int8 that are outside of its range and precision can
modify the resulting value, note the behavior of the following scenarios.
"""

# A floating point number cast to int8 loses decimal precision.
float_number = ee.Number(1.7)
print('Floating point value:', float_number.getInfo())

float_to_int8 = float_number.int8()
print('Floating point value cast to int8:', float_to_int8.getInfo())

# A number greater than int8 range max cast to int8 becomes int8 range max.
INT8_MAX = 127
out_of_range_hi = ee.Number(INT8_MAX + 12345)
print('Greater than int8 max:', out_of_range_hi.getInfo())

out_of_range_hi_to_int8 = out_of_range_hi.int8()
print('Greater than int8 max cast to int8 becomes int8 max:',
      out_of_range_hi_to_int8.getInfo())

# A number greater than int8 range min cast to int8 becomes int8 range min.
INT8_MIN = -128
out_of_range_lo = ee.Number(INT8_MIN - 12345)
print('Less than int8 min:', out_of_range_lo.getInfo())

out_of_range_lo_to_int8 = out_of_range_lo.int8()
print('Less than int8 min cast to int8 becomes int8 min:',
      out_of_range_lo_to_int8.getInfo())
```

