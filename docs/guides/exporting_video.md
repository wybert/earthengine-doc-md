 
#  Exporting Video and Animations 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [to Drive](https://developers.google.com/earth-engine/guides/exporting_video#to_drive)
  * [to Cloud Storage](https://developers.google.com/earth-engine/guides/exporting_video#to_cloud_storage)


To export ordered image collections as video, where frames are defined by images in the collection, use `Export.video()`. You can configure the way the `ImageCollection` is turned into video by setting frame rate, scale and dimensions. The video will be encoded as an MP4.
## to Drive
Export video to your Drive account with `Export.video.toDrive()`. For example, the following export makes a video from 20 years of Landsat imagery:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/exporting_video#code-editor-javascript-sample) More
```
// Load a Landsat 5 image collection.
varcollection=ee.ImageCollection('LANDSAT/LT05/C02/T1_TOA')
// San Francisco Bay.
.filter(ee.Filter.eq('WRS_PATH',44))
.filter(ee.Filter.eq('WRS_ROW',34))
// Filter cloudy scenes.
.filter(ee.Filter.lt('CLOUD_COVER',30))
// Get 20 years of imagery.
.filterDate('1991-01-01','2011-12-30')
// Make each image an 8-bit RGB image.
.map(function(image){
returnimage.visualize({bands:['B4','B3','B2'],min:0.02,max:0.35});
});
// Define an area to export.
varpolygon=ee.Geometry.Rectangle([-122.7286,37.6325,-122.0241,37.9592]);
// Export (change dimensions or scale for higher quality).
Export.video.toDrive({
collection:collection,
description:'sfVideoExample',
dimensions:720,
framesPerSecond:12,
region:polygon
});
```

Note that the frame rate and dimensions can be set from a dictionary of parameters passed to the export. Adjust these parameters to customize the video. Also note that the input ImageCollection is required to have 3-band (RGB), 8-bit images. In this example, the 8-bit, 3-band format is explicitly set. Alternatively, map a function which calls `image.visualize()` over the collection. See [the section on Visualization images](https://developers.google.com/earth-engine/guides/image_visualization#visualization-images) for details. Video exports can take a significant amount of time to complete, so it's not unusual to see the export task running for an extended period.
## to Cloud Storage
To export a video to Cloud Storage, use `Export.video.toCloudStorage()`. For example, using the `ImageCollection` from the previous example:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/exporting_video#code-editor-javascript-sample) More
```
// Export video to cloud storage.
Export.video.toCloudStorage({
collection:collection,
description:'sfVideoExampleToCloud',
bucket:'your-bucket-name',
dimensions:720,
framesPerSecond:12,
region:polygon
});
```

