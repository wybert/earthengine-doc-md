 
#  ee.Image.spectralErosion 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Computes the spectral/spatial erosion of an image by computing the spectral distance of each pixel under a structuring kernel from the centroid of all pixels under the kernel and taking the closest result. See 'Spatial/spectral endmember extraction by multidimensional morphological operations.' IEEE transactions on geoscience and remote sensing 40.9 (2002): 2025-2041. 
Usage| Returns  
---|---  
`Image.spectralErosion( _metric_, _kernel_, _useCentroid_)`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The input image.  
`metric`| String, default: "sam"| The spectral distance metric to use. One of 'sam' (spectral angle mapper), 'sid' (spectral information divergence), 'sed' (squared Euclidean distance), or 'emd' (earth movers distance).  
`kernel`| Kernel, default: null| Connectedness kernel. Defaults to a square of radius 1 (8-way connected).  
`useCentroid`| Boolean, default: false| If true, distances are computed from the mean of all pixels under the kernel instead of the kernel's center pixel.  
Was this helpful?
