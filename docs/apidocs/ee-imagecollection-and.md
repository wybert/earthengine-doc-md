 
#  ee.ImageCollection.and 
Stay organized with collections  Save and categorize content based on your preferences. 
Reduces an image collection by setting each pixel to 1 if and only if all the non-masked values at that pixel are non-zero across the stack of all matching bands. Bands are matched by name. Usage| Returns  
---|---  
`ImageCollection.and()`| Image  
Argument| Type| Details  
---|---|---  
this: `collection`| ImageCollection| The image collection to reduce.  
