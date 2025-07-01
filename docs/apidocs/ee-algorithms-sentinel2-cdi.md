 
#  ee.Algorithms.Sentinel2.CDI
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Computes the Cloud Displacement Index (CDI) from a Sentinel-2 Level 1C image. CDI is a measure of the optical separation in elevated objects due to sensor parallax. Returns a floating point band named "cdi". 
See Frantz, D., Hass, E., Uhl, A., Stoffels, J., & Hill, J. (2018). Improvement of the Fmask algorithm for Sentinel-2 images: Separating clouds from bright surfaces based on parallax effects. Remote sensing of environment, 215, 471-481.
Usage| Returns  
---|---  
`ee.Algorithms.Sentinel2.CDI(source)`| Image  
Argument| Type| Details  
---|---|---  
`source`| Image| The source image.  
Was this helpful?
