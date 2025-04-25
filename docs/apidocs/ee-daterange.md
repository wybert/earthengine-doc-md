 
#  ee.DateRange 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-daterange#examples)


Creates a DateRange with the given start (inclusive) and end (exclusive), which may be Dates, numbers (interpreted as milliseconds since 1970-01-01T00:00:00Z), or strings (such as '1996-01-01T08:00'). If 'end' is not specified, a 1-millisecond range starting at 'start' is created. 
Usage| Returns  
---|---  
`ee.DateRange(start,  _end_, _timeZone_)`| DateRange  
Argument| Type| Details  
---|---|---  
`start`| Object  
`end`| Object, default: null  
`timeZone`| String, default: null| If start and/or end are provided as strings, the time zone in which to interpret them; defaults to UTC.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-daterange#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-daterange#colab-python-sample) More
```
print('String date inputs (interpreted as UTC by default)',
ee.DateRange('2017-06-24','2017-07-24'));
print('String date inputs with timeZone argument',
ee.DateRange('2017-06-24','2017-07-24','America/Los_Angeles'));
print('String date-time inputs with timeZone argument',
ee.DateRange('2017-06-24T07:00:00','2017-07-24T07:00:00',
'America/Los_Angeles'));
print('A single date input results in a 1-millisecond range',
ee.DateRange('2017-06-24'));
print('ee.Date inputs',
ee.DateRange(ee.Date('2017-06-24'),ee.Date('2017-07-24')));
print('ee.Date date-time inputs (UTC by default)',
ee.DateRange(ee.Date('2017-06-24T07:00:00'),
ee.Date('2017-07-24T07:00:00')));
print('ee.Date date-time inputs with timeZone arguments',
ee.DateRange(ee.Date('2017-06-24T07:00:00','UTC'),
ee.Date('2017-07-24T07:00:00','America/Los_Angeles')));
print('Number inputs as milliseconds from Unix epoch (2017-06-24, 2017-07-24)',
ee.DateRange(1498262400000,1500854400000));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print('String date inputs (interpreted as UTC by default):',
   ee.DateRange('2017-06-24', '2017-07-24').getInfo())
print('String date inputs with timeZone argument:',
   ee.DateRange('2017-06-24', '2017-07-24', 'America/Los_Angeles').getInfo())
print('String date-time inputs with timeZone argument:',
   ee.DateRange('2017-06-24T07:00:00', '2017-07-24T07:00:00',
          'America/Los_Angeles').getInfo())
print('A single date input results in a 1-millisecond range:',
   ee.DateRange('2017-06-24').getInfo())
print('ee.Date inputs',
   ee.DateRange(ee.Date('2017-06-24'), ee.Date('2017-07-24')).getInfo())
print('ee.Date date-time inputs (UTC by default):',
   ee.DateRange(ee.Date('2017-06-24T07:00:00'),
          ee.Date('2017-07-24T07:00:00')).getInfo())
print('ee.Date date-time inputs with timeZone arguments:',
   ee.DateRange(ee.Date('2017-06-24T07:00:00', 'UTC'),
          ee.Date('2017-07-24T07:00:00',
              'America/Los_Angeles')).getInfo())
print('Number inputs as milliseconds from Unix epoch (2017-06-24, 2017-07-24):',
   ee.DateRange(1498262400000, 1500854400000).getInfo())
```

Was this helpful?
