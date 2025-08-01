 
#  ee.Number.int16
Stay organized with collections  Save and categorize content based on your preferences. 
Casts the input value to a signed 16-bit integer. Usage | Returns  
---|---  
`Number.int16()` | Number  
Argument | Type | Details  
---|---|---  
this: `input` | Number | The input value.  
## Examples
### Code Editor (JavaScript)
```
// Cast a number to signed 16-bit integer: [-32768, 32767].
varnumber=ee.Number(100);
print('Number:',number);

varint16Number=number.int16();
print('Number cast to int16:',int16Number);


/**
 * Casting numbers to int16 that are outside of its range and precision can
 * modify the resulting value, note the behavior of the following scenarios.
 */

// A floating point number cast to int16 loses decimal precision.
varfloat=ee.Number(1.7);
print('Floating point value:',float);

varfloatToInt16=float.int16();
print('Floating point value cast to int16:',floatToInt16);

// A number greater than int16 range max cast to int16 becomes int16 range max.
varINT16_MAX=32767;
varoutOfRangeHi=ee.Number(INT16_MAX+12345);
print('Greater than int16 max:',outOfRangeHi);

varoutOfRangeHiToInt16=outOfRangeHi.int16();
print('Greater than int16 max cast to int16 becomes int16 max:',outOfRangeHiToInt16);

// A number greater than int16 range min cast to int16 becomes int16 range min.
varINT16_MIN=-32768;
varoutOfRangeLo=ee.Number(INT16_MIN-12345);
print('Less than int16 min:',outOfRangeLo);

varoutOfRangeLoToInt16=outOfRangeLo.int16();
print('Less than int16 min cast to int16 becomes int16 min:',outOfRangeLoToInt16);
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Cast a number to signed 16-bit integer: [-32768, 32767].
number = ee.Number(100)
print('Number:', number.getInfo())

int16_number = number.int16()
print('Number cast to int16:', int16_number.getInfo())


"""Casting numbers to int16 that are outside of its range and precision can
modify the resulting value, note the behavior of the following scenarios.
"""

# A floating point number cast to int16 loses decimal precision.
float_number = ee.Number(1.7)
print('Floating point value:', float_number.getInfo())

float_to_int16 = float_number.int16()
print('Floating point value cast to int16:', float_to_int16.getInfo())

# A number greater than int16 range max cast to int16 becomes int16 range max.
INT16_MAX = 32767
out_of_range_hi = ee.Number(INT16_MAX + 12345)
print('Greater than int16 max:', out_of_range_hi.getInfo())

out_of_range_hi_to_int16 = out_of_range_hi.int16()
print('Greater than int16 max cast to int16 becomes int16 max:',
      out_of_range_hi_to_int16.getInfo())

# A number greater than int16 range min cast to int16 becomes int16 range min.
INT16_MIN = -32768
out_of_range_lo = ee.Number(INT16_MIN - 12345)
print('Less than int16 min:', out_of_range_lo.getInfo())

out_of_range_lo_to_int16 = out_of_range_lo.int16()
print('Less than int16 min cast to int16 becomes int16 min:',
      out_of_range_lo_to_int16.getInfo())
```

