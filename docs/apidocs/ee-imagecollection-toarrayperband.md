 
#  ee.ImageCollection.toArrayPerBand
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Concatenates multiple images into a single array image. The result will be masked if any input is masked.
Usage | Returns  
---|---  
`ImageCollection.toArrayPerBand(_axis_)`|  Image  
Argument | Type | Details  
---|---|---  
this: `collection` | ImageCollection | Images to concatenate. A separate concatenation is done per band, so all the images must have the same dimensionality and shape per band, except length along the concatenation axis.  
`axis` | Integer, default: 0 | Axis to concatenate along; must be at least 0 and at most the minimum dimension of any band in the collection.  
Was this helpful?
