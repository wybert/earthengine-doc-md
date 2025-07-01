 
#  ee.Kernel.octagon
Stay organized with collections  Save and categorize content based on your preferences. 
Generates an octagon-shaped boolean kernel. Usage| Returns  
---|---  
`ee.Kernel.octagon(radius,  _units_, _normalize_, _magnitude_)`| Kernel  
Argument| Type| Details  
---|---|---  
`radius`| Float| The radius of the kernel to generate.  
`units`| String, default: "pixels"| The system of measurement for the kernel ('pixels' or 'meters'). If the kernel is specified in meters, it will resize when the zoom-level is changed.  
`normalize`| Boolean, default: true| Normalize the kernel values to sum to 1.  
`magnitude`| Float, default: 1| Scale each value by this amount.  
## Examples
### Code Editor (JavaScript)
```
print('An octagon kernel',ee.Kernel.octagon({radius:3}));
/**
 * Output weights matrix (up to 1/1000 precision for brevity)
 *
 * [0.000, 0.000, 0.027, 0.027, 0.027, 0.000, 0.000]
 * [0.000, 0.027, 0.027, 0.027, 0.027, 0.027, 0.000]
 * [0.027, 0.027, 0.027, 0.027, 0.027, 0.027, 0.027]
 * [0.027, 0.027, 0.027, 0.027, 0.027, 0.027, 0.027]
 * [0.027, 0.027, 0.027, 0.027, 0.027, 0.027, 0.027]
 * [0.000, 0.027, 0.027, 0.027, 0.027, 0.027, 0.000]
 * [0.000, 0.000, 0.027, 0.027, 0.027, 0.000, 0.000]
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
print('An octagon kernel:')
pprint(ee.Kernel.octagon(**{'radius': 3}).getInfo())
# Output weights matrix (up to 1/1000 precision for brevity)
# [0.000, 0.000, 0.027, 0.027, 0.027, 0.000, 0.000]
# [0.000, 0.027, 0.027, 0.027, 0.027, 0.027, 0.000]
# [0.027, 0.027, 0.027, 0.027, 0.027, 0.027, 0.027]
# [0.027, 0.027, 0.027, 0.027, 0.027, 0.027, 0.027]
# [0.027, 0.027, 0.027, 0.027, 0.027, 0.027, 0.027]
# [0.000, 0.027, 0.027, 0.027, 0.027, 0.027, 0.000]
# [0.000, 0.000, 0.027, 0.027, 0.027, 0.000, 0.000]
```

