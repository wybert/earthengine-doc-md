 
#  ee.Feature.getInfo
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
An imperative function that returns information about this feature via an AJAX call. 
Returns a description of the feature.
Usage| Returns  
---|---  
`Feature.getInfo( _callback_)`| GeoJSONFeature  
Argument| Type| Details  
---|---|---  
this: `feature`| Feature| The Feature instance.  
`callback`| Function, optional| An optional callback. If not supplied, the call is made synchronously. If supplied, will be called with the first parameter if successful and the second if unsuccessful.  
