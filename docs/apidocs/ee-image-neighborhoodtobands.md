 
#  ee.Image.neighborhoodToBands 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Turns the neighborhood of a pixel into a set of bands. The neighborhood is specified using a Kernel and only non-zero-weight kernel values are used. The weights of the kernel is otherwise ignored. 
Each input band produces x * y output bands. Each output band is named 'input_x_y' where x and y indicate the pixel's location in the kernel. For example, a 3x3 kernel operating on a 2-band image produces 18 output bands.
Usage| Returns  
---|---  
`Image.neighborhoodToBands(kernel)`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The image to get pixels from.  
`kernel`| Kernel| The kernel specifying the neighborhood. Zero-weight values are ignored.  
Was this helpful?
