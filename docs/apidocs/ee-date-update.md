 
#  ee.Date.update 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-date-update#examples)


Create a new Date by setting one or more of the units of the given Date to a new value. If a timeZone is given the new value(s) is interpreted in that zone. 
Usage| Returns  
---|---  
`Date.update( _year_, _month_, _day_, _hour_, _minute_, _second_, _timeZone_)`| Date  
Argument| Type| Details  
---|---|---  
this: `date`| Date  
`year`| Integer, default: null  
`month`| Integer, default: null  
`day`| Integer, default: null  
`hour`| Integer, default: null  
`minute`| Integer, default: null  
`second`| Number, default: null  
`timeZone`| String, default: null| The time zone (e.g., 'America/Los_Angeles'); defaults to UTC.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-date-update#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-date-update#colab-python-sample) More
```
vardate=ee.Date('2021-4-30T07:15:31.24');
print('Updated year and minute components of the input date',
date.update({
year:2010,
minute:59
})
);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
date = ee.Date('2021-4-30T07:15:31.24')
display(
  'Updated year and minute components of the input date:',
  date.update(year=2010, minute=59)
)
```

