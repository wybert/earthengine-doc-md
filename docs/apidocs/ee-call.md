 
#  ee.call 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Call a function with the given positional arguments. 
Returns an object representing the called function. If the signature specifies a recognized return type, the returned value will be cast to that type.
Usage| Returns  
---|---  
`ee.call(func, var_args)`| ComputedObject  
Argument| Type| Details  
---|---|---  
`func`| Function|String| The function to call. Either an ee.Function object or the name of an API function.  
`var_args`| VarArgs| Positional arguments to pass to the function.  
