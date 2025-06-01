 
#  ee.ImageCollection.map 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Maps an algorithm over a collection. 
Returns the mapped collection.
Usage| Returns  
---|---  
`ImageCollection.map(algorithm,  _dropNulls_)`| Collection  
Argument| Type| Details  
---|---|---  
this: `collection`| Collection| The Collection instance.  
`algorithm`| Function| The operation to map over the images or features of the collection. A JavaScript function that receives an image or features and returns one. The function is called only once and the result is captured as a description, so it cannot perform imperative operations or rely on external state.  
`dropNulls`| Boolean, optional| If true, the mapped algorithm is allowed to return nulls, and the elements for which it returns nulls will be dropped.  
Was this helpful?
