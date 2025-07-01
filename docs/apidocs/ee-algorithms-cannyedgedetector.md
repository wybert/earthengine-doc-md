 
#  ee.Algorithms.CannyEdgeDetector
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Applies the Canny edge detection algorithm to an image. The output is an image whose bands have the same names as the input bands, and in which non-zero values indicate edges, and the magnitude of the value is the gradient magnitude. 
Usage| Returns  
---|---  
`ee.Algorithms.CannyEdgeDetector(image, threshold,  _sigma_)`| Image  
Argument| Type| Details  
---|---|---  
`image`| Image| The image on which to apply edge detection.  
`threshold`| Float| Threshold value. The pixel is only considered for edge detection if the gradient magnitude is higher than this threshold.  
`sigma`| Float, default: 1| Sigma value for a gaussian filter applied before edge detection. 0 means apply no filtering.  
Was this helpful?
