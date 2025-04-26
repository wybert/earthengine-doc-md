 
#  ee.Reducer.fixedHistogram 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Creates a reducer that will compute a histogram of the inputs using a fixed number of fixed width bins. Values outside of the [min, max) range are ignored. The output is a Nx2 array of bucket lower edges and counts (or cumulative counts) and is suitable for use per-pixel. 
Usage| Returns  
---|---  
`ee.Reducer.fixedHistogram(min, max, steps,  _cumulative_)`| Reducer  
Argument| Type| Details  
---|---|---  
`min`| Float| The lower (inclusive) bound of the first bucket.  
`max`| Float| The upper (exclusive) bound of the last bucket.  
`steps`| Integer| The number of buckets to use.  
`cumulative`| Boolean, default: false| When true, generates a cumulative histogram.  
Was this helpful?
