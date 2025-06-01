 
#  ee.Date.getRelative 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Returns the specified (0-based) unit of this date relative to a larger unit, e.g., getRelative('day', 'year') returns a value between 0 and 365. 
Usage| Returns  
---|---  
`Date.getRelative(unit, inUnit,  _timeZone_)`| Long  
Argument| Type| Details  
---|---|---  
this: `date`| Date|   
`unit`| String| One of 'month' 'week', 'day', 'hour', 'minute', or 'second'.  
`inUnit`| String| One of 'year', 'month' 'week', 'day', 'hour', or 'minute'.  
`timeZone`| String, default: null| The time zone (e.g., 'America/Los_Angeles'); defaults to UTC.  
## Examples
### Code Editor (JavaScript)
```
vardate=ee.Date('2021-4-30T07:15:31.24');
print('0-based month of year',date.getRelative('month','year'));
print('0-based week of year',date.getRelative('week','year'));
print('0-based day of year',date.getRelative('day','year'));
print('0-based day of month',date.getRelative('day','month'));
print('0-based minute of day',date.getRelative('minute','day'));
print('0-based second of minute',date.getRelative('second','minute'));
// 0 is returned when unit argument is larger than inUnit argument.
print('0-based year of month (bad form)',date.getRelative('year','month'));
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
date = ee.Date('2021-4-30T07:15:31.24')
display('0-based month of year:', date.getRelative('month', 'year'))
display('0-based week of year:', date.getRelative('week', 'year'))
display('0-based day of year:', date.getRelative('day', 'year'))
display('0-based day of month:', date.getRelative('day', 'month'))
display('0-based minute of day:', date.getRelative('minute', 'day'))
display('0-based second of minute:', date.getRelative('second', 'minute'))
# 0 is returned when unit argument is larger than inUnit argument.
display('0-based year of month (bad form):', date.getRelative('year', 'month'))
```

