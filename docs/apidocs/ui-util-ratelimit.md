 
#  ui.util.rateLimit
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Example use: For the callback to a click on a ui.Button, in order to prevent the button from being accidentally double-clicked and the callback running twice.
Returns the rate-limited function.
Usage | Returns  
---|---  
`ui.util.rateLimit(func, delay, _scope_)`|  Function  
Argument | Type | Details  
---|---|---  
`func` | Function | Function to call.  
`delay` | Number | After the function is called and executed, the number of milliseconds to delay before allowing an additional invocation of the function.  
`scope` | Object, optional | Object in whose scope to call the function.  
