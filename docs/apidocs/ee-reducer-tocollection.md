 
#  ee.Reducer.toCollection
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Returns a reducer that collects its inputs into a FeatureCollection.
Usage | Returns  
---|---  
`ee.Reducer.toCollection(propertyNames, _numOptional_)`|  Reducer  
Argument | Type | Details  
---|---|---  
`propertyNames` | List | The property names that will be defined on each output feature; determines the number of reducer inputs.  
`numOptional` | Integer, default: 0 | The last numOptional inputs will be considered optional; the other inputs must be non-null or the input tuple will be dropped.  
