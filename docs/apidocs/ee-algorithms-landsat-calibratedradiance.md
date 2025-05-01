 
#  ee.Algorithms.Landsat.calibratedRadiance 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Calibrates each band of an image by applying linear transformation with slope `RADIANCE_MULT_BAND_N` and y-intercept `RADIANCE_ADD_BAND_N`; these values are extracted from the image metadata. Usage| Returns  
---|---  
`ee.Algorithms.Landsat.calibratedRadiance(image)`| Image  
Argument| Type| Details  
---|---|---  
`image`| Image| The input Landsat image.  
