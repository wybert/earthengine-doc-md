 
#  ee.ImageCollection.iterate 
Stay organized with collections  Save and categorize content based on your preferences. 
Applies a user-supplied function to each element of a collection. The user-supplied function is given two arguments: the current element, and the value returned by the previous call to iterate() or the first argument, for the first iteration. The result is the value returned by the final call to the user-supplied function. 
Returns the result of the Collection.iterate() call.
Usage| Returns  
---|---  
`ImageCollection.iterate(algorithm,  _first_)`| ComputedObject  
Argument| Type| Details  
---|---|---  
this: `collection`| Collection| The Collection instance.  
`algorithm`| Function| The function to apply to each element. Must take two arguments: an element of the collection and the value from the previous iteration.  
`first`| Object, optional| The initial state.  
