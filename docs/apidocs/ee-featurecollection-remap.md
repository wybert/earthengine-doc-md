 
#  ee.FeatureCollection.remap
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-remap#examples)


Remaps the value of a specific property in a collection. Takes two parallel lists and maps values found in one to values in the other. Any element with a value that is not specified in the first list is dropped from the output collection.
Usage | Returns  
---|---  
`FeatureCollection.remap(lookupIn, lookupOut, columnName)` | FeatureCollection  
Argument | Type | Details  
---|---|---  
this: `collection` | FeatureCollection | The collection to be modified.  
`lookupIn` | List | The input mapping values. Restricted to strings and integers.  
`lookupOut` | List | The output mapping values. Must be the same size as lookupIn.  
`columnName` | String | The name of the property to remap.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-remap#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-remap#colab-python-sample) More
```
// Classify features based on a string property.
// The 'nonsense' category gets dropped.
varfc=ee.FeatureCollection([
ee.Feature(ee.Geometry.Point([1,2]),{isTree:'Tree'}),
ee.Feature(ee.Geometry.Point([3,4]),{isTree:'NotTree'}),
ee.Feature(ee.Geometry.Point([5,6]),{isTree:'nonsense'}),
]);

vartrees=fc.remap(['NotTree','Tree'],[0,1],'isTree');
print('remapped trees',trees);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Classify features based on a string property.
# The 'nonsense' category gets dropped.
fc = ee.FeatureCollection([
    ee.Feature(ee.Geometry.Point([1, 2]), {'isTree': 'Tree'}),
    ee.Feature(ee.Geometry.Point([3, 4]), {'isTree': 'NotTree'}),
    ee.Feature(ee.Geometry.Point([5, 6]), {'isTree': 'nonsense'}),
    ])

trees = fc.remap(['NotTree', 'Tree'], [0, 1], 'isTree')
print('Remapped trees:', trees.getInfo())
```

