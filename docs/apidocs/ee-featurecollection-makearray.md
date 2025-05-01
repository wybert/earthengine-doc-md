 
#  ee.FeatureCollection.makeArray 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-makearray#examples)


Add a 1-D Array to each feature in a collection by combining a list of properties for each feature into a 1-D Array. All of the properties must be numeric values. If a feature doesn't contain all of the named properties, or any of them aren't numeric, the feature will be dropped from the resulting collection. 
Usage| Returns  
---|---  
`FeatureCollection.makeArray(properties,  _name_)`| FeatureCollection  
Argument| Type| Details  
---|---|---  
this: `collection`| FeatureCollection| The input collection from which properties will be selected.  
`properties`| List| The properties to select.  
`name`| String, default: "array"| The name of the new array property.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-makearray#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-makearray#colab-python-sample) More
```
// FeatureCollection of power plants in Belgium.
varfc=ee.FeatureCollection('WRI/GPPD/power_plants')
.filter('country_lg == "Belgium"');
// A list of feature properties to combine into an array
// (power generation by year).
varproperties=['gwh_2013','gwh_2014','gwh_2015','gwh_2016'];
// Add array of power-generation-by-year property to features.
fc=fc.makeArray(properties,'gwh_by_year');
print('FeatureCollection with array of selected properties added',fc);
print('See example of new "gwh_by_year" property',fc.first().toDictionary());
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
frompprintimport pprint
# FeatureCollection of power plants in Belgium.
fc = ee.FeatureCollection('WRI/GPPD/power_plants').filter(
  'country_lg == "Belgium"')
# A list of feature properties to combine into an array
# (power generation by year).
properties = ['gwh_2013', 'gwh_2014', 'gwh_2015', 'gwh_2016']
# Add array of power-generation-by-year property to features.
fc = fc.makeArray(properties, 'gwh_by_year')
print('FeatureCollection with array of selected properties added:',
   fc.getInfo())
print('See example of new "gwh_by_year" property:')
pprint(fc.first().toDictionary().getInfo())
```

