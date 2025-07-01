 
#  ee.Geometry.LineString.evaluate
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Asynchronously retrieves the value of this object from the server and passes it to the provided callback function. 
Usage| Returns  
---|---  
`LineString.evaluate(callback)`|   
Argument| Type| Details  
---|---|---  
this: `computedobject`| ComputedObject| The ComputedObject instance.  
`callback`| Function| A function of the form function(success, failure), called when the server returns an answer. If the request succeeded, the success argument contains the evaluated result. If the request failed, the failure argument will contains an error message.  
