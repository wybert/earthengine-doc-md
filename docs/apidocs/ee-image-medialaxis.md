 
#  ee.Image.medialAxis 
Stay organized with collections  Save and categorize content based on your preferences. 
Computes the discrete medial axis of the zero valued pixels of the first band of the input. Outputs 4 bands: 
medial - the medial axis points, scaled by the distance.
coverage - the number of points supporting each medial axis point.
xlabel - the horizontal distance to the power point for each pixel.
ylabel - the vertical distance to the power point for each pixel.
Usage| Returns  
---|---  
`Image.medialAxis( _neighborhood_, _units_)`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The input image.  
`neighborhood`| Integer, default: 256| Neighborhood size in pixels.  
`units`| String, default: "pixels"| The units of the neighborhood, currently only 'pixels' are supported.  
