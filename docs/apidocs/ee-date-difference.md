 
#  ee.Date.difference
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-date-difference#examples)


Returns the difference between two Dates in the specified units; the result is floating-point and based on the average length of the unit. 
Usage| Returns  
---|---  
`Date.difference(start, unit)`| Float  
Argument| Type| Details  
---|---|---  
this: `date`| Date|   
`start`| Date|   
`unit`| String| One of 'year', 'month', 'week', 'day', 'hour', 'minute', or 'second'.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-date-difference#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-date-difference#colab-python-sample) More
```
// Demonstrates the ee.Date.difference method.
varDATE_1=ee.Date('2020-01-01');
varDATE_2=ee.Date('2020-01-15');
vardiff_1=DATE_2.difference(DATE_1,'days');
vardiff_2=DATE_1.difference(DATE_2,'weeks');
print('The difference between ',
DATE_2,
' relative to ',
DATE_1,
' is ',
diff_1,
' days.');
print('The difference between ',
DATE_1,
' relative to ',
DATE_2,
' is ',
diff_2,
' weeks.');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
DATE_1 = ee.Date('2020-01-01')
DATE_2 = ee.Date('2020-01-15')
# Format the dates as strings.
t1 = DATE_1.format('YYYY-MM-DD').getInfo()
t2 = DATE_2.format('YYYY-MM-DD').getInfo()
# Calculate the differences between dates.
diff_1 = DATE_2.difference(DATE_1, 'days').getInfo()
diff_2 = DATE_1.difference(DATE_2, 'weeks').getInfo()
print(f'The difference between {t2} relative to {t1} is {diff_1} days.')
print(f'The difference between {t1} relative to {t2} is {diff_2} weeks.')
```

Was this helpful?
