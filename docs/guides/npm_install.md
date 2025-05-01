 
#  NPM Installation 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Keep your client library up to date by running: `npm update @google/earthengine`
The Earth Engine JavaScript API is distributed as an [npm package](https://www.npmjs.com/package/@google/earthengine) that is [hosted on GitHub](https://github.com/google/earthengine-api). The following instructions give an overview of installing the Google Earth Engine JavaScript API. To use the Earth Engine JavaScript API you'll need to [install the client library and its dependencies](https://developers.google.com/earth-engine/guides/npm_install#installing-the-client-library) on your computer and then [set up authentication credentials](https://developers.google.com/earth-engine/guides/npm_install#setting-up-authentication-credentials).
_The JavaScript client library does not include all functionality of the Earth Engine[Code Editor](https://developers.google.com/earth-engine/guides/playground). Notably, user interface features such as buttons, panels, and charts are excluded._
## Installing the client library
#### 1. Set up Node.js and npm
[npm](https://www.npmjs.com/) is a package manager for JavaScript and Node.js. Verify that you have Node.js 6+ and npm 3+.
```
node --version
npm --version
```

If needed, install both using the [official installer for your platform](https://nodejs.org/en/download/).
#### 2. Install the Earth Engine client library
The client library can be installed from npm with the following command:
```
npm install --save @google/earthengine
```

Once installed, the client library is placed within the current project directory: `node_modules/@google/earthengine/*`. On future projects, install the client in the same way.
#### 3. Use the client library in an application
Within your application code, require the Earth Engine API:
```
varee=require('@google/earthengine');
```

## Updating the client library
Use npm to update the client library to the latest version. From the current project directory: ```
npm update @google/earthengine
```

_Learn more about[updating libraries with npm](https://docs.npmjs.com/cli/update). _
## Uninstalling the client library
To uninstall using the npm package manager, run the following command:
```
npm uninstall --save @google/earthengine
```

This removes `node_modules/@google/earthengine` from the current project, but does not affect any projects in other directories on the same machine.
##  Create a Cloud Project and activate the Earth Engine API 
Follow [these instructions](https://developers.google.com/earth-engine/guides/access#get_access_to_earth_engine) to create a Cloud project and enable the Earth Engine API. 
## Setting Up Authentication Credentials
Earth Engine APIs use the [OAuth 2.0 protocol](http://oauth.net/2/) for authenticating browser-based clients. For server-side authentication in Node.js, service accounts are recommended. Web apps may use either approach, with pros and cons discussed below.
### Client-side authentication with OAuth
With client-side authentication in a web browser, users of your application log in with their own Google accounts. These users must already be authorized to access Earth Engine, and must have permission to read the assets used by your application.
After [creating an OAuth 2.0 Client ID](https://developers.google.com/earth-engine/guides/access#oauth_20_client_id), authenticate as shown below:
```
//Loadclientlibrary.
varee=require('@google/earthengine');
//Initializeclientlibraryandrunanalysis.
varinitialize=function(){
ee.initialize(null,null,function(){
//...runanalysis...
},function(e){
console.error('Initialization error: '+e);
});
};
//AuthenticateusinganOAuthpop-up.
ee.data.authenticateViaOauth(YOUR_CLIENT_ID,initialize,function(e){
console.error('Authentication error: '+e);
},null,function(){
ee.data.authenticateViaPopup(initialize);
});
```
**Notice:** Client-side authentication only works in the browser. In server or command-line code, service account authentication is required.
### Server-side authentication with a service account
With server-side authentication, a private key is stored with your application, allowing it to access the Earth Engine API through a service account. Users of your application do not need their own access to Earth Engine, and are not required to log in.
In Node.js, only server-side authentication is provided by the client library.
After [creating a new service account](https://developers.google.com/earth-engine/guides/service_account#create-a-service-account), use your JSON private key to authenticate:
```
//Requireclientlibraryandprivatekey.
varee=require('@google/earthengine');
varprivateKey=require('./.private-key.json');
//Initializeclientlibraryandrunanalysis.
varrunAnalysis=function(){
ee.initialize(null,null,function(){
//...runanalysis...
},function(e){
console.error('Initialization error: '+e);
});
};
//Authenticateusingaserviceaccount.
ee.data.authenticateViaPrivateKey(privateKey,runAnalysis,function(e){
console.error('Authentication error: '+e);
});
```
**Caution:** A private key gives an application permission to act as your service account, and should be treated like a password. Never share a private key or include it in version control. Instead, specify the private key using a config file, or load it from an environment variable.
## Testing the installation
To test that authentication has been set up correctly, run the following script:
```
varee=require('@google/earthengine');
//Authenticateusingone(butnotboth)ofthemethodsbelow.
ee.data.authenticateViaOauth(YOUR_CLIENT_ID);
ee.data.authenticateViaPrivateKey(YOUR_PRIVATE_KEY);
ee.initialize();
//RunanEarthEnginescript.
varimage=newee.Image('srtm90_v4');
image.getMap({min:0,max:1000},function(map){
console.log(map);
});
```

If everything is installed correctly, the metadata for an image should be printed.
**Notice:** When using Earth Engine in a Node.js environment, some best practices differ from typical scripts. Synchronous API calls should be avoided — they prevent the app from handling other requests while waiting for a response from the Earth Engine API. Instead, use asynchronous requests with callback functions. When using the Earth Engine API in Google Cloud Functions, _synchronous requests are not supported._
