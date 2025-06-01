 
#  ee.Kernel.add 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-kernel-add#examples)


Adds two kernels (pointwise) after aligning their centers. 
Usage| Returns  
---|---  
`Kernel.add(kernel2,  _normalize_)`| Kernel  
Argument| Type| Details  
---|---|---  
this: `kernel1`| Kernel| The first kernel.  
`kernel2`| Kernel| The second kernel.  
`normalize`| Boolean, default: false| Normalize the kernel.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-kernel-add#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-kernel-add#colab-python-sample) More
```
// Two kernels, they do not need to have the same dimensions.
varkernelA=ee.Kernel.chebyshev({radius:3});
varkernelB=ee.Kernel.square({radius:1,normalize:false,magnitude:100});
print(kernelA,kernelB);
/**
 * Two kernel weights matrices
 *
 *  [3, 3, 3, 3, 3, 3, 3]
 *  [3, 2, 2, 2, 2, 2, 3]
 *  [3, 2, 1, 1, 1, 2, 3]    [100, 100, 100]
 * A [3, 2, 1, 0, 1, 2, 3]   B [100, 100, 100]
 *  [3, 2, 1, 1, 1, 2, 3]    [100, 100, 100]
 *  [3, 2, 2, 2, 2, 2, 3]
 *  [3, 3, 3, 3, 3, 3, 3]
 */
print('Pointwise addition of two kernels',kernelA.add(kernelB));
/**
 * [3, 3,  3,  3,  3, 3, 3]
 * [3, 2,  2,  2,  2, 2, 3]
 * [3, 2, 101, 101, 101, 2, 3]
 * [3, 2, 101, 100, 101, 2, 3]
 * [3, 2, 101, 101, 101, 2, 3]
 * [3, 2,  2,  2,  2, 2, 3]
 * [3, 3,  3,  3,  3, 3, 3]
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
# Two kernels, they do not need to have the same dimensions.
kernel_a = ee.Kernel.chebyshev(**{'radius': ee.Number(3)})
kernel_b = ee.Kernel.square(**{
  'radius': 1,
  'normalize': False,
  'magnitude': 100
})
pprint(kernel_a.getInfo())
pprint(kernel_b.getInfo())
# Two kernel weights matrices
#  [3, 3, 3, 3, 3, 3, 3]
#  [3, 2, 2, 2, 2, 2, 3]
#  [3, 2, 1, 1, 1, 2, 3]    [100, 100, 100]
# A [3, 2, 1, 0, 1, 2, 3]   B [100, 100, 100]
#  [3, 2, 1, 1, 1, 2, 3]    [100, 100, 100]
#  [3, 2, 2, 2, 2, 2, 3]
#  [3, 3, 3, 3, 3, 3, 3]
print('Pointwise addition of two kernels:')
pprint(kernel_a.add(kernel_b).getInfo())
# [3, 3,  3,  3,  3, 3, 3]
# [3, 2,  2,  2,  2, 2, 3]
# [3, 2, 101, 101, 101, 2, 3]
# [3, 2, 101, 100, 101, 2, 3]
# [3, 2, 101, 101, 101, 2, 3]
# [3, 2,  2,  2,  2, 2, 3]
# [3, 3,  3,  3,  3, 3, 3]
```

Was this helpful?
