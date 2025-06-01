 
#  ee.DateRange.intersects 
Stay organized with collections  Save and categorize content based on your preferences. 
Returns true if the given DateRange has at least one point in common with this DateRange. Usage| Returns  
---|---  
`DateRange.intersects(other)`| Boolean  
Argument| Type| Details  
---|---|---  
this: `dateRange`| DateRange|   
`other`| DateRange|   
## Examples
### Code Editor (JavaScript)
```
// A series of ee.DateRange objects.
vardateRange1=ee.DateRange('2017-06-24','2017-07-24');
vardateRange2=ee.DateRange('2017-06-30','2018-07-10');
vardateRange3=ee.DateRange('1970-06-24','1971-07-24');
vardateRange4=ee.DateRange('2017-06-25','2017-07-25');
// Determine if an ee.DateRange intersects another.
print('Does dateRange1 contain dateRange2?',dateRange1.intersects(dateRange2));
print('Does dateRange1 contain dateRange3?',dateRange1.intersects(dateRange3));
print('Does dateRange1 contain dateRange4?',dateRange1.intersects(dateRange4));
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
date_range_2 = ee.DateRange('2017-06-30', '2018-07-10')
date_range_3 = ee.DateRange('1970-06-24', '1971-07-24')
date_range_4 = ee.DateRange('2017-06-25', '2017-07-25')
# Determine if an ee.DateRange intersects another.
display(
  'Does date_range_1 contain date_range_2?',
  date_range_1.intersects(date_range_2)
)
display(
  'Does date_range_1 contain date_range_3?',
  date_range_1.intersects(date_range_3)
)
display(
  'Does date_range_1 contain date_range_4?',
  date_range_1.intersects(date_range_4)
)
```

