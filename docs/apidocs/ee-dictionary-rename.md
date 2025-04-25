 
#  ee.Dictionary.rename 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-dictionary-rename#examples)


Rename elements in a dictionary. 
Usage| Returns  
---|---  
`Dictionary.rename(from, to,  _overwrite_)`| Dictionary  
Argument| Type| Details  
---|---|---  
this: `dictionary`| Dictionary  
`from`| List| A list of keys to be renamed.  
`to`| List| A list of the new names for the keys listed in the 'from' parameter. Must have the same length as the 'from' list.  
`overwrite`| Boolean, default: false| Allow overwriting existing properties with the same name.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-dictionary-rename#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-dictionary-rename#colab-python-sample) More
```
// A dictionary (e.g. results of ee.Image.reduceRegion of an S2 image).
vardict=ee.Dictionary({
B1:182,
B2:219,
B3:443
});
// Define from-to key name lists for selected keys.
varfrom=['B2','B3'];
varto=['Band_2','Band_3'];
print('Renamed keys',dict.rename(from,to));
print('Overwrite existing key names, e.g. B3 becomes B1',
dict.rename({from:['B3'],to:['B1'],overwrite:true}));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# A dictionary (e.g. results of ee.Image.reduceRegion of an S2 image).
dic = ee.Dictionary({
  'B1': 182,
  'B2': 219,
  'B3': 443
})
# Define from-to key name lists for selected keys.
frm = ['B2', 'B3']
to = ['Band_2', 'Band_3']
print('Renamed keys:', dic.rename(frm, to).getInfo())
dic_overwrite = dic.rename(**{'from': ['B3'], 'to': ['B1'], 'overwrite': True})
print('Overwrite existing key names, e.g. B3 becomes B1:',
   dic_overwrite.getInfo())
```

Was this helpful?
