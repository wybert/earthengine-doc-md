 
#  Array Transformations
Stay organized with collections  Save and categorize content based on your preferences. 
Earth Engine supports array transformations such as transpose, inverse and pseudo-inverse. As an example, consider an ordinary least squares (OLS) regression of a time series of images. In the following example, an image with bands for predictors and a response is converted to an array image, then “solved” to obtain least squares coefficients estimates three ways. First, assemble the image data and convert to arrays:
### Code Editor (JavaScript)
```
// Scales and masks Landsat 8 surface reflectance images.
functionprepSrL8(image){
// Develop masks for unwanted pixels (fill, cloud, cloud shadow).
varqaMask=image.select('QA_PIXEL').bitwiseAnd(parseInt('11111',2)).eq(0);
varsaturationMask=image.select('QA_RADSAT').eq(0);

// Apply the scaling factors to the appropriate bands.
varopticalBands=image.select('SR_B.').multiply(0.0000275).add(-0.2);
varthermalBands=image.select('ST_B.*').multiply(0.00341802).add(149.0);

// Replace the original bands with the scaled ones and apply the masks.
returnimage.addBands(opticalBands,null,true)
.addBands(thermalBands,null,true)
.updateMask(qaMask)
.updateMask(saturationMask);
}

// Load a Landsat 8 surface reflectance image collection.
varcollection=ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
// Filter to get only two years of data.
.filterDate('2019-04-01','2021-04-01')
// Filter to get only imagery at a point of interest.
.filterBounds(ee.Geometry.Point(-122.08709,36.9732))
// Prepare images by mapping the prepSrL8 function over the collection.
.map(prepSrL8)
// Select NIR and red bands only.
.select(['SR_B5','SR_B4'])
// Sort the collection in chronological order.
.sort('system:time_start',true);

// This function computes the predictors and the response from the input.
varmakeVariables=function(image){
// Compute time of the image in fractional years relative to the Epoch.
varyear=ee.Image(image.date().difference(ee.Date('1970-01-01'),'year'));
// Compute the season in radians, one cycle per year.
varseason=year.multiply(2*Math.PI);
// Return an image of the predictors followed by the response.
returnimage.select()
.addBands(ee.Image(1))// 0. constant
.addBands(year.rename('t'))// 1. linear trend
.addBands(season.sin().rename('sin'))// 2. seasonal
.addBands(season.cos().rename('cos'))// 3. seasonal
.addBands(image.normalizedDifference().rename('NDVI'))// 4. response
.toFloat();
};

// Define the axes of variation in the collection array.
varimageAxis=0;
varbandAxis=1;

// Convert the collection to an array.
vararray=collection.map(makeVariables).toArray();

// Check the length of the image axis (number of images).
vararrayLength=array.arrayLength(imageAxis);
// Update the mask to ensure that the number of images is greater than or
// equal to the number of predictors (the linear model is solvable).
array=array.updateMask(arrayLength.gt(4));

// Get slices of the array according to positions along the band axis.
varpredictors=array.arraySlice(bandAxis,0,4);
varresponse=array.arraySlice(bandAxis,4);
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
importmath


# Scales and masks Landsat 8 surface reflectance images.
defprep_sr_l8(image):
  # Develop masks for unwanted pixels (fill, cloud, cloud shadow).
  qa_mask = image.select('QA_PIXEL').bitwiseAnd(int('11111', 2)).eq(0)
  saturation_mask = image.select('QA_RADSAT').eq(0)

  # Apply the scaling factors to the appropriate bands.
  optical_bands = image.select('SR_B.').multiply(0.0000275).add(-0.2)
  thermal_bands = image.select('ST_B.*').multiply(0.00341802).add(149.0)

  # Replace the original bands with the scaled ones and apply the masks.
  return (
      image.addBands(optical_bands, None, True)
      .addBands(thermal_bands, None, True)
      .updateMask(qa_mask)
      .updateMask(saturation_mask)
  )


# Load a Landsat 8 surface reflectance image collection.
collection = (
    ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
    # Filter to get only two years of data.
    .filterDate('2019-04-01', '2021-04-01')
    # Filter to get only imagery at a point of interest.
    .filterBounds(ee.Geometry.Point(-122.08709, 36.9732))
    # Prepare images by mapping the prep_sr_l8 function over the collection.
    .map(prep_sr_l8)
    # Select NIR and red bands only.
    .select(['SR_B5', 'SR_B4'])
    # Sort the collection in chronological order.
    .sort('system:time_start', True)
)


# This function computes the predictors and the response from the input.
defmake_variables(image):
  # Compute time of the image in fractional years relative to the Epoch.
  year = ee.Image(image.date().difference(ee.Date('1970-01-01'), 'year'))
  # Compute the season in radians, one cycle per year.
  season = year.multiply(2 * math.pi)
  # Return an image of the predictors followed by the response.
  return (
      image.select()
      .addBands(ee.Image(1))  # 0. constant
      .addBands(year.rename('t'))  # 1. linear trend
      .addBands(season.sin().rename('sin'))  # 2. seasonal
      .addBands(season.cos().rename('cos'))  # 3. seasonal
      .addBands(image.normalizedDifference().rename('NDVI'))  # 4. response
      .toFloat()
  )


# Define the axes of variation in the collection array.
image_axis = 0
band_axis = 1

# Convert the collection to an array.
array = collection.map(make_variables).toArray()

# Check the length of the image axis (number of images).
array_length = array.arrayLength(image_axis)
# Update the mask to ensure that the number of images is greater than or
# equal to the number of predictors (the linear model is solvable).
array = array.updateMask(array_length.gt(4))

# Get slices of the array according to positions along the band axis.
predictors = array.arraySlice(band_axis, 0, 4)
response = array.arraySlice(band_axis, 4)
```

Note that `arraySlice()` returns all the images in the time series for the range of indices specified along the `bandAxis` (the 1-axis). At this point, matrix algebra can be used to solve for the OLS coefficients:
### Code Editor (JavaScript)
```
// Compute coefficients the hard way.
varcoefficients1=predictors.arrayTranspose().matrixMultiply(predictors)
.matrixInverse().matrixMultiply(predictors.arrayTranspose())
.matrixMultiply(response);
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Compute coefficients the hard way.
coefficients_1 = (
    predictors.arrayTranspose()
    .matrixMultiply(predictors)
    .matrixInverse()
    .matrixMultiply(predictors.arrayTranspose())
    .matrixMultiply(response)
)
```

Although this method works, it is inefficient and makes for difficult to read code. A better way is to use the `pseudoInverse()` method (`matrixPseudoInverse()` for an array image):
### Code Editor (JavaScript)
```
// Compute coefficients the easy way.
varcoefficients2=predictors.matrixPseudoInverse()
.matrixMultiply(response);
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Compute coefficients the easy way.
coefficients_2 = predictors.matrixPseudoInverse().matrixMultiply(response)
```

From a readability and computational efficiency perspective, the best way to get the OLS coefficients is `solve()` (`matrixSolve()` for an array image). The `solve()` function determines how to best solve the system from characteristics of the inputs, using the pseudo-inverse for overdetermined systems, the inverse for square matrices and special techniques for nearly singular matrices:
### Code Editor (JavaScript)
```
// Compute coefficients the easiest way.
varcoefficients3=predictors.matrixSolve(response);
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Compute coefficients the easiest way.
coefficients_3 = predictors.matrixSolve(response)
```

To get a multi-band image, project the array image into a lower dimensional space, then flatten it:
### Code Editor (JavaScript)
```
// Turn the results into a multi-band image.
varcoefficientsImage=coefficients3
// Get rid of the extra dimensions.
.arrayProject([0])
.arrayFlatten([
['constant','trend','sin','cos']
]);
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Turn the results into a multi-band image.
coefficients_image = (
    coefficients_3
    # Get rid of the extra dimensions.
    .arrayProject([0]).arrayFlatten([['constant', 'trend', 'sin', 'cos']])
)
```

Examine the outputs of the three methods and observe that the resultant matrix of coefficients is the same regardless of the solver. That `solve()` is flexible and efficient makes it a good choice for general purpose linear modeling.
