 
#  ee.Image.slice
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Selects a contiguous group of bands from an image by position. 
Usage| Returns  
---|---  
`Image.slice(start,  _end_)`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The image from which to select bands.  
`start`| Integer| Where to start the selection. Negative numbers select from the end, counting backwards.  
`end`| Integer, default: null| Where to end the selection. If omitted, selects all bands from the start position to the end.  
