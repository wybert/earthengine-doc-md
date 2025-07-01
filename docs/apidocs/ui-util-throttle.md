 
#  ui.util.throttle
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Wraps a function to allow it to be called, at most, twice per interval. If the wrapper function is called multiple times before the delay elapses, only the first and the last calls will go through. 
Example use: For the callback to a slide event on a ui.Slider. The callback will run immediately, making the slide action feel responsive. The callback is also guaranteed to run after the user has finished interacting with the slider, ensuring that the final callback invocation has access to the slider's final value.
Returns the wrapped function.
Usage| Returns  
---|---  
`ui.util.throttle(func, delay,  _scope_)`| Function  
Argument| Type| Details  
---|---|---  
`func`| Function| The function to call.  
`delay`| Number| The delay, in milliseconds, for the throttle. The function can only be called once after the initial invocation until after the delay has elapsed.  
`scope`| Object, optional| The object in whose scope to call the function.  
Was this helpful?
