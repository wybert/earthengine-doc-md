 
#  ee.Image.rsedTransform 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Reverse Squared Euclidean Distance (RSED) computes the 2D maximal height surface created by placing an inverted parabola over each non-zero pixel of the input image, where the pixel's value is the height of the parabola. Viewed as a binary image (zero/not-zero) this is equivalent to buffering each non-zero input pixel by the square root of its value, in pixels. 
Usage| Returns  
---|---  
`Image.rsedTransform( _neighborhood_, _units_)`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The input image.  
`neighborhood`| Integer, default: 256| Neighborhood size in pixels.  
`units`| String, default: "pixels"| The units of the neighborhood, currently only 'pixels' are supported.  
Was this helpful?
