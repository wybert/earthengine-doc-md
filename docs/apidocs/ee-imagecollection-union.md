 
#  ee.ImageCollection.union
Stay organized with collections  Save and categorize content based on your preferences. 
Merges all geometries in a given collection into one and returns a collection containing a single feature with only an ID of 'union_result' and a geometry. Usage | Returns  
---|---  
`ImageCollection.union(_maxError_)`|  FeatureCollection  
Argument | Type | Details  
---|---|---  
this: `collection` | FeatureCollection | The collection being merged.  
`maxError` | ErrorMargin, default: null | The maximum error allowed when performing any necessary reprojections. If not specified, defaults to the error margin requested from the output.  
