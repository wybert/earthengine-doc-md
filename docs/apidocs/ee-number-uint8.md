 
#  ee.Number.uint8
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-uint8#examples)


Casts the input value to an unsigned 8-bit integer.
Usage | Returns  
---|---  
`Number.uint8()` | Number  
Argument | Type | Details  
---|---|---  
this: `input` | Number | The input value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-uint8#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-uint8#colab-python-sample) More
```
// Cast a number to unsigned 8-bit integer: [0, 255].
varnumber=ee.Number(100);
print('Number:',number);

varuint8Number=number.uint8();
print('Number cast to uint8:',uint8Number);


/**
 * Casting numbers to uint8 that are outside of its range and precision can
 * modify the resulting value, note the behavior of the following scenarios.
 */

// A floating point number cast to uint8 loses decimal precision.
varfloat=ee.Number(1.7);
print('Floating point value:',float);

varfloatToUint8=float.uint8();
print('Floating point value cast to uint8:',floatToUint8);

// A number greater than uint8 range max cast to uint8 becomes uint8 range max.
varUINT8_MAX=255;
varoutOfRangeHi=ee.Number(UINT8_MAX+12345);
print('Greater than uint8 max:',outOfRangeHi);

varoutOfRangeHiToUint8=outOfRangeHi.uint8();
print('Greater than uint8 max cast to uint8 becomes uint8 max:',outOfRangeHiToUint8);

// A number greater than uint8 range min cast to uint8 becomes uint8 range min.
varUINT8_MIN=0;
varoutOfRangeLo=ee.Number(UINT8_MIN-12345);
print('Less than uint8 min:',outOfRangeLo);

varoutOfRangeLoToUint8=outOfRangeLo.uint8();
print('Less than uint8 min cast to uint8 becomes uint8 min:',outOfRangeLoToUint8);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Cast a number to unsigned 8-bit integer: [0, 255].
number = ee.Number(100)
print('Number:', number.getInfo())

uint8_number = number.uint8()
print('Number cast to uint8:', uint8_number.getInfo())


"""Casting numbers to uint8 that are outside of its range and precision can
modify the resulting value, note the behavior of the following scenarios.
"""

# A floating point number cast to uint8 loses decimal precision.
float_number = ee.Number(1.7)
print('Floating point value:', float_number.getInfo())

float_to_uint8 = float_number.uint8()
print('Floating point value cast to uint8:', float_to_uint8.getInfo())

# A number greater than uint8 range max cast to uint8 becomes uint8 range max.
UINT8_MAX = 255
out_of_range_hi = ee.Number(UINT8_MAX + 12345)
print('Greater than uint8 max:', out_of_range_hi.getInfo())

out_of_range_hi_to_uint8 = out_of_range_hi.uint8()
print('Greater than uint8 max cast to uint8 becomes uint8 max:',
      out_of_range_hi_to_uint8.getInfo())

# A number greater than uint8 range min cast to uint8 becomes uint8 range min.
UINT8_MIN = 0
out_of_range_lo = ee.Number(UINT8_MIN - 12345)
print('Less than uint8 min:', out_of_range_lo.getInfo())

out_of_range_lo_to_uint8 = out_of_range_lo.uint8()
print('Less than uint8 min cast to uint8 becomes uint8 min:',
      out_of_range_lo_to_uint8.getInfo())
```

Was this helpful?
