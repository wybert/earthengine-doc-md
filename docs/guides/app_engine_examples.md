 
#  App Engine Example Apps 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Authentication with service accounts](https://developers.google.com/earth-engine/guides/app_engine_examples#authentication-with-service-accounts)
    * [server-auth-python](https://developers.google.com/earth-engine/guides/app_engine_examples#server-auth-python)
    * [server-auth-nodejs](https://developers.google.com/earth-engine/guides/app_engine_examples#server-auth-nodejs)
    * [trendy-lights](https://developers.google.com/earth-engine/guides/app_engine_examples#trendy-lights)
    * [cloud-functions](https://developers.google.com/earth-engine/guides/app_engine_examples#cloud-functions)
  * [Authentication with OAuth2](https://developers.google.com/earth-engine/guides/app_engine_examples#authentication-with-oauth2)
    * [client-auth](https://developers.google.com/earth-engine/guides/app_engine_examples#client-auth)
    * [map-layer](https://developers.google.com/earth-engine/guides/app_engine_examples#map-layer)
    * [polygon-drawing](https://developers.google.com/earth-engine/guides/app_engine_examples#polygon-drawing)
    * [export-to-drive](https://developers.google.com/earth-engine/guides/app_engine_examples#export-to-drive)


The following describes examples in the [Earth Engine demos directory on GitHub](https://github.com/google/earthengine-api/tree/master/demos). The title of each example is a link to the source on GitHub. The examples are organized by how they authenticate with Earth Engine. To learn more about authentication options and how to deploy these applications, see the [App Engine & Earth Engine Overview](https://developers.google.com/earth-engine/app_engine_intro). 
## Authentication with service accounts
### [server-auth-python](https://github.com/google/earthengine-api/tree/master/demos/server-auth-python)
![assets](https://developers.google.com/static/earth-engine/images/Demo_server_auth.png)
To get started, consider this example the 'hello world' of Earth Engine applications on the App Engine platform. The app displays an interactive map with an Earth Engine Image (SRTM elevation). Inspect the `config.py` file, noting that it needs to be modified with your project's service account credentials. The only Earth Engine specific code is in `server.py` (two lines!). Note that Earth Engine gets a mapid for the image to be displayed on the the app's page, then passes this value to the [Jinja](http://jinja.pocoo.org/) template used to render the page.
### [server-auth-nodejs](https://github.com/google/earthengine-api/tree/master/demos/server-auth-nodejs)
Same as the example above, using Node.js instead. The `server.js` file loads service account credentials from a `.private-key.json` file, and gets a mapid for the image to be displayed on the app's page.
### [trendy-lights](https://github.com/google/earthengine-api/tree/master/demos/trendy-lights)
![assets](https://developers.google.com/static/earth-engine/images/Demo_trendy_lights.png)
This is a more complex example of using server authentication. It adds several polygons to the map, displaying details about the polygons when a user clicks them. It uses the Google Visualization API for charting, and a technique called AJAX to retrieve new data from the server without needing to refresh the page.
### [cloud-functions](https://github.com/google/earthengine-api/tree/master/demos/cloud-functions)
![assets](https://developers.google.com/static/earth-engine/images/Demo_cloud_functions.png)
This example uses a Node.js [Cloud Function](https://cloud.google.com/functions/) for server authentication. With the Earth Engine API and [TurfJS](http://turfjs.org/), the function creates GeoJSON for a hexbin visualization. The webpage is static (hosted in [Cloud Storage](https://cloud.google.com/storage/)), and displays the hexbin visualization on a map. _Unlike other examples, this demo does not use App Engine._
## Authentication with OAuth2
### [client-auth](https://github.com/google/earthengine-api/tree/master/demos/client-auth)
![assets](https://developers.google.com/static/earth-engine/images/Demo_client_auth.png)
This example demonstrates the OAuth flow for authenticating from the client. Specifically, a user will need to authenticate as themselves (meaning they are already an Earth Engine user) to use the app. To make that work, JavaScript origins and authorized redirects need to be set from the Developers Console.
### [map-layer](https://github.com/google/earthengine-api/tree/master/demos/map-layer)
![assets](https://developers.google.com/static/earth-engine/images/Demo_map_layer_overlay.png)
This example also uses the client authorization flow. It demonstrates using `ee.MapLayerOverlay` to add Earth Engine data to the map with a callback function to keep track how many tiles have been loaded. (All of the mapping functionality in this demo can be done with mapids generated on the server, as is done in the server-auth demo).
### [polygon-drawing](https://github.com/google/earthengine-api/tree/master/demos/polygon-drawing)
![assets](https://developers.google.com/static/earth-engine/images/Demo_polygon_drawing.png)
This example also uses the client authorization flow. The example demonstrates functionality to draw a polygon over the map, perform a reduce region with the polygon in Earth Engine, and display the polygon mean. (All of the mapping functionality in this demo can be done with mapids generated on the server, as is done in the server-auth demo).
### [export-to-drive](https://github.com/google/earthengine-api/tree/master/demos/export-to-drive)
![assets](https://developers.google.com/static/earth-engine/images/Demo_export_to_drive.png)
This is a relatively complex example. It demonstrates the use of two authentication flows, one for Earth Engine using the application's credentials and one for Google Drive using the user's personal credentials. It allows the user to select a layer, draw a polygon and export the layer clipped by the polygon to Drive.
Was this helpful?
