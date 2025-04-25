 
#  ee.data.setDefaultWorkloadTag 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Sets the workload tag, and as the default for which to reset back to. 
For example, calling `ee.data.resetWorkloadTag()` will reset the workload tag back to the default chosen here. To reset the default back to none, pass in an empty string or pass in true to `ee.data.resetWorkloadTag(true)`, like so.
Workload tag must be 1 - 63 characters, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots
(.), and alphanumerics between, or an empty string to reset the default back to none.
Usage| Returns  
---|---  
`ee.data.setDefaultWorkloadTag(tag)`|   
Argument| Type| Details  
---|---|---  
`tag`| String|   
