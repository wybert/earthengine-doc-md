 
#  ee.Algorithms.HoughTransform 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Applies the Hough transform to an image. For every input band, outputs a band where lines are detected by thresholding the Hough transform with a value of lineThreshold. The output band is named [input]_lines, where [input] is the name of the original band. The defaults provided for the parameters are intended as a starting point for use with UINT8 images. 
Usage| Returns  
---|---  
`ee.Algorithms.HoughTransform(image,  _gridSize_, _inputThreshold_, _lineThreshold_, _smooth_)`| Image  
Argument| Type| Details  
---|---|---  
`image`| Image| The image to which to apply the transform.  
`gridSize`| Integer, default: 256| The size of the grid over which to perform the computation.  
`inputThreshold`| Float, default: 64| Value threshold for input image. Pixels equal to or above this value are considered active.  
`lineThreshold`| Float, default: 72| Threshold for line detection. Values equal to or above this threshold on the Hough transform are considered to be detected lines.  
`smooth`| Boolean, default: true| Whether to smooth the Hough transform before line detection.  
