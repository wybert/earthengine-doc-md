 
#  ee.FeatureCollection.sort 
Stay organized with collections  Save and categorize content based on your preferences. 
Sort a collection by the specified property. 
Returns the sorted collection.
Usage| Returns  
---|---  
`FeatureCollection.sort(property,  _ascending_)`| Collection  
Argument| Type| Details  
---|---|---  
this: `collection`| Collection| The Collection instance.  
`property`| String| The property to sort by.  
`ascending`| Boolean, optional| Whether to sort in ascending or descending order. The default is true (ascending).  
## Examples
### Code Editor (JavaScript)
```
// FeatureCollection of power plants in Belgium.
varfc=ee.FeatureCollection('WRI/GPPD/power_plants')
.filter('country_lg == "Belgium"');
print('Belgium power plants in ascending order by capacity',
fc.sort('capacitymw'));
print('Belgium power plants in descending order by capacity',
fc.sort('capacitymw',false));
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# FeatureCollection of power plants in Belgium.
fc = ee.FeatureCollection('WRI/GPPD/power_plants').filter(
  'country_lg == "Belgium"')
print('Belgium power plants in ascending order by capacity:',
   fc.sort('capacitymw').getInfo())
print('Belgium power plants in descending order by capacity:',
   fc.sort('capacitymw', False).getInfo())
```

