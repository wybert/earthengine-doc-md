 
#  ee.data.startTableIngestion
Stay organized with collections  Save and categorize content based on your preferences. 
See ee.data.startProcessing for details on task IDs and response format.
Usage | Returns  
---|---  
`ee.data.startTableIngestion(taskId, request, _callback_)`|  ProcessingResponse  
Argument | Type | Details  
---|---|---  
`taskId` | String | Unsubmitted ID for the task (obtained from newTaskId).  
`request` | TableIngestionRequest | The object that describes the ingestion.  
`callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously.  
