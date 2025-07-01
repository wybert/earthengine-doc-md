 
#  ee.Image.hersFeature
Stay organized with collections  Save and categorize content based on your preferences. 
Computes the Histogram Error Ring Statistic (HERS) for each pixel in each band matching the keys in the descriptor. Only the bands for which HERS could be computed are returned. Usage| Returns  
---|---  
`Image.hersFeature(reference,  _peakWidthScale_)`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The input image.  
`reference`| Dictionary| The reference descriptor computed with ee.Feature.hersDescriptor(...).  
`peakWidthScale`| Float, default: 1| The HERS peak width scale.  
