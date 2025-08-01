 
#  ee.ImageCollection.remap
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Remaps the value of a specific property in a collection. Takes two parallel lists and maps values found in one to values in the other. Any element with a value that is not specified in the first list is dropped from the output collection.
Usage | Returns  
---|---  
`ImageCollection.remap(lookupIn, lookupOut, columnName)` | FeatureCollection  
Argument | Type | Details  
---|---|---  
this: `collection` | FeatureCollection | The collection to be modified.  
`lookupIn` | List | The input mapping values. Restricted to strings and integers.  
`lookupOut` | List | The output mapping values. Must be the same size as lookupIn.  
`columnName` | String | The name of the property to remap.  
Was this helpful?
