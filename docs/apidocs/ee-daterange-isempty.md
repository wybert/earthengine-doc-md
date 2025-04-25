 
#  ee.DateRange.isEmpty 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-daterange-isempty#examples)


Returns true if this DateRange contains no dates (i.e. start >= end). 
Usage| Returns  
---|---  
`DateRange.isEmpty()`| Boolean  
Argument| Type| Details  
---|---|---  
this: `dateRange`| DateRange  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-daterange-isempty#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-daterange-isempty#colab-python-sample) More
```
// A series of ee.DateRange objects.
vardateRange1=ee.DateRange('2017-06-24','2017-07-24');
vardateRange2=ee.DateRange('2017-07-24','2017-06-24');
vardateRange3=ee.DateRange('2017-07-24','2017-07-24');
// Determine if the ee.DateRange is empty.
print('Is dateRange1 empty?',dateRange1.isEmpty());
print('Is dateRange2 empty?',dateRange2.isEmpty());
print('Is dateRange3 empty?',dateRange3.isEmpty());
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
date_range_2 = ee.DateRange('2017-07-24', '2017-06-24')
date_range_3 = ee.DateRange('2017-07-24', '2017-07-24')
# Determine if the ee.DateRange is empty.
display('Is date_range_1 empty?', date_range_1.isEmpty())
display('Is date_range_2 empty?', date_range_2.isEmpty())
display('Is date_range_3 empty?', date_range_3.isEmpty())
```

