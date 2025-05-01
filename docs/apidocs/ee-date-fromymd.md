 
#  ee.Date.fromYMD 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-date-fromymd#examples)


Returns a Date given year, month, day. 
Usage| Returns  
---|---  
`ee.Date.fromYMD(year, month, day,  _timeZone_)`| Date  
Argument| Type| Details  
---|---|---  
`year`| Integer| The year, 2013, for example.  
`month`| Integer| The month, 3, for example.  
`day`| Integer| The day, 15, for example.  
`timeZone`| String, default: null| The time zone (e.g., 'America/Los_Angeles'); defaults to UTC.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-date-fromymd#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-date-fromymd#colab-python-sample) More
```
print('Date with default UTC',
ee.Date.fromYMD(2021,4,30));
print('Date with time zone specified',
ee.Date.fromYMD(2021,4,30,'America/Los_Angeles'));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
display('Date with default UTC:', ee.Date.fromYMD(2021, 4, 30))
display(
  'Date with time zone specified:',
  ee.Date.fromYMD(2021, 4, 30, 'America/Los_Angeles')
)
```

Was this helpful?
