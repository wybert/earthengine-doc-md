 
#  Concepts
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Authentication](https://developers.google.com/earth-engine/reference/Concepts#authentication)
  * [Assets](https://developers.google.com/earth-engine/reference/Concepts#assets)
  * [Pixels and Map Projections](https://developers.google.com/earth-engine/reference/Concepts#pixels-and-map-projections)
  * [Collections and Folders](https://developers.google.com/earth-engine/reference/Concepts#collections-and-folders)


This API provides simple, uniform access to a wide variety geospatial image data. By _geospatial_ we mean that the data is associated with locations on the Earth's surface. By _image data_ we mean data that is structured as a uniform grid of pixel values, much like a traditional image.
The most familiar example of this type of data is satellite imagery, much like users are accustomed to seeing in Google Maps and Earth. However, many other datasets have the same structure, including for example gridded weather and climate datasets, terrain and land cover datasets, and population density datasets.
## Authentication
The Earth Engine API uses the **OAuth 2.0** protocol for authentication and authorization. There are convenient libraries for using OAuth 2.0 to issue API calls in a wide range of languages. If you have not used OAuth 2.0 to access Google APIs before, you may wish to familiarize yourself with the documentation on [Using OAuth 2.0 to Access Google APIs](https://developers.google.com/identity/protocols/OAuth2).
This API uses the Earth Engine OAuth 2.0 **scope** `https://www.googleapis.com/auth/earthengine.readonly`. If you are configuring service account credentials yourself then you will need to request that scope explicitly. If you are using the default application credentials available in Compute Engine virtual machine instances, you will need to configure your VM instance to request that scope.
## Assets
At the heart of the Earth Engine data model is a filesystem-like structure of **assets**. There are three primary types of assets, described in more detail below: geospatial raster data itself is stored in **images** , images can be grouped into large **collections** , and images and collections are further organized in a hierarchy of **folders**.
For example, the following path describes a particular Landsat image:
```
LANDSAT/LC8_L1T/LC81180562013193LGN00

```

In this example, `LANDSAT` is a top-level folder that contains all the Landsat data, `LC8_L1T` identifies a particular collection of calibrated and terrain-corrected Landsat 8 images, and `LC81180562013193LGN00` identifies a particular image within that collection. Asset paths may contain letters, numbers, underscores, and hyphens, separated by forward slashes.
Each image has metadata that makes it easy to identify data of interest. These per-image metadata properties typically include:
  * The footprint geometry of the image, such as the spatial extent of a satellite image or terrain dataset.
  * The timestamp of the image, such as the satellite image acquisition time, or the day or month in a climate model dataset.
  * Arbitrary key/value properties, such as the estimated cloud cover percentage of a Landsat satellite image.


## Pixels and Map Projections
In Earth Engine each image consists of one or more **bands** of data. These might correspond to the red, green, and blue bands of an ordinary RGB satellite image, or they might correspond to something completely different, such as temperature and precipitation in a weather dataset. The **pixels** in each band have a particular data type, e.g. `uint8` or `float32`.
Pixels in a pixel grid correspond to points on the Earth's surface via a mathematical function known as a **map projection**. This relationship typically has two components. First a **coordinate reference system** (CRS) defines 2D coordinates that represent points on the curved surface of the Earth. Different coordinate reference systems have different properties that make them appropriate to use with different types of data in different applications. Coordinate reference systems are typically identified using [standard identifier codes](http://epsg.io/); common examples are [equirectangular](https://en.wikipedia.org/wiki/Equirectangular_projection), [web Mercator](https://en.wikipedia.org/wiki/Web_Mercator), and [UTM](https://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system) coordinates.
Pixel coordinates are then typically related to the spatial coordinate reference system via an **affine transformation** that controls the physical scale and origin of the pixel grid. In Earth Engine we store a **pyramid** of data for each image: the base level of the pyramid contains the original data in its native resolution, and higher levels of the pyramid store reduced-resolution overview data. These levels of the pyramid are described by affine transformations whose scales differ by successive factors of two.
## Collections and Folders
Images often come in large **collections** of data, such as a collection of all images acquired by a particular satellite, or a collection of global temperature estimates over time. Earth Engine builds metadata indexes that allow you to **filter** or **query** the images in collections based on their metadata, including filtering by location and time. Typically, all images within a single collection have the same structure, i.e. the same bands and the same metadata properties.
Images and collections are themselves organized into a hierarchy of **folders**. A folder is much like an ordinary folder or directory in a traditional filesystem: it is a simple container for other assets, i.e. for images, collections, and other folders. Not all images are contained in collections: some datasets, such as a particular global terrain model, may consist of only a single image. Regardless, every asset is uniquely identified by a particular path that identifies its location in the Earth Engine data catalog.
