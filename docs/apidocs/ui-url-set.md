 
#  ui.url.set
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Sets the value of the page's URL fragment. The fragment encodes a dictionary of keys and values. If a dictionary is supplied as the first argument, the key/value pairs in that dictionary will be encoded and replace the current URL fragment. If a key string is provided, then only that key (and its value, the second argument) are updated, and the rest of the URL fragment is unchanged. 
Usage| Returns  
---|---  
`ui.url.set(keyOrDict,  _value_)`|   
Argument|  Type| Details  
---|---|---  
`keyOrDict`| Dictionary| Either a key to update a single value in the URL fragment, or a dictionary of key/value pairs which will replace the existing URL fragment. Dictionary values must be of type string, number, or boolean.  
`value`| Boolean|Number|String, optional| The new value to associate with a single key. This is required when the first argument is a string and is otherwise ignored.  
Was this helpful?
