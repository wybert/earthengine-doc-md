 
#  ee.Model.fromVertexAi 
Stay organized with collections  Save and categorize content based on your preferences. 
Returns an ee.Model from a description of a Vertex AI model endpoint. (See https://cloud.google.com/vertex-ai). **Warning:** This method is in public preview and may undergo breaking changes. Usage| Returns  
---|---  
`ee.Model.fromVertexAi(endpoint,  _inputProperties_, _inputTypeOverride_, _inputShapes_, _proj_, _fixInputProj_, _inputTileSize_, _inputOverlapSize_, _outputTileSize_, _outputBands_, _outputProperties_, _outputMultiplier_, _maxPayloadBytes_, _payloadFormat_)`| Model  
Argument| Type| Details  
---|---|---  
`endpoint`| String| The endpoint name for predictions.  
`inputProperties`| List, default: null| Properties passed with each prediction instance. Image predictions are tiled, so these properties will be replicated into each image tile instance. Defaults to no properties.  
`inputTypeOverride`| Dictionary, default: null| Types to which model inputs will be coerced if specified. Both Image bands and Image/Feature properties are valid.  
`inputShapes`| Dictionary, default: null| The fixed shape of input array bands. For each array band not specified, the fixed array shape will be automatically deduced from a non-masked pixel.  
`proj`| Projection, default: null| The input projection at which to sample all bands. Defaults to the default projection of an image's first band.  
`fixInputProj`| Boolean, default: null| If true, pixels will be sampled in a fixed projection specified by 'proj'. The output projection is used otherwise. Defaults to false.  
`inputTileSize`| List, default: null| Rectangular dimensions of pixel tiles passed in to prediction instances. Required for image predictions.  
`inputOverlapSize`| List, default: null| Amount of adjacent-tile overlap in X/Y along each edge of pixel tiles passed in to prediction instances. Defaults to [0, 0].  
`outputTileSize`| List, default: null| Rectangular dimensions of pixel tiles returned from AI Platform. Defaults to the value in 'inputTileSize'.  
`outputBands`| Dictionary, default: null| A map from output band names to a dictionary of output band info. Valid band info fields are 'type' and 'dimensions'. 'type' should be a ee.PixelType describing the output band, and 'dimensions' is an optional integer with the number of dimensions in that band e.g., "outputBands: {'p': {'type': ee.PixelType.int8(), 'dimensions': 1}}". Required for image predictions.  
`outputProperties`| Dictionary, default: null| A map from output property names to a dictionary of output property info. Valid property info fields are 'type' and 'dimensions'. 'type' should be a ee.PixelType describing the output property, and 'dimensions' is an optional integer with the number of dimensions for that property if it is an array e.g., "outputBands: {'p': {'type': ee.PixelType.int8(), 'dimensions': 1}}". Required for predictions from FeatureCollections.  
`outputMultiplier`| Float, default: null| An approximation to the increase in data volume for the model outputs over the model inputs. If specified this must be >= 1. This is only needed if the model produces more data than it consumes, e.g., a model that takes 5 bands and produces 10 outputs per pixel.  
`maxPayloadBytes`| Long, default: null| The prediction payload size limit in bytes. Defaults to 1.5MB (1500000 bytes.)  
`payloadFormat`| String, default: null| The payload format of entries in prediction requests and responses. One of: ['SERIALIZED_TF_TENSORS, 'RAW_JSON', 'ND_ARRAYS', 'GRPC_TF_TENSORS', 'GRPC_SERIALIZED_TF_TENSORS', 'GRPC_TF_EXAMPLES']. Defaults to 'SERIALIZED_TF_TENSORS'.  
