 
#  ee.Kernel.rectangle 
Stay organized with collections  Save and categorize content based on your preferences. 
Generates a rectangular-shaped kernel. Usage| Returns  
---|---  
`ee.Kernel.rectangle(xRadius, yRadius,  _units_, _normalize_, _magnitude_)`| Kernel  
Argument| Type| Details  
---|---|---  
`xRadius`| Float| The horizontal radius of the kernel to generate.  
`yRadius`| Float| The vertical radius of the kernel to generate.  
`units`| String, default: "pixels"| The system of measurement for the kernel ("pixels" or "meters"). If the kernel is specified in meters, it will resize when the zoom-level is changed.  
`normalize`| Boolean, default: true| Normalize the kernel values to sum to 1.  
`magnitude`| Float, default: 1| Scale each value by this amount.  
## Examples
### Code Editor (JavaScript)
```
print('A rectangle kernel',ee.Kernel.rectangle({xRadius:2,yRadius:1}));
/**
 * Output weights matrix (up to 1/1000 precision for brevity)
 *
 * [0.066, 0.066, 0.066, 0.066, 0.066]
 * [0.066, 0.066, 0.066, 0.066, 0.066]
 * [0.066, 0.066, 0.066, 0.066, 0.066]
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
print('A rectangle kernel:')
pprint(ee.Kernel.rectangle(**{'xRadius': 2, 'yRadius': 1}).getInfo());
# Output weights matrix (up to 1/1000 precision for brevity)
# [0.066, 0.066, 0.066, 0.066, 0.066]
# [0.066, 0.066, 0.066, 0.066, 0.066]
# [0.066, 0.066, 0.066, 0.066, 0.066]
```

