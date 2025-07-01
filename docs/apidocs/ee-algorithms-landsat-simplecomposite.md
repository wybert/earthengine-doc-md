 
#  ee.Algorithms.Landsat.simpleComposite
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Computes a Landsat TOA composite from a collection of raw Landsat scenes. It applies standard TOA calibration and then assigns a cloud score to each pixel using the SimpleLandsatCloudScore algorithm. It selects the lowest possible range of cloud scores at each point and then computes per-band percentile values from the accepted pixels. This algorithm also uses the LandsatPathRowLimit algorithm to select only the least-cloudy scenes in regions where more than maxDepth input scenes are available. 
Usage| Returns  
---|---  
`ee.Algorithms.Landsat.simpleComposite(collection,  _percentile_, _cloudScoreRange_, _maxDepth_, _asFloat_)`| Image  
Argument| Type| Details  
---|---|---  
`collection`| ImageCollection| The raw Landsat ImageCollection to composite.  
`percentile`| Integer, default: 50| The percentile value to use when compositing each band.  
`cloudScoreRange`| Integer, default: 10| The size of the range of cloud scores to accept per pixel.  
`maxDepth`| Integer, default: 40| An approximate limit on the maximum number of scenes used to compute each pixel.  
`asFloat`| Boolean, default: false| If true, output bands are in the same units as the Landsat.TOA algorithm; if false, TOA values are converted to uint8 by multiplying by 255 (reflective bands) or subtracting 100 (thermal bands) and rounding to the nearest integer.  
