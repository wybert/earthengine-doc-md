 
#  ee.Image.cluster 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Applies a clusterer to an image. Returns a new image with a single band containing values from 0 to N, indicating the cluster each pixel is assigned to. 
Usage| Returns  
---|---  
`Image.cluster(clusterer,  _outputName_)`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The image to cluster. Must contain all the bands in the clusterer's schema.  
`clusterer`| Clusterer| The clusterer to use.  
`outputName`| String, default: "cluster"| The name of the output band.  
Was this helpful?
