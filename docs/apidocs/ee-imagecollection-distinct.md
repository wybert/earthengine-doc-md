 
#  ee.ImageCollection.distinct
Stay organized with collections  Save and categorize content based on your preferences. 
Removes duplicates from a collection. Note that duplicates are determined using a strong hash over the serialized form of the selected properties. Usage | Returns  
---|---  
`ImageCollection.distinct(properties)` | FeatureCollection  
Argument | Type | Details  
---|---|---  
this: `collection` | FeatureCollection | The input collection from which objects will be selected.  
`properties` | Object | A property name or a list of property names to use for comparison. The '.geo' property can be included to compare object geometries.  
