 
#  ee.FeatureCollection.aside
Stay organized with collections  Save and categorize content based on your preferences. 
var c = ee.ImageCollection('foo').aside(print)
.filterDate('2001-01-01', '2002-01-01').aside(print, 'In 2001')
.filterBounds(geom).aside(print, 'In region')
.aside(Map.addLayer, {min: 0, max: 142}, 'Filtered')
.select('a', 'b');
Returns the same object, for chaining.
Usage | Returns  
---|---  
`FeatureCollection.aside(func, var_args)` | ComputedObject  
Argument | Type | Details  
---|---|---  
this: `computedobject` | ComputedObject | The ComputedObject instance.  
`func` | Function | The function to call.  
`var_args` | VarArgs<Object> | Any extra arguments to pass to the function.  
## Examples
### Code Editor (JavaScript)
```
// Get a FeatureCollection of power plants in Belgium. Use "aside" to print the
// collection and display it on the Map.
varfc=ee.FeatureCollection('WRI/GPPD/power_plants')
.filter('country_lg == "Belgium"')
.aside(print,'Power plants in Belgium')
.aside(Map.centerObject,7)
.aside(Map.addLayer,{color:'blue'},'Power plants');
```

