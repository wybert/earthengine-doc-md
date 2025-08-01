 
#  ee.Kernel.inverse
Stay organized with collections  Save and categorize content based on your preferences. 
Returns a kernel which has each of its weights multiplicatively inverted. Weights with a value of zero are not inverted and remain zero. Usage | Returns  
---|---  
`Kernel.inverse()` | Kernel  
Argument | Type | Details  
---|---|---  
this: `kernel` | Kernel | The kernel to have its entries inverted.  
## Examples
### Code Editor (JavaScript)
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

### Colab (Python)
```
frompprintimport pprint

sobel_kernel = ee.Kernel.sobel()
pprint(sobel_kernel.getInfo())

# Output weights matrix

#  [-1, 0, 1]
#  [-2, 0, 2]
#  [-1, 0, 1]

print('Inverse of Sobel kernel weights:')
pprint(sobel_kernel.inverse().getInfo())

#  [-1.0, 0.0, 1.0]
#  [-0.5, 0.0, 0.5]
#  [-1.0, 0.0, 1.0]
```

