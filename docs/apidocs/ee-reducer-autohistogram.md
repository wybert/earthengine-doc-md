 
#  ee.Reducer.autoHistogram
Stay organized with collections  Save and categorize content based on your preferences. 
Create a reducer that will compute a histogram of the inputs. The output is a Nx2 array of the lower bucket bounds and the counts (or cumulative counts) of each bucket and is suitable for use per-pixel. Usage| Returns  
---|---  
`ee.Reducer.autoHistogram( _maxBuckets_, _minBucketWidth_, _maxRaw_, _cumulative_)`| Reducer  
Argument| Type| Details  
---|---|---  
`maxBuckets`| Integer, default: null| The maximum number of buckets to use when building a histogram; will be rounded up to a power of 2.  
`minBucketWidth`| Float, default: null| The minimum histogram bucket width, or null to allow any power of 2.  
`maxRaw`| Integer, default: null| The number of values to accumulate before building the initial histogram.  
`cumulative`| Boolean, default: false|   
