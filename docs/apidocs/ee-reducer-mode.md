 
#  ee.Reducer.mode 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Create a reducer that will compute the mode of the inputs. For small numbers of inputs (up to maxRaw) the mode will be computed directly; for larger numbers of inputs the mode will be derived from a histogram. 
Usage| Returns  
---|---  
`ee.Reducer.mode( _maxBuckets_, _minBucketWidth_, _maxRaw_)`| Reducer  
Argument| Type| Details  
---|---|---  
`maxBuckets`| Integer, default: null| The maximum number of buckets to use when building a histogram; will be rounded up to a power of 2.  
`minBucketWidth`| Float, default: null| The minimum histogram bucket width, or null to allow any power of 2.  
`maxRaw`| Integer, default: null| The number of values to accumulate before building the initial histogram.  
