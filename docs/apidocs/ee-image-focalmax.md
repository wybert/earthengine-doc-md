 
#  ee.Image.focalMax 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Applies a morphological reducer() filter to each band of an image using a named or custom kernel. 
Usage| Returns  
---|---  
`Image.focalMax( _radius_, _kernelType_, _units_, _iterations_, _kernel_)`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The image to which to apply the operations.  
`radius`| Float, default: 1.5| The radius of the kernel to use.  
`kernelType`| String, default: "circle"| The type of kernel to use. Options include: 'circle', 'square', 'cross', 'plus', 'octagon', and 'diamond'.  
`units`| String, default: "pixels"| If a kernel is not specified, this determines whether the kernel is in meters or pixels.  
`iterations`| Integer, default: 1| The number of times to apply the given kernel.  
`kernel`| Kernel, default: null| A custom kernel. If used, kernelType and radius are ignored.  
