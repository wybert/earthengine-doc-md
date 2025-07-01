 
#  Importing Raster Data
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Uploading image assets](https://developers.google.com/earth-engine/guides/image_upload#uploading-image-assets)
    * [GeoTIFF](https://developers.google.com/earth-engine/guides/image_upload#geotiff)
    * [GeoTIFF Compression](https://developers.google.com/earth-engine/guides/image_upload#geotiff-compression)
    * [TFRecord](https://developers.google.com/earth-engine/guides/image_upload#tfrecord)
    * [Properties editing](https://developers.google.com/earth-engine/guides/image_upload#properties-editing)
    * [Advanced options](https://developers.google.com/earth-engine/guides/image_upload#advanced-options)
    * [Tiled uploads](https://developers.google.com/earth-engine/guides/image_upload#tiled-uploads)


You can use the [Asset Manager](https://developers.google.com/earth-engine/guides/asset_manager) or [command line interface (CLI)](https://developers.google.com/earth-engine/guides/command_line#upload) to upload image or other georeferenced raster datasets in GeoTIFF or TFRecord format. (See [Importing Vector Data](https://developers.google.com/earth-engine/guides/table_upload) for details on importing vectors using the Code Editor.)
## Uploading image assets
### GeoTIFF
In the Code Editor, you can upload [GeoTIFF](https://github.com/OSGeo/libgeotiff) image files up to 10 GB in size to your Earth Engine user folder. (For larger files, use the [command-line upload](https://developers.google.com/earth-engine/command_line#upload) option.)
To upload a GeoTIFF using the Code Editor, select the Assets tab in the upper left corner, click the ![](https://developers.google.com/static/earth-engine/images/Asset_manager_new_button.png) button, then select **Image upload**. Earth Engine presents an upload dialog which should look similar to Figure 1. Click the **SELECT** button and navigate to a GeoTIFF on your local file system.
Give the image an appropriate asset ID (which doesn't already exist) in your user folder. If you'd like to upload the image into an existing folder or collection, prefix the asset ID with the folder or collection ID, for example `projects/myproject/folder-or-collection-id/new-asset`.
Click **UPLOAD** to start the upload.
![assets](https://developers.google.com/static/earth-engine/images/Asset_manager_upload_anon.png) Figure 1. The asset manager image upload dialog
Once you have started the upload, an "Asset ingestion" task appears on the Tasks tab at the right side of the Code Editor. Hovering over the task in the task manager shows a **?** icon which you can use to check the upload status. To cancel an upload, click the spinning icon ![](https://developers.google.com/static/earth-engine/images/Playground_button_running.gif) next to the task. Once the ingestion is complete, the asset will appear in your user folder with a image icon.
### GeoTIFF Compression
GeoTIFF files can be compressed with DEFLATE, JPEG-XL/JXL, LERC, LERC_DEFLATE, LERC_ZSTD, LZMA, LZW, WEBP, or ZSTD.
Recommendations for the best upload experience for large files:
  * **Best choice:** ZSTD offers a good balance of speed and compression.
  * **Avoid:** LZMA can be very slow despite good compression.
  * **Uncompressed files:** Will result in larger files and longer upload times.
  * **Lossy compression (e.g., JPEG):** May alter pixel values. Use lossless compression (e.g., DEFLATE, LZMA, LZW, ZSTD) rather than lossy, unless you understand the potential impact on your data.


### TFRecord
To upload an image from a TFRecord file, you must have the associated mixer file that was generated when you exported imagery on which you performed inference. See [the export page](https://developers.google.com/earth-engine/guides/exporting#mixer) for details on the mixer file. More specifically, to import predictions (as an image) made on exported imagery,
  1. Export imagery into one or more TFRecord files.
  2. Perform inference on the imagery (i.e. `model.predict()`).
  3. Write the output of `model.predict()` into a TFRecord file. The predictions should be in the _same order_ as the image exports on which you performed inference. Order can be enforced by a sort of the filenames produced by the export. See [the large file exports section](https://developers.google.com/earth-engine/guides/exporting#large-file-exports) for details.
  4. Upload the TFRecord file(s) and associated mixer to Earth Engine.


### Properties editing
Edit asset metadata by specifying one or more metadata properties. In the **Properties** menu, click **Add property** to define a property name and value (Figure 2). The value can be a string or a number. Enter strings without quotes. To format a number as a string, enter a single quote (`'`) before the number.
By default, a `system:time_start` property is added with no value. This property is used by Earth Engine when applying `ImageCollection` date filters. Enter either a date in the format shown in Figure 2, or a number representing milliseconds since January 1, 1970. (See [the glossary](https://developers.google.com/earth-engine/glossary) for more information on timestamps in Earth Engine). The Asset Manager interprets a number entered as the value for a property named `system:time_start` or `system:time_end` as milliseconds and formats it as a date.
Click the delete icon to remove a property.
### Advanced options
In the **Advanced** menu, choose the pyramiding policy and the masking mode for your data.
The [pyramiding policy](https://en.wikipedia.org/wiki/Pyramid_\(image_processing\)) specifies how Earth Engine generates lower resolution versions of the image. Learn more about how Earth Engine handles multiple resolutions in the [scale doc](https://developers.google.com/earth-engine/guides/scale). Choose a 'Mean', 'Min', or 'Max' pyramiding policy to compute lower resolution levels of the image pyramid as the mean, minimum or maximum of each 2x2 group of higher resolution pixels. This is a suitable option for continuous-valued images. For categorical (e.g. land cover) or QA data, choose a 'Sample' (the upper left pixel) or 'Mode' (most frequently occurring value, or sample if there is no mode) pyramiding policy.
The masking mode indicates how the uploaded image is [masked](https://developers.google.com/earth-engine/guides/getstarted#masking) (if at all). To specify a no-data value, select 'No-data value' and enter the value. Pixels with this value will be masked in the uploaded image. This value is applied to every band of the image independently. To use the last band of your image as a mask for the other image bands, select 'Use last band as alpha band'. The [alpha band](https://en.wikipedia.org/wiki/Alpha_compositing) should be an unsigned 8-bit band where 0 is masked (completely transparent) data and 255 is completely opaque.
### Tiled uploads
To upload a single image as multiple tiles, where each tile is stored in a different source file, click **Add another file** to add additional files to the upload. Earth Engine will combine the tiles to create a single image in your user folder. 
There are a few constraints on the types of files that can be uploaded into an image asset. In particular:
  1. The images must have the same number of bands, bit depth, projection, resolution and fill values.
  2. The offset from one file to the next must be an integer multiple of the pixel size. 
  3. Gaps between tiles will be filled with masked pixels in the final image, so the tiles should ideally be adjacent and not sparsely spread out. Images with gaps taking up >99% of the image area won't be ingested.


