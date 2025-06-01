 
#  ee.Dictionary.evaluate 
Stay organized with collections  Save and categorize content based on your preferences. 
Asynchronously retrieves the value of this object from the server and passes it to the provided callback function. Usage| Returns  
---|---  
`Dictionary.evaluate(callback)`|   
Argument| Type| Details  
---|---|---  
this: `computedobject`| ComputedObject| The ComputedObject instance.  
`callback`| Function| A function of the form function(success, failure), called when the server returns an answer. If the request succeeded, the success argument contains the evaluated result. If the request failed, the failure argument will contains an error message.  
## Examples
### Code Editor (JavaScript)
```
// A dictionary (e.g. results of ee.Image.reduceRegion of an S2 image).
vardictServer=ee.Dictionary({
B1:182,
B2:219,
B3:443
});
// Use evaluate to transfer server-side dictionary to the client.
dictServer.evaluate(function(dictClient){
print('Client-side dot notation to access "B1" value',dictClient.B1);
print('Client-side bracket notation to access "B1" value',dictClient['B1']);
print('Client-side operations to print all key-value pairs');
Object.keys(dictClient).forEach(function(key){
print('  '+key+': '+dictClient[key]);
});
});
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# The Earth Engine Python client library does not have an evaluate method for
# asynchronous evaluation of ee.Dictionary objects.
# Use ee.Dictionary.getInfo() instead.
```

