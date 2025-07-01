 
#  ee.Date
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-date#examples)


Constructs a new Date object. 
Usage| Returns  
---|---  
`ee.Date(date,  _tz_)`| Date  
Argument| Type| Details  
---|---|---  
`date`| ComputedObject|Date|Number|String| The date to convert, one of: a number (number of milliseconds since the epoch), an ISO Date string, a JavaScript Date or a ComputedObject.  
`tz`| String, optional| An optional timezone only to be used with a string date.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-date#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-date#colab-python-sample) More
```
// Numeric inputs are interpreted as milliseconds from Unix epoch.
print(ee.Date(0));// Date (1970-01-01 00:00:00)
// Scale factors can make numerical inputs more readable (e.g. 60 seconds).
print(ee.Date(60*1000));// Date (1970-01-01 00:01:00)
// ISO 8601 date string input examples.
print(ee.Date('2020'));// Date (2020-01-01 00:00:00)
print(ee.Date('2017-6-24'));// Date (2017-06-24 00:00:00)
print(ee.Date('2017-06-24'));// Date (2017-06-24 00:00:00)
print(ee.Date('2017-6-24T00:14:46'));// Date (2017-06-24 00:14:46)
print(ee.Date('2017-06-24T23:59:59'));// Date (2017-06-24 23:59:59)
// With an optional time zone.
print(ee.Date('2020','US/Mountain'));// Date (2020-01-01T07:00:00)
// Convert JavaScript now to Earth Engine Date
print(ee.Date(Date.now()));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
fromdatetimeimport datetime
# Numeric inputs are interpreted as milliseconds from Unix epoch.
print(ee.Date(0).format().getInfo()) # 1970-01-01T00:00:00
# Scale factors can make numerical inputs more readable (e.g. 60 seconds).
print(ee.Date(60 * 1000).format().getInfo()) # 1970-01-01T00:01:00
# ISO 8601 date string input examples.
print(ee.Date('2020').format().getInfo()) # 2020-01-01T00:00:00
print(ee.Date('2017-6-24').format().getInfo()) # 2017-06-24T00:00:00
print(ee.Date('2017-06-24').format().getInfo()) # 2017-06-24T00:00:00
print(ee.Date('2017-6-24T00:14:46').format().getInfo()) # 2017-06-24T00:14:46
print(ee.Date('2017-06-24T23:59:59').format().getInfo()) # 2017-06-24T23:59:59
# With an optional time zone.
print(ee.Date('2020', 'US/Mountain').format().getInfo()) # 2020-01-01T07:00:00
# Convert Python datetime.now() to Earth Engine Date
print(ee.Date(datetime.now()).format().getInfo())
```

Was this helpful?
