 
#  ee.Image.connectedPixelCount 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Generate an image where each pixel contains the number of 4- or 8-connected neighbors (including itself). 
Usage| Returns  
---|---  
`Image.connectedPixelCount( _maxSize_, _eightConnected_)`| Image  
Argument| Type| Details  
---|---|---  
this: `input`| Image| The input image.  
`maxSize`| Integer, default: 100| The maximum size of the neighborhood in pixels.  
`eightConnected`| Boolean, default: true| Whether to use 8-connected rather 4-connected rules.  
