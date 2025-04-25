 
#  ee.FeatureCollection.aggregate_total_var 
Stay organized with collections  Save and categorize content based on your preferences. 
Aggregates over a given property of the objects in a collection, calculating the total variance of the values of the selected property. Usage| Returns  
---|---  
`FeatureCollection.aggregate_total_var(property)`| Number  
Argument| Type| Details  
---|---|---  
this: `collection`| FeatureCollection| The collection to aggregate over.  
`property`| String| The property to use from each element of the collection.  
## Examples
### Code Editor (JavaScript)
```
// FeatureCollection of power plants in Belgium.
varfc=ee.FeatureCollection('WRI/GPPD/power_plants')
.filter('country_lg == "Belgium"');
print('Total variance of power plant capacities (MW)',
fc.aggregate_total_var('capacitymw'));// 214307.38335169878
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
print('Total variance of power plant capacities (MW):',
   fc.aggregate_total_var('capacitymw').getInfo()) # 214307.38335169878
```

