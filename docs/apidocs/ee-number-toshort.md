 
#  ee.Number.toShort 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-toshort#examples)


Casts the input value to a signed 16-bit integer. 
Usage| Returns  
---|---  
`Number.toShort()`| Number  
Argument| Type| Details  
---|---|---  
this: `input`| Number| The input value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-toshort#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-toshort#colab-python-sample) More
```
// Cast a number to signed 16-bit integer: [-32768, 32767].
varnumber=ee.Number(100);
print('Number:',number);
varshortNumber=number.toShort();
print('Number cast to short:',shortNumber);

/**
 * Casting numbers to short that are outside of its range and precision can
 * modify the resulting value, note the behavior of the following scenarios.
 */
// A floating point number cast to short loses decimal precision.
varfloat=ee.Number(1.7);
print('Floating point value:',float);
varfloatToShort=float.toShort();
print('Floating point value cast to short:',floatToShort);
// A number greater than short range max cast to short becomes short range max.
varSHORT_MAX=32767;
varoutOfRangeHi=ee.Number(SHORT_MAX+12345);
print('Greater than short max:',outOfRangeHi);
varoutOfRangeHiToShort=outOfRangeHi.toShort();
print('Greater than short max cast to short becomes short max:',outOfRangeHiToShort);
// A number greater than short range min cast to short becomes short range min.
varSHORT_MIN=-32768;
varoutOfRangeLo=ee.Number(SHORT_MIN-12345);
print('Less than short min:',outOfRangeLo);
varoutOfRangeLoToShort=outOfRangeLo.toShort();
print('Less than short min cast to short becomes short min:',outOfRangeLoToShort);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Cast a number to signed 16-bit integer: [-32768, 32767].
number = ee.Number(100)
print('Number:', number.getInfo())
short_number = number.toShort()
print('Number cast to short:', short_number.getInfo())

"""Casting numbers to short that are outside of its range and precision can
modify the resulting value, note the behavior of the following scenarios.
"""
# A floating point number cast to short loses decimal precision.
float_number = ee.Number(1.7)
print('Floating point value:', float_number.getInfo())
float_to_short = float_number.toShort()
print('Floating point value cast to short:', float_to_short.getInfo())
# A number greater than short range max cast to short becomes short range max.
SHORT_MAX = 32767
out_of_range_hi = ee.Number(SHORT_MAX + 12345)
print('Greater than short max:', out_of_range_hi.getInfo())
out_of_range_hi_to_short = out_of_range_hi.toShort()
print('Greater than short max cast to short becomes short max:',
   out_of_range_hi_to_short.getInfo())
# A number greater than short range min cast to short becomes short range min.
SHORT_MIN = -32768
out_of_range_lo = ee.Number(SHORT_MIN - 12345)
print('Less than short min:', out_of_range_lo.getInfo())
out_of_range_lo_to_short = out_of_range_lo.toShort()
print('Less than short min cast to short becomes short min:',
   out_of_range_lo_to_short.getInfo())
```

