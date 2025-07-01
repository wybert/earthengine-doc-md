 
#  ee.Number.byte
Stay organized with collections  Save and categorize content based on your preferences. 
Casts the input value to an unsigned 8-bit integer. Usage| Returns  
---|---  
`Number.byte()`| Number  
Argument| Type| Details  
---|---|---  
this: `input`| Number| The input value.  
## Examples
### Code Editor (JavaScript)
```
// Cast a number to unsigned 8-bit integer: [0, 255].
varnumber=ee.Number(100);
print('Number:',number);
varbyteNumber=number.byte();
print('Number cast to byte:',byteNumber);

/**
 * Casting numbers to byte that are outside of its range and precision can
 * modify the resulting value, note the behavior of the following scenarios.
 */
// A floating point number cast to byte loses decimal precision.
varfloat=ee.Number(1.7);
print('Floating point value:',float);
varfloatToByte=float.byte();
print('Floating point value cast to byte:',floatToByte);
// A number greater than byte range max cast to byte becomes byte range max.
varBYTE_MAX=255;
varoutOfRangeHi=ee.Number(BYTE_MAX+12345);
print('Greater than byte max:',outOfRangeHi);
varoutOfRangeHiToByte=outOfRangeHi.byte();
print('Greater than byte max cast to byte becomes byte max:',outOfRangeHiToByte);
// A number greater than byte range min cast to byte becomes byte range min.
varBYTE_MIN=0;
varoutOfRangeLo=ee.Number(BYTE_MIN-12345);
print('Less than byte min:',outOfRangeLo);
varoutOfRangeLoToByte=outOfRangeLo.byte();
print('Less than byte min cast to byte becomes byte min:',outOfRangeLoToByte);
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Cast a number to unsigned 8-bit integer: [0, 255].
number = ee.Number(100)
print('Number:', number.getInfo())
byte_number = number.byte()
print('Number cast to byte:', byte_number.getInfo())

"""Casting numbers to byte that are outside of its range and precision can
modify the resulting value, note the behavior of the following scenarios.
"""
# A floating point number cast to byte loses decimal precision.
float_number = ee.Number(1.7)
print('Floating point value:', float_number.getInfo())
float_to_byte = float_number.byte()
print('Floating point value cast to byte:', float_to_byte.getInfo())
# A number greater than byte range max cast to byte becomes byte range max.
BYTE_MAX = 255
out_of_range_hi = ee.Number(BYTE_MAX + 12345)
print('Greater than byte max:', out_of_range_hi.getInfo())
out_of_range_hi_to_byte = out_of_range_hi.byte()
print('Greater than byte max cast to byte becomes byte max:',
   out_of_range_hi_to_byte.getInfo())
# A number greater than byte range min cast to byte becomes byte range min.
BYTE_MIN = 0
out_of_range_lo = ee.Number(BYTE_MIN - 12345)
print('Less than byte min:', out_of_range_lo.getInfo())
out_of_range_lo_to_byte = out_of_range_lo.byte()
print('Less than byte min cast to byte becomes byte min:',
   out_of_range_lo_to_byte.getInfo())
```

