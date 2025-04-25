 
#  Overview 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Introduction](https://developers.google.com/earth-engine/reference#introduction)
  * [Audience](https://developers.google.com/earth-engine/reference#audience)
  * [Quota and Limits](https://developers.google.com/earth-engine/reference#quota-and-limits)
  * [Attribution Requirements](https://developers.google.com/earth-engine/reference#attribution-requirements)


## Introduction
This REST API allows you to access Earth Engine's multi-petabyte Public Data Catalog from analysis jobs running in Google Cloud Platform.
![](https://developers.google.com/static/earth-engine/images/africa_rgb.jpg) ![](https://developers.google.com/static/earth-engine/images/landsat_nrg.jpg)
The [Earth Engine Public Data Catalog](https://earthengine.google.com/datasets) includes a range of geospatial data, including satellite data like Landsat, Sentinel-2, and MODIS, as well as geophysical, weather, climate and demographic data. You can use this API to filter these data collections to identify the data you need for your analysis, and then to fetch the pixels you need from any of these datasets on demand. To get started, you can [search for and view documentation about specific datasets](https://developers.google.com/earth-engine/datasets/catalog).
## Audience
The REST API contains new and advanced features that may not be suitable for all users. If you are new to Earth Engine, please get started with the [JavaScript guide](https://developers.google.com/earth-engine/getstarted).
## Quota and Limits
You can see your [quota usage in the Cloud Console](https://console.cloud.google.com/apis/api/earthengine.googleapis.com/quotas).
Individual requests for pixel data are also limited to 16MB in uncompressed data per request, computed as the product of the request dimensions in pixels, the number of image bands requested, and the number of bytes per pixel for each band. Requests are also limited to at most 10000 pixels in either dimension and at most 100 bands.
## Attribution Requirements
You are not required to attribute your use of the Earth Engine API in your application. However, individual datasets may be subject to attribution requirements from the dataset owner. See each dataset's documentation page for details. It is recommended to include legal notices as an independent menu item or as part of an "About" menu item.
Was this helpful?
