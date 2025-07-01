 
#  ee.FeatureCollection.select
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-select#examples)


Select properties from each Feature in a collection. It is also possible to call this function with only string arguments; they will be all be interpreted as propertySelectors (varargs). 
Returns the feature collection with selected properties.
Usage| Returns  
---|---  
`FeatureCollection.select(propertySelectors,  _newProperties_, _retainGeometry_)`| FeatureCollection  
Argument| Type| Details  
---|---|---  
this: `featurecollection`| FeatureCollection| The FeatureCollection instance.  
`propertySelectors`| List| A list of names or regexes specifying the attributes to select.  
`newProperties`| List, optional| A list of new names for the output properties. Must match the number of properties selected.  
`retainGeometry`| Boolean, optional| When false, the result will have a NULL geometry. Defaults to true.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-select#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-select#colab-python-sample) More
```
// FeatureCollection of power plants in Belgium.
varfc=ee.FeatureCollection('WRI/GPPD/power_plants')
.filter('country_lg == "Belgium"');
// Select a single property.
varsingleProp=fc.select('fuel1');
print('Single property selected',
singleProp.first());
// Select multiple properties.
varmultiProp=fc.select(['fuel1','capacitymw']);
print('Multiple properties selected',
multiProp.first());
// Select multiple properties and rename them.
varmultiPropRename=fc.select({
propertySelectors:['fuel1','capacitymw'],
newProperties:['Fuel_1','Capacity_MW']
});
print('Multiple properties selected, renamed',
multiPropRename.first());
// Select multiple properties, remove geometry.
varmultiPropNoGeom=fc.select({
propertySelectors:['fuel1','capacitymw'],
retainGeometry:false
});
print('Multiple properties selected, geometry removed',
multiPropNoGeom.first());
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# FeatureCollection of power plants in Belgium.
fc = ee.FeatureCollection('WRI/GPPD/power_plants').filter(
  'country_lg == "Belgium"')
# Select a single property.
single_prop = fc.select('fuel1')
print('Single property selected:', single_prop.first().getInfo())
# Select multiple properties.
multi_prop = fc.select(['fuel1', 'capacitymw'])
print('Multiple properties selected:', multi_prop.first().getInfo())
# Select multiple properties and rename them.
multi_prop_rename = fc.select(**{
  'propertySelectors': ['fuel1', 'capacitymw'],
  'newProperties': ['Fuel_1', 'Capacity_MW']
  })
print('Multiple properties selected, renamed:',
   multi_prop_rename.first().getInfo())
# Select multiple properties, remove geometry.
multi_prop_no_geom = fc.select(**{
  'propertySelectors': ['fuel1', 'capacitymw'],
  'retainGeometry': False
  })
print('Multiple properties selected, geometry removed:',
   multi_prop_no_geom.first().getInfo())
```

Was this helpful?
