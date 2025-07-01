 
#  ee.data.newTaskId
Stay organized with collections  Save and categorize content based on your preferences. 
Generates an "unsubmitted" ID for a long-running task. 
Before tasks are submitted, they may be assigned IDs to track them. The server ensures that the same ID cannot be reused. These IDs have a UUID format: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
Tasks that are running on the server have a ID without hyphens. This is returned by ee.data.startProcessing and other batch methods.
Returns an array containing generated ID strings, or null if a callback is specified.
Usage| Returns  
---|---  
`ee.data.newTaskId( _count_, _callback_)`| List  
Argument| Type| Details  
---|---|---  
`count`| Number, optional| The number of IDs to generate, one by default.  
`callback`| Function, optional| An optional callback. If not supplied, the call is made synchronously.  
