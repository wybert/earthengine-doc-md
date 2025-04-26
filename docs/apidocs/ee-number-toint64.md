 
#  ee.Number.toInt64 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-toint64#examples)


Casts the input value to a signed 64-bit integer. 
Usage| Returns  
---|---  
`Number.toInt64()`| Number  
Argument| Type| Details  
---|---|---  
this: `input`| Number| The input value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-toint64#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-toint64#colab-python-sample) More
```
// Cast a number to signed 64-bit integer: [-9223372036854776000, 9223372036854776000].
varnumber=ee.Number(100);
print('Number:',number);
varint64Number=number.toInt64();
print('Number cast to int64:',int64Number);

/**
 * Casting numbers to int64 that are outside of its range and precision can
 * modify the resulting value, note the behavior of the following scenarios.
 */
// A floating point number cast to int64 loses decimal precision.
varfloat=ee.Number(1.7);
print('Floating point value:',float);
varfloatToInt64=float.toInt64();
print('Floating point value cast to int64:',floatToInt64);
// A number greater than int64 range max cast to int64 becomes int64 range max.
varINT64_MAX=9223372036854776000;
varoutOfRangeHi=ee.Number(INT64_MAX+12345);
print('Greater than int64 max:',outOfRangeHi);
varoutOfRangeHiToInt64=outOfRangeHi.toInt64();
print('Greater than int64 max cast to int64 becomes int64 max:',outOfRangeHiToInt64);
// A number greater than int64 range min cast to int64 becomes int64 range min.
varINT64_MIN=-9223372036854776000;
varoutOfRangeLo=ee.Number(INT64_MIN-12345);
print('Less than int64 min:',outOfRangeLo);
varoutOfRangeLoToInt64=outOfRangeLo.toInt64();
print('Less than int64 min cast to int64 becomes int64 min:',outOfRangeLoToInt64);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Cast a number to signed 64-bit integer:
# [-9223372036854775808, 9223372036854775808].
number = ee.Number(100)
print('Number:', number.getInfo())
int64_number = number.toInt64()
print('Number cast to int64:', int64_number.getInfo())

"""Casting numbers to int64 that are outside of its range and precision can
modify the resulting value, note the behavior of the following scenarios.
"""
# A floating point number cast to int64 loses decimal precision.
float_number = ee.Number(1.7)
print('Floating point value:', float_number.getInfo())
float_to_int64 = float_number.toInt64()
print('Floating point value cast to int64:', float_to_int64.getInfo())
# A number greater than int64 range max becomes int64 range max.
# Python int is too large to be mapped to int64, use float instead.
INT64_MAX = 9223372036854775808.0
out_of_range_hi = ee.Number(INT64_MAX + 12345)
print('Greater than int64 max:', '{:.0f}'.format(out_of_range_hi.getInfo()))
out_of_range_hi_to_int64 = out_of_range_hi.toInt64()
print('Greater than int64 max cast to int64 becomes int64 max:',
   '{:.0f}'.format(out_of_range_hi_to_int64.getInfo()))
# A number greater than int64 range min becomes int64 range min.
# Python int is too large to be mapped to int64, use float instead.
INT64_MIN = -9223372036854775808.0
out_of_range_lo = ee.Number(INT64_MIN - 12345)
print('Less than int64 min:', '{:.0f}'.format(out_of_range_lo.getInfo()))
out_of_range_lo_to_int64 = out_of_range_lo.toInt64()
print('Less than int64 min cast to int64 becomes int64 min:',
   '{:.0f}'.format(out_of_range_lo_to_int64.getInfo()))
```

Was this helpful?
