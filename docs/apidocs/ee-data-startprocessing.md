 
#  ee.data.startProcessing
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Create processing task that exports or pre-renders an image. 
Return value is null if a callback is specified.
Returns an object with fields:
- taskId: Submitted task ID (without hyphens).
- name: Full operation name in the format projects/X/operations/Y
- started: will be 'OK'
- note: may have value 'ALREADY_EXISTS' if an identical task with the same unsubmitted ID already exists.
Usage| Returns  
---|---  
`ee.data.startProcessing(taskId, params,  _callback_)`| ProcessingResponse  
Argument| Type| Details  
---|---|---  
`taskId`| String| Unsubmitted ID for the task (obtained from newTaskId). Used to identify duplicated tasks; may be null. The server will create and return a submitted ID.  
`params`| Object| The object that describes the processing task; only fields that are common for all processing types are documented here. type (string) Either 'EXPORT_IMAGE', 'EXPORT_FEATURES', 'EXPORT_VIDEO' or 'EXPORT_TILES'. json (string) JSON description of the image.  
`callback`| Function, optional| An optional callback. If not supplied, the call is made synchronously.  
Was this helpful?
