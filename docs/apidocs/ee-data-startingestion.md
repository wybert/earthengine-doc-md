 
#  ee.data.startIngestion
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Creates an image asset ingestion task. 
See ee.data.startProcessing for details on task IDs and response format.
Usage| Returns  
---|---  
`ee.data.startIngestion(taskId, request,  _callback_)`| ProcessingResponse  
Argument| Type| Details  
---|---|---  
`taskId`| String| Unsubmitted ID for the task (obtained from newTaskId).  
`request`| IngestionRequest| The object that describes the ingestion.  
`callback`| Function, optional| An optional callback. If not supplied, the call is made synchronously.  
Was this helpful?
