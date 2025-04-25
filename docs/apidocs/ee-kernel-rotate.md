 
#  ee.Kernel.rotate 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-kernel-rotate#examples)


Creates a Kernel. 
Usage| Returns  
---|---  
`Kernel.rotate(rotations)`| Kernel  
Argument| Type| Details  
---|---|---  
this: `kernel`| Kernel| The kernel to be rotated.  
`rotations`| Integer| Number of 90 degree rotations to make. Negative numbers rotate counterclockwise.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-kernel-rotate#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-kernel-rotate#colab-python-sample) More
```
// A kernel to be rotated.
varsobelKernel=ee.Kernel.sobel();
print(sobelKernel);
/**
 * Output weights matrix
 *
 * [-1, 0, 1]
 * [-2, 0, 2]
 * [-1, 0, 1]
 */
print('One 90 degree clockwise rotation',sobelKernel.rotate(1));
/**
 * [-1, -2, -1]
 * [ 0, 0, 0]
 * [ 1, 2, 1]
 */
print('Two 90 degree counterclockwise rotations',sobelKernel.rotate(-2));
/**
 * [1, 0, -1]
 * [2, 0, -2]
 * [1, 0, -1]
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
# A kernel to be rotated.
sobel_kernel = ee.Kernel.sobel()
pprint(sobel_kernel.getInfo())
# Output weights matrix
# [-1, 0, 1]
# [-2, 0, 2]
# [-1, 0, 1]
print('One 90 degree clockwise rotation:')
pprint(sobel_kernel.rotate(1).getInfo())
# [-1, -2, -1]
# [ 0, 0, 0]
# [ 1, 2, 1]
print('Two 90 degree counterclockwise rotations:')
pprint(sobel_kernel.rotate(-2).getInfo())
# [1, 0, -1]
# [2, 0, -2]
# [1, 0, -1]
```

Was this helpful?
