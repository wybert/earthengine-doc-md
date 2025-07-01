 
#  ee.data.authenticateViaPopup
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Shows a popup asking for the user's permission. Should only be called if ee.data.authenticate() called its opt_onImmediateFailed argument in the past. 
May be blocked by pop-up blockers if called outside a user-initiated handler.
Usage| Returns  
---|---  
`ee.data.authenticateViaPopup( _success_, _error_)`|   
Argument|  Type| Details  
---|---|---  
`success`| Function, optional| The function to call if authentication succeeds.  
`error`| Function, optional| The function to call if authentication fails, passing the error message.  
Was this helpful?
