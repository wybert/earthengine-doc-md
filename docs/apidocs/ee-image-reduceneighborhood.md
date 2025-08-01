 
#  ee.Image.reduceNeighborhood
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Applies the given reducer to the neighborhood around each pixel, as determined by the given kernel. If the reducer has a single input, it will be applied separately to each band of the collection; otherwise it must have the same number of inputs as the input image has bands.
The reducer output names determine the names of the output bands: reducers with multiple inputs will use the output names directly, while reducers with a single input will prefix the output name with the input band name (e.g., '10_mean', '20_mean').
Reducers with weighted inputs can have the input weight based on the input mask, the kernel value, or the smaller of those two.
Usage | Returns  
---|---  
`Image.reduceNeighborhood(reducer, kernel, _inputWeight_, _skipMasked_, _optimization_)`|  Image  
Argument | Type | Details  
---|---|---  
this: `image` | Image | The input image.  
`reducer` | Reducer | The reducer to apply to pixels within the neighborhood.  
`kernel` | Kernel | The kernel defining the neighborhood.  
`inputWeight` | String, default: "kernel" | One of 'mask', 'kernel', or 'min'.  
`skipMasked` | Boolean, default: true | Mask output pixels if the corresponding input pixel is masked.  
`optimization` | String, default: null | Optimization strategy. Options are 'boxcar' and 'window'. The 'boxcar' method is a fast method for computing count, sum or mean. It requires a homogeneous kernel, a single-input reducer and either MASK, KERNEL or no weighting. The 'window' method uses a running window, and has the same requirements as 'boxcar', but can use any single input reducer. Both methods require considerable additional memory.  
Was this helpful?
