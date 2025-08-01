 
#  ee.Kernel.chebyshev
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-kernel-chebyshev#examples)


Generates a distance kernel based on Chebyshev distance (greatest distance along any dimension).
Usage | Returns  
---|---  
`ee.Kernel.chebyshev(radius, _units_, _normalize_, _magnitude_)`|  Kernel  
Argument | Type | Details  
---|---|---  
`radius` | Float | The radius of the kernel to generate.  
`units` | String, default: "pixels" | The system of measurement for the kernel ('pixels' or 'meters'). If the kernel is specified in meters, it will resize when the zoom-level is changed.  
`normalize` | Boolean, default: false | Normalize the kernel values to sum to 1.  
`magnitude` | Float, default: 1 | Scale each value by this amount.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-kernel-chebyshev#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-kernel-chebyshev#colab-python-sample) More
```
print('A Chebyshev distance kernel',ee.Kernel.chebyshev({radius:3}));

/**
 * Output weights matrix
 *
 * [3, 3, 3, 3, 3, 3, 3]
 * [3, 2, 2, 2, 2, 2, 3]
 * [3, 2, 1, 1, 1, 2, 3]
 * [3, 2, 1, 0, 1, 2, 3]
 * [3, 2, 1, 1, 1, 2, 3]
 * [3, 2, 2, 2, 2, 2, 3]
 * [3, 3, 3, 3, 3, 3, 3]
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

print('A Chebyshev distance kernel:')
pprint(ee.Kernel.chebyshev(**{'radius': 3}).getInfo())

#  Output weights matrix
#  [3, 3, 3, 3, 3, 3, 3]
#  [3, 2, 2, 2, 2, 2, 3]
#  [3, 2, 1, 1, 1, 2, 3]
#  [3, 2, 1, 0, 1, 2, 3]
#  [3, 2, 1, 1, 1, 2, 3]
#  [3, 2, 2, 2, 2, 2, 3]
#  [3, 3, 3, 3, 3, 3, 3]
```

Was this helpful?
