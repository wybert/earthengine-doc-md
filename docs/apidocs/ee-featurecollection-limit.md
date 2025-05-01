 
#  ee.FeatureCollection.limit 
Stay organized with collections  Save and categorize content based on your preferences. 
Limit a collection to the specified number of elements, optionally sorting them by a specified property first. 
Returns the limited collection.
Usage| Returns  
---|---  
`FeatureCollection.limit(max,  _property_, _ascending_)`| Collection  
Argument| Type| Details  
---|---|---  
this: `collection`| Collection| The Collection instance.  
`max`| Number| The number to limit the collection to.  
`property`| String, optional| The property to sort by, if sorting.  
`ascending`| Boolean, optional| Whether to sort in ascending or descending order. The default is true (ascending).  
## Examples
### Code Editor (JavaScript)
```
// FeatureCollection of global power plants.
varfc=ee.FeatureCollection('WRI/GPPD/power_plants');
print('First 5 features (power plants)',fc.limit(5));
print('Smallest 5 power plants by capacity in ascending order',
fc.limit({max:5,property:'capacitymw'}));
print('Largest 5 power plants by capacity in descending order',
fc.limit({max:5,property:'capacitymw',ascending:false}));
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# FeatureCollection of global power plants.
fc = ee.FeatureCollection('WRI/GPPD/power_plants')
print('First 5 features (power plants):', fc.limit(5).getInfo())
print('Smallest 5 power plants by capacity in ascending order:',
   fc.limit(**{'maximum': 5, 'opt_property': 'capacitymw'}).getInfo())
print('Largest 5 power plants by capacity in descending order:',
   fc.limit(**{'maximum': 5, 'opt_property': 'capacitymw',
         'opt_ascending': False}).getInfo())
```

