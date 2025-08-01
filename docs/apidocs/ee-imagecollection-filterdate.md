 
#  ee.ImageCollection.filterDate
Stay organized with collections  Save and categorize content based on your preferences. 
This is equivalent to this.filter(ee.Filter.date(...)); see the ee.Filter type for other date filtering options.
Returns the filtered collection.
Usage | Returns  
---|---  
`ImageCollection.filterDate(start, _end_)`|  Collection  
Argument | Type | Details  
---|---|---  
this: `collection` | Collection | The Collection instance.  
`start` | Date|Number|String | The start date (inclusive).  
`end` | Date|Number|String, optional | The end date (exclusive). Optional. If not specified, a 1-millisecond range starting at 'start' is created.  
## Examples
### Code Editor (JavaScript)
```
// A Landsat 8 TOA image collection intersecting a specific point.
varcol=ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA')
.filterBounds(ee.Geometry.Point(-90.70,34.71));

// Filter the collection by date using date strings.
print('2020 images',col.filterDate('2020','2021'));
print('July images, 2020',col.filterDate('2020-07','2020-08'));
print('Early July images, 2020',col.filterDate('2020-07-01','2020-07-10'));
print('Include time (13 hours, July 7, 2020)',
col.filterDate('2020-07-05T06:34:46','2020-07-05T19:34:46'));

// Use milliseconds since Unix epoch.
print('Milliseconds inputs',col.filterDate(1593967014062,1595349419611));

// Use ee.Date objects.
print('ee.Date inputs',col.filterDate(ee.Date('2020'),ee.Date('2021')));

// Use an ee.DateRange object.
vardateRange=ee.DateRange('2020-07-01','2020-07-10');
print('ee.DateRange input',col.filterDate(dateRange));
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# A Landsat 8 TOA image collection intersecting a specific point.
col = ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA').filterBounds(
    ee.Geometry.Point(-90.70, 34.71))

# Filter the collection by date using date strings.
print('2020 images:', col.filterDate('2020', '2021').getInfo())
print('July images, 2020:', col.filterDate('2020-07', '2020-08').getInfo())
print('Early July images, 2020:',
      col.filterDate('2020-07-01', '2020-07-10').getInfo())
print('Include time (13 hours, July 7, 2020):',
      col.filterDate('2020-07-05T06:34:46', '2020-07-05T19:34:46').getInfo())

# Use milliseconds since Unix epoch.
print('Milliseconds inputs:',
      col.filterDate(1593967014062, 1595349419611).getInfo())

# Use ee.Date objects.
print('ee.Date inputs',
      col.filterDate(ee.Date('2020'), ee.Date('2021')).getInfo())

# Use an ee.DateRange object.
date_range = ee.DateRange('2020-07-01', '2020-07-10')
print('ee.DateRange input', col.filterDate(date_range).getInfo())
```

