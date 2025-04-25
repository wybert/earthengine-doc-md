 
#  ee.FeatureCollection.distinct 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-distinct#examples)


Removes duplicates from a collection. Note that duplicates are determined using a strong hash over the serialized form of the selected properties. 
Usage| Returns  
---|---  
`FeatureCollection.distinct(properties)`| FeatureCollection  
Argument| Type| Details  
---|---|---  
this: `collection`| FeatureCollection| The input collection from which objects will be selected.  
`properties`| Object| A property name or a list of property names to use for comparison. The '.geo' property can be included to compare object geometries.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-distinct#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-distinct#colab-python-sample) More
```
// FeatureCollection of power plants in Belgium.
varfc=ee.FeatureCollection('WRI/GPPD/power_plants')
.filter('country_lg == "Belgium"');
print('FeatureCollection of power plants in Belgium',fc);
// Remove duplicate features according to property values.
print('Distinct based on a single property',fc.distinct('fuel1'));
print('Distinct based on two properties',fc.distinct(['fuel1','source']));
print('Distinct based on geometry',fc.distinct('.geo'));
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
print('FeatureCollection of power plants in Belgium:', fc.getInfo())
# Remove duplicate features according to property values.
print('Distinct based on a single property:', fc.distinct('fuel1').getInfo())
print('Distinct based on two properties:',
   fc.distinct(['fuel1', 'source']).getInfo())
print('Distinct based on geometry', fc.distinct('.geo').getInfo())
```

Was this helpful?
