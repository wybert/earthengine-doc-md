 
#  ee.DateRange.start 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-daterange-start#examples)


Returns the (inclusive) start of this DateRange. 
Usage| Returns  
---|---  
`DateRange.start()`| Date  
Argument| Type| Details  
---|---|---  
this: `dateRange`| DateRange|   
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-daterange-start#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-daterange-start#colab-python-sample) More
```
// An ee.DateRange.
vardateRange=ee.DateRange('2017-06-24','2017-07-24');
// Return the start of the ee.DateRange as an ee.Date.
print('The start of this ee.DateRange is',dateRange.start());
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# An ee.DateRange.
date_range = ee.DateRange('2017-06-24', '2017-07-24')
# Return the start of the ee.DateRange as an ee.Date.
display('The start of this ee.DateRange is', date_range.start())
```

