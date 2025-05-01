 
#  ee.DateRange.contains 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-daterange-contains#examples)


Returns true if the given Date or DateRange is within this DateRange. 
Usage| Returns  
---|---  
`DateRange.contains(other)`| Boolean  
Argument| Type| Details  
---|---|---  
this: `dateRange`| DateRange|   
`other`| Object|   
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-daterange-contains#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-daterange-contains#colab-python-sample) More
```
// A series of ee.DateRange objects.
vardateRange1=ee.DateRange('2017-06-24','2017-07-24');
vardateRange2=ee.DateRange('2017-06-30','2017-07-10');
vardateRange3=ee.DateRange('2010-06-24','2020-07-24');
// Determine if an ee.DateRange is contained within another.
print('Does dateRange1 contain dateRange2?',dateRange1.contains(dateRange2));
print('Does dateRange1 contain dateRange3?',dateRange1.contains(dateRange3));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# A series of ee.DateRange objects.
date_range_1 = ee.DateRange('2017-06-24', '2017-07-24')
date_range_2 = ee.DateRange('2017-06-30', '2017-07-10')
date_range_3 = ee.DateRange('2010-06-24', '2020-07-24')
# Determine if an ee.DateRange is contained within another.
display(
  'Does date_range_1 contain date_range_2?',
  date_range_1.contains(date_range_2)
)
display(
  'Does date_range_1 contain date_range_3?',
  date_range_1.contains(date_range_3)
)
```

