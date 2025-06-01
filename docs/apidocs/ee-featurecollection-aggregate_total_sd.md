 
#  ee.FeatureCollection.aggregate_total_sd 
Stay organized with collections  Save and categorize content based on your preferences. 
Aggregates over a given property of the objects in a collection, calculating the total std. deviation of the values of the selected property. Usage| Returns  
---|---  
`FeatureCollection.aggregate_total_sd(property)`| Number  
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
print('Total std. deviation of power plant capacities (MW)',
fc.aggregate_total_sd('capacitymw'));// 462.9334545609107
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
print('Total std. deviation of power plant capacities (MW):',
   fc.aggregate_total_sd('capacitymw').getInfo()) # 462.9334545609107
```

