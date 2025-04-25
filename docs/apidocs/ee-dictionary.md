 
#  ee.Dictionary 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-dictionary#examples)


Constructs a new Dictionary. 
Usage| Returns  
---|---  
`ee.Dictionary( _dict_)`| Dictionary  
Argument| Type| Details  
---|---|---  
`dict`| ComputedObject|Object, optional| An object to convert to a dictionary. This constructor accepts the following types: 1) Another dictionary. 2) A list of key/value pairs. 3) A null or no argument (producing an empty dictionary)  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-dictionary#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-dictionary#colab-python-sample) More
```
// A dictionary input (e.g. results of ee.Image.reduceRegion of an S2 image).
vardict={
B1:182,
B2:219,
B3:443
};
print('ee.Dictionary from dictionary input',ee.Dictionary(dict));
// A list of key/value pairs (from previous dictionary).
varlist=[
'B1',182,
'B2',219,
'B3',443
];
print('ee.Dictionary from list input',ee.Dictionary(list));
// To create an ee.Dictionary from two corresponding lists of keys and values,
// use the ee.Dictionary.fromLists constructor.
varkeys=['B1','B2','B3'];
varvalues=[182,219,443];
print('Dictionary from lists of keys and values',
ee.Dictionary.fromLists(keys,values));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# A dictionary input (e.g. results of ee.Image.reduceRegion of an S2 image).
dic = {
  'B1': 182,
  'B2': 219,
  'B3': 443
}
print('ee.Dictionary from dictionary input:', ee.Dictionary(dic).getInfo())
# A list of key/value pairs (from previous dictionary).
lst = [
  'B1', 182,
  'B2', 219,
  'B3', 443
]
print('ee.Dictionary from list input', ee.Dictionary(lst).getInfo())
```

Was this helpful?
