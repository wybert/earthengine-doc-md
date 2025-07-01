 
#  ee.Clusterer.wekaCobweb
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Implementation of the Cobweb clustering algorithm. For more information see: 
D. Fisher (1987). Knowledge acquisition via incremental conceptual clustering. Machine Learning. 2(2):139-172. and J. H. Gennari, P. Langley, D. Fisher (1990). Models of incremental concept formation. Artificial Intelligence. 40:11-61.
Usage| Returns  
---|---  
`ee.Clusterer.wekaCobweb( _acuity_, _cutoff_, _seed_)`| Clusterer  
Argument| Type| Details  
---|---|---  
`acuity`| Float, default: 1| Acuity (minimum standard deviation).  
`cutoff`| Float, default: 0.002| Cutoff (minimum category utility).  
`seed`| Integer, default: 42| Random number seed.  
Was this helpful?
