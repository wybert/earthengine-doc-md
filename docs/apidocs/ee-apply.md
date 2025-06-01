 
#  ee.apply 
Stay organized with collections  Save and categorize content based on your preferences. 
Call a function with a dictionary of named arguments. 
Returns an object representing the called function. If the signature specifies a recognized return type, the returned value will be cast to that type.
Usage| Returns  
---|---  
`ee.apply(func, namedArgs)`| ComputedObject  
Argument| Type| Details  
---|---|---  
`func`| Function|String| The function to call. Either an ee.Function object or the name of an API function.  
`namedArgs`| Object| A dictionary of arguments to the function.  
