 
#  ee.Kernel.inverse 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-kernel-inverse#examples)


Returns a kernel which has each of its weights multiplicatively inverted. Weights with a value of zero are not inverted and remain zero. 
Usage| Returns  
---|---  
`Kernel.inverse()`| Kernel  
Argument| Type| Details  
---|---|---  
this: `kernel`| Kernel| The kernel to have its entries inverted.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-kernel-inverse#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-kernel-inverse#colab-python-sample) More
```
varsobelKernel=ee.Kernel.sobel();
print(sobelKernel);
/**
 * Output weights matrix
 *
 * [-1, 0, 1]
 * [-2, 0, 2]
 * [-1, 0, 1]
 */
print('Inverse of Sobel kernel weights',sobelKernel.inverse());
/**
 * [-1.0, 0.0, 1.0]
 * [-0.5, 0.0, 0.5]
 * [-1.0, 0.0, 1.0]
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
sobel_kernel = ee.Kernel.sobel()
pprint(sobel_kernel.getInfo())
# Output weights matrix
# [-1, 0, 1]
# [-2, 0, 2]
# [-1, 0, 1]
print('Inverse of Sobel kernel weights:')
pprint(sobel_kernel.inverse().getInfo())
# [-1.0, 0.0, 1.0]
# [-0.5, 0.0, 0.5]
# [-1.0, 0.0, 1.0]
```

Was this helpful?
