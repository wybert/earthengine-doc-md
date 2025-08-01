 
#  ee.Kernel.compass
Stay organized with collections  Save and categorize content based on your preferences. 
Generates a 3x3 Prewitt's Compass edge-detection kernel. Usage | Returns  
---|---  
`ee.Kernel.compass(_magnitude_, _normalize_)`|  Kernel  
Argument | Type | Details  
---|---|---  
`magnitude` | Float, default: 1 | Scale each value by this amount.  
`normalize` | Boolean, default: false | Normalize the kernel values to sum to 1.  
## Examples
### Code Editor (JavaScript)
```
print('A Prewitt compass kernel',ee.Kernel.compass());

/**
 * Output weights matrix
 *
 * [1,  1, -1]
 * [1, -2, -1]
 * [1,  1, -1]
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

print('A Prewitt compass kernel:')
pprint(ee.Kernel.compass().getInfo())

# Output weights matrix

#  [1,  1, -1]
#  [1, -2, -1]
#  [1,  1, -1]
```

