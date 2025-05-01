 
#  ee.ImageCollection.copyProperties 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Copies metadata properties from one element to another. 
Usage| Returns  
---|---  
`ImageCollection.copyProperties( _source_, _properties_, _exclude_)`| Element  
Argument| Type| Details  
---|---|---  
this: `destination`| Element, default: null| The object whose properties to override.  
`source`| Element, default: null| The object from which to copy the properties.  
`properties`| List, default: null| The properties to copy. If omitted, all ordinary (i.e. non-system) properties are copied.  
`exclude`| List, default: null| The list of properties to exclude when copying all properties. Must not be specified if properties is.  
