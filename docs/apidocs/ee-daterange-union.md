 
#  ee.DateRange.union
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-daterange-union#examples)


Returns a DateRange that contains all points in the union of this DateRange and another. 
Usage| Returns  
---|---  
`DateRange.union(other)`| DateRange  
Argument| Type| Details  
---|---|---  
this: `dateRange`| DateRange|   
`other`| DateRange|   
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-daterange-union#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-daterange-union#colab-python-sample) More
```
// A series of ee.DateRange objects.
vardateRange1=ee.DateRange('2017-06-24','2017-07-24');
vardateRange2=ee.DateRange('2017-06-30','2018-07-10');
vardateRange3=ee.DateRange('1970-06-24','1971-07-24');
// Determine the union of ee.DateRange objects.
print('Union of dateRange1 and dateRange2, which overlap',
dateRange1.union(dateRange2));
print('Union of dateRange1 and dateRange3, which do not overlap',
dateRange1.union(dateRange3));
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
date_range_2 = ee.DateRange('2017-06-30', '2018-07-10')
date_range_3 = ee.DateRange('1970-06-24', '1971-07-24')
# Determine the union of ee.DateRange objects.
display(
  'Union of date_range_1 and date_range_2, which overlap:',
  date_range_1.union(date_range_2)
)
display(
  'Union of date_range_1 and date_range_3, which do not overlap:',
  date_range_1.union(date_range_3)
)
```

Was this helpful?
