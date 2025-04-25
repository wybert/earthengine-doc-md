 
#  ee.Classifier.spectralRegion 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Creates a classifier that tests if its inputs lie within a polygon defined by a set of coordinates in an arbitrary 2D coordinate system. Each input to be classified must have 2 values (e.g., images must have 2 bands). The result will be 1 wherever the input values are contained within the given polygon and 0 otherwise. 
Usage| Returns  
---|---  
`ee.Classifier.spectralRegion(coordinates,  _schema_)`| Classifier  
Argument| Type| Details  
---|---|---  
`coordinates`| List| The coordinates of the polygon, as a list of rings. Each ring is a list of coordinate pairs (e.g., [u1, v1, u2, v2, ..., uN, vN]). No edge may intersect any other edge. The resulting classification will be a 1 wherever the input values are within the interior of the given polygon, that is, an odd number of polygon edges must be crossed to get outside the polygon and 0 otherwise.  
`schema`| List, default: null| The classifier's schema. A list of band or property names that the classifier will operate on. Since this classifier doesn't undergo a training step, these have to be specified manually. Defaults to ['u', 'v'].  
Was this helpful?
