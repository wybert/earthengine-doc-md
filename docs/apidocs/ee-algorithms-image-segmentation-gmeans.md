 
#  ee.Algorithms.Image.Segmentation.GMeans 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Performs G-Means clustering on the input image. Iteratively applies k-means followed by a normality test to automatically determine the number of clusters to use. The output contains a 'clusters' band containing the integer ID of the cluster that each pixel belongs to. The algorithm can work either on a fixed grid of non-overlapping cells (gridSize, which can be smaller than a tile) or on tiles with overlap (neighborhoodSize). The default is to use tiles with no overlap. Clusters in one cell or tile are unrelated to clusters in another. Any cluster that spans a cell or tile boundary may receive two different labels in the two halves. Any input pixels with partial masks are fully masked in the output. This algorithm is only expected to perform well for images with a narrow dynamic range (i.e., bytes or shorts). 
See: G. Hamerly and C. Elkan. 'Learning the k in k-means'. NIPS, 2003.
Usage| Returns  
---|---  
`ee.Algorithms.Image.Segmentation.GMeans(image,  _numIterations_, _pValue_, _neighborhoodSize_, _gridSize_, _uniqueLabels_)`| Image  
Argument| Type| Details  
---|---|---  
`image`| Image| The input image for clustering.  
`numIterations`| Integer, default: 10| Number of iterations. Default 10.  
`pValue`| Float, default: 50| Significance level for normality test.  
`neighborhoodSize`| Integer, default: 0| Neighborhood size. The amount to extend each tile (overlap) when computing the clusters. This option is mutually exclusive with gridSize.  
`gridSize`| Integer, default: null| Grid cell-size. If greater than 0, kMeans will be run independently on cells of this size. This has the effect of limiting the size of any cluster to be gridSize or smaller. This option is mutually exclusive with neighborhoodSize.  
`uniqueLabels`| Boolean, default: true| If true, clusters are assigned unique IDs. Otherwise, they repeat per tile or grid cell.  
