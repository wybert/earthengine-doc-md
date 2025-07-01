 
#  ee.Kernel.fixed
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-kernel-fixed#examples)


Creates a Kernel. 
Usage| Returns  
---|---  
`ee.Kernel.fixed( _width_, _height_, weights, _x_, _y_, _normalize_)`| Kernel  
Argument| Type| Details  
---|---|---  
`width`| Integer, default: -1| The width of the kernel in pixels.  
`height`| Integer, default: -1| The height of the kernel in pixels.  
`weights`| List| A 2-D list of [height] x [width] values to use as the weights of the kernel.  
`x`| Integer, default: -1| The location of the focus, as an offset from the left.  
`y`| Integer, default: -1| The location of the focus, as an offset from the top.  
`normalize`| Boolean, default: false| Normalize the kernel values to sum to 1.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-kernel-fixed#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-kernel-fixed#colab-python-sample) More
```
// Kernel weights.
varweights=[[4,3,2,1,2,3,4],
[4,3,2,1,2,3,4],
[4,3,2,1,2,3,4]];
print('A fixed kernel',ee.Kernel.fixed({weights:weights}));
/**
 * Output weights matrix
 *
 * [4, 3, 2, 1, 2, 3, 4]
 * [4, 3, 2, 1, 2, 3, 4]
 * [4, 3, 2, 1, 2, 3, 4]
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
weights = [[4, 3, 2, 1, 2, 3, 4],
      [4, 3, 2, 1, 2, 3, 4],
      [4, 3, 2, 1, 2, 3, 4]]
print('A fixed kernel:')
pprint(ee.Kernel.fixed(**{'weights': weights}).getInfo())
# Output weights matrix
# [4, 3, 2, 1, 2, 3, 4]
# [4, 3, 2, 1, 2, 3, 4]
# [4, 3, 2, 1, 2, 3, 4]
```

Was this helpful?
