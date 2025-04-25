 
#  Property Predictions 
Stay organized with collections  Save and categorize content based on your preferences. 
Use `model.predictProperties()` to make predictions on an `ee.FeatureCollection`. Each Feature is a data point, and each property is a model input feature The inputs and outputs can be scalar string values, scalar boolean values, or numeric values of any shape, from scalars to multidimensional arrays. The outputs of the model are represented as new properties in the output table.
## Input and Outputs
To control the inputs and outputs of the model use the following arguments:
### `inputProperties`
Set input properties to the list of properties you explicitly want to send do your hosted model.
#### `inputTypeOverride`
`inputTypeOverride` is a dictionary of property names with specific type and dimension information provided. This might be necessary because many Earth Engine algorithms create outputs with dynamic types that cannot be inferred until runtime.
For example we may compute a value "slope" by mapping the `ee.Terrain.slope` function over a collection we may need to specify the output type of "slope" in our inference inputs like so:
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

TIP: You may occasionally encounter the error message that a property "cannot be converted to a tensor". The likely solution is to use a type override to force the input to a given type.
### `outputProperties`
A map from output property names to a dictionary of output property info. Valid property info fields are 'type' and 'dimensions'. 'type' should be a `ee.PixelType` describing the output property, and 'dimensions' is an optional integer with the number of dimensions for that property if it is an array. For example, given an 1D array property "p" specify the following output property:
```
outputProperties = {
 "p": {
  "type": ee.PixelType.int8(),
  "dimensions": 1
 }
}

```

