 
#  ee.Kernel.euclidean
Stay organized with collections  Save and categorize content based on your preferences. 
Generates a distance kernel based on Euclidean (straight-line) distance. Usage| Returns  
---|---  
`ee.Kernel.euclidean(radius,  _units_, _normalize_, _magnitude_)`| Kernel  
Argument| Type| Details  
---|---|---  
`radius`| Float| The radius of the kernel to generate.  
`units`| String, default: "pixels"| The system of measurement for the kernel ('pixels' or 'meters'). If the kernel is specified in meters, it will resize when the zoom-level is changed.  
`normalize`| Boolean, default: false| Normalize the kernel values to sum to 1.  
`magnitude`| Float, default: 1| Scale each value by this amount.  
## Examples
### Code Editor (JavaScript)
```
print('A Euclidean distance kernel',ee.Kernel.euclidean({radius:3}));
/**
 * Output weights matrix (up to 1/1000 precision for brevity)
 *
 * [4.242, 3.605, 3.162, 3.000, 3.162, 3.605, 4.242]
 * [3.605, 2.828, 2.236, 2.000, 2.236, 2.828, 3.605]
 * [3.162, 2.236, 1.414, 1.000, 1.414, 2.236, 3.162]
 * [3.000, 2.000, 1.000, 0.000, 1.000, 2.000, 3.000]
 * [3.162, 2.236, 1.414, 1.000, 1.414, 2.236, 3.162]
 * [3.605, 2.828, 2.236, 2.000, 2.236, 2.828, 3.605]
 * [4.242, 3.605, 3.162, 3.000, 3.162, 3.605, 4.242]
 */
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
frompprintimport pprint
print('A Euclidean distance kernel:')
pprint(ee.Kernel.euclidean(**{'radius': 3}).getInfo())
# Output weights matrix (up to 1/1000 precision for brevity)
# [4.242, 3.605, 3.162, 3.000, 3.162, 3.605, 4.242]
# [3.605, 2.828, 2.236, 2.000, 2.236, 2.828, 3.605]
# [3.162, 2.236, 1.414, 1.000, 1.414, 2.236, 3.162]
# [3.000, 2.000, 1.000, 0.000, 1.000, 2.000, 3.000]
# [3.162, 2.236, 1.414, 1.000, 1.414, 2.236, 3.162]
# [3.605, 2.828, 2.236, 2.000, 2.236, 2.828, 3.605]
# [4.242, 3.605, 3.162, 3.000, 3.162, 3.605, 4.242]
```

