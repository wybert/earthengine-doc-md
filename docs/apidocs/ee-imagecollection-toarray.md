 
#  ee.ImageCollection.toArray 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Converts an image collection into an image of 2D arrays. At each pixel, the images that have valid (unmasked) values in all bands are laid out along the first axis of the array in the order they appear in the image collection. The bands of each image are laid out along the second axis of the array, in the order the bands appear in that image. The array element type will be the union of the types of each band. 
Usage| Returns  
---|---  
`ImageCollection.toArray()`| Image  
Argument| Type| Details  
---|---|---  
this: `collection`| ImageCollection| Image collection to convert to an array image. Bands must have scalar values, not array values.  
