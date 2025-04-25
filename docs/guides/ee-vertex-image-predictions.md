 
#  Image Predictions 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [ee.Model.predictImage](https://developers.google.com/earth-engine/guides/ee-vertex-image-predictions#eemodelpredictimage)
  * [Input Options](https://developers.google.com/earth-engine/guides/ee-vertex-image-predictions#input_options)
    * [Bands and Properties](https://developers.google.com/earth-engine/guides/ee-vertex-image-predictions#bands_and_properties)
    * [Tile Sizes](https://developers.google.com/earth-engine/guides/ee-vertex-image-predictions#tile_sizes)
    * [Projection](https://developers.google.com/earth-engine/guides/ee-vertex-image-predictions#projection)


Earth Engine provides `ee.Model` as a connector to models hosted on [Vertex AI](https://cloud.google.com/vertex-ai/docs/start/introduction-unified-platform). This connector sends image or table data as online prediction requests to a trained model deployed on a Vertex AI endpoint. The model outputs are then returned as Earth Engine images or tables.
## ee.Model.predictImage
Use `model.predictImage()` to make predictions on an `ee.Image` using a hosted model. The `ee.Image` is used to create tiles (image patch) of bands which are then sent to the hosted model. The return type of `predictImage()` is an `ee.Image` which can be added to the map, exported, or used in other computations.
## Input Options
When performing inference using on a `ee.Image` there are a number of parameters used in the `ee.Model` connector. These controls are for the input bands and properties, the input image patch tiling, output image patch size and output image bands.
### Bands and Properties
To specify the input bands and properties use the following parameters:
#### `inputProperties`
`inputProperties` is a list of property names to forward to every prediction instance. Numeric, string, and boolean properties are supported.
#### `inputTypeOverride`
`inputTypeOverride` is a dictionary of property and or band names with specific type and dimension information provided. This might be necessary because many Earth Engine algorithms create outputs with dynamic types that cannot be inferred until runtime.
For example if you are computing "slope" by mapping the `ee.Terrain.slope` function over a collection you will need to specify the output type of "slope" in our inference inputs like so:
```
inputTypeOverride = {
 "slope": {
  "type": "PixelType",
  "precision": "float",
  "dimensions": 0,
  "min": -100.0,
  "max": 100.0
 }
}

```

TIP: If you encounter the error message that a band or property "cannot be converted to a tensor," a possible solution is to use a type override to force the input to a given type.
#### `inputShapes`
`inputShapes` is a dictionary of band names and array-pixel shape. To send your model array-valued pixels with lengths greater than 1 then set the `inputShapes` argument. to be set. The argument is similar to `inputTypeOverride` but is specific to input band shapes for image predictions. For example, to encode three bands, (1) "ndvi_series" as a 1D time series with 12 values, (2) "temp" as a scalar, and (3) "patch" as a 2D pixel array, use the following:
```
inputShapes = {
 "ndvi_series": [12], # 12 ndvi samples
 "temp": [], # scalar
 "patch": [2, 2], # 2px * 2px patch
}

```

#### `outputBands`
`outputBands` is a dictionary of output band names to an object containing the `ee.PixelType` and dimensions of the band. Here dimensions should be the same as the length of the tensor shape array. In other words, scalar data with shape () should have dimension 0, 1D data with shape (N) should have dimensions 1, 2D data with shape (N, M) should have dimensions 2. For example, an output band named "B1" with array-valued pixels with shape is specified with the following:
```
outputBands = {
 'B1': {'type': ee.PixelType.float(), 'dimensions': 1}
}

```

### Tile Sizes
You control how the image is tiled using the following parameters:
  * `inputTileSize`
  * `inputOverlapSize`
  * `outputTileSize`


#### Input Tile Sizes
To set input tile sizes use `inputTileSize` and `inputOverlapSize`. Set these parameters by providing a pair of tile width and height in pixels (for example [32, 32]). The total patch size is determined by adding the `inputTileSize` and `outputTileSize` heights and widths.
For example, a fully convolutional model may expect inputs with shape (256 x 256 x Channels). If we are worried about edges effects between inference results, we can discard `inputOverlapSize[0]` pixels from the left and right, and `inputOverlapSize[1]` from the top and bottom of each inference result. This will result in more prediction calls in order to fully cover the prediction area.
For example if our model expects (256 x 256 x 3) and we want to discard the 32 border pixels we would specify the following:
```
ee.Model({
 "endpoint": endpoint,
 "inputTileSize": [192, 192],
 "inputOverlapSize": [64, 64],
 # rest omitted.
}

```

NOTE: The `inputOverlapSize` is a total x and y overlap. If you intend to have a buffer of N pixels around the entire image the overlap would then be `[2N, 2N]`
#### Output Tile Size
To set the output tile size set the `outputTileSize` argument. If `outputTileSize` is not set the default tile size is identical to `inputTileSize`.
For some models the output size may be different from the input size. For example, a classification model may accept (256, 256, Channels) shaped inputs, but return tensors with the shape (1, 1, 1). In this case the `outputTileSize` needs to be set to `[1, 1]`. This is fairly common with models that return the output of probability (at a reduced resolution) of some tile characteristic.
**Note:** Earth Engine will always forward each band in the input Image as a 3D `(inputTileSize[0], inputTileSize[1], 1)` shaped tensor, even if the band's values are scalar. For non-scalar input and output bands see the earlier `inputTypeOverride`, `inputShape`, and `outputBands` arguments.
### Projection
Nearly all convolutional models will expect input of a fixed projection. This is because most convolutional models are trained on a fixed scale. In this case, set the `fixInputProj` parameter to **true** in your call to `ee.Model.fromVertexAi()` and specify the data's projection in the `proj` parameter.
**Warning:** When visualizing predictions, use caution when zooming out on a model that has a fixed input projection. As explained in the [EE reprojecting guide](https://developers.google.com/earth-engine/guides/projections#reprojecting), zooming to a large spatial scope can result in requests for too much data, too many concurrent requests, or too much billable compute.
The input Image's projection and the model's fixed projection will affect the output values. See the [EE Reprojection](https://developers.google.com/earth-engine/guides/projections) guide.
