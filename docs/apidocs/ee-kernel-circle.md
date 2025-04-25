 
#  ee.Kernel.circle 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-kernel-circle#examples)


Generates a circle-shaped boolean kernel. 
Usage| Returns  
---|---  
`ee.Kernel.circle(radius,  _units_, _normalize_, _magnitude_)`| Kernel  
Argument| Type| Details  
---|---|---  
`radius`| Float| The radius of the kernel to generate.  
`units`| String, default: "pixels"| The system of measurement for the kernel ('pixels' or 'meters'). If the kernel is specified in meters, it will resize when the zoom-level is changed.  
`normalize`| Boolean, default: true| Normalize the kernel values to sum to 1.  
`magnitude`| Float, default: 1| Scale each value by this amount.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-kernel-circle#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-kernel-circle#colab-python-sample) More
```
print('A circle kernel',ee.Kernel.circle({radius:3}));
/**
 * Output weights matrix (up to 1/1000 precision for brevity)
 *
 * [0.000, 0.000, 0.000, 0.034, 0.000, 0.000, 0.000]
 * [0.000, 0.034, 0.034, 0.034, 0.034, 0.034, 0.000]
 * [0.000, 0.034, 0.034, 0.034, 0.034, 0.034, 0.000]
 * [0.034, 0.034, 0.034, 0.034, 0.034, 0.034, 0.034]
 * [0.000, 0.034, 0.034, 0.034, 0.034, 0.034, 0.000]
 * [0.000, 0.034, 0.034, 0.034, 0.034, 0.034, 0.000]
 * [0.000, 0.000, 0.000, 0.034, 0.000, 0.000, 0.000]
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
print('A circle kernel:')
pprint(ee.Kernel.circle(**{'radius': 3}).getInfo())
# Output weights matrix (up to 1/1000 precision for brevity)
# [0.000, 0.000, 0.000, 0.034, 0.000, 0.000, 0.000]
# [0.000, 0.034, 0.034, 0.034, 0.034, 0.034, 0.000]
# [0.000, 0.034, 0.034, 0.034, 0.034, 0.034, 0.000]
# [0.034, 0.034, 0.034, 0.034, 0.034, 0.034, 0.034]
# [0.000, 0.034, 0.034, 0.034, 0.034, 0.034, 0.000]
# [0.000, 0.034, 0.034, 0.034, 0.034, 0.034, 0.000]
# [0.000, 0.000, 0.000, 0.034, 0.000, 0.000, 0.000]
```

Was this helpful?
