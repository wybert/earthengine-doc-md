 
#  ee.Algorithms.Landsat.simpleCloudScore
Stay organized with collections  Save and categorize content based on your preferences. 
Computes a simple cloud-likelihood score in the range [0,100] using a combination of brightness, temperature, and NDSI. This is not a robust cloud detector, and is intended mainly to compare multiple looks at the same point for _relative_ cloud likelihood. Usage | Returns  
---|---  
`ee.Algorithms.Landsat.simpleCloudScore(image)` | Image  
Argument | Type | Details  
---|---|---  
`image` | Image | The Landsat TOA image to process.  
