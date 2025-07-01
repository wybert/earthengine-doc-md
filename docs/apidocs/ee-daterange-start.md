 
#  ee.DateRange.start
Stay organized with collections  Save and categorize content based on your preferences. 
Returns the (inclusive) start of this DateRange. Usage| Returns  
---|---  
`DateRange.start()`| Date  
Argument| Type| Details  
---|---|---  
this: `dateRange`| DateRange|   
## Examples
### Code Editor (JavaScript)
```
// An ee.DateRange.
vardateRange=ee.DateRange('2017-06-24','2017-07-24');
// Return the start of the ee.DateRange as an ee.Date.
print('The start of this ee.DateRange is',dateRange.start());
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# An ee.DateRange.
date_range = ee.DateRange('2017-06-24', '2017-07-24')
# Return the start of the ee.DateRange as an ee.Date.
display('The start of this ee.DateRange is', date_range.start())
```

