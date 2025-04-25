 
#  ui.DateSlider 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
A draggable target that ranges linearly between two dates. The date slider can be configured to display dates of various interval sizes, including day, 8-day, and year. The value of the slider is displayed as a label alongside it. 
Usage| Returns  
---|---  
`ui.DateSlider( _start_, _end_, _value_, _period_, _onChange_, _disabled_, _style_)`| ui.DateSlider  
Argument| Type| Details  
---|---|---  
`start`| Date|Number|String, optional| The start date, as a UTC timestamp, date string, or ee.Date. Defaults to one week ago.  
`end`| Date|Number|String, optional| The end date, as a UTC timestamp, date string, or ee.Date. Defaults to today.  
`value`| Date|Number|String, optional| The initial value. The value is an array consisting of the start and end date for the selected date range, but for convenience, it can be set by specifying the start date alone. Defaults to yesterday.  
`period`| Number, optional| The interval size for values on the slider in days. Defaults to one.  
`onChange`| Function, optional| A callback to fire when the slider's state changes. The callback is passed an ee.DateRange representing the slider's current value and the slider widget.  
`disabled`| Boolean, optional| Whether the slider is disabled. Defaults to false.  
`style`| Object, optional| An object of allowed CSS styles with their values to be set for this widget. Defaults to an empty object.  
