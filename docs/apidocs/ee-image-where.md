 
#  ee.Image.where 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Performs conditional replacement of values. 
For each pixel in each band of 'input', if the corresponding pixel in 'test' is nonzero, output the corresponding pixel in value, otherwise output the input pixel.
If at a given pixel, either test or value is masked, the input value is used. If the input is masked, nothing is done.
The output bands have the same names as the input bands. The output type of each band is the larger of the input and value types. The output image retains the metadata and footprint of the input image.
Usage| Returns  
---|---  
`Image.where(test, value)`| Image  
Argument| Type| Details  
---|---|---  
this: `input`| Image| The input image.  
`test`| Image| The test image. The pixels of this image determines which of the input pixels is returned. If this is a single band, it is used for all bands in the input image. This may not be an array image.  
`value`| Image| The output value to use where test is not zero. If this is a single band, it is used for all bands in the input image.  
