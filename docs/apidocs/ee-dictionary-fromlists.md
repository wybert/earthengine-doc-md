 
#  ee.Dictionary.fromLists 
Stay organized with collections  Save and categorize content based on your preferences. 
Construct a dictionary from two parallel lists of keys and values. Usage| Returns  
---|---  
`ee.Dictionary.fromLists(keys, values)`| Dictionary  
Argument| Type| Details  
---|---|---  
`keys`| List| A list of keys.  
`values`| List| A list of values.  
## Examples
### Code Editor (JavaScript)
```
// Corresponding lists of keys and values.
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

### Colab (Python)
```
# Corresponding lists of keys and values.
keys = ['B1', 'B2', 'B3']
values = [182, 219, 443]
print('Dictionary from lists of keys and values:',
   ee.Dictionary.fromLists(keys, values).getInfo())
```

