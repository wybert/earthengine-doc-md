 
#  Export.image.toAsset 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/export-image-toasset#examples)


Creates a batch task to export an Image as a raster to an Earth Engine asset. Tasks can be started from the Tasks tab. 
Usage| Returns  
---|---  
`Export.image.toAsset(image,  _description_, _assetId_, _pyramidingPolicy_, _dimensions_, _region_, _scale_, _crs_, _crsTransform_, _maxPixels_, _shardSize_, _priority_)`  
Argument|  Type| Details  
---|---|---  
`image`| Image| The image to export.  
`description`| String, optional| A human-readable name of the task. Defaults to "myExportImageTask".  
`assetId`| String, optional| The destination asset ID.  
`pyramidingPolicy`| Object, optional| The pyramiding policy to apply to each band in the image, keyed by band name. Values must be one of: mean, sample, min, max, or mode. Defaults to "mean". A special key, ".default" may be used to change the default for all bands.  
`dimensions`| Number|String, optional| The dimensions to use for the exported image. Takes either a single positive integer as the maximum dimension or "WIDTHxHEIGHT" where WIDTH and HEIGHT are each positive integers.  
`region`| Geometry.LinearRing|Geometry.Polygon|String, optional| A LinearRing, Polygon, or coordinates representing region to export. These may be specified as the Geometry objects or coordinates serialized as a string.  
`scale`| Number, optional| Resolution in meters per pixel. Defaults to 1000.  
`crs`| String, optional| CRS to use for the exported image.  
`crsTransform`| List, optional| Affine transform to use for the exported image. Requires "crs" to be defined.  
`maxPixels`| Number, optional| Restrict the number of pixels in the export. By default, you will see an error if the export exceeds 1e8 pixels. Setting this value explicitly allows one to raise or lower this limit.  
`shardSize`| Number, optional| Size in pixels of the tiles in which this image will be computed. Defaults to 256.  
`priority`| Number, optional| The priority of the task within the project. Higher priority tasks are scheduled sooner. Must be an integer between 0 and 9999. Defaults to 100.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/export-image-toasset#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/export-image-toasset#colab-python-sample) More
```
// A Landsat 8 surface reflectance image.
varimage=ee.Image('LANDSAT/LC08/C02/T1_L2/LC08_044034_20210508')
.select(['SR_B.']);// reflectance bands
// A region of interest.
varregion=ee.Geometry.BBox(-122.24,37.13,-122.11,37.20);
// Set the export "scale" and "crs" parameters.
Export.image.toAsset({
image:image,
description:'image_export',
assetId:'projects/<project-name>/assets/<asset-name>',// <> modify these
region:region,
scale:30,
crs:'EPSG:5070'
});
// Use the "crsTransform" export parameter instead of "scale" for more control
// over the output grid. Here, "crsTransform" is set to align the output grid
// with the grid of another dataset. To view an image's CRS transform:
// print(image.projection())
Export.image.toAsset({
image:image,
description:'image_export_crstransform',
assetId:'projects/<project-name>/assets/<asset-name>',// <> modify these
region:region,
crsTransform:[30,0,-2493045,0,-30,3310005],
crs:'EPSG:5070'
});
// If the export has more than 1e8 pixels, set "maxPixels" higher.
Export.image.toAsset({
image:image,
description:'image_export_maxpixels',
assetId:'projects/<project-name>/assets/<asset-name>',// <> modify these
region:region,
scale:30,
crs:'EPSG:5070',
maxPixels:1e13
});
// The default "pyramidingPolicy" is mean. If data are categorical,
// consider mode.
Export.image.toAsset({
image:image.select('SR_B5'),
description:'image_export_pyramiding',
assetId:'projects/<project-name>/assets/<asset-name>',// <> modify these
region:region,
scale:30,
crs:'EPSG:5070',
pyramidingPolicy:{SR_B5:'mode'}
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
task = ee.batch.Export.image.toAsset(
  image=image,
  description='image_export',
  assetId='projects/<project-name>/assets/<asset-name>', # <> modify these
  region=region,
  scale=30,
  crs='EPSG:5070'
)
task.start()
# Use the "crsTransform" export parameter instead of "scale" for more control
# over the output grid. Here, "crsTransform" is set to align the output grid
# with the grid of another dataset. To view an image's CRS transform:
# print(image.projection().getInfo())
task = ee.batch.Export.image.toAsset(
  image=image,
  description='image_export_crstransform',
  assetId='projects/<project-name>/assets/<asset-name>', # <> modify these
  region=region,
  crsTransform=[30, 0, -2493045, 0, -30, 3310005],
  crs='EPSG:5070'
)
task.start()
# If the export has more than 1e8 pixels, set "maxPixels" higher.
task = ee.batch.Export.image.toAsset(
  image=image,
  description='image_export_maxpixels',
  assetId='projects/<project-name>/assets/<asset-name>', # <> modify these
  region=region,
  scale=30,
  crs='EPSG:5070',
  maxPixels=1e13
)
task.start()
# The default "pyramidingPolicy" is mean. If data are categorical,
# consider mode.
task = ee.batch.Export.image.toAsset(
  image=image.select('SR_B5'),
  description='image_export_pyramiding',
  assetId='projects/<project-name>/assets/<asset-name>', # <> modify these
  region=region,
  scale=30,
  crs='EPSG:5070',
  pyramidingPolicy={'SR_B5': 'mode'}
)
task.start()
```

