 
#  ee.Image.neighborhoodToArray
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Turns the neighborhood of each pixel in a scalar image into a 2D array. Axes 0 and 1 of the output array correspond to Y and X axes of the image, respectively. The output image will have as many bands as the input; each output band has the same mask as the corresponding input band. The footprint and metadata of the input image are preserved. 
Usage| Returns  
---|---  
`Image.neighborhoodToArray(kernel,  _defaultValue_)`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The image to get pixels from; must be scalar-valued.  
`kernel`| Kernel| The kernel specifying the shape of the neighborhood. Only fixed, square and rectangle kernels are supported. Weights are ignored; only the shape of the kernel is used.  
`defaultValue`| Float, default: 0| The value to use in the output arrays to replace the invalid (masked) pixels of the input. If the band type is integral, the fractional part of this value is discarded; in all cases, the value is clamped to the value range of the band.  
Was this helpful?
