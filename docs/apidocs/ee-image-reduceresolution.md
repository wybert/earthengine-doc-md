 
#  ee.Image.reduceResolution 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Enables reprojection using the given reducer to combine all input pixels corresponding to each output pixel. If the reducer has a single input, it will be applied separately to each band of the collection; otherwise it must have the same number of inputs as the input image has bands. 
The reducer output names determine the names of the output bands: reducers with multiple inputs will use the output names directly, reducers with a single input and single output will preserve the input band names, and reducers with a single input and multiple outputs will prefix the output name with the input band name (e.g., '10_mean', '10_stdDev', '20_mean', '20_stdDev').
Reducer input weights will be the product of the input mask and the fraction of the output pixel covered by the input pixel.
Usage| Returns  
---|---  
`Image.reduceResolution(reducer,  _bestEffort_, _maxPixels_)`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The input image.  
`reducer`| Reducer| The reducer to apply to be used for combining pixels.  
`bestEffort`| Boolean, default: false| If using the input at its default resolution would require too many pixels, start with already-reduced input pixels from a pyramid level that allows the operation to succeed.  
`maxPixels`| Integer, default: 64| The maximum number of input pixels to combine for each output pixel. Setting this too large will cause out-of-memory problems.  
Was this helpful?
