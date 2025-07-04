 
#  ee.Image.register
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Registers an image to a reference image while allowing local, rubber sheet deformations. Displacements are computed in the CRS of the reference image, at a scale dictated by the lowest resolution of the following three projections: input image projection, reference image projection, and requested projection. The displacements then applied to the input image to register it with the reference. 
Usage| Returns  
---|---  
`Image.register(referenceImage, maxOffset,  _patchWidth_, _stiffness_)`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The image to register.  
`referenceImage`| Image| The image to register to.  
`maxOffset`| Float| The maximum offset allowed when attempting to align the input images, in meters. Using a smaller value can reduce computation time significantly, but it must still be large enough to cover the greatest displacement within the entire image region.  
`patchWidth`| Float, default: null| Patch size for detecting image offsets, in meters. This should be set large enough to capture texture, as well as large enough that ignorable objects are small within the patch. Default is null. Patch size will be determined automatically if notprovided.  
`stiffness`| Float, default: 5| Enforces a stiffness constraint on the solution. Valid values are in the range [0,10]. The stiffness is used for outlier rejection when determining displacements at adjacent grid points. Higher values move the solution towards a rigid transformation. Lower values allow more distortion or warping of the image during registration.  
