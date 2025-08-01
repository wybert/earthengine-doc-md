 
#  ee.Image.cast
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Casts some or all bands of an image to the specified types.
Usage | Returns  
---|---  
`Image.cast(bandTypes, _bandOrder_)`|  Image  
Argument | Type | Details  
---|---|---  
this: `image` | Image | The image to cast.  
`bandTypes` | Dictionary | A dictionary from band name to band types. Types can be PixelTypes or strings. The valid strings are: 'int8', 'int16', 'int32', 'int64', 'uint8', 'uint16', 'uint32', 'byte', 'short', 'int', 'long', 'float', and 'double'. If bandTypes includes bands that are not already in the input image, they will be added to the image as transparent bands. If bandOrder isn't also specified, new bands will be appended in alphabetical order.  
`bandOrder` | List, default: null | A list specifying the order of the bands in the result. If specified, must match the full list of bands in the result.  
