 
#  ee.Date.get
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-date-get#examples)


Returns the specified unit of this date. 
Usage| Returns  
---|---  
`Date.get(unit,  _timeZone_)`| Long  
Argument| Type| Details  
---|---|---  
this: `date`| Date|   
`unit`| String| One of 'year', 'month' (returns 1-12), 'week' (1-53), 'day' (1-31), 'hour' (0-23), 'minute' (0-59), or 'second' (0-59).  
`timeZone`| String, default: null| The time zone (e.g., 'America/Los_Angeles'); defaults to UTC.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-date-get#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-date-get#colab-python-sample) More
```
vardate=ee.Date('2021-4-30T07:15:31');
print('Year',date.get('year'));
print('Month',date.get('month'));
print('Week',date.get('week'));
print('Day',date.get('day'));
print('Hour',date.get('hour'));
print('Minute',date.get('minute'));
print('Second',date.get('second'));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
date = ee.Date('2021-4-30T07:15:31')
display('Year:', date.get('year'))
display('Month:', date.get('month'))
display('Week:', date.get('week'))
display('Day:', date.get('day'))
display('Hour:', date.get('hour'))
display('Minute:', date.get('minute'))
display('Second:', date.get('second'))
```

Was this helpful?
