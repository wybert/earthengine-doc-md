 
#  ee.Kernel.sobel
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-kernel-sobel#examples)


Generates a 3x3 Sobel edge-detection kernel. 
Usage| Returns  
---|---  
`ee.Kernel.sobel( _magnitude_, _normalize_)`| Kernel  
Argument| Type| Details  
---|---|---  
`magnitude`| Float, default: 1| Scale each value by this amount.  
`normalize`| Boolean, default: false| Normalize the kernel values to sum to 1.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-kernel-sobel#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-kernel-sobel#colab-python-sample) More
```
print('A Sobel kernel',ee.Kernel.sobel());
/**
 * Output weights matrix
 *
 * [-1, 0, 1]
 * [-2, 0, 2]
 * [-1, 0, 1]
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
print('A Sobel kernel:')
pprint(ee.Kernel.sobel().getInfo())
# Output weights matrix
# [-1, 0, 1]
# [-2, 0, 2]
# [-1, 0, 1]
```

Was this helpful?
