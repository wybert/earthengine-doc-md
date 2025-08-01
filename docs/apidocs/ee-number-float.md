 
#  ee.Number.float
Stay organized with collections  Save and categorize content based on your preferences. 
Casts the input value to a 32-bit float. Usage | Returns  
---|---  
`Number.float()` | Number  
Argument | Type | Details  
---|---|---  
this: `input` | Number | The input value.  
## Examples
### Code Editor (JavaScript)
```
// Declare an ee.Number.
varnumber=ee.Number(100);
print('ee.Number:',number);

// Cast a number to signed 32-bit floating point.
varfloatNumber=number.float();
print('ee.Number cast to float:',floatNumber);
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Declare an ee.Number.
number = ee.Number(100)
print('ee.Number:', number.getInfo())

# Cast a number to signed 32-bit floating point.
float_number = number.float()
print('ee.Number cast to float:', float_number.getInfo())
```

