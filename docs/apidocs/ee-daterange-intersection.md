 
#  ee.DateRange.intersection
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Returns a DateRange that contains all points in the intersection of this DateRange and another.
Usage | Returns  
---|---  
`DateRange.intersection(other)` | DateRange  
Argument | Type | Details  
---|---|---  
this: `dateRange` | DateRange |   
`other` | DateRange |   
## Examples
### Code Editor (JavaScript)
```
// A series of ee.DateRange objects.
vardateRange1=ee.DateRange('2017-06-24','2017-07-24');
vardateRange2=ee.DateRange('2017-07-01','2018-08-24');

// Determine the intersection of two ee.DateRange objects.
print('Intersection of dateRange1 and dateRange2',
dateRange1.intersection(dateRange2));
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# A series of ee.DateRange objects.
date_range_1 = ee.DateRange('2017-06-24', '2017-07-24')
date_range_2 = ee.DateRange('2017-07-01', '2018-08-24')

# Determine the intersection of two ee.DateRange objects.
display(
    'Intersection of date_range_1 and date_range_2:',
    date_range_1.intersection(date_range_2)
)
```

