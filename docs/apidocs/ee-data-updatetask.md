 
#  ee.data.updateTask
Stay organized with collections  Save and categorize content based on your preferences. 
Returns an array of updated tasks, or null if a callback is specified.
Usage | Returns  
---|---  
`ee.data.updateTask(taskId, action, _callback_)`|  List<TaskStatus>  
Argument | Type | Details  
---|---|---  
`taskId` | List<String>|String | Submitted ID of the task or an array of multiple task IDs. May also contain operation names.  
`action` | TaskUpdateActions | Action performed on tasks.  
`callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously.  
