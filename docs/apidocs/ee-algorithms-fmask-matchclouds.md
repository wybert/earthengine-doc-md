 
#  ee.Algorithms.FMask.matchClouds 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Runs the FMask cloud and shadow matching. Outputs a single band ('csm'), containing the computed cloud and shadow masks. 
Usage| Returns  
---|---  
`ee.Algorithms.FMask.matchClouds(input, cloud, shadow, btemp, sceneLow, sceneHigh,  _neighborhood_)`| Image  
Argument| Type| Details  
---|---|---  
`input`| Image| The scene for which to compute cloud and shadow masks.  
`cloud`| Image| Potential cloud mask image. Expected to contain 1s for cloudy pixels and masked pixels everywhere else.  
`shadow`| Image| Potential shadow mask image. Expected to contain 1s for shadow pixels and masked pixels everywhere else.  
`btemp`| Image| Brightness temperature image, in Celsius.  
`sceneLow`| Float| The 0.175 percentile brightness temperature of the scene.  
`sceneHigh`| Float| The 0.825 percentile brightness temperature of the scene.  
`neighborhood`| Integer, default: 50| The neighborhood to pad around each tile.  
Was this helpful?
