 
#  ee.Number.toUint32 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-touint32#examples)


Casts the input value to an unsigned 32-bit integer. 
Usage| Returns  
---|---  
`Number.toUint32()`| Number  
Argument| Type| Details  
---|---|---  
this: `input`| Number| The input value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-touint32#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-touint32#colab-python-sample) More
```
// Cast a number to unsigned 32-bit integer: [0, 4294967295].
varnumber=ee.Number(100);
print('Number:',number);
varuint32Number=number.toUint32();
print('Number cast to uint32:',uint32Number);

/**
 * Casting numbers to uint32 that are outside of its range and precision can
 * modify the resulting value, note the behavior of the following scenarios.
 */
// A floating point number cast to uint32 loses decimal precision.
varfloat=ee.Number(1.7);
print('Floating point value:',float);
varfloatToUint32=float.toUint32();
print('Floating point value cast to uint32:',floatToUint32);
// A number greater than uint32 range max cast to uint32 becomes uint32 range max.
varUINT32_MAX=4294967295;
varoutOfRangeHi=ee.Number(UINT32_MAX+12345);
print('Greater than uint32 max:',outOfRangeHi);
varoutOfRangeHiToUint32=outOfRangeHi.toUint32();
print('Greater than uint32 max cast to uint32 becomes uint32 max:',outOfRangeHiToUint32);
// A number greater than uint32 range min cast to uint32 becomes uint32 range min.
varUINT32_MIN=0;
varoutOfRangeLo=ee.Number(UINT32_MIN-12345);
print('Less than uint32 min:',outOfRangeLo);
varoutOfRangeLoToUint32=outOfRangeLo.toUint32();
print('Less than uint32 min cast to uint32 becomes uint32 min:',outOfRangeLoToUint32);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Cast a number to unsigned 32-bit integer: [0, 4294967295].
number = ee.Number(100)
print('Number:', number.getInfo())
uint32_number = number.toUint32()
print('Number cast to uint32:', uint32_number.getInfo())

"""Casting numbers to uint32 that are outside of its range and precision can
modify the resulting value, note the behavior of the following scenarios.
"""
# A floating point number cast to uint32 loses decimal precision.
float_number = ee.Number(1.7);
print('Floating point value:', float_number.getInfo())
float_to_uint32 = float_number.toUint32();
print('Floating point value cast to uint32:', float_to_uint32.getInfo())
# A number greater than uint32 range max cast to uint32
# becomes uint32 range max.
UINT32_MAX = 4294967295
out_of_range_hi = ee.Number(UINT32_MAX + 12345)
print('Greater than uint32 max:', out_of_range_hi.getInfo())
out_of_range_hi_to_uint32 = out_of_range_hi.toUint32()
print('Greater than uint32 max cast to uint32 becomes uint32 max:',
   out_of_range_hi_to_uint32.getInfo())
# A number greater than uint32 range min cast to uint32
# becomes uint32 range min.
UINT32_MIN = 0
out_of_range_lo = ee.Number(UINT32_MIN - 12345)
print('Less than uint32 min:', out_of_range_lo.getInfo())
out_of_range_lo_to_uint32 = out_of_range_lo.toUint32()
print('Less than uint32 min cast to uint32 becomes uint32 min:',
   out_of_range_lo_to_uint32.getInfo())
```

