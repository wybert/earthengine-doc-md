 
#  ee.Clusterer.wekaKMeans 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Cluster data using the k-means algorithm. Can use either the Euclidean distance (default) or the Manhattan distance. If the Manhattan distance is used, then centroids are computed as the component-wise median rather than mean. For more information see: 
D. Arthur, S. Vassilvitskii: k-means++: the advantages of careful seeding. In: Proceedings of the eighteenth annual ACM-SIAM symposium on Discrete algorithms, 1027-1035, 2007.
Usage| Returns  
---|---  
`ee.Clusterer.wekaKMeans(nClusters,  _init_, _canopies_, _maxCandidates_, _periodicPruning_, _minDensity_, _t1_, _t2_, _distanceFunction_, _maxIterations_, _preserveOrder_, _fast_, _seed_)`| Clusterer  
Argument| Type| Details  
---|---|---  
`nClusters`| Integer| Number of clusters.  
`init`| Integer, default: 0| Initialization method to use. 0 = random, 1 = k-means++, 2 = canopy, 3 = farthest first.  
`canopies`| Boolean, default: false| Use canopies to reduce the number of distance calculations.  
`maxCandidates`| Integer, default: 100| Maximum number of candidate canopies to retain in memory at any one time when using canopy clustering. T2 distance plus, data characteristics, will determine how many candidate canopies are formed before periodic and final pruning are performed, which might result in exceess memory consumption. This setting avoids large numbers of candidate canopies consuming memory.  
`periodicPruning`| Integer, default: 10000| How often to prune low density canopies when using canopy clustering.  
`minDensity`| Integer, default: 2| Minimum canopy density, when using canopy clustering, below which a canopy will be pruned during periodic pruning.  
`t1`| Float, default: -1.5| The T1 distance to use when using canopy clustering. A value < 0 is taken as a positive multiplier for T2.  
`t2`| Float, default: -1| The T2 distance to use when using canopy clustering. Values < 0 cause a heuristic based on attribute std. deviation to be used.  
`distanceFunction`| String, default: "Euclidean"| Distance function to use. Options are: Euclidean and Manhattan.  
`maxIterations`| Integer, default: null| Maximum number of iterations.  
`preserveOrder`| Boolean, default: false| Preserve order of instances.  
`fast`| Boolean, default: false| Enables faster distance calculations, using cut-off values. Disables the calculation/output of squared errors/distances.  
`seed`| Integer, default: 10| The randomization seed.  
