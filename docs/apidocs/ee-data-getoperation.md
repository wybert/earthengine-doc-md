 
#  ee.data.getOperation 
Stay organized with collections  Save and categorize content based on your preferences. 
Gets information on an operation or list of operations. 
See more details on Operations here: https://cloud.google.com/apis/design/design_patterns#long_running_operations
Returns operation status, or a map from operation names to status. Each Operation contains:
- name: operation name in the format projects/X/operations/Y
- done: true when operation has finished running.
- error: may be set when done=true. Contains message and other fields from https://cloud.google.com/tasks/docs/reference/rpc/google.rpc#status
- metadata, which contains
+ state: PENDING, RUNNING, CANCELLING, SUCCEEDED, CANCELLED, or FAILED
+ description: Supplied task description
+ type: EXPORT_IMAGE, EXPORT_FEATURES, etc.
+ create_time: Time the operation was first submitted.
+ update_time: Timestamp of most recent update.
+ start_time: Time the operation started, when so.
+ end_time: Time the operation finished running, when so.
+ attempt: Number of retries of this task, starting at 1.
+ destination_uris: Resources output by this operation.
+ batch_eecu_usage_seconds: CPU used by this operation.
Usage| Returns  
---|---  
`ee.data.getOperation(operationName,  _callback_)`| Dictionary |api.Operation  
Argument| Type| Details  
---|---|---  
`operationName`| List| Operation name(s).  
`callback`| Function, optional| An optional callback. If not supplied, the call is made synchronously.  
