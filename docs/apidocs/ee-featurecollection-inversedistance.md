 
#  ee.FeatureCollection.inverseDistance 
Stay organized with collections  Save and categorize content based on your preferences. 
Returns an inverse-distance weighted estimate of the value at each pixel. Usage| Returns  
---|---  
`FeatureCollection.inverseDistance(range, propertyName, mean, stdDev,  _gamma_, _reducer_)`| Image  
Argument| Type| Details  
---|---|---  
this: `collection`| FeatureCollection| Feature collection to use as source data for the estimation.  
`range`| Float| Size of the interpolation window (in meters).  
`propertyName`| String| Name of the numeric property to be estimated.  
`mean`| Float| Global expected mean.  
`stdDev`| Float| Global standard deviation.  
`gamma`| Float, default: 1| Determines how quickly the estimates tend towards the global mean.  
`reducer`| Reducer, default: null| Reducer used to collapse the 'propertyName' value of overlapping points into a single value.  
