 
#  ee.Kernel.laplacian4 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-kernel-laplacian4#examples)


Generates a 3x3 Laplacian-4 edge-detection kernel. 
Usage| Returns  
---|---  
`ee.Kernel.laplacian4( _magnitude_, _normalize_)`| Kernel  
Argument| Type| Details  
---|---|---  
`magnitude`| Float, default: 1| Scale each value by this amount.  
`normalize`| Boolean, default: false| Normalize the kernel values to sum to 1.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-kernel-laplacian4#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-kernel-laplacian4#colab-python-sample) More
```
print('A Laplacian-4 kernel',ee.Kernel.laplacian4());
/**
 * Output weights matrix
 *
 * [0, 1, 0]
 * [1, -4, 1]
 * [0, 1, 0]
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
print('A Laplacian-4 kernel:')
pprint(ee.Kernel.laplacian4().getInfo())
# Output weights matrix
# [0, 1, 0]
# [1, -4, 1]
# [0, 1, 0]
```

Was this helpful?
