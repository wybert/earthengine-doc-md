 
#  ee.FeatureCollection.getNumber 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-getnumber#examples)


Extract a property from a feature. 
Usage| Returns  
---|---  
`FeatureCollection.getNumber(property)`| Number  
Argument| Type| Details  
---|---|---  
this: `object`| Element| The feature to extract the property from.  
`property`| String| The property to extract.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-getnumber#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-getnumber#colab-python-sample) More
```
// A FeatureCollection with a number property value.
varfc=ee.FeatureCollection([]).set('number_property',1.5);
// Fetch the number property value as an ee.Number object.
print('Number property value as ee.Number',fc.getNumber('number_property'));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# A FeatureCollection with a number property value.
fc = ee.FeatureCollection([]).set('number_property', 1.5)
# Fetch the number property value as an ee.Number object.
print('Number property value as ee.Number:',
   fc.getNumber('number_property').getInfo())
```

Was this helpful?
