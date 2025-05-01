 
#  Objects and Methods Overview 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
The Earth Engine API is composed of objects and methods. Objects represent data types such as raster images, vector features, numbers, and strings. Each of these objects belongs to a specific class, and each class has a strict set of functions available to it.
Objects and methods are combined in workflow scripts and sent to Earth Engine servers for processing. Learn about common object classes and their methods by clicking on the following cards to see example procedures.
The full list of Earth Engine classes and their methods can be found in the **Client Libraries** section of the [API Reference Guide](https://developers.google.com/earth-engine/apidocs) (e.g. [`ee.Image.add`](https://developers.google.com/earth-engine/apidocs/ee-date-advance)). The same reference information is also available under the JavaScript Code Editor [**Docs**](https://developers.google.com/earth-engine/guides/playground#api-reference-docs-tab) tab.
## Common Earth Engine object classes
[ ![](https://developers.google.com/static/earth-engine/images/classes_image.png) ](https://developers.google.com/earth-engine/guides/image_overview)
### [Image ](https://developers.google.com/earth-engine/guides/image_overview)
The fundamental raster data type in Earth Engine. 
[ ![](https://developers.google.com/static/earth-engine/images/classes_image_collection.png) ](https://developers.google.com/earth-engine/guides/ic_creating)
### [ImageCollection ](https://developers.google.com/earth-engine/guides/ic_creating)
A set of images. 
[ ![](https://developers.google.com/static/earth-engine/images/classes_geometry.png) ](https://developers.google.com/earth-engine/guides/geometries)
### [Geometry ](https://developers.google.com/earth-engine/guides/geometries)
The fundamental vector data type in Earth Engine. 
[ ![](https://developers.google.com/static/earth-engine/images/classes_feature.png) ](https://developers.google.com/earth-engine/guides/features)
### [Feature ](https://developers.google.com/earth-engine/guides/features)
A geometry with attributes. 
[ ![](https://developers.google.com/static/earth-engine/images/classes_feature_collection.png) ](https://developers.google.com/earth-engine/guides/feature_collections)
### [FeatureCollection ](https://developers.google.com/earth-engine/guides/feature_collections)
A set of features. 
[ ![](https://developers.google.com/static/earth-engine/images/classes_reducer.png) ](https://developers.google.com/earth-engine/guides/reducers_intro)
### [Reducer ](https://developers.google.com/earth-engine/guides/reducers_intro)
An object used to compute statistics or perform aggregations. 
[ ![](https://developers.google.com/static/earth-engine/images/classes_join.png) ](https://developers.google.com/earth-engine/guides/joins_intro)
### [Join ](https://developers.google.com/earth-engine/guides/joins_intro)
Combine datasets (Image or Feature collections) based on time, location, or an attribute property. 
[ ![](https://developers.google.com/static/earth-engine/images/classes_array.png) ](https://developers.google.com/earth-engine/guides/arrays_intro)
### [Array ](https://developers.google.com/earth-engine/guides/arrays_intro)
An object for multi-dimensional analyses. 
[ ![](https://developers.google.com/static/earth-engine/images/classes_chart.png) ](https://developers.google.com/earth-engine/guides/charts_overview)
### [Chart ](https://developers.google.com/earth-engine/guides/charts_overview)
An object for charting properties and spatiotemporal reductions. 
