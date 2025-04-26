 
#  TFRecord and Earth Engine 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [ Exporting data to TFRecord ](https://developers.google.com/earth-engine/guides/tfrecord#exporting-data-to-tfrecord)
    * [ Exporting tables ](https://developers.google.com/earth-engine/guides/tfrecord#exporting-tables)
    * [ Exporting images ](https://developers.google.com/earth-engine/guides/tfrecord#exporting-images)
  * [ Uploading TFRecords to Earth Engine ](https://developers.google.com/earth-engine/guides/tfrecord#uploading-tfrecords-to-earth-engine)
    * [ Uploading imagery ](https://developers.google.com/earth-engine/guides/tfrecord#uploading-imagery)


[TFRecord](https://www.tensorflow.org/tutorials/load_data/tfrecord#tfrecords_format_details) is a binary format for efficiently encoding long sequences of [tf.Example protos](https://github.com/tensorflow/tensorflow/blob/r1.14/tensorflow/core/example/example.proto). TFRecord files are easily loaded by TensorFlow through the `tf.data` package as described [here](https://www.tensorflow.org/guide/datasets#consuming_tfrecord_data) and [here](https://www.tensorflow.org/tutorials/load_data/tf_records#tfrecord_files_using_tfdata). This page describes how Earth Engine converts between `ee.FeatureCollection` or `ee.Image` and TFRecord format. 
##  Exporting data to TFRecord 
You can export tables (`ee.FeatureCollection`) or images (`ee.Image`) to TFRecord files in Google Drive or Cloud Storage. Configuration of the export depends on what you are exporting as described below. All numbers exported from Earth Engine to TFRecord are coerced to float type. 
###  Exporting tables 
When exporting an `ee.FeatureCollection` to a TFRecord file, there is a 1:1 correspondence between each [`ee.Feature`](https://developers.google.com/earth-engine/apidocs/ee-feature) in the table and each [`tf.train.Example`](https://www.tensorflow.org/api_docs/python/tf/train/Example) (i.e. each record) in the TFRecord file. Each property of the `ee.Feature` is encoded as a [`tf.train.Feature`](https://www.tensorflow.org/api_docs/python/tf/train/Feature) with a list of floats corresponding to the number or `ee.Array` stored in the property. If you export a table with arrays in the properties, you need to tell TensorFlow the shape of the array when it is read. A table exported to a TFRecord file will always be compressed with the GZIP compression type. You always get exactly one TFRecord file for each export.
The following example demonstrates parsing data from an exported table of scalar properties ('B2',...,'B7', 'landcover'). Note that the dimension of the float lists is `[1]` and the type is `tf.float32`: 
[Python](https://developers.google.com/earth-engine/guides/tfrecord#python) More
```
dataset = tf.data.TFRecordDataset(exportedFilePath)
featuresDict = {
 'B2': tf.io.FixedLenFeature(shape=[1], dtype=tf.float32),
 'B3': tf.io.FixedLenFeature(shape=[1], dtype=tf.float32),
 'B4': tf.io.FixedLenFeature(shape=[1], dtype=tf.float32),
 'B5': tf.io.FixedLenFeature(shape=[1], dtype=tf.float32),
 'B6': tf.io.FixedLenFeature(shape=[1], dtype=tf.float32),
 'B7': tf.io.FixedLenFeature(shape=[1], dtype=tf.float32),
 'landcover': tf.io.FixedLenFeature(shape=[1], dtype=tf.float32)
}
parsedDataset = dataset.map(lambda example: tf.io.parse_single_example(example, featuresDict))
    
```

Note that this example illustrates reading scalar features (i.e. `shape=[1]`). If you are exporting 2D or 3D arrays (e.g. image patches), then you would specify the shape of your patches at parse time, for example `shape=[16, 16]` for a 16x16 pixel patch. 
###  Exporting images 
When you export an image, the data are ordered as channels, height, width (CHW). The export may be split into multiple TFRecord files with each file containing one or more patches of size `patchSize`, which is user specified in the export. The size of the files in bytes is user specified in the `maxFileSize` parameter. There is a 1:1 correspondence between each patch and each [`tf.train.Example`](https://www.tensorflow.org/api_docs/python/tf/train/Example) in the resulting TFRecord file. Each band of the image is stored as a separate [`tf.train.Feature`](https://www.tensorflow.org/api_docs/python/tf/train/Feature) in each `tf.train.Example`, where the length of the float list stored in each feature is the patch width * height. The flattened lists can be split into multiple individual pixels as shown in [this example](https://developers.google.com/earth-engine/guides/tf_examples#multi-class-prediction-with-a-dnn). Or the shape of the exported patch can be recoved as in [this example](https://developers.google.com/earth-engine/guides/tf_examples#regression-with-an-fcnn). 
To help reduce edge effects, the exported patches can overlap. Specifically, you can specify a `kernelSize` which will result in tiles of size:
```
[patchSize[0] + kernelSize[0], patchSize[1] + kernelSize[1]]
  
```

Each tile overlaps adjacent tiles by `[kernelSize[0]/2, kernelSize[1]/2]`. As a result, a kernel of size `kernelSize` centered on an edge pixel of a patch of size `patchSize` contains entirely valid data. The spatial arrangement of the patches in space is illustrated by Figure 1, where Padding Dimension corresponds to the part of the kernel that overlaps the adjacent image: 
![TFRecord image diagram](https://developers.google.com/static/earth-engine/images/TFRecord_diagram.png) Figure 1. How image patches are exported. The Padding Dimension is `kernelSize/2`. 
####  `formatOptions`
The `patchSize`, `maxFileSize`, and `kernelSize` parameters are passed to the `ee.Export` (JavaScript) or `ee.batch.Export` (Python) call through a `formatOptions` dictionary, where keys are the names of additional parameters passed to `Export`. Possible `formatOptions` for an image exported to TFRecord format are:
Property| Description| Type  
---|---|---  
`patchDimensions` | Dimensions tiled over the export area, covering every pixel in the bounding box exactly once (except when the patch dimensions do not evenly divide the bounding box in which case border tiles along the greatest x/y edges will be dropped). Dimensions must be > 0. | Array<int>[2].  
`kernelSize` | If specified, tiles will be buffered by the margin dimensions both positively and negatively, resulting in overlap between neighboring patches. If specified, two dimensions must be provided (X and Y, respectively).  | Array<int>[2]. Default: [1, 1]  
`compressed` | If true, compresses the .tfrecord files with gzip and appends the ".gz" suffix | Boolean. Default: true  
`maxFileSize` | Maximum size, in bytes, for an exported .tfrecord (before compression). A smaller file size will result in greater sharding (and, thus, more output files). | Int. Default: 1 GiB  
`defaultValue` | The value set in each band of a pixel that is partially or completely masked, and the value set at each value in an output 3D feature made from an array band where the array length at the source pixel was less than the depth of the feature value (i.e. the value at index 3 of an array pixel of length 2 in an array band with a corresponding feature depth of 3). The fractional part is dropped for integer type bands, and clamped to the range of the band type. Defaults to 0. | Int. Default: 0  
`tensorDepths` | Mapping from the names of input array bands to the depth of the 3D tensors they create. Arrays will be truncated, or padded with default values to fit the shape specified. For each array band, this must have a corresponding entry.  | Array<int>[]. Default: []  
`sequenceData` | If true, each pixel is output as a SequenceExample mapping scalar bands to the context and array bands to the example’s sequences. The SequenceExamples are output in row-major order of pixels in each patch, and then by row-major order of area patches in the file sequence. | Boolean. Default: false  
`collapseBands` |  If true, all bands will be combined into a single 3D tensor, taking on the name of the first band in the image. All bands are promoted to bytes, int64s, then floats in that order depending on the type furthest in that equence within all bands. Array bands are allowed as long as tensor_depths is specified. | Boolean. Default: false  
`maskedThreshold` | Maximum allowed proportion of masked pixels in a patch. Patches which exceed this allowance will be dropped rather than written to files. If this field is set to anything but 1, the JSON sidecar will not be produced. Defaults to 1. | Float. Default: 1  
#### The TFRecord “mixer” file
When you export to TFRecord, Earth Engine will generate a sidecar with your TFRecord files called the “mixer.” This is a simple JSON file used to define the spatial arrangement of the patches (i.e. georeferencing). This file is needed for uploading predicions made on the imagery as described in the [next section](https://developers.google.com/earth-engine/guides/tfrecord#uploading-imagery). 
#### Exporting Time Series
Image exports to both Examples and SequenceExamples are supported. When you export to Examples, the export region is cut into patches and those patches are exported in row-major order to some number of .tfrecord files with each band its own feature (unless you specify `collapseBands`). When you export to SequenceExamples, a SequenceExample per-pixel will be exported, with those SequenceExamples in row-major order within a patch, and then in row-major order of patches in the original export region (if you’re ever unsure, always assume things will be in row-major order in some capacity). Note: any scalar bands of an image will be packed into the context of a SequenceExample, while the array bands will become the actual sequence data.
#### Array Bands
Array bands are exportable when an image is exported to TFRecord format. Export of array bands provides a means to populate the “FeatureLists” of SequenceExamples, and a way to create 3D tensors when exporting to regular Examples. For information on how the lengths/depths of array bands are managed, see `collapseBands` and/or `tensorDepths` in the table above. Note: usage of `collapseBands` and export to SequenceExamples (so setting the parameter `sequenceData`) will result in all bands being collapsed to a single time series per-pixel.
##  Uploading TFRecords to Earth Engine 
You can upload tables ([command line](https://developers.google.com/earth-engine/guides/command_line#upload) only) and images to Earth Engine as TFRecord files. For tables, the 1:1 relationship [described previously](https://developers.google.com/earth-engine/guides/tfrecord#exporting-tables) applies in the reverse direction (i.e. `tf.train.Example` -> `ee.Feature`). 
###  Uploading imagery 
If you generate predictions on exported imagery, supply the mixer when you upload the predictions (as TFRecord files) to obtain georeferenced imagery. Note that the overlapping portion of the patches (Padding Dimension in Figure 1) will be discarded to result in conterminous coverage of the exported region. The predictions should be arranged as a `tf.train.Example` sequence of the same number and order as your originally exported image examples (even between an arbitrary number of files). 
