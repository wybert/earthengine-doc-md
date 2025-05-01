 
#  Map.setGestureHandling 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Controls how gestures are handled on the map. 
See https://developers.google.com/maps/documentation/javascript/reference/map#MapOptions.gestureHandling.
Usage| Returns  
---|---  
`Map.setGestureHandling(option)`|   
Argument| Type| Details  
---|---|---  
`option`| String| The option that controls how gestures are handled on the map. Allowed values: 
  * "cooperative": Scroll events and one-finger touch gestures scroll the page, and do not zoom or pan the map. Two-finger touch gestures pan and zoom the map. Scroll events with a ctrl key or ⌘ key pressed zoom the map. In this mode the map cooperates with the page.
  * "greedy": All touch gestures and scroll events pan or zoom the map.
  * "none": The map cannot be panned or zoomed by user gestures.
  * "auto": (default) Gesture handling is either cooperative or greedy, depending on whether the page is scrollable or in an iframe.

  
