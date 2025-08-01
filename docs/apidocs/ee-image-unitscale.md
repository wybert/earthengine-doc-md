 
#  ee.Image.unitScale
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Scales the input so that the range of input values [low, high] becomes [0, 1]. Values outside the range are NOT clamped. This algorithm always produces floating point pixels.
Usage | Returns  
---|---  
`Image.unitScale(low, high)` | Image  
Argument | Type | Details  
---|---|---  
this: `input` | Image | The image to scale.  
`low` | Float | The value mapped to 0.  
`high` | Float | The value mapped to 1.  
