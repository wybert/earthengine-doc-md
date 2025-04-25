 
#  ee.Dictionary.select 
Stay organized with collections  Save and categorize content based on your preferences. 
Returns a dictionary with only the specified keys. Usage| Returns  
---|---  
`Dictionary.select(selectors,  _ignoreMissing_)`| Dictionary  
Argument| Type| Details  
---|---|---  
this: `dictionary`| Dictionary|   
`selectors`| List| A list of keys or regular expressions to select.  
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
print('Select keys by name',dict.select(['B1','B2']));
print('Select keys by regex',dict.select(['B[1-2]']));
print('Set ignoreMissing as true to avoid an unmatched key error',
dict.select({selectors:['B1','B2','Region'],ignoreMissing:true}));
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
print('Select keys by name:', dic.select(['B1', 'B2']).getInfo())
print('Select keys by regex:', dic.select(['B[1-2]']).getInfo())
dic_select = dic.select(**{'selectors': ['B1', 'B2', 'Region'],
              'ignoreMissing': True})
print('Set ignoreMissing as true to avoid an unmatched key error:',
   dic_select.getInfo())
```

