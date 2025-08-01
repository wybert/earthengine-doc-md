 
#  ee.Reducer.intervalMean
Stay organized with collections  Save and categorize content based on your preferences. 
Creates a Reducer to compute the mean of all inputs in the specified percentile range. For small numbers of inputs (up to maxRaw) the mean will be computed directly; for larger numbers of inputs the mean will be derived from a histogram. Usage | Returns  
---|---  
`ee.Reducer.intervalMean(minPercentile, maxPercentile, _maxBuckets_, _minBucketWidth_, _maxRaw_)`|  Reducer  
Argument | Type | Details  
---|---|---  
`minPercentile` | Float | The lower bound of the percentile range.  
`maxPercentile` | Float | The upper bound of the percentile range.  
`maxBuckets` | Integer, default: null | The maximum number of buckets to use when building a histogram; will be rounded up to a power of 2.  
`minBucketWidth` | Float, default: null | The minimum histogram bucket width, or null to allow any power of 2.  
`maxRaw` | Integer, default: null | The number of values to accumulate before building the initial histogram.  
