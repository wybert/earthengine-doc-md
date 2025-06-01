 
#  ui.util.debounce 
Stay organized with collections  Save and categorize content based on your preferences. 
Wraps a function to allow it to be called, at most, once for each sequence of calls fired repeatedly so long as they are fired less than a specified interval apart (in milliseconds). This can be used to reduce the number of invocations of an expensive function while ensuring it eventually runs. 
Example use: For the callback to a change event on a ui.Checkbox. If the user clicks the checkbox repeatedly, only the last click of the checkbox will run the callback.
Returns the debounced function.
Usage| Returns  
---|---  
`ui.util.debounce(func, delay,  _scope_)`| Function  
Argument| Type| Details  
---|---|---  
`func`| Function| The function to debounce.  
`delay`| Number| After the function is called once, the number of milliseconds to delay for an additional invocation of the function before allowing it to run.  
`scope`| Object, optional| Object in whose scope to call the function.  
