 
#  ee.Image.cat 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Combines the given images into a single image which contains all bands from all of the images. 
If two or more bands share a name, they are suffixed with an incrementing index.
The resulting image will have the metadata from the first input image, only.
This function will promote constant values into constant images.
Returns the combined image.
Usage| Returns  
---|---  
`ee.Image.cat(var_args)`| Image  
Argument| Type| Details  
---|---|---  
`var_args`| VarArgs| The images to be combined.  
Was this helpful?
