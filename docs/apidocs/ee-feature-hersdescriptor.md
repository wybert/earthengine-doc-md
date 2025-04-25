 
#  ee.Feature.hersDescriptor 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Creates a dictionary of Histogram Error Ring Statistic (HERS) descriptor arrays from square array properties of an element. The HERS radius is taken to be the array's (side_length - 1) / 2. 
Usage| Returns  
---|---  
`Feature.hersDescriptor( _selectors_, _buckets_, _peakWidthScale_)`| Dictionary  
Argument| Type| Details  
---|---|---  
this: `element`| Element| The element with array properties.  
`selectors`| List, default: null| The array properties for which descriptors will be created. Selected array properties must be square, floating point arrays. Defaults to all array properties.  
`buckets`| Integer, default: 100| The number of HERS buckets. Defaults to 100.  
`peakWidthScale`| Float, default: 1| The HERS peak width scale. Defaults to 1.0.  
Was this helpful?
