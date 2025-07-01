 
#  ee.Date.getRange
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-date-getrange#examples)


Returns a DateRange covering the unit of the specified type that contains this date, e.g., Date('2013-3-15').getRange('year') returns DateRange('2013-1-1', '2014-1-1'). 
Usage| Returns  
---|---  
`Date.getRange(unit,  _timeZone_)`| DateRange  
Argument| Type| Details  
---|---|---  
this: `date`| Date|   
`unit`| String| One of 'year', 'month', 'week', 'day', 'hour', 'minute', or 'second'.  
`timeZone`| String, default: null| The time zone (e.g., 'America/Los_Angeles'); defaults to UTC.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-date-getrange#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-date-getrange#colab-python-sample) More
```
vardate=ee.Date('2021-4-30T07:15:31.24');
print('1-year date range covering input date',date.getRange('year'));
print('1-month date range covering input date',date.getRange('month'));
print('1-week date range covering input date',date.getRange('week'));
print('1-day date range covering input date',date.getRange('day'));
print('1-hour date range covering input date',date.getRange('hour'));
print('1-minute date range covering input date',date.getRange('minute'));
print('1-second date range covering input date',date.getRange('second'));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
date = ee.Date('2021-4-30T07:15:31.24')
display('1-year date range covering input date:', date.getRange('year'))
display('1-month date range covering input date:', date.getRange('month'))
display('1-week date range covering input date:', date.getRange('week'))
display('1-day date range covering input date:', date.getRange('day'))
display('1-hour date range covering input date:', date.getRange('hour'))
display('1-minute date range covering input date:', date.getRange('minute'))
display('1-second date range covering input date:', date.getRange('second'))
```

Was this helpful?
