 
#  ee.Image.fastDistanceTransform 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Returns the distance, as determined by the specified distance metric, to the nearest non-zero valued pixel in the input. The output contains values for all pixels within the given neighborhood size, regardless of the input's mask. Note: the default distance metric returns squared distance. 
Usage| Returns  
---|---  
`Image.fastDistanceTransform( _neighborhood_, _units_, _metric_)`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The input image.  
`neighborhood`| Integer, default: 256| Neighborhood size in pixels.  
`units`| String, default: "pixels"| The units of the neighborhood, currently only 'pixels' are supported.  
`metric`| String, default: "squared_euclidean"| Distance metric to use: options are `squared_euclidean`, `manhattan` or `chebyshev`.  
