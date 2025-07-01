 
#  ee.initialize
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Initialize the library. If this hasn't been called by the time any object constructor is used, it will be called then. If this is called a second time with a different baseurl or tileurl, this doesn't do an un-initialization of e.g.: the previously loaded Algorithms, but will overwrite them and let point at alternate servers. 
If initialize() is first called in asynchronous mode (by passing a success callback), any future asynchronous mode calls will add their callbacks to a queue and all the callbacks will be run together.
If a synchronous mode call is made after any number of asynchronous calls, it will block and execute all the previously supplied callbacks before returning.
In most cases, an authorization token should be set before the library is initialized, either with ee.data.authorize() or ee.data.setAuthToken().
In Python, this method is named ee.Initialize, with a capital I. Note that some parameters differ between JavaScript and Python. In addition to opt_url and project below, Python also supports: credentials - a google.oauth2.Credentials object or 'persistent' to use stored credentials (the default); http_transport - a httplib2.Http client.
Usage| Returns  
---|---  
`ee.initialize( _baseurl_, _tileurl_, _successCallback_, _errorCallback_, _xsrfToken_, _project_)`|   
Argument|  Type| Details  
---|---|---  
`baseurl`| String, optional| The Earth Engine REST API endpoint. (Python argument name: opt_url)  
`tileurl`| String, optional| The Earth Engine REST tile endpoint, this is optional and defaults to baseurl. (JavaScript only)  
`successCallback`| Function, optional| An optional callback to be invoked when the initialization is successful. If not provided, the initialization is done synchronously. (JavaScript only)  
`errorCallback`| Function, optional| An optional callback to be invoked with an error if the initialization fails. (JavaScript only)  
`xsrfToken`| String, optional| A string to pass in the "xsrfToken" parameter of EE API XHRs. (JavaScript only)  
`project`| String, optional| Optional client project ID or number to use when making API calls. (Python argument name: project)  
