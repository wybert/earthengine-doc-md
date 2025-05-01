 
#  ee.data.authenticateViaPrivateKey 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Configures server-side authentication of EE API calls through the Google APIs Node.js Client. Private key authentication is strictly for server-side API calls: for browser-based applications, use ee.data.authenticateViaOauth(). No user interaction (e.g. authentication popup) is necessary when using server-side authentication. 
This or another authentication method should be called before ee.initialize().
The auth token will be refreshed automatically when possible. You can safely assume that all async calls will be sent with the appropriate credentials. For synchronous calls, however, you should check for an auth token with ee.data.getAuthToken() and call ee.data.refreshAuthToken() manually if there is none. The token refresh operation is asynchronous and cannot be performed behind-the-scenes, on demand, prior to synchronous calls.
Usage| Returns  
---|---  
`ee.data.authenticateViaPrivateKey(privateKey,  _success_, _error_, _extraScopes_, _suppressDefaultScopes_)`|   
Argument|  Type| Details  
---|---|---  
`privateKey`| AuthPrivateKey| JSON content of private key.  
`success`| Function, optional| The function to call if authentication succeeded.  
`error`| Function, optional| The function to call if authentication failed, passed the error message.  
`extraScopes`| List, optional| Extra OAuth scopes to request.  
`suppressDefaultScopes`| Boolean, optional| When true, only scopes specified in opt_extraScopes are requested; the default scopes are not not requested unless explicitly specified in opt_extraScopes.  
