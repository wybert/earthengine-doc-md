 
#  ee.Image.resample 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
An algorithm that returns an image identical to its argument, but which uses bilinear or bicubic interpolation (rather than the default nearest-neighbor) to compute pixels in projections other than its native projection or other levels of the same image pyramid. 
This relies on the input image's default projection being meaningful, and so cannot be used on composites, for example. (Instead, you should resample the images that are used to create the composite.)
Usage| Returns  
---|---  
`Image.resample( _mode_)`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The Image to resample.  
`mode`| String, default: "bilinear"| The interpolation mode to use. One of 'bilinear' or 'bicubic'.  
