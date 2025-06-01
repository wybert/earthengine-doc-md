 
#  ui.Chart.onClick 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Registers a callback that's fired when the chart is clicked. 
Returns an ID which can be passed to unlisten() to unregister the callback.
Usage| Returns  
---|---  
`Chart.onClick(callback)`| String  
Argument| Type| Details  
---|---|---  
this: `ui.chart`| ui.Chart| The ui.Chart instance.  
`callback`| Function| The callback to fire when the chart is clicked. The callback is passed three arguments: the x-value, the y-value, and the series name. Time values are represented in UTC epoch milliseconds, like "system:time_start" values on assets. If the user clicks on a legend entry to select an entire series, the x- and y-values are null. If the user clicks an already-selected point, all arguments are null, indicating the selection was cleared.  
