 
#  ee.Image.spectralGradient
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Computes the spectral gradient over all bands of an image (or the first band if the image is Array typed) by computing the per-pixel difference between the spectral erosion and dilation with a given structuring kernel and distance metric. See: Plaza, Antonio, et al. 'Spatial/spectral endmember extraction by multidimensional morphological operations.' IEEE transactions on geoscience and remote sensing 40.9 (2002): 2025-2041. 
Usage| Returns  
---|---  
`Image.spectralGradient( _metric_, _kernel_, _useCentroid_)`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The input image.  
`metric`| String, default: "sam"| The spectral distance metric to use. One of 'sam' (spectral angle mapper), 'sid' (spectral information divergence), 'sed' (squared Euclidean distance), or 'emd' (earth movers distance).  
`kernel`| Kernel, default: null| Connectedness kernel. Defaults to a square of radius 1 (8-way connected).  
`useCentroid`| Boolean, default: false| If true, distances are computed from the mean of all pixels under the kernel instead of the kernel's center pixel.  
Was this helpful?
