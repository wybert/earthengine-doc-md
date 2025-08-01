 
#  ee.Image.directionalDistanceTransform
Stay organized with collections  Save and categorize content based on your preferences. 
For each zero-valued pixel in the source, get the distance to the nearest non-zero pixels in the given direction.
Returns a band of floating point distances called "distance".
Usage | Returns  
---|---  
`Image.directionalDistanceTransform(angle, maxDistance, _labelBand_)`|  Image  
Argument | Type | Details  
---|---|---  
this: `source` | Image | The source image.  
`angle` | Float | The angle, in degrees, at which to search for non-zero pixels.  
`maxDistance` | Integer | The maximum distance, in pixels, over which to search.  
`labelBand` | String, default: null | If provided, multi-band inputs are permitted and only this band is used for searching. All other bands are returned and populated with the per-band values found at the searched non-zero pixels in the label band.  
