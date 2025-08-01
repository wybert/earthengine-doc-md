 
#  ee.Image.entropy
Stay organized with collections  Save and categorize content based on your preferences. 
Computes the windowed entropy for each band using the specified kernel centered on each input pixel. Entropy is computed as -sum(p * log2(p)), where p is the normalized probability of occurrence of the values encountered in each window. Usage | Returns  
---|---  
`Image.entropy(kernel)` | Image  
Argument | Type | Details  
---|---|---  
this: `image` | Image | The image for which to compute the entropy.  
`kernel` | Kernel | A kernel specifying the window in which to compute.  
