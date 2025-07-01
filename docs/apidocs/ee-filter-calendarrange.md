 
#  ee.Filter.calendarRange
Stay organized with collections  Save and categorize content based on your preferences. 
Returns a filter that passes if the object's timestamp falls within the given range of a calendar field. The `month`, `day_of_year`, `day_of_month`, and `day_of_week` are 1-based. Times are assumed to be in UTC. Weeks are assumed to begin on Monday as day 1. If `end` < `start` then this tests for `value` >= `start` OR `value` <= `end`, to allow for wrapping. Usage| Returns  
---|---  
`ee.Filter.calendarRange(start,  _end_, _field_)`| Filter  
Argument| Type| Details  
---|---|---  
`start`| Integer| The start of the desired calendar field, inclusive.  
`end`| Integer, default: null| The end of the desired calendar field, inclusive. Defaults to the same value as start.  
`field`| String, default: "day_of_year"| The calendar field to filter over. Options are: `year`, `month`, `hour`, `minute`, `day_of_year`, `day_of_month`, and `day_of_week`.  
## Examples
### Code Editor (JavaScript)
```
// A Sentinel-2 surface reflectance image collection intersecting the peak of
// Mount Shasta, California, USA.
varic=ee.ImageCollection('COPERNICUS/S2_SR')
.filterBounds(ee.Geometry.Point(-122.196,41.411));
print('Images for a month range (June-August)',
ic.filter(ee.Filter.calendarRange(6,8,'month')));
print('A start value greater than end value is valid (Dec-Feb)',
ic.filter(ee.Filter.calendarRange(12,2,'month')));
// This example uses the 'year' field value. Note that ee.Filter.date is the
// preferred method when filtering by whole years, as it is much faster.
print('Images for a year range (2020-2021)',
ic.filter(ee.Filter.calendarRange(2020,2021,'year')));
// This example uses the 'day_of_year' field value. Note that
// ee.Filter.dayOfYear is the preferred method for filtering by DOY.
// The ee.Date.getRelative function is used to identify DOY from an ee.Date
// object for a representative year. Be mindful of leap years when filtering
// by DOY.
varstartDoy=ee.Date('2000-06-01').getRelative('day','year');
varendDoy=ee.Date('2000-06-15').getRelative('day','year');
print('start DOY =',startDoy,
'end DOY =',endDoy,
'Images for a day-of-year range',
ic.filter(ee.Filter.calendarRange(startDoy,endDoy,'day_of_year')));
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# A Sentinel-2 surface reflectance image collection intersecting the peak of
# Mount Shasta, California, USA.
ic = ee.ImageCollection('COPERNICUS/S2_SR').filterBounds(
  ee.Geometry.Point(-122.196, 41.411))
print('Images for a month range (June-August):',
   ic.filter(ee.Filter.calendarRange(6, 8, 'month')).getInfo())
print('A start value greater than end value is valid (Dec-Feb):',
   ic.filter(ee.Filter.calendarRange(12, 2, 'month')).size().getInfo())
# This example uses the 'year' field value. Note that ee.Filter.date is the
# preferred method when filtering by whole years, as it is much faster.
print('Images for a year range (2020-2021):',
   ic.filter(ee.Filter.calendarRange(2020, 2021, 'year')).size().getInfo())
# This example uses the 'day_of_year' field value. Note that
# ee.Filter.dayOfYear is the preferred method for filtering by DOY.
# The ee.Date.getRelative function is used to identify DOY from an ee.Date
# object for a representative year. Be mindful of leap years when filtering
# by DOY.
start_doy = ee.Date('2000-06-01').getRelative('day', 'year')
end_doy = ee.Date('2000-06-15').getRelative('day', 'year')
print('start DOY =', start_doy.getInfo(), 'end DOY =', end_doy.getInfo())
print(
  'Images for a day-of-year range:',
  ic.filter(ee.Filter.calendarRange(start_doy, end_doy, 'day_of_year'))
  .getInfo()
)
```

