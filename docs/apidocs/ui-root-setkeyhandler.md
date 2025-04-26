 
#  ui.root.setKeyHandler 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Sets a keydown event handler to the root panel with a non-predefined key. The handler is fired only once when a user presses the bound key command. The same key will be bound to the latest handler set to it. 
Usage| Returns  
---|---  
`ui.root.setKeyHandler(keyCode, handler,  _description_)`|   
Argument|  Type| Details  
---|---|---  
`keyCode`| List| A key code or an array of key codes. For example, ui.Key.A or [ui.Key.SHIFT, ui.Key.A].  
`handler`| Function| The handler for the key command.  
`description`| String, optional| A short description that explains this key command. The description will be visible in the Shortcuts Menu.  
