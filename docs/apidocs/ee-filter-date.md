 
#  ee.Filter.date
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-filter-date#examples)


(interpreted as milliseconds since 1970-01-01T00:00:00Z), or strings (such as '1996-01-01T08:00'). Based on 'system:time_start' property.
Returns the constructed filter.
Usage | Returns  
---|---  
`ee.Filter.date(start, _end_)`|  Filter  
Argument | Type | Details  
---|---|---  
`start` | Date|Number|String | The start date (inclusive).  
`end` | Date|Number|String, optional | The end date (exclusive). Optional. If not specified, a 1-millisecond range starting at 'start' is created.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-filter-date#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-filter-date#colab-python-sample) More
```
// collection.filterDate is preferred.
// Constructed FeatureCollection representing a field site sampled at
// four different dates.
vargeom=ee.Geometry.Point([-119.56,37.67]);
varfc=ee.FeatureCollection([
ee.Feature(geom,{'prop':10,'system:time_start':ee.Date('2021-06-10')}),
ee.Feature(geom,{'prop':11,'system:time_start':ee.Date('2021-06-20')}),
ee.Feature(geom,{'prop':19,'system:time_start':ee.Date('2021-07-10')}),
ee.Feature(geom,{'prop':10,'system:time_start':ee.Date('2021-07-20')})
]);

// Filter the observations in July 2021.
print('Field site observations collection in July 2021',
fc.filter(ee.Filter.date('2021-07-01','2021-08-01')));

// Alternative input formats.
vardateRange=ee.DateRange('2021-07-01','2021-08-01');
print('ee.DateRange as an input',
fc.filter(ee.Filter.date(dateRange)));

print('Numbers (milliseconds since Unix epoch) as an input',
fc.filter(ee.Filter.date(1625875200000,1626739200001)));

print('ee.Date objects as an input',
fc.filter(ee.Filter.date(ee.Date('2021-07-01'),ee.Date('2021-08-01'))));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
frompprintimport pprint

# collection.filterDate is preferred.
# Constructed FeatureCollection representing a field site sampled at
# four different dates.
geom = ee.Geometry.Point([-119.56, 37.67])
fc = ee.FeatureCollection([
    ee.Feature(geom, {'prop': 10, 'system:time_start': ee.Date('2021-06-10')}),
    ee.Feature(geom, {'prop': 11, 'system:time_start': ee.Date('2021-06-20')}),
    ee.Feature(geom, {'prop': 19, 'system:time_start': ee.Date('2021-07-10')}),
    ee.Feature(geom, {'prop': 10, 'system:time_start': ee.Date('2021-07-20')})
])

# Filter the observations in July 2021.
print('Field site observations collection in July 2021:')
pprint(fc.filter(ee.Filter.date('2021-07-01', '2021-08-01')).getInfo())

# Alternative input formats.
date_range = ee.DateRange('2021-07-01', '2021-08-01')
pprint(fc.filter(ee.Filter.date(date_range)).getInfo())

print('Numbers (milliseconds since Unix epoch) as an input:')
pprint(fc.filter(ee.Filter.date(1625875200000, 1626739200001)).getInfo())

print('ee.Date objects as an input:')
pprint(
    fc.filter(
        ee.Filter.date(ee.Date('2021-07-01'), ee.Date('2021-08-01'))
    ).getInfo()
)
```

