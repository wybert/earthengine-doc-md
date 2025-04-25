 
#  ee.Algorithms.Image.Segmentation.KMeans 
Stay organized with collections  Save and categorize content based on your preferences. 
Performs K-Means clustering on the input image. Outputs a 1-band image containing the ID of the cluster that each pixel belongs to. The algorithm can work either on a fixed grid of non-overlapping cells (gridSize, which can be smaller than a tile) or on tiles with overlap (neighborhoodSize). The default is to use tiles with no overlap. Clusters in one cell or tile are unrelated to clusters in another. Any cluster that spans a cell or tile boundary may receive two different labels in the two halves. Any input pixels with partial masks are fully masked in the output. Usage| Returns  
---|---  
`ee.Algorithms.Image.Segmentation.KMeans(image,  _numClusters_, _numIterations_, _neighborhoodSize_, _gridSize_, _forceConvergence_, _uniqueLabels_)`| Image  
Argument| Type| Details  
---|---|---  
`image`| Image| The input image for clustering.  
`numClusters`| Integer, default: 8| Number of clusters.  
`numIterations`| Integer, default: 20| Number of iterations.  
`neighborhoodSize`| Integer, default: 0| Neighborhood size. The amount to extend each tile (overlap) when computing the clusters. This option is mutually exclusive with gridSize.  
`gridSize`| Integer, default: null| Grid cell-size. If greater than 0, kMeans will be run independently on cells of this size. This has the effect of limiting the size of any cluster to be gridSize or smaller. This option is mutually exclusive with neighborhoodSize.  
`forceConvergence`| Boolean, default: false| If true, an error is thrown if convergence is not achieved before numIterations.  
`uniqueLabels`| Boolean, default: true| If true, clusters are assigned unique IDs. Otherwise, they repeat per tile or grid cell.  
