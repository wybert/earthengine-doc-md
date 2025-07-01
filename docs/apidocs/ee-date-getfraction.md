 
#  ee.Date.getFraction
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-date-getfraction#examples)


Returns this date's elapsed fraction of the specified unit (between 0 and 1). 
Usage| Returns  
---|---  
`Date.getFraction(unit,  _timeZone_)`| Float  
Argument| Type| Details  
---|---|---  
this: `date`| Date|   
`unit`| String| One of 'year', 'month', 'week', 'day', 'hour', 'minute', or 'second'.  
`timeZone`| String, default: null| The time zone (e.g., 'America/Los_Angeles'); defaults to UTC.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-date-getfraction#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-date-getfraction#colab-python-sample) More
```
vardate=ee.Date('2021-4-30T07:15:31.24');
print('Elapsed fraction of a year',date.getFraction('year'));
print('Elapsed fraction of a month',date.getFraction('month'));
print('Elapsed fraction of a week',date.getFraction('week'));
print('Elapsed fraction of a day',date.getFraction('day'));
print('Elapsed fraction of an hour',date.getFraction('hour'));
print('Elapsed fraction of a minute',date.getFraction('minute'));
print('Elapsed fraction of a second',date.getFraction('second'));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
date = ee.Date('2021-4-30T07:15:31.24')
display('Elapsed fraction of a year:', date.getFraction('year'))
display('Elapsed fraction of a month:', date.getFraction('month'))
display('Elapsed fraction of a week:', date.getFraction('week'))
display('Elapsed fraction of a day:', date.getFraction('day'))
display('Elapsed fraction of an hour:', date.getFraction('hour'))
display('Elapsed fraction of a minute:', date.getFraction('minute'))
display('Elapsed fraction of a second:', date.getFraction('second'))
```

Was this helpful?
