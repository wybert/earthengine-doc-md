 
#  ee.Image.unmix 
Stay organized with collections  Save and categorize content based on your preferences. 
Unmix each pixel with the given endmembers, by computing the pseudo-inverse and multiplying it through each pixel. Returns an image of doubles with the same number of bands as endmembers. Usage| Returns  
---|---  
`Image.unmix(endmembers,  _sumToOne_, _nonNegative_)`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The input image.  
`endmembers`| List| The endmembers to unmix with.  
`sumToOne`| Boolean, default: false| Constrain the outputs to sum to one.  
`nonNegative`| Boolean, default: false| Constrain the outputs to be non-negative.  
