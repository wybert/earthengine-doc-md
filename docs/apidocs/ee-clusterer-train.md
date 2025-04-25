 
#  ee.Clusterer.train 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Trains the Clusterer on a collection of features using the specified numeric properties of each feature as training data. The geometry of the features is ignored. 
Usage| Returns  
---|---  
`Clusterer.train(features,  _inputProperties_, _subsampling_, _subsamplingSeed_)`| Clusterer  
Argument| Type| Details  
---|---|---  
this: `clusterer`| Clusterer| An input Clusterer.  
`features`| FeatureCollection| The collection to train on.  
`inputProperties`| List, default: null| The list of property names to include as training data. Each feature must have all these properties, and their values must be numeric. This argument is optional if the input collection contains a 'band_order' property (as produced by Image.sample).  
`subsampling`| Float, default: 1| An optional subsampling factor, within (0, 1].  
`subsamplingSeed`| Integer, default: 0| A randomization seed to use for subsampling.  
Was this helpful?
