 
#  ee.Algorithms.Terrain 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Calculates slope, aspect, and a simple hillshade from a terrain DEM. 
Expects an image containing either a single band of elevation, measured in meters, or if there's more than one band, one named 'elevation'. Adds output bands named 'slope' and 'aspect' measured in degrees plus an unsigned byte output band named 'hillshade' for visualization. All other bands and metadata are copied from the input image. The local gradient is computed using the 4-connected neighbors of each pixel, so missing values will occur around the edges of an image.
Usage| Returns  
---|---  
`ee.Algorithms.Terrain(input)`| Image  
Argument| Type| Details  
---|---|---  
`input`| Image| An elevation image, in meters.  
