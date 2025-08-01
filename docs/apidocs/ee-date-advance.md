 
#  ee.Date.advance
Stay organized with collections  Save and categorize content based on your preferences. 
Create a new Date by adding the specified units to the given Date. Usage | Returns  
---|---  
`Date.advance(delta, unit, _timeZone_)`|  Date  
Argument | Type | Details  
---|---|---  
this: `date` | Date |   
`delta` | Float |   
`unit` | String | One of 'year', 'month', 'week', 'day', 'hour', 'minute', or 'second'.  
`timeZone` | String, default: null | The time zone (e.g., 'America/Los_Angeles'); defaults to UTC.  
## Examples
### Code Editor (JavaScript)
```
// Defines a base date/time for the following examples.
varBASE_DATE=ee.Date('2020-7-1T13:00','UTC');
print(BASE_DATE,'The base date/time');

// Demonstrates basic usage.
print(BASE_DATE.advance(1,'week'),'+1 week');
print(BASE_DATE.advance(2,'years'),'+2 years');

// Demonstrates that negative delta moves back in time.
print(BASE_DATE.advance(-1,'second'),'-1 second');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Defines a base date/time for the following examples.
BASE_DATE = ee.Date('2020-01-01T00:00', 'UTC')
display('The base date/time', BASE_DATE)

# Demonstrates basic usage.
display('+1 week', BASE_DATE.advance(1, 'week'))
display('+2 years', BASE_DATE.advance(2, 'years'))

# Demonstrates that negative delta moves back in time.
display('-1 second', BASE_DATE.advance(-1, 'second'))
```

