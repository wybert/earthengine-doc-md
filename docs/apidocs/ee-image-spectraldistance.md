 
#  ee.Image.spectralDistance
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Computes the per-pixel spectral distance between two images. If the images are array based then only the first band of each image is used; otherwise all bands are involved in the distance computation. The two images are therefore expected to contain the same number of bands or have the same 1-dimensional array length. 
Usage| Returns  
---|---  
`Image.spectralDistance(image2,  _metric_)`| Image  
Argument| Type| Details  
---|---|---  
this: `image1`| Image| The first image.  
`image2`| Image| The second image.  
`metric`| String, default: "sam"| The spectral distance metric to use. One of 'sam' (spectral angle mapper), 'sid' (spectral information divergence), 'sed' (squared Euclidean distance), or 'emd' (earth movers distance).  
Was this helpful?
