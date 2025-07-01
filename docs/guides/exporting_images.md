 
#  Exporting Images
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Example Setup](https://developers.google.com/earth-engine/guides/exporting_images#example_setup)
    * [Setting scale](https://developers.google.com/earth-engine/guides/exporting_images#setting_scale)
  * [to Drive](https://developers.google.com/earth-engine/guides/exporting_images#to_drive)
  * [to Cloud Storage](https://developers.google.com/earth-engine/guides/exporting_images#to_cloud_storage)
  * [to Asset](https://developers.google.com/earth-engine/guides/exporting_images#to_asset)
  * [Configuration parameters](https://developers.google.com/earth-engine/guides/exporting_images#configuration_parameters)
    * [formatOptions parameter](https://developers.google.com/earth-engine/guides/exporting_images#formatoptions_parameter)
  * [maxPixels](https://developers.google.com/earth-engine/guides/exporting_images#maxpixels)
  * [Large file exports](https://developers.google.com/earth-engine/guides/exporting_images#large_file_exports)
  * [Exporting images as they appear in the Code Editor](https://developers.google.com/earth-engine/guides/exporting_images#exporting_images_as_they_appear_in_the_code_editor)


You can export images from Earth Engine in [GeoTIFF](https://github.com/OSGeo/libgeotiff) or [TFRecord format](https://www.tensorflow.org/api_guides/python/python_io#TFRecords_Format_Details). See [Configuration Parameters](https://developers.google.com/earth-engine/guides/exporting#configuration_parameters) for more output options.
## Example Setup
Start by defining the image data that will be exported:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/exporting_images#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/exporting_images#colab-python-sample) More
```
// Load a landsat image and select three bands.
varlandsat=ee.Image('LANDSAT/LC08/C02/T1_TOA/LC08_123032_20140515')
.select(['B4','B3','B2']);
// Create a geometry representing an export region.
vargeometry=ee.Geometry.Rectangle([116.2621,39.8412,116.4849,40.01236]);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Load a landsat image and select three bands.
landsat = ee.Image('LANDSAT/LC08/C02/T1_TOA/LC08_123032_20140515').select(
  ['B4', 'B3', 'B2']
)
# Create a geometry representing an export region.
geometry = ee.Geometry.Rectangle([116.2621, 39.8412, 116.4849, 40.01236])
```

Next define the [projection](https://developers.google.com/earth-engine/guides/projections) parameters that will be used in the following exports. We use the `crs` parameter to specify the coordinate system, and the `crsTransform` parameter to precisely specify the pixel grid. The `crsTransform` parameter is a list of parameters from an affine transformation matrix in row-major order `[xScale, xShearing, xTranslation, yShearing, yScale,     yTranslation]`. An image's origin is defined by the `xTranslation` and `yTranslation` values, and the image's pixel size is defined by the `xScale` and `yScale` values. See [examples of affine matrices](https://en.wikipedia.org/wiki/Affine_transformation#Image_transformation).
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/exporting_images#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/exporting_images#colab-python-sample) More
```
// Retrieve the projection information from a band of the original image.
// Call getInfo() on the projection to request a client-side object containing
// the crs and transform information needed for the client-side Export function.
varprojection=landsat.select('B2').projection().getInfo();
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Retrieve the projection information from a band of the original image.
# Call getInfo() on the projection to request a client-side object containing
# the crs and transform information needed for the client-side Export function.
projection = landsat.select('B2').projection().getInfo()
```
**Warning:** The `scale` parameter can be subtly misleading. If you're trying to match an existing projection exactly, you shouldn't use `scale` - see the [following section](https://developers.google.com/earth-engine/guides/exporting_images#setting_scale) for details.
### Setting `scale`
As a shortcut, you can specify a `scale` parameter and Earth Engine will calculate a `crsTransform` parameter for you. However, simply setting the scale of an image does not specify the origin of the projection, and may result in an image that is shifted relative to another image with the same pixel size!
The reason for the potential shift is that the `scale` parameter is used to populate the `xScale` and `yScale` values of the `crsTransform`, but the `xTranslation` and `yTranslation` values are calculated so that if they are divided by the corresponding `xScale` and `yScale` values the remainder will be zero. These parameters specify a pixel grid where the projection's origin is at the corner of a pixel. This convention differs from the translation parameters used by some data providers, which use grids that are offset from the projection's origin. For example, Landsat images provided by USGS use translation parameters that are offset by a 1/2 pixel from the projection's origin (15m offset for the 30m bands) while Sentinel-2 images provided by ESA use translation parameters that are aligned with the projection's origin. If the `crsTransform` specified in an export do not match the `crsTransform` of the original image, the output pixels will be resampled (using nearest neighbor by default), which will make the resulting image be shifted relative to the original image.
To sum up, if you need to match the exported image's pixels to a specific image, make sure to use the `crs` and `crsTransform` parameters for full control of the grid.
## to Drive
To export an image to your Drive account, use `Export.image.toDrive()`. For example, to export portions of a Landsat image, define a region to export, then call `Export.image.toDrive()`:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/exporting_images#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/exporting_images#colab-python-sample) More
```
// Export the image, specifying the CRS, transform, and region.
Export.image.toDrive({
image:landsat,
description:'imageToDriveExample_transform',
crs:projection.crs,
crsTransform:projection.transform,
region:geometry
});
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Export the image, specifying the CRS, transform, and region.
task = ee.batch.Export.image.toDrive(
  image=landsat,
  description='imageToDriveExample_transform',
  crs=projection['crs'],
  crsTransform=projection['transform'],
  region=geometry,
)
task.start()
```

When this code is run, an export task will be created in the Code Editor **Tasks** tab. Click the **Run** button next to the task to start it. (Learn more about the Task Manager from the [Code Editor section](https://developers.google.com/earth-engine/guides/playground#tasks-tab)). The image will be created in your Drive account with the specified `fileFormat`.
## to Cloud Storage
To export an image to a Google Cloud Storage bucket, use `Export.image.toCloudStorage()`. To export the Landsat image in the previous example to Cloud Storage instead of Drive, use:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/exporting_images#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/exporting_images#colab-python-sample) More
```
// Export the image to Cloud Storage.
Export.image.toCloudStorage({
image:landsat,
description:'imageToCloudExample',
bucket:'your-bucket-name',
fileNamePrefix:'exampleExport',
crs:projection.crs,
crsTransform:projection.transform,
region:geometry
});
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Export the image to Cloud Storage.
task = ee.batch.Export.image.toCloudStorage(
  image=landsat,
  description='imageToCloudExample',
  bucket='your-bucket-name',
  fileNamePrefix='exampleExport',
  crs=projection['crs'],
  crsTransform=projection['transform'],
  region=geometry,
)
task.start()
```

As with exports to Drive, start the export from the **Tasks** tab. The Cloud Storage bucket location can affect performance and storage costs, see the [FAQ entry on location considerations](https://developers.google.com/earth-engine/faq#what_cloud_storage_bucket_location_should_i_use_to_store_cog_assets) for more information.
## to Asset
To export an image to an asset in your Earth Engine assets folder, use `Export.image.toAsset()`. To manage your Earth Engine assets, or check how much of your storage quota is in use, use the [Asset Manager](https://developers.google.com/earth-engine/guides/asset_manager). The following example illustrates exporting portions of a Landsat image using different pyramiding policies for the same band. The pyramiding policy indicates how Earth Engine computes lower-resolution versions of the asset. Learn more about how Earth Engine handles multiple resolutions in the [scale doc](https://developers.google.com/earth-engine/guides/scale).
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/exporting_images#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/exporting_images#colab-python-sample) More
```
// Get band 4 from the Landsat image, copy it.
varband4=landsat.select('B4').rename('b4_mean')
.addBands(landsat.select('B4').rename('b4_sample'))
.addBands(landsat.select('B4').rename('b4_max'));
// Export the image to an Earth Engine asset.
Export.image.toAsset({
image:band4,
description:'imageToAssetExample',
assetId:'exampleExport',
crs:projection.crs,
crsTransform:projection.transform,
region:geometry,
pyramidingPolicy:{
'b4_mean':'mean',
'b4_sample':'sample',
'b4_max':'max'
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
# Get band 4 from the Landsat image, copy it.
band_4 = (
  landsat.select('B4')
  .rename('b4_mean')
  .addBands(landsat.select('B4').rename('b4_sample'))
  .addBands(landsat.select('B4').rename('b4_max'))
)
# Export the image to an Earth Engine asset.
task = ee.batch.Export.image.toAsset(
  image=band_4,
  description='imageToAssetExample',
  assetId='projects/your-project/assets/exampleExport',
  crs=projection['crs'],
  crsTransform=projection['transform'],
  region=geometry,
  pyramidingPolicy={
    'b4_mean': 'mean',
    'b4_sample': 'sample',
    'b4_max': 'max',
  },
)
task.start()
```

You can provide a default pyramiding policy for every band that isn't explicitly specified by using the `'.default'` key. You may also pass in just the `'.default'` key. For example, to make all bands default to the 'sample' pyramiding policy, use `{'.default': 'sample'}`.
## Configuration parameters
Observe that the dictionary of configuration parameters passed to `Export.image` includes `scale` (in meters) and the export region as an `ee.Geometry`. The exported image will cover the specified region with pixels at the specified scale. If not explicitly specified, the CRS of the output will be taken from the first band of the image to be exported.
You may also specify the `dimensions`, `crs` and/or `crsTransform` of the exported image. See [the glossary](https://developers.google.com/earth-engine/glossary) for more information on `crs` and `crsTransform`. For example, to get a block of pixels precisely aligned to another data source, specify `dimensions`, `crs` and `crsTransform`. To get a block of pixels of predefined size (for example a 256x256 thumbnail image) that covers a region, specify `dimensions` and `region`.
You can specify image output format (if the destination is not `toAsset()`) with the `fileFormat` parameter (`'GeoTIFF'` by default).
### `formatOptions` parameter
Other configuration options are set with the `formatOptions` parameter, which should be a dictionary keyed by other format options, specific to each `fileFormat` as described below.
#### GeoTIFF
##### Cloud optimized GeoTIFF
To export a [cloud optimized GeoTIFF](http://www.cogeo.org/), pass a JavaScript literal for `formatOptions` in which the `cloudOptimized` key is set to **true**. Continuing the previous example:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/exporting_images#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/exporting_images#colab-python-sample) More
```
// Export a cloud-optimized GeoTIFF.
Export.image.toDrive({
image:landsat,
description:'imageToCOGeoTiffExample',
crs:projection.crs,
crsTransform:projection.transform,
region:geometry,
fileFormat:'GeoTIFF',
formatOptions:{
cloudOptimized:true
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
# Export a cloud-optimized GeoTIFF.
task = ee.batch.Export.image.toDrive(
  image=landsat,
  description='imageToCOGeoTiffExample',
  crs=projection['crs'],
  crsTransform=projection['transform'],
  region=geometry,
  fileFormat='GeoTIFF',
  formatOptions={'cloudOptimized': True},
)
task.start()
```

Cloud optimized GeoTIFFs can be reloaded from Cloud Storage into an `Image`. See [the `Image` overview docs](https://developers.google.com/earth-engine/guides/image_overview#images-from-cloud-geotiffs) for details.
##### Nodata
Specify the GeoTIFF nodata value using the `noData` key within the `formatOptions` parameter. For example:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/exporting_images#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/exporting_images#colab-python-sample) More
```
// Set a nodata value and replace masked pixels around the image edge with it.
varnoDataVal=-9999;
landsat=landsat.unmask(noDataVal);
Export.image.toDrive({
image:landsat,
description:'imageNoDataExample',
crs:projection.crs,
scale:2000,// large scale for minimal demo
region:landsat.geometry(),// full image bounds
fileFormat:'GeoTIFF',
formatOptions:{
noData:noDataVal,
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
# Set a nodata value and replace masked pixels around the image edge with it.
no_data_val = -9999
landsat = landsat.unmask(no_data_val)
task = ee.batch.Export.image.toDrive(
  image=landsat,
  description='imageNoDataExample',
  crs=projection['crs'],
  scale=2000, # large scale for minimal demo
  region=landsat.geometry(), # full image bounds
  fileFormat='GeoTIFF',
  formatOptions={'noData': no_data_val},
)
task.start()
```

Note that the nodata value should be inside the valid range for the image's `PixelType`. You can check `PixelType` by [printing image metadata](https://developers.google.com/earth-engine/guides/image_info) and looking at the first band's `data_type` property. You can also set the image's`PixelType` by casting the data to a specific type using image methods `toShort()` or `toInt()`, for example.
#### TFRecord
See the [TFRecord data format](https://developers.google.com/earth-engine/guides/tfrecord#exporting-images) page.
## `maxPixels`
The `maxPixels` parameter is intended to prevent very large exports from inadvertently being created. If the default value is too low for your intended output image, you can increase `maxPixels`. For example:
```
Export.image.toDrive({
image:landsat,
description:'maxPixelsExample',
crs:projection.crs,
crsTransform:projection.transform,
region:geometry,
**maxPixels:1e9**
});
```

## Large file exports
If the output image is large, it will be exported as multiple files. If you are exporting to GeoTIFF(s), the image is split into tiles. The filename of each tile will be in the form `baseFilename-yMin-xMin` where `xMin` and `yMin` are the coordinates of each tile within the overall bounding box of the exported image.
If you are exporting to TFRecord, the files will be appended by `-00000`, `-00001`,... `-0000N` for _N+1_ files. Maintaining this order is important if you intend to perform inference on the files and upload the predictions back to Earth Engine as an image. See [uploading images as TFRecord files](https://developers.google.com/earth-engine/guides/image_upload#tfrecord) for details.
## Exporting images as they appear in the Code Editor
To export imagery as rendered on screen in Earth Engine, create visualization images as demonstrated in the [Visualization images](https://developers.google.com/earth-engine/guides/image_visualization#visualization-images) and the [Compositing and Mosaicking](https://developers.google.com/earth-engine/guides/ic_composite_mosaic) sections. Since the Code Editor uses the `'EPSG:3857'` CRS, specify a CRS of `'EPSG:3857'` in the export to get an image in the same projection as that displayed in the Code Editor map. See [the section on configuring image exports](https://developers.google.com/earth-engine/guides/exporting#configuration-parameters) for details on specifying the resolution and coordinate system of the output.
