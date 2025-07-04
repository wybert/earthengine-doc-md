 
#  ee.ImageCollection.set
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-set#examples)


Overrides one or more metadata properties of an Element. 
Returns the element with the specified properties overridden.
Usage| Returns  
---|---  
`ImageCollection.set(var_args)`| Element  
Argument| Type| Details  
---|---|---  
this: `element`| Element| The Element instance.  
`var_args`| VarArgs| Either a dictionary of properties, or a vararg sequence of properties, e.g. key1, value1, key2, value2, ...  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-set#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-set#colab-python-sample) More
```
// A contrived, empty image collection for simple demonstration.
varcol=ee.ImageCollection([]);
print('Collection without properties',col);
// Set collection properties using a dictionary.
col=col.set({
project_name:'biomass_tracking',
project_id:3,
plot_ids:ee.Array([7,11,20])
});
// Set collection properties using a series of key-value pairs.
col=col.set('project_year',2018,
'rgb_vis','false_color');
print('Collection with properties',col);
// Get a dictionary of collection property keys and values.
print('Property keys and values (ee.Dictionary)',col.toDictionary());
// Get the value of a collection property. To use the result of
// ee.ImageCollection.get in further computation, you need to cast it to the
// appropriate class, for example, ee.Number(result) or ee.String(result).
print('Project ID (ambiguous object)',col.get('project_id'));
// Get the value of a string collection property as an ee.String object.
print('Project name (ee.String)',col.getString('project_name'));
// Get the value of a numeric collection property as an ee.Number object.
print('Project year (ee.Number)',col.getNumber('project_year'));
// Get the value of an ee.Array collection property as an ee.Array object.
print('Plot IDs (ee.Array)',col.getArray('plot_ids'));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# A contrived, empty image collection for simple demonstration.
col = ee.ImageCollection([])
print('Collection without properties:', col.getInfo())
# Set collection properties using a dictionary.
col = col.set({
  'project_name': 'biomass_tracking',
  'project_id': 3,
  'plot_ids': ee.Array([7, 11, 20])
})
# Set collection properties using a series of key-value pairs.
col = col.set('project_year', 2018,
       'rgb_vis', 'false_color')
print('Collection with properties:', col.getInfo())
# Get a dictionary of collection property keys and values.
print('Property keys and values (ee.Dictionary):', col.toDictionary().getInfo())
# Get the value of a collection property. To use the result of
# ee.ImageCollection.get in further computation, you need to cast it to the
# appropriate class, for example, ee.Number(result) or ee.String(result).
print('Project ID (ambiguous object):', col.get('project_id').getInfo())
# Get the value of a string collection property as an ee.String object.
print('Project name (ee.String):', col.getString('project_name').getInfo())
# Get the value of a numeric collection property as an ee.Number object.
print('Project year (ee.Number):', col.getNumber('project_year').getInfo())
# Get the value of an ee.Array collection property as an ee.Array object.
print('Plot IDs (ee.Array):', col.getArray('plot_ids').getInfo())
```

Was this helpful?
