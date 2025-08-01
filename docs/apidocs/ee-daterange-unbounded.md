 
#  ee.DateRange.unbounded
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-daterange-unbounded#examples)


Returns a DateRange that includes all possible dates.
Usage | Returns  
---|---  
`ee.DateRange.unbounded()` | DateRange  
**No arguments.**
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-daterange-unbounded#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-daterange-unbounded#colab-python-sample) More
```
vardateRangeUnbounded=ee.DateRange.unbounded();
print('An unbounded ee.DateRange object',dateRangeUnbounded);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
date_range_unbounded = ee.DateRange.unbounded()
display('An unbounded ee.DateRange object:', date_range_unbounded)
```

Was this helpful?
