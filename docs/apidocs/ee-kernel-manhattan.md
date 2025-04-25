 
#  ee.Kernel.manhattan 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-kernel-manhattan#examples)


Generates a distance kernel based on rectilinear (city-block) distance. 
Usage| Returns  
---|---  
`ee.Kernel.manhattan(radius,  _units_, _normalize_, _magnitude_)`| Kernel  
Argument| Type| Details  
---|---|---  
`radius`| Float| The radius of the kernel to generate.  
`units`| String, default: "pixels"| The system of measurement for the kernel ('pixels' or 'meters'). If the kernel is specified in meters, it will resize when the zoom-level is changed.  
`normalize`| Boolean, default: false| Normalize the kernel values to sum to 1.  
`magnitude`| Float, default: 1| Scale each value by this amount.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-kernel-manhattan#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-kernel-manhattan#colab-python-sample) More
```
print('A Manhattan kernel',ee.Kernel.manhattan({radius:3}));
/**
 * Output weights matrix
 *
 * [6, 5, 4, 3, 4, 5, 6]
 * [5, 4, 3, 2, 3, 4, 5]
 * [4, 3, 2, 1, 2, 3, 4]
 * [3, 2, 1, 0, 1, 2, 3]
 * [4, 3, 2, 1, 2, 3, 4]
 * [5, 4, 3, 2, 3, 4, 5]
 * [6, 5, 4, 3, 4, 5, 6]
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
print('A Manhattan kernel:')
pprint(ee.Kernel.manhattan(**{'radius': 3}).getInfo())
# Output weights matrix
# [6, 5, 4, 3, 4, 5, 6]
# [5, 4, 3, 2, 3, 4, 5]
# [4, 3, 2, 1, 2, 3, 4]
# [3, 2, 1, 0, 1, 2, 3]
# [4, 3, 2, 1, 2, 3, 4]
# [5, 4, 3, 2, 3, 4, 5]
# [6, 5, 4, 3, 4, 5, 6]
```

Was this helpful?
