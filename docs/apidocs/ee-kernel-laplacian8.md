 
#  ee.Kernel.laplacian8 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-kernel-laplacian8#examples)


Generates a 3x3 Laplacian-8 edge-detection kernel. 
Usage| Returns  
---|---  
`ee.Kernel.laplacian8( _magnitude_, _normalize_)`| Kernel  
Argument| Type| Details  
---|---|---  
`magnitude`| Float, default: 1| Scale each value by this amount.  
`normalize`| Boolean, default: false| Normalize the kernel values to sum to 1.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-kernel-laplacian8#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-kernel-laplacian8#colab-python-sample) More
```
print('A Laplacian-8 kernel',ee.Kernel.laplacian8());
/**
 * Output weights matrix
 *
 * [1, 1, 1]
 * [1, -8, 1]
 * [1, 1, 1]
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
print('A Laplacian-8 kernel:')
pprint(ee.Kernel.laplacian8().getInfo())
# Output weights matrix
# [1, 1, 1]
# [1, -8, 1]
# [1, 1, 1]
```

Was this helpful?
