 
#  ee.Date.millis
Stay organized with collections  Save and categorize content based on your preferences. 
The number of milliseconds since 1970-01-01T00:00:00Z. Usage | Returns  
---|---  
`Date.millis()` | Long  
Argument | Type | Details  
---|---|---  
this: `date` | Date |   
## Examples
### Code Editor (JavaScript)
```
vardate=ee.Date(Date.now());

print('Milliseconds since Unix epoch',date.millis());
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
fromdatetimeimport datetime

date = ee.Date(datetime.now())

display('Milliseconds since Unix epoch:', date.millis())
```

