 
#  ui.Chart.feature.histogram 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Generates a Chart from a set of features. Computes and plots a histogram of the given property. 
- X-axis = Histogram buckets (of property value).
- Y-axis = Frequency (i.e. the number of features whose value of property lands within the x-axis bucket bounds).
Returns a chart.
Usage| Returns  
---|---  
`ui.Chart.feature.histogram(features, property,  _maxBuckets_, _minBucketWidth_, _maxRaw_)`| ui.Chart  
Argument| Type| Details  
---|---|---  
`features`| Feature|FeatureCollection|List| The features to include in the chart.  
`property`| String| The name of the property to generate the histogram for.  
`maxBuckets`| Number, optional| The maximum number of buckets to use when building a histogram; will be rounded up to a power of 2. Not used when the value of property is non-numeric.  
`minBucketWidth`| Number, optional| The minimum histogram bucket width, or null to allow any power of 2. Not used when property is non-numeric.  
`maxRaw`| Number, optional| The number of values to accumulate before building the initial histogram. Not used when property is non-numeric.  
Was this helpful?
