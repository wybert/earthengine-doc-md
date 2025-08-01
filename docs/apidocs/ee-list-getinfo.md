 
#  ee.List.getInfo
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
If no callback function is provided, the request is made synchronously. If a callback is provided, the request is made asynchronously.
The asynchronous mode is preferred because the synchronous mode stops all other code (for example, the EE Code Editor UI) while waiting for the server. To make an asynchronous request, evaluate() is preferred over getInfo().
Returns the computed value of this object.
Usage | Returns  
---|---  
`List.getInfo(_callback_)`|  Object  
Argument | Type | Details  
---|---|---  
this: `computedobject` | ComputedObject | The ComputedObject instance.  
`callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously.  
