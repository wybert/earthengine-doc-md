 
#  ee.Number.uint16 
Stay organized with collections  Save and categorize content based on your preferences. 
Casts the input value to an unsigned 16-bit integer. Usage| Returns  
---|---  
`Number.uint16()`| Number  
Argument| Type| Details  
---|---|---  
this: `input`| Number| The input value.  
## Examples
### Code Editor (JavaScript)
```
// Cast a number to unsigned 16-bit integer: [0, 65535].
varnumber=ee.Number(100);
print('Number:',number);
varuint16Number=number.uint16();
print('Number cast to uint16:',uint16Number);

/**
 * Casting numbers to uint16 that are outside of its range and precision can
 * modify the resulting value, note the behavior of the following scenarios.
 */
// A floating point number cast to uint16 loses decimal precision.
varfloat=ee.Number(1.7);
print('Floating point value:',float);
varfloatToUint16=float.uint16();
print('Floating point value cast to uint16:',floatToUint16);
// A number greater than uint16 range max cast to uint16 becomes uint16 range max.
varUINT16_MAX=65535;
varoutOfRangeHi=ee.Number(UINT16_MAX+12345);
print('Greater than uint16 max:',outOfRangeHi);
varoutOfRangeHiToUint16=outOfRangeHi.uint16();
print('Greater than uint16 max cast to uint16 becomes uint16 max:',outOfRangeHiToUint16);
// A number greater than uint16 range min cast to uint16 becomes uint16 range min.
varUINT16_MIN=0;
varoutOfRangeLo=ee.Number(UINT16_MIN-12345);
print('Less than uint16 min:',outOfRangeLo);
varoutOfRangeLoToUint16=outOfRangeLo.uint16();
print('Less than uint16 min cast to uint16 becomes uint16 min:',outOfRangeLoToUint16);
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Cast a number to unsigned 16-bit integer: [0, 65535].
number = ee.Number(100)
print('Number:', number.getInfo())
uint16_number = number.uint16()
print('Number cast to uint16:', uint16_number.getInfo())

"""Casting numbers to uint16 that are outside of its range and precision can
modify the resulting value, note the behavior of the following scenarios.
"""
# A floating point number cast to uint16 loses decimal precision.
float_number = ee.Number(1.7)
print('Floating point value:', float_number.getInfo())
float_number_to_uint16 = float_number.uint16()
print('Floating point value cast to uint16:', float_number_to_uint16.getInfo())
# A number greater than uint16 range max cast to uint16
# becomes uint16 range max.
UINT16_MAX = 65535
out_of_range_hi = ee.Number(UINT16_MAX + 12345)
print('Greater than uint16 max:', out_of_range_hi.getInfo())
out_of_range_hi_to_uint16 = out_of_range_hi.uint16()
print('Greater than uint16 max cast to uint16 becomes uint16 max:',
   out_of_range_hi_to_uint16.getInfo())
# A number greater than uint16 range min cast to uint16
# becomes uint16 range min.
UINT16_MIN = 0
out_of_range_lo = ee.Number(UINT16_MIN - 12345)
print('Less than uint16 min:', out_of_range_lo.getInfo())
out_of_range_lo_to_uint16 = out_of_range_lo.uint16()
print('Less than uint16 min cast to uint16 becomes uint16 min:',
   out_of_range_lo_to_uint16.getInfo())
```

