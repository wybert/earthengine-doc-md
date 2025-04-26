 
#  ee.Reducer.fixed2DHistogram 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Creates a reducer that will compute a 2D histogram of the inputs using a fixed number of fixed-width bins. Values outside of the [min, max) range on either axis are ignored. The output is a 2D array of counts, and 2 1-D arrays of bucket lower edges for the xAxis and the yAxis. This reducer is suitable for use per-pixel, however it is always unweighted. The maximum count for any bucket is 2^31 - 1. 
Usage| Returns  
---|---  
`ee.Reducer.fixed2DHistogram(xMin, xMax, xSteps, yMin, yMax, ySteps)`| Reducer  
Argument| Type| Details  
---|---|---  
`xMin`| Float| The lower (inclusive) bound of the first bucket on the X axis.  
`xMax`| Float| The upper (exclusive) bound of the last bucket on the X axis.  
`xSteps`| Integer| The number of buckets to use on the X axis.  
`yMin`| Float| The lower (inclusive) bound of the first bucket on the Y axis.  
`yMax`| Float| The upper (exclusive) bound of the last bucket on the Y axis.  
`ySteps`| Integer| The number of buckets to use on the Y axis.  
