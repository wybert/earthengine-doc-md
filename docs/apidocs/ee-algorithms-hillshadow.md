 
#  ee.Algorithms.HillShadow 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Creates a shadow band, with output 1 where pixels are illumunated and 0 where they are shadowed. Takes as input an elevation band, azimuth and zenith of the light source in degrees, a neighborhood size, and whether or not to apply hysteresis when a shadow appears. Currently, this algorithm only works for Mercator projections, in which light rays are parallel. 
Usage| Returns  
---|---  
`ee.Algorithms.HillShadow(image, azimuth, zenith,  _neighborhoodSize_, _hysteresis_)`| Image  
Argument| Type| Details  
---|---|---  
`image`| Image| The image to which to apply the shadow algorithm, in which each pixel should represent an elevation in meters.  
`azimuth`| Float| Azimuth in degrees.  
`zenith`| Float| Zenith in degrees.  
`neighborhoodSize`| Integer, default: 0| Neighborhood size.  
`hysteresis`| Boolean, default: false| Use hysteresis. Less physically accurate, but may generate better images.  
