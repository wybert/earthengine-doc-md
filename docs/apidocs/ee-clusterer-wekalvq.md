 
#  ee.Clusterer.wekaLVQ
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
A Clusterer that implements the Learning Vector Quantization algorithm. For more details, see: 
T. Kohonen, "Learning Vector Quantization", The Handbook of Brain Theory and Neural Networks, 2nd Edition, MIT Press, 2003, pp. 631-634.
Usage| Returns  
---|---  
`ee.Clusterer.wekaLVQ( _numClusters_, _learningRate_, _epochs_, _normalizeInput_)`| Clusterer  
Argument| Type| Details  
---|---|---  
`numClusters`| Integer, default: 7| The number of clusters.  
`learningRate`| Float, default: 1| The learning rate for the training algorithm. Value should be greater than 0 and less or equal to 1.  
`epochs`| Integer, default: 1000| Number of training epochs. Value should be greater than or equal to 1.  
`normalizeInput`| Boolean, default: false| Skip normalizing the attributes.  
Was this helpful?
