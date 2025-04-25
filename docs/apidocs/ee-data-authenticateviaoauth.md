 
#  ee.data.authenticateViaOauth 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Configures client-side authentication of EE API calls through the Google APIs Client Library for JavaScript. The library will be loaded automatically if it is not already loaded on the page. The user will be asked to grant the application identified by clientId access to their EE data if they have not done so previously. 
This or another authentication method should be called before ee.initialize().
Note that if the user has not previously granted access to the application identified by the client ID, by default this will try to pop up a dialog window prompting the user to grant the required permission. However, this popup can be blocked by the browser. To avoid this, specify the opt_onImmediateFailed callback, and in it render an in-page login button, then call ee.data.authenticateViaPopup() from the click event handler of this button. This stops the browser from blocking the popup, as it is now the direct result of a user action.
The auth token will be refreshed automatically when possible. You can safely assume that all async calls will be sent with the appropriate credentials. For synchronous calls, however, you should check for an auth token with ee.data.getAuthToken() and call ee.data.refreshAuthToken() manually if there is none. The token refresh operation is asynchronous and cannot be performed behind-the-scenes on-demand prior to synchronous calls.
Usage| Returns  
---|---  
`ee.data.authenticateViaOauth(clientId, success,  _error_, _extraScopes_, _onImmediateFailed_, _suppressDefaultScopes_)`  
Argument|  Type| Details  
---|---|---  
`clientId`| String| The application's OAuth client ID, or null to disable authenticated calls. This can be obtained through the Google Developers Console. The project must have a JavaScript origin that corresponds to the domain where the script is running.  
`success`| Function| The function to call if authentication succeeded.  
`error`| Function, optional| The function to call if authentication failed, passed the error message. If authentication in immediate (behind-the-scenes) mode fails and opt_onImmediateFailed is specified, that function is called instead of opt_error.  
`extraScopes`| List, optional| Extra OAuth scopes to request.  
`onImmediateFailed`| Function, optional| The function to call if automatic behind-the-scenes authentication fails. Defaults to ee.data.authenticateViaPopup(), bound to the passed callbacks.  
`suppressDefaultScopes`| Boolean, optional| When true, only scopes specified in opt_extraScopes are requested; the default scopes are not requested unless explicitly specified in opt_extraScopes.  
