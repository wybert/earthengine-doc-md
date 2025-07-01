 
#  ee.Kernel.diamond
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-kernel-diamond#examples)


Generates a diamond-shaped boolean kernel. 
Usage| Returns  
---|---  
`ee.Kernel.diamond(radius,  _units_, _normalize_, _magnitude_)`| Kernel  
Argument| Type| Details  
---|---|---  
`radius`| Float| The radius of the kernel to generate.  
`units`| String, default: "pixels"| The system of measurement for the kernel ('pixels' or 'meters'). If the kernel is specified in meters, it will resize when the zoom-level is changed.  
`normalize`| Boolean, default: true| Normalize the kernel values to sum to 1.  
`magnitude`| Float, default: 1| Scale each value by this amount.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-kernel-diamond#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-kernel-diamond#colab-python-sample) More
```
print('A diamond kernel',ee.Kernel.diamond({radius:3}));
/**
 * Output weights matrix (up to 1/100 precision for brevity)
 *
 * [0.00, 0.00, 0.00, 0.04, 0.00, 0.00, 0.00]
 * [0.00, 0.00, 0.04, 0.04, 0.04, 0.00, 0.00]
 * [0.00, 0.04, 0.04, 0.04, 0.04, 0.04, 0.00]
 * [0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04]
 * [0.00, 0.04, 0.04, 0.04, 0.04, 0.04, 0.00]
 * [0.00, 0.00, 0.04, 0.04, 0.04, 0.00, 0.00]
 * [0.00, 0.00, 0.00, 0.04, 0.00, 0.00, 0.00]
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
print('A diamond kernel:')
pprint(ee.Kernel.diamond(**{'radius': 3}).getInfo())
# Output weights matrix (up to 1/100 precision for brevity)
# [0.00, 0.00, 0.00, 0.04, 0.00, 0.00, 0.00]
# [0.00, 0.00, 0.04, 0.04, 0.04, 0.00, 0.00]
# [0.00, 0.04, 0.04, 0.04, 0.04, 0.04, 0.00]
# [0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04]
# [0.00, 0.04, 0.04, 0.04, 0.04, 0.04, 0.00]
# [0.00, 0.00, 0.04, 0.04, 0.04, 0.00, 0.00]
# [0.00, 0.00, 0.00, 0.04, 0.00, 0.00, 0.00]
```

Was this helpful?
