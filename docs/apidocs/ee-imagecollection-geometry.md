 
#  ee.ImageCollection.geometry 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Extracts and merges the geometries of a collection. Requires that all the geometries in the collection share the projection and edge interpretation. **Caution:** providing a large or complex collection as input can result in poor performance. Collating the geometry of collections does not scale well; use the smallest collection that is required to achieve the desired outcome.**Note:** If only a bounding box around the collection is needed, consider using Collection.bounds instead.
Usage| Returns  
---|---  
`ImageCollection.geometry( _maxError_)`| Geometry  
Argument| Type| Details  
---|---|---  
this: `collection`| FeatureCollection| The collection whose geometries will be extracted.  
`maxError`| ErrorMargin, optional| An error margin to use when merging geometries.  
Was this helpful?
