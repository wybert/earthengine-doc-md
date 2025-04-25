 
#  ee.ImageCollection.reduce 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Applies a reducer across all of the images in a collection. 
If the reducer has a single input, it will be applied separately to each band of the collection; otherwise it must have the same number of inputs as the collection has bands.
The reducer output names determine the names of the output bands: reducers with multiple inputs will use the output names directly, while reducers with a single input will prefix the output name with the input band name (e.g., '10_mean', '20_mean').
Usage| Returns  
---|---  
`ImageCollection.reduce(reducer,  _parallelScale_)`| Image  
Argument| Type| Details  
---|---|---  
this: `collection`| ImageCollection| The image collection to reduce.  
`reducer`| Reducer| The reducer to apply to the given collection.  
`parallelScale`| Float, default: 1| A scaling factor used to limit memory use; using a larger parallelScale (e.g., 2 or 4) may enable computations that run out of memory with the default.  
