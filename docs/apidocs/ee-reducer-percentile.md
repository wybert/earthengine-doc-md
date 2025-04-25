 
#  ee.Reducer.percentile 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Create a reducer that will compute the specified percentiles, e.g. given [0, 50, 100] will produce outputs named 'p0', 'p50', and 'p100' with the min, median, and max respectively. For small numbers of inputs (up to maxRaw) the percentiles will be computed directly; for larger numbers of inputs the percentiles will be derived from a histogram. 
Usage| Returns  
---|---  
`ee.Reducer.percentile(percentiles,  _outputNames_, _maxBuckets_, _minBucketWidth_, _maxRaw_)`| Reducer  
Argument| Type| Details  
---|---|---  
`percentiles`| List| A list of numbers between 0 and 100.  
`outputNames`| List, default: null| A list of names for the outputs, or null to get default names.  
`maxBuckets`| Integer, default: null| The maximum number of buckets to use when building a histogram; will be rounded up to a power of 2.  
`minBucketWidth`| Float, default: null| The minimum histogram bucket width, or null to allow any power of 2.  
`maxRaw`| Integer, default: null| The number of values to accumulate before building the initial histogram.  
