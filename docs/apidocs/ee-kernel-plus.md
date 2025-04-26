 
#  ee.Kernel.plus 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Generates a plus-shaped boolean kernel. Usage| Returns  
---|---  
`ee.Kernel.plus(radius,  _units_, _normalize_, _magnitude_)`| Kernel  
Argument| Type| Details  
---|---|---  
`radius`| Float| The radius of the kernel to generate.  
`units`| String, default: "pixels"| The system of measurement for the kernel ('pixels' or 'meters'). If the kernel is specified in meters, it will resize when the zoom-level is changed.  
`normalize`| Boolean, default: true| Normalize the kernel values to sum to 1.  
`magnitude`| Float, default: 1| Scale each value by this amount.  
## Examples
### Code Editor (JavaScript)
```
print('A plus kernel',ee.Kernel.plus({radius:3}));
/**
 * Output weights matrix (1/1000 precision shown for brevity)
 *
 * [0.000, 0.000, 0.000, 0.076, 0.000, 0.000, 0.000]
 * [0.000, 0.000, 0.000, 0.076, 0.000, 0.000, 0.000]
 * [0.000, 0.000, 0.000, 0.076, 0.000, 0.000, 0.000]
 * [0.076, 0.076, 0.076, 0.076, 0.076, 0.076, 0.076]
 * [0.000, 0.000, 0.000, 0.076, 0.000, 0.000, 0.000]
 * [0.000, 0.000, 0.000, 0.076, 0.000, 0.000, 0.000]
 * [0.000, 0.000, 0.000, 0.076, 0.000, 0.000, 0.000]
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
print('A plus kernel:')
pprint(ee.Kernel.plus(**{'radius': 3}).getInfo())
# Output weights matrix (1/1000 precision shown for brevity)
# [0.000, 0.000, 0.000, 0.076, 0.000, 0.000, 0.000]
# [0.000, 0.000, 0.000, 0.076, 0.000, 0.000, 0.000]
# [0.000, 0.000, 0.000, 0.076, 0.000, 0.000, 0.000]
# [0.076, 0.076, 0.076, 0.076, 0.076, 0.076, 0.076]
# [0.000, 0.000, 0.000, 0.076, 0.000, 0.000, 0.000]
# [0.000, 0.000, 0.000, 0.076, 0.000, 0.000, 0.000]
# [0.000, 0.000, 0.000, 0.076, 0.000, 0.000, 0.000]
```

