 
#  ee.Image.eq
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Returns 1 if and only if the first value is equal to the second for each matched pair of bands in image1 and image2. If either image1 or image2 has only 1 band, then it is used against all the bands in the other image. If the images have the same number of bands, but not the same names, they're used pairwise in the natural order. The output bands are named for the longer of the two inputs, or if they're equal in length, in image1's order. The type of the output pixels is boolean. 
Usage| Returns  
---|---  
`Image.eq(image2)`| Image  
Argument| Type| Details  
---|---|---  
this: `image1`| Image| The image from which the left operand bands are taken.  
`image2`| Image| The image from which the right operand bands are taken.  
Was this helpful?
