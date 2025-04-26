 
#  ee.Array.reshape 
Stay organized with collections  Save and categorize content based on your preferences. 
Reshapes an array to a new list of dimension lengths. Usage| Returns  
---|---  
`Array.reshape(shape)`| Array  
Argument| Type| Details  
---|---|---  
this: `array`| Array| Array to reshape.  
`shape`| Array| New shape to which arrays are converted. If one component of the shape is the special value -1, the size of that dimension is computed so that the total size remains constant. In particular, a shape of [-1] flattens into 1-D. At most one component of shape can be -1.  
