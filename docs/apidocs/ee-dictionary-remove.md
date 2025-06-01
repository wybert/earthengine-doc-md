 
#  ee.Dictionary.remove 
Stay organized with collections  Save and categorize content based on your preferences. 
Returns a dictionary with the specified keys removed. Usage| Returns  
---|---  
`Dictionary.remove(selectors,  _ignoreMissing_)`| Dictionary  
Argument| Type| Details  
---|---|---  
this: `dictionary`| Dictionary|   
`selectors`| List| A list of keys names or regular expressions of key names to remove.  
`ignoreMissing`| Boolean, default: false| Ignore selectors that don't match at least 1 key.  
## Examples
### Code Editor (JavaScript)
```
// A dictionary (e.g. results of ee.Image.reduceRegion of an S2 image).
vardict=ee.Dictionary({
B1:182,
B2:219,
B3:443
});
print('Dictionary with selected keys removed',dict.remove(['B2','B3']));
print('Set ignoreMissing as true to avoid an unmatched key error',
dict.remove({selectors:['B2','B3','Region'],ignoreMissing:true}));
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# A dictionary (e.g. results of ee.Image.reduceRegion of an S2 image).
dic = ee.Dictionary({
  'B1': 182,
  'B2': 219,
  'B3': 443
})
print('Dictionary with selected keys removed:',
   dic.remove(['B2', 'B3']).getInfo())
dic_subset = dic.remove(**{'selectors': ['B2', 'B3', 'Region'],
             'ignoreMissing': True})
print('Set ignoreMissing as true to avoid an unmatched key error:',
   dic_subset.getInfo())
```

