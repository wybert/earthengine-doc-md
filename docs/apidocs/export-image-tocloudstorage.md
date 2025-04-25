 
#  Export.image.toCloudStorage 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/export-image-tocloudstorage#examples)


Creates a batch task to export an Image as a raster to Google Cloud Storage. Tasks can be started from the Tasks tab. 
"crsTransform", "scale", and "dimensions" are mutually exclusive.
Usage| Returns  
---|---  
`Export.image.toCloudStorage(image,  _description_, _bucket_, _fileNamePrefix_, _dimensions_, _region_, _scale_, _crs_, _crsTransform_, _maxPixels_, _shardSize_, _fileDimensions_, _skipEmptyTiles_, _fileFormat_, _formatOptions_, _priority_)`  
Argument|  Type| Details  
---|---|---  
`image`| Image| The image to export.  
`description`| String, optional| A human-readable name of the task. Defaults to "myExportImageTask".  
`bucket`| String, optional| The Cloud Storage destination bucket.  
`fileNamePrefix`| String, optional| The string used as the output's prefix. A trailing "/" indicates a path. Defaults to the task's description.  
`dimensions`| Number|String, optional| The dimensions to use for the exported image. Takes either a single positive integer as the maximum dimension or "WIDTHxHEIGHT" where WIDTH and HEIGHT are each positive integers.  
`region`| Geometry.LinearRing|Geometry.Polygon|String, optional| A LinearRing, Polygon, or coordinates representing region to export. These may be specified as the Geometry objects or coordinates serialized as a string.  
`scale`| Number, optional| Resolution in meters per pixel. Defaults to 1000.  
`crs`| String, optional| CRS to use for the exported image.  
`crsTransform`| List, optional| Affine transform to use for the exported image. Requires "crs" to be defined.  
`maxPixels`| Number, optional| Restrict the number of pixels in the export. By default, you will see an error if the export exceeds 1e8 pixels. Setting this value explicitly allows one to raise or lower this limit.  
`shardSize`| Number, optional| Size in pixels of the tiles in which this image will be computed. Defaults to 256.  
`fileDimensions`| List, optional| The dimensions in pixels of each image file, if the image is too large to fit in a single file. May specify a single number to indicate a square shape, or an array of two dimensions to indicate (width,height). Note that the image will still be clipped to the overall image dimensions. Must be a multiple of shardSize.  
`skipEmptyTiles`| Boolean, optional| If true, skip writing empty (i.e. fully-masked) image tiles. Defaults to false. Only supported on GeoTIFF exports.  
`fileFormat`| String, optional| The string file format to which the image is exported. Currently only 'GeoTIFF' and 'TFRecord' are supported, defaults to 'GeoTIFF'.  
`formatOptions`| ImageExportFormatConfig, optional| A dictionary of string keys to format-specific options. For 'GeoTIFF': 'cloudOptimized' (Boolean), 'noData' (float). For 'TFRecord': see https://developers.google.com/earth-engine/guides/tfrecord#formatoptions  
`priority`| Number, optional| The priority of the task within the project. Higher priority tasks are scheduled sooner. Must be an integer between 0 and 9999. Defaults to 100.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/export-image-tocloudstorage#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/export-image-tocloudstorage#colab-python-sample) More
```
// A Landsat 8 surface reflectance image.
varimage=ee.Image('LANDSAT/LC08/C02/T1_L2/LC08_044034_20210508')
.select(['SR_B.']);// reflectance bands
// A region of interest.
varregion=ee.Geometry.BBox(-122.24,37.13,-122.11,37.20);
// Set the export "scale" and "crs" parameters.
Export.image.toCloudStorage({
image:image,
description:'image_export',
bucket:'gcs-bucket-name',
fileNamePrefix:'image_export',
region:region,
scale:30,
crs:'EPSG:5070'
});
// Use the "crsTransform" export parameter instead of "scale" for more control
// over the output grid. Here, "crsTransform" is set to align the output grid
// with the grid of another dataset. To view an image's CRS transform:
// print(image.projection())
Export.image.toCloudStorage({
image:image,
description:'image_export_crstransform',
bucket:'gcs-bucket-name',
fileNamePrefix:'image_export_crstransform',
region:region,
crsTransform:[30,0,-2493045,0,-30,3310005],
crs:'EPSG:5070'
});
// If the export has more than 1e8 pixels, set "maxPixels" higher.
Export.image.toCloudStorage({
image:image,
description:'image_export_maxpixels',
bucket:'gcs-bucket-name',
fileNamePrefix:'image_export_maxpixels',
region:region,
scale:30,
crs:'EPSG:5070',
maxPixels:1e13
});
// Export a Cloud Optimized GeoTIFF (COG) by setting the "cloudOptimized"
// parameter to true.
Export.image.toCloudStorage({
image:image,
description:'image_export_cog',
bucket:'gcs-bucket-name',
fileNamePrefix:'image_export_cog',
region:region,
scale:30,
crs:'EPSG:5070',
formatOptions:{
cloudOptimized:true
}
});
// Define a nodata value and replace masked pixels with it using "unmask".
// Set the "sameFootprint" parameter as "false" to include pixels outside of the
// image geometry in the unmasking operation.
varnoDataVal=-9999;
varunmaskedImage=image.unmask({value:noDataVal,sameFootprint:false});
// Use the "noData" key in the "formatOptions" parameter to set the nodata value
// (GeoTIFF format only).
Export.image.toDrive({
image:unmaskedImage,
description:'image_export_nodata',
bucket:'gcs-bucket-name',
fileNamePrefix:'image_export_nodata',
region:image.geometry(),// full image bounds
scale:2000,// large scale for minimal demo
crs:'EPSG:5070',
fileFormat:'GeoTIFF',
formatOptions:{
noData:noDataVal
}
});
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# A Landsat 8 surface reflectance image.
image = ee.Image(
  'LANDSAT/LC08/C02/T1_L2/LC08_044034_20210508'
).select(['SR_B.']) # reflectance bands
# A region of interest.
region = ee.Geometry.BBox(-122.24, 37.13, -122.11, 37.20)
# Set the export "scale" and "crs" parameters.
task = ee.batch.Export.image.toCloudStorage(
  image=image,
  description='image_export',
  bucket='gcs-bucket-name',
  fileNamePrefix='image_export',
  region=region,
  scale=30,
  crs='EPSG:5070'
)
task.start()
# Use the "crsTransform" export parameter instead of "scale" for more control
# over the output grid. Here, "crsTransform" is set to align the output grid
# with the grid of another dataset. To view an image's CRS transform:
# print(image.projection().getInfo())
task = ee.batch.Export.image.toCloudStorage(
  image=image,
  description='image_export_crstransform',
  bucket='gcs-bucket-name',
  fileNamePrefix='image_export_crstransform',
  region=region,
  crsTransform=[30, 0, -2493045, 0, -30, 3310005],
  crs='EPSG:5070'
)
task.start()
# If the export has more than 1e8 pixels, set "maxPixels" higher.
task = ee.batch.Export.image.toCloudStorage(
  image=image,
  description='image_export_maxpixels',
  bucket='gcs-bucket-name',
  fileNamePrefix='image_export_maxpixels',
  region=region,
  scale=30,
  crs='EPSG:5070',
  maxPixels=1e13
)
task.start()
# Export a Cloud Optimized GeoTIFF (COG) by setting the "cloudOptimized"
# parameter to true.
task = ee.batch.Export.image.toCloudStorage(
  image=image,
  description='image_export_cog',
  bucket='gcs-bucket-name',
  fileNamePrefix='image_export_cog',
  region=region,
  scale=30,
  crs='EPSG:5070',
  formatOptions={
    'cloudOptimized': True
  }
)
task.start()
# Define a nodata value and replace masked pixels with it using "unmask".
# Set the "sameFootprint" parameter as "false" to include pixels outside of the
# image geometry in the unmasking operation.
nodata_val = -9999
unmasked_image = image.unmask(value=nodata_val, sameFootprint=False)
# Use the "noData" key in the "formatOptions" parameter to set the nodata value
# (GeoTIFF format only).
task = ee.batch.Export.image.toDrive(
  image=unmasked_image,
  description='image_export_nodata',
  bucket='gcs-bucket-name',
  fileNamePrefix='image_export_nodata',
  region=image.geometry(), # full image bounds
  scale=2000, # large scale for minimal demo
  crs='EPSG:5070',
  fileFormat='GeoTIFF',
  formatOptions={
    'noData': nodata_val
  }
)
task.start()
```

