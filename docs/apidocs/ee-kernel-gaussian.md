 
#  ee.Kernel.gaussian
Stay organized with collections  Save and categorize content based on your preferences. 
Generates a Gaussian kernel from a sampled continuous Gaussian. Usage | Returns  
---|---  
`ee.Kernel.gaussian(radius, _sigma_, _units_, _normalize_, _magnitude_)`|  Kernel  
Argument | Type | Details  
---|---|---  
`radius` | Float | The radius of the kernel to generate.  
`sigma` | Float, default: 1 | Standard deviation of the Gaussian function (same units as radius).  
`units` | String, default: "pixels" | The system of measurement for the kernel ('pixels' or 'meters'). If the kernel is specified in meters, it will resize when the zoom-level is changed.  
`normalize` | Boolean, default: true | Normalize the kernel values to sum to 1.  
`magnitude` | Float, default: 1 | Scale each value by this amount.  
## Examples
### Code Editor (JavaScript)
```
print('A Gaussian kernel',ee.Kernel.gaussian({radius:3}));

/**
 * Output weights matrix (up to 1/1000 precision for brevity)
 *
 * [0.002, 0.013, 0.021, 0.013, 0.002]
 * [0.013, 0.059, 0.098, 0.059, 0.013]
 * [0.021, 0.098, 0.162, 0.098, 0.021]
 * [0.013, 0.059, 0.098, 0.059, 0.013]
 * [0.002, 0.013, 0.021, 0.013, 0.002]
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

print('A Gaussian kernel:')
pprint(ee.Kernel.gaussian(**{'radius': 3}).getInfo())

#  Output weights matrix (up to 1/1000 precision for brevity)

#  [0.002, 0.013, 0.021, 0.013, 0.002]
#  [0.013, 0.059, 0.098, 0.059, 0.013]
#  [0.021, 0.098, 0.162, 0.098, 0.021]
#  [0.013, 0.059, 0.098, 0.059, 0.013]
#  [0.002, 0.013, 0.021, 0.013, 0.002]
```

