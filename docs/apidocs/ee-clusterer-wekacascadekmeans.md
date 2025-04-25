 
#  ee.Clusterer.wekaCascadeKMeans 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Cascade simple k-means selects the best k according to the Calinski-Harabasz criterion. For more information see: 
Calinski, T. and J. Harabasz. 1974. A dendrite method for cluster analysis. Commun. Stat. 3: 1-27.
Usage| Returns  
---|---  
`ee.Clusterer.wekaCascadeKMeans( _minClusters_, _maxClusters_, _restarts_, _manual_, _init_, _distanceFunction_, _maxIterations_)`| Clusterer  
Argument| Type| Details  
---|---|---  
`minClusters`| Integer, default: 2| Min number of clusters.  
`maxClusters`| Integer, default: 10| Max number of clusters.  
`restarts`| Integer, default: 10| Number of restarts.  
`manual`| Boolean, default: false| Manually select the number of clusters.  
`init`| Boolean, default: false| Set whether to initialize using the probabilistic farthest first like method of the k-means++ algorithm (rather than the standard random selection of initial cluster centers).  
`distanceFunction`| String, default: "Euclidean"| Distance function to use. Options are: Euclidean and Manhattan.  
`maxIterations`| Integer, default: null| Maximum number of iterations for k-means.  
Was this helpful?
