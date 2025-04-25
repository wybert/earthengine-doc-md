 
#  ee.Kernel.roberts 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-kernel-roberts#examples)


Generates a 2x2 Roberts edge-detection kernel. 
Usage| Returns  
---|---  
`ee.Kernel.roberts( _magnitude_, _normalize_)`| Kernel  
Argument| Type| Details  
---|---|---  
`magnitude`| Float, default: 1| Scale each value by this amount.  
`normalize`| Boolean, default: false| Normalize the kernel values to sum to 1.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-kernel-roberts#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-kernel-roberts#colab-python-sample) More
```
print('A Roberts kernel',ee.Kernel.roberts());
/**
 * Output weights matrix; center is position [1,1]
 *
 * [1, 0]
 * [0, -1]
 */
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
frompprintimport pprint
print('A Roberts kernel:')
pprint(ee.Kernel.roberts().getInfo())
# Output weights matrix; center is position [1,1]
# [1, 0]
# [0, -1]
```

Was this helpful?
