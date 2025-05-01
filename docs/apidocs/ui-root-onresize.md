 
#  ui.root.onResize 
Stay organized with collections  Save and categorize content based on your preferences. 
Registers a callback that's fired when the script starts and whenever the browser window size changes. It will be passed an object with boolean fields "is_mobile", "is_tablet", "is_desktop", "is_portrait" and "is_landscape", and numeric fields "width" and "height". 
These fields indicate whether a user's device is mobile, tablet or desktop, the device orientation (portrait or landscape), and the width and height of the window in pixels. See the Width and Height (dp) section of device metrics at https://material.io/resources/devices/.
Usage| Returns  
---|---  
`ui.root.onResize(callback)`|   
Argument| Type| Details  
---|---|---  
`callback`| Function| The callback to fire after the window has been resized. The callback is passed an object with the information of the device.  
