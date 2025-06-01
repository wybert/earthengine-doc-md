 
#  ee.ImageCollection.cast 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Casts some or all bands of each image in an ImageCollection to the specified types. 
Usage| Returns  
---|---  
`ImageCollection.cast(bandTypes, bandOrder)`| ImageCollection  
Argument| Type| Details  
---|---|---  
this: `collection`| ImageCollection| The image collection to cast.  
`bandTypes`| Dictionary| A dictionary from band name to band types. Types can be PixelTypes or strings. The valid strings are: 'int8', 'int16', 'int32', 'int64', 'uint8', 'uint16', 'uint32', 'byte', 'short', 'int', 'long', 'float', and 'double'. Must include all bands already in any image in the collection. If this includes bands that are not already in an input image, they will be added to the image as transparent bands.  
`bandOrder`| List| A list specifying the order of the bands in the result. Must match the keys of bandTypes.  
