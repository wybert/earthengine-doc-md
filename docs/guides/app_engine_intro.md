 
#  App Engine & Earth Engine Overview 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Deploying App Engine apps with Earth Engine](https://developers.google.com/earth-engine/guides/app_engine_intro#deploying-app-engine-apps-with-earth-engine)
    * [ Enable the Earth Engine API on your Google Cloud project ](https://developers.google.com/earth-engine/guides/app_engine_intro#enable-the-earth-engine-api-on-your-google-cloud-project)
    * [Set up credentials](https://developers.google.com/earth-engine/guides/app_engine_intro#set-up-credentials)
    * [Set up the local development environment](https://developers.google.com/earth-engine/guides/app_engine_intro#set-up-the-local-development-environment)
    * [Run locally](https://developers.google.com/earth-engine/guides/app_engine_intro#run-locally)


[Google App Engine](https://cloud.google.com/appengine) lets you build and run your own custom applications on Google’s servers. App Engine applications are easy to create, maintain, and scale as your traffic and data storage needs change. You simply upload your application source code and it’s ready to go. If you're new to developing for App Engine, be sure to check out the App Engine [Python](https://cloud.google.com/appengine/docs/standard/python/quickstart) or [Node.js](https://cloud.google.com/appengine/docs/flexible/nodejs/quickstart) quickstart before proceeding.
Earth Engine and App Engine can be used together to build scalable geospatial applications. Typically, your App Engine code includes the [Earth Engine Python client library](https://github.com/google/earthengine-api/tree/master/python) and makes requests to the Earth Engine backend using a [service account](https://developers.google.com/earth-engine/guides/service_account). This is advantageous because it allows anyone to use your app without logging in or being a registered Earth Engine user. Note that the standard Earth Engine [usage limits](https://developers.google.com/earth-engine/guides/usage) apply to each service account.
Another development approach is to use [ client-side authentication](https://github.com/google/earthengine-api/tree/master/demos/client-auth) instead of a service account. With this approach, visitors to your application must be registered for Earth Engine and log in. The benefit of this approach is that requests to Earth Engine are made using the end user's credentials, so you are less likely to hit usage limits. The challenge is that your users must signup for Earth Engine and log in before using the application.
The [Earth Engine App Engine demos directory](https://github.com/google/earthengine-api/tree/master/demos) on GitHub contains a set of useful App Engine examples. See the [Example Apps page](https://developers.google.com/earth-engine/guides/app_engine_examples) for a brief description of each example. This doc provides instructions for how to set up and deploy the examples or custom apps you create.
## Deploying App Engine apps with Earth Engine
The following instructions explain how to deploy the [demo apps](https://github.com/google/earthengine-api/tree/master/demos). The Python instructions are intended for Mac OS and Linux. If you're using Python on Windows, [ try this](https://groups.google.com/forum/#!msg/google-earth-engine-developers/aL5ufRsiWlA/s0dvAri0SGoJ).
###  Enable the Earth Engine API on your Google Cloud project 
Create or select a Google Cloud project and enable the Earth Engine API according to [these instructions](https://developers.google.com/earth-engine/earthengine_cloud_project_setup). 
### Set up credentials
#### Service Account
A [service account](https://developers.google.com/identity/protocols/OAuth2ServiceAccount) may be used to authorize requests to Earth Engine on behalf of whomever is using your app. The `config.py` file contains authentication code using the service account email address and a private key file. To set up authentication with a service account, follow [these instructions](https://developers.google.com/earth-engine/guides/service_account) to create the service account and private key file. Name the key file `.private-key.json` and move it into your project directory.
##### Python
If you haven't already, first [set up the Earth Engine Python API](https://developers.google.com/earth-engine/guides/python_install). Test the service account according to [these instructions](https://developers.google.com/earth-engine/guides/service_account#use-the-service-account).
If the test succeeds, update `config.py` (or an equivalent file in your source code) with your service account email address. (The path to the key file should not change since it's in your project directory).
##### Node.js
Install the project's dependencies by running `npm install`. The Earth Engine Node.js API and any other dependencies will be copied to a `./node_modules` folder in your project directory. If installation fails, [check that a recent version of Node.js is installed](https://developers.google.com/earth-engine/guides/npm_install). 
```
constee=require('@google/earthengine');
ee.data.authenticateViaPrivateKey('.private-key.json');
ee.initialize();
```

#### OAuth 2.0 Client ID
If you want users to authenticate as themselves (rather than using a service account), you need to set up an OAuth Client ID from your Cloud Project. To do that: 
  1. Set up a client ID according to [these instructions](https://developers.google.com/earth-engine/earthengine_cloud_project_setup#create-oauth-2.0-client).
  2. Update `static/script.js` (or an equivalent file in your source code) to use your client ID.
  3. Ensure `ee_api_js.js` is available in the `/static/` directory (or equivalent). You can download it [ directly from GitHub](https://github.com/google/earthengine-api/blob/master/javascript/build/ee_api_js.js), [ install it from npm](https://www.npmjs.com/package/@google/earthengine), or, if you've already cloned the entire EE API repo, copy it from `earthengine-api/javascript/build` on your local filesystem.


### Set up the local development environment
##### Python
Follow the instructions in each example directory on GitHub to download and build the project. If there's a `build.sh` file, run it from your application root folder with the command:
```
./build.sh

```

The setup script will download dependencies and install Google command line tools, if they don't already exist on your system. The Earth Engine Python API and its dependencies will be copied to a `./lib` folder in your project directory.
Verify that the App Engine command line tools are available by running:
```
dev_appserver.py

```

If the command is not found, try manually downloading and installing the [Google App Engine SDK for Python](https://cloud.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python). If the command is available, it should fail with "error: too few arguments".
##### Node.js
No setup needed.
### Run locally
Once your service account is [registered for Earth Engine access](https://developers.google.com/earth-engine/guides/service_account#register-the-service-account-to-use-earth-engine), you can use it to authenticate (see `config.py`) when you test the examples. Try testing the examples locally first by going into your project directory and running:
##### Python
```
dev_appserver.py .

```

##### Node.js
```
npm install
npm start

```

Point your browser to <http://localhost:8080> to see the app running on a local server. Any changes you make (and save) will be automatically picked up when you refresh the page.
