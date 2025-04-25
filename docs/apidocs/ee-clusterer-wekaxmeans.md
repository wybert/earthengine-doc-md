 
#  ee.Clusterer.wekaXMeans 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
X-Means is K-Means with an efficient estimation of the number of clusters. For more information see: 
Dan Pelleg, Andrew W. Moore: X-means: Extending K-means with Efficient Estimation of the Number of Clusters. In: Seventeenth International Conference on Machine Learning, 727-734, 2000.
Usage| Returns  
---|---  
`ee.Clusterer.wekaXMeans( _minClusters_, _maxClusters_, _maxIterations_, _maxKMeans_, _maxForChildren_, _useKD_, _cutoffFactor_, _distanceFunction_, _seed_)`| Clusterer  
Argument| Type| Details  
---|---|---  
`minClusters`| Integer, default: 2| Minimum number of clusters.  
`maxClusters`| Integer, default: 8| Maximum number of clusters.  
`maxIterations`| Integer, default: 3| Maximum number of overall iterations.  
`maxKMeans`| Integer, default: 1000| The maximum number of iterations to perform in KMeans.  
`maxForChildren`| Integer, default: 1000| The maximum number of iterations in KMeans that is performed on the child centers.  
`useKD`| Boolean, default: false| Use a KDTree.  
`cutoffFactor`| Float, default: 0| Takes the given percentage of the split centroids if none of the children win.  
`distanceFunction`| String, default: "Euclidean"| Distance function to use. Options are: Chebyshev, Euclidean, and Manhattan.  
`seed`| Integer, default: 10| The randomization seed.  
