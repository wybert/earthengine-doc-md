 
#  ee.Kernel.prewitt 
Stay organized with collections  Save and categorize content based on your preferences. 
Generates a 3x3 Prewitt edge-detection kernel. Usage| Returns  
---|---  
`ee.Kernel.prewitt( _magnitude_, _normalize_)`| Kernel  
Argument| Type| Details  
---|---|---  
`magnitude`| Float, default: 1| Scale each value by this amount.  
`normalize`| Boolean, default: false| Normalize the kernel values to sum to 1.  
## Examples
### Code Editor (JavaScript)
```
print('A Prewitt kernel',ee.Kernel.prewitt());
/**
 * Output weights matrix
 *
 * [1, 0, -1]
 * [1, 0, -1]
 * [1, 0, -1]
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
print('A Prewitt kernel:')
pprint(ee.Kernel.prewitt().getInfo())
# Output weights matrix
# [1, 0, -1]
# [1, 0, -1]
# [1, 0, -1]
```

