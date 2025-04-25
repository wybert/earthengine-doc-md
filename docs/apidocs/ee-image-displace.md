 
#  ee.Image.displace 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Warps an image using an image of displacements. 
Usage| Returns  
---|---  
`Image.displace(displacement,  _mode_, _maxOffset_)`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The image to warp.  
`displacement`| Image| An image containing displacement values. The first band is interpreted as the 'X' displacement and the second as the 'Y' displacement. Each displacement pixel is a [dx,dy] vector added to the pixel location to determine the corresponding pixel location in 'image'. Displacements are interpreted as meters in the default projection of the displacement image.  
`mode`| String, default: "bicubic"| The interpolation mode to use. One of 'nearest_neighbor', 'bilinear', or 'bicubic'.  
`maxOffset`| Float, default: null| The maximum absolute offset in the displacement image. Providing this may improve processing performance.  
