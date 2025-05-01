 
#  ee.DateRange.isUnbounded 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-daterange-isunbounded#examples)


Returns true if this DateRange contains all dates. 
Usage| Returns  
---|---  
`DateRange.isUnbounded()`| Boolean  
Argument| Type| Details  
---|---|---  
this: `dateRange`| DateRange|   
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-daterange-isunbounded#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-daterange-isunbounded#colab-python-sample) More
```
// A series of ee.DateRange objects.
vardateRangeBounded=ee.DateRange('2017-06-24','2017-07-24');
vardateRangeUnbounded=ee.DateRange.unbounded();
// Determine if an ee.DateRange object is unbounded.
print('Is dateRangeBounded unbounded?',dateRangeBounded.isUnbounded());
print('Is dateRangeUnbounded unbounded?',dateRangeUnbounded.isUnbounded());
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# A series of ee.DateRange objects.
date_range_bounded = ee.DateRange('2017-06-24', '2017-07-24')
date_range_unbounded = ee.DateRange.unbounded()
# Determine if an ee.DateRange object is unbounded.
display('Is date_range_bounded unbounded?', date_range_bounded.isUnbounded())
display(
  'Is date_range_unbounded unbounded?', date_range_unbounded.isUnbounded()
)
```

Was this helpful?
