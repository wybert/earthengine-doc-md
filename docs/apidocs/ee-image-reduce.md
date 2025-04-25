 
#  ee.Image.reduce 
Stay organized with collections  Save and categorize content based on your preferences. 
Applies a reducer to all of the bands of an image. 
The reducer must have a single input and will be called at each pixel to reduce the stack of band values.
The output image will have one band for each reducer output.
Usage| Returns  
---|---  
`Image.reduce(reducer)`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The image to reduce.  
`reducer`| Reducer| The reducer to apply to the given image.  
