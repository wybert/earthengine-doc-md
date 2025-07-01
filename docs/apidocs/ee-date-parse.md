 
#  ee.Date.parse
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-date-parse#examples)


Parse a date string, given a string describing its format. 
Usage| Returns  
---|---  
`ee.Date.parse(format, date,  _timeZone_)`| Date  
Argument| Type| Details  
---|---|---  
`format`| String| A pattern, as described at http://joda-time.sourceforge.net/apidocs/org/joda/time/format/DateTimeFormat.html.  
`date`| String| A string matching the given pattern.  
`timeZone`| String, default: null| The time zone (e.g., 'America/Los_Angeles'); defaults to UTC.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-date-parse#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-date-parse#colab-python-sample) More
```
print(ee.Date.parse('yyyy MM dd','2021 4 30'));
print(ee.Date.parse('yyyy-MM-dd','2021-4-30'));
print(ee.Date.parse('yyyy/MM/dd','2021/4/30'));
print(ee.Date.parse('MM/dd/yy','4/30/21'));
print(ee.Date.parse('MMM. dd, yyyy','Apr. 30, 2021'));
print(ee.Date.parse('yyyy-MM-dd HH:mm:ss','2021-4-30 00:00:00'));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
display(ee.Date.parse('YYYY MM dd', '2021 4 30'))
display(ee.Date.parse('YYYY-MM-dd', '2021-4-30'))
display(ee.Date.parse('YYYY/MM/dd', '2021/4/30'))
display(ee.Date.parse('MM/dd/YY', '4/30/21'))
display(ee.Date.parse('MMM. dd, YYYY', 'Apr. 30, 2021'))
display(ee.Date.parse('YYYY-MM-dd HH:mm:ss', '2021-4-30 00:00:00'))
```

Was this helpful?
