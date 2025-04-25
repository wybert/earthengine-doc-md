 
#  ee.Date.unitRatio 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-date-unitratio#examples)


Returns the ratio of the length of one unit to the length of another, e.g., unitRatio('day', 'minute') returns 1440. Valid units are 'year', 'month' 'week', 'day', 'hour', 'minute', and 'second'. 
Usage| Returns  
---|---  
`ee.Date.unitRatio(numerator, denominator)`| Float  
Argument| Type| Details  
---|---|---  
`numerator`| String  
`denominator`| String  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-date-unitratio#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-date-unitratio#colab-python-sample) More
```
print('Minutes in a day',ee.Date.unitRatio('day','minute'));
print('Seconds in a year',ee.Date.unitRatio('year','second'));
print('Years in a month',ee.Date.unitRatio('month','year'));
print('Hours in a week',ee.Date.unitRatio('week','hour'));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
display('Minutes in a day:', ee.Date.unitRatio('day', 'minute'))
display('Seconds in a year:', ee.Date.unitRatio('year', 'second'))
display('Years in a month:', ee.Date.unitRatio('month', 'year'))
display('Hours in a week:', ee.Date.unitRatio('week', 'hour'))
```

