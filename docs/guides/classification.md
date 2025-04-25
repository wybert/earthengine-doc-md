 
#  Supervised Classification 
Stay organized with collections  Save and categorize content based on your preferences. 
The `Classifier` package handles supervised classification by traditional ML algorithms running in Earth Engine. These classifiers include CART, RandomForest, NaiveBayes and SVM. The general workflow for classification is:
  1. Collect training data. Assemble features which have a property that stores the known class label and properties storing numeric values for the predictors.
  2. Instantiate a classifier. Set its parameters if necessary.
  3. Train the classifier using the training data.
  4. Classify an image or feature collection.
  5. Estimate classification error with independent validation data.


The training data is a `FeatureCollection` with a property storing the class label and properties storing predictor variables. Class labels should be consecutive, integers starting from 0. If necessary, use `remap()` to convert class values to consecutive integers. The predictors should be numeric.
Training and/or validation data can come from a variety of sources. To collect training data interactively in Earth Engine, you can use the geometry drawing tools (see the [geometry tools section of the Code Editor page](https://developers.google.com/earth-engine/guides/playground#geometry-tools)). Alternatively, you can import predefined training data from an Earth Engine table asset (see the [Importing Table Data page](https://developers.google.com/earth-engine/guides/table_upload) for details). Get a classifier from one of the constructors in `ee.Classifier`. Train the classifier using `classifier.train()`. Classify an `Image` or `FeatureCollection` using `classify()`. The following example uses a Classification and Regression Trees (CART) classifier ([Breiman et al. 1984](https://books.google.com/books?id=JwQx-WOmSyQC)) to predict three simple classes:
### Code Editor (JavaScript)
```
// Define a function that scales and masks Landsat 8 surface reflectance images.
functionprepSrL8(image){
// Develop masks for unwanted pixels (fill, cloud, cloud shadow).
varqaMask=image.select('QA_PIXEL').bitwiseAnd(parseInt('11111',2)).eq(0);
varsaturationMask=image.select('QA_RADSAT').eq(0);
// Apply the scaling factors to the appropriate bands.
vargetFactorImg=function(factorNames){
varfactorList=image.toDictionary().select(factorNames).values();
returnee.Image.constant(factorList);
};
varscaleImg=getFactorImg([
'REFLECTANCE_MULT_BAND_.|TEMPERATURE_MULT_BAND_ST_B10']);
varoffsetImg=getFactorImg([
'REFLECTANCE_ADD_BAND_.|TEMPERATURE_ADD_BAND_ST_B10']);
varscaled=image.select('SR_B.|ST_B10').multiply(scaleImg).add(offsetImg);
// Replace original bands with scaled bands and apply masks.
returnimage.addBands(scaled,null,true)
.updateMask(qaMask).updateMask(saturationMask);
}
// Make a cloud-free Landsat 8 surface reflectance composite.
varimage=ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
.filterDate('2021-03-01','2021-07-01')
.map(prepSrL8)
.median();
// Use these bands for prediction.
varbands=['SR_B2','SR_B3','SR_B4','SR_B5',
'SR_B6','SR_B7','ST_B10'];
// Load training points. The numeric property 'class' stores known labels.
varpoints=ee.FeatureCollection('GOOGLE/EE/DEMOS/demo_landcover_labels');
// This property stores the land cover labels as consecutive
// integers starting from zero.
varlabel='landcover';
// Overlay the points on the imagery to get training.
vartraining=image.select(bands).sampleRegions({
collection:points,
properties:[label],
scale:30
});
// Train a CART classifier with default parameters.
vartrained=ee.Classifier.smileCart().train(training,label,bands);
// Classify the image with the same bands used for training.
varclassified=image.select(bands).classify(trained);
// Display the inputs and the results.
Map.setCenter(-122.0877,37.7880,11);
Map.addLayer(image,
{bands:['SR_B4','SR_B3','SR_B2'],min:0,max:0.25},
'image');
Map.addLayer(classified,
{min:0,max:2,palette:['orange','green','blue']},
'classification');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Define a function that scales and masks Landsat 8 surface reflectance images.
defprep_sr_l8(image):
"""Scales and masks Landsat 8 surface reflectance images."""
 # Develop masks for unwanted pixels (fill, cloud, cloud shadow).
 qa_mask = image.select('QA_PIXEL').bitwiseAnd(0b11111).eq(0)
 saturation_mask = image.select('QA_RADSAT').eq(0)
 # Apply the scaling factors to the appropriate bands.
 def_get_factor_img(factor_names):
  factor_list = image.toDictionary().select(factor_names).values()
  return ee.Image.constant(factor_list)
 scale_img = _get_factor_img([
   'REFLECTANCE_MULT_BAND_.|TEMPERATURE_MULT_BAND_ST_B10'])
 offset_img = _get_factor_img([
   'REFLECTANCE_ADD_BAND_.|TEMPERATURE_ADD_BAND_ST_B10'])
 scaled = image.select('SR_B.|ST_B10').multiply(scale_img).add(offset_img)
 # Replace original bands with scaled bands and apply masks.
 return image.addBands(scaled, None, True).updateMask(
   qa_mask).updateMask(saturation_mask)

# Make a cloud-free Landsat 8 surface reflectance composite.
l8_image = (
  ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
  .filterDate('2021-03-01', '2021-07-01')
  .map(prep_sr_l8)
  .median())
# Use these bands for prediction.
bands = ['SR_B2', 'SR_B3', 'SR_B4', 'SR_B5', 'SR_B6', 'SR_B7', 'ST_B10']
# Load training points. The numeric property 'class' stores known labels.
points = ee.FeatureCollection('GOOGLE/EE/DEMOS/demo_landcover_labels')
# This property stores the land cover labels as consecutive
# integers starting from zero.
label = 'landcover'
# Overlay the points on the imagery to get training.
training = l8_image.select(bands).sampleRegions(
  collection=points, properties=[label], scale=30
)
# Train a CART classifier with default parameters.
trained = ee.Classifier.smileCart().train(training, label, bands)
# Classify the image with the same bands used for training.
classified = l8_image.select(bands).classify(trained)
# Display the inputs and the results.
m = geemap.Map()
m.set_center(-122.0877, 37.7880, 11)
m.add_layer(
  l8_image,
  {'bands': ['SR_B4', 'SR_B3', 'SR_B2'], 'min': 0, 'max': 0.25},
  'image',
)
m.add_layer(
  classified,
  {'min': 0, 'max': 2, 'palette': ['orange', 'green', 'blue']},
  'classification',
)
m
```

In this example, the training points in the table store only the class label. Note that the training property (`'landcover'`) stores consecutive integers starting at 0 (Use [`remap()`](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-remap) on your table to turn your class labels into consecutive integers starting at zero if necessary). Also note the use of `image.sampleRegions()` to get the predictors into the table and create a training dataset. To train the classifier, specify the name of the class label property and a list of properties in the training table which the classifier should use for predictors. The number and order of the bands in the image to be classified must exactly match the order of the properties list provided to `classifier.train()`. Use `image.select()` to ensure that the classifier schema matches the image.
If the training data are polygons representing homogeneous regions, every pixel in each polygon is a training point. You can use polygons to train as illustrated in the following example:
### Code Editor (JavaScript)
```
// Define a function that scales and masks Landsat 8 surface reflectance images.
functionprepSrL8(image){
// Develop masks for unwanted pixels (fill, cloud, cloud shadow).
varqaMask=image.select('QA_PIXEL').bitwiseAnd(parseInt('11111',2)).eq(0);
varsaturationMask=image.select('QA_RADSAT').eq(0);
// Apply the scaling factors to the appropriate bands.
vargetFactorImg=function(factorNames){
varfactorList=image.toDictionary().select(factorNames).values();
returnee.Image.constant(factorList);
};
varscaleImg=getFactorImg([
'REFLECTANCE_MULT_BAND_.|TEMPERATURE_MULT_BAND_ST_B10']);
varoffsetImg=getFactorImg([
'REFLECTANCE_ADD_BAND_.|TEMPERATURE_ADD_BAND_ST_B10']);
varscaled=image.select('SR_B.|ST_B10').multiply(scaleImg).add(offsetImg);
// Replace original bands with scaled bands and apply masks.
returnimage.addBands(scaled,null,true)
.updateMask(qaMask).updateMask(saturationMask);
}
// Make a cloud-free Landsat 8 surface reflectance composite.
varimage=ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
.filterDate('2018-01-01','2019-01-01')
.map(prepSrL8)
.median();
// Use these bands for prediction.
varbands=['SR_B2','SR_B3','SR_B4','SR_B5',
'SR_B6','SR_B7'];
// Manually created polygons.
varforest1=ee.Geometry.Rectangle(-63.0187,-9.3958,-62.9793,-9.3443);
varforest2=ee.Geometry.Rectangle(-62.8145,-9.206,-62.7688,-9.1735);
varnonForest1=ee.Geometry.Rectangle(-62.8161,-9.5001,-62.7921,-9.4486);
varnonForest2=ee.Geometry.Rectangle(-62.6788,-9.044,-62.6459,-8.9986);
// Make a FeatureCollection from the hand-made geometries.
varpolygons=ee.FeatureCollection([
ee.Feature(nonForest1,{'class':0}),
ee.Feature(nonForest2,{'class':0}),
ee.Feature(forest1,{'class':1}),
ee.Feature(forest2,{'class':1}),
]);
// Get the values for all pixels in each polygon in the training.
vartraining=image.sampleRegions({
// Get the sample from the polygons FeatureCollection.
collection:polygons,
// Keep this list of properties from the polygons.
properties:['class'],
// Set the scale to get Landsat pixels in the polygons.
scale:30
});
// Create an SVM classifier with custom parameters.
varclassifier=ee.Classifier.libsvm({
kernelType:'RBF',
gamma:0.5,
cost:10
});
// Train the classifier.
vartrained=classifier.train(training,'class',bands);
// Classify the image.
varclassified=image.classify(trained);
// Display the classification result and the input image.
Map.setCenter(-62.836,-9.2399,9);
Map.addLayer(image,
{bands:['SR_B4','SR_B3','SR_B2'],min:0,max:0.25},
'image');
Map.addLayer(polygons,{color:'yellow'},'training polygons');
Map.addLayer(classified,
{min:0,max:1,palette:['orange','green']},
'deforestation');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Define a function that scales and masks Landsat 8 surface reflectance images.
defprep_sr_l8(image):
 # Develop masks for unwanted pixels (fill, cloud, cloud shadow).
 qa_mask = image.select('QA_PIXEL').bitwiseAnd(0b11111).eq(0)
 saturation_mask = image.select('QA_RADSAT').eq(0)
 # Apply the scaling factors to the appropriate bands.
 def_get_factor_img(factor_names):
  factor_list = image.toDictionary().select(factor_names).values()
  return ee.Image.constant(factor_list)
 scale_img = _get_factor_img([
   'REFLECTANCE_MULT_BAND_.|TEMPERATURE_MULT_BAND_ST_B10'])
 offset_img = _get_factor_img([
   'REFLECTANCE_ADD_BAND_.|TEMPERATURE_ADD_BAND_ST_B10'])
 scaled = image.select('SR_B.|ST_B10').multiply(scale_img).add(offset_img)
 # Replace original bands with scaled bands and apply masks.
 return image.addBands(scaled, None, True).updateMask(
   qa_mask).updateMask(saturation_mask)

# Make a cloud-free Landsat 8 surface reflectance composite.
l8_image = (
  ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
  .filterDate('2018-01-01', '2019-01-01')
  .map(prep_sr_l8)
  .median())
# Use these bands for prediction.
bands = ['SR_B2', 'SR_B3', 'SR_B4', 'SR_B5', 'SR_B6', 'SR_B7']
# Manually created polygons.
forest1 = ee.Geometry.Rectangle(-63.0187, -9.3958, -62.9793, -9.3443)
forest2 = ee.Geometry.Rectangle(-62.8145, -9.206, -62.7688, -9.1735)
non_forest1 = ee.Geometry.Rectangle(-62.8161, -9.5001, -62.7921, -9.4486)
non_forest2 = ee.Geometry.Rectangle(-62.6788, -9.044, -62.6459, -8.9986)
# Make a FeatureCollection from the hand-made geometries.
polygons = ee.FeatureCollection([
  ee.Feature(non_forest1, {'class': 0}),
  ee.Feature(non_forest1, {'class': 0}),
  ee.Feature(forest1, {'class': 1}),
  ee.Feature(forest2, {'class': 1}),
])
# Get the values for all pixels in each polygon in the training.
training = l8_image.sampleRegions(
  # Get the sample from the polygons FeatureCollection.
  collection=polygons,
  # Keep this list of properties from the polygons.
  properties=['class'],
  # Set the scale to get Landsat pixels in the polygons.
  scale=30,
)
# Create an SVM classifier with custom parameters.
classifier = ee.Classifier.libsvm(kernelType='RBF', gamma=0.5, cost=10)
# Train the classifier.
trained = classifier.train(training, 'class', bands)
# Classify the image.
classified = l8_image.classify(trained)
# Display the classification result and the input image.
m = geemap.Map()
m.set_center(-62.836, -9.2399, 9)
m.add_layer(
  l8_image,
  {'bands': ['SR_B4', 'SR_B3', 'SR_B2'], 'min': 0, 'max': 0.25},
  'image',
)
m.add_layer(polygons, {'color': 'yellow'}, 'training polygons')
m.add_layer(
  classified,
  {'min': 0, 'max': 1, 'palette': ['orange', 'green']},
  'deforestation',
)
m
```

This example uses a Support Vector Machine (SVM) classifier ([Burges 1998](http://rd.springer.com/article/10.1023%2FA%3A1009715923555)). Note that the SVM is specified with a set of custom parameters. Without _a priori_ information about the physical nature of the prediction problem, optimal parameters are unknown. See [Hsu et al. (2003)](http://www.csie.ntu.edu.tw/~cjlin/papers/guide/guide.pdf) for a rough guide to choosing parameters for an SVM.
##  Classifier output modes 
The [`     ee.Classifier.setOutputMode()`](https://developers.google.com/earth-engine/apidocs/ee-classifier-setoutputmode) method controls the format of supervised classification results, allowing outputs to be structured in several distinct ways: 
  * **CLASSIFICATION (default)** : The output is the class number.
  * **REGRESSION** : The output is the result of standard regression.
  * **PROBABILITY** : The output is the probability that the classification is correct.
  * **MULTIPROBABILITY** : The output is an array of probabilities that each class is correct ordered by classes seen.
  * **RAW** : The output is an array of the internal representation of the classification process. For example, the raw votes in multi-decision tree models.
  * **RAW_REGRESSION** : The output is an array of the internal representation of the regression process. For example, the raw predictions of multiple regression trees.


Support for these output modes varies. The following table summarizes the supported modes for each classifier. 
Classifier | CLASSIFICATION | REGRESSION | PROBABILITY | MULTIPROBABILITY | RAW | RAW_REGRESSION  
---|---|---|---|---|---|---  
ee.Classifier.amnhMaxent | close | close | check_circle | close | close | close  
ee.Classifier.minimumDistance | check_circle | check_circle | close | close | check_circle | close  
ee.Classifier.smileCart | check_circle | check_circle | check_circle | check_circle | close | close  
ee.Classifier.smileGradientTreeBoost | check_circle | check_circle | check_circle | check_circle | close | close  
ee.Classifier.smileKNN | check_circle | close | check_circle | close | close | close  
ee.Classifier.smileNaiveBayes | check_circle | close | check_circle | check_circle | close | close  
ee.Classifier.smileRandomForest | check_circle | check_circle | check_circle | check_circle | check_circle | check_circle  
ee.Classifier.libsvm C_SVC | check_circle | close | check_circle | check_circle | close | close  
ee.Classifier.libsvm NU_SVC | check_circle | close | check_circle | check_circle | close | close  
ee.Classifier.libsvm ONE_CLASS | check_circle | close | close | close | close | close  
ee.Classifier.libsvm EPSILON_SVR | check_circle | close | close | close | close | close  
ee.Classifier.libsvm NU_SVR | close | check_circle | close | close | close | close  
Use `setOutputMode()` before training a classifier to define the output format. For example, you could configure the SVM classifier in the previous code block to output probability instead of the default classification labels: 
### Code Editor (JavaScript)
```
varclassifier=ee.Classifier.libsvm({
kernelType:'RBF',
gamma:0.5,
cost:10
}).setOutputMode('PROBABILITY');
vartrained=classifier.train(training,'class',bands);
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
classifier = ee.Classifier.libsvm(
  kernelType='RBF', gamma=0.5, cost=10
).setOutputMode('PROBABILITY')
trained = classifier.train(training, 'class', bands)
```

##  Accuracy Assessment 
To assess the accuracy of a classifier, use a `ConfusionMatrix` ([Stehman 1997](http://www.sciencedirect.com/science/article/pii/S0034425797000837)). The following example uses `sample()` to generate training and validation data from a MODIS reference image and compares confusion matrices representing training and validation accuracy:
### Code Editor (JavaScript)
```
// Define a region of interest.
varroi=ee.Geometry.BBox(-122.93,36.99,-121.20,38.16);
// Define a function that scales and masks Landsat 8 surface reflectance images.
functionprepSrL8(image){
// Develop masks for unwanted pixels (fill, cloud, cloud shadow).
varqaMask=image.select('QA_PIXEL').bitwiseAnd(parseInt('11111',2)).eq(0);
varsaturationMask=image.select('QA_RADSAT').eq(0);
// Apply the scaling factors to the appropriate bands.
vargetFactorImg=function(factorNames){
varfactorList=image.toDictionary().select(factorNames).values();
returnee.Image.constant(factorList);
};
varscaleImg=getFactorImg([
'REFLECTANCE_MULT_BAND_.|TEMPERATURE_MULT_BAND_ST_B10']);
varoffsetImg=getFactorImg([
'REFLECTANCE_ADD_BAND_.|TEMPERATURE_ADD_BAND_ST_B10']);
varscaled=image.select('SR_B.|ST_B10').multiply(scaleImg).add(offsetImg);
// Replace original bands with scaled bands and apply masks.
returnimage.addBands(scaled,null,true)
.updateMask(qaMask).updateMask(saturationMask);
}
// Make a cloud-free Landsat 8 surface reflectance composite.
varinput=ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
.filterBounds(roi)
.filterDate('2020-03-01','2020-07-01')
.map(prepSrL8)
.median()
.setDefaultProjection('EPSG:4326',null,30)
.select(['SR_B2','SR_B3','SR_B4','SR_B5','SR_B6','SR_B7']);
// Use MODIS land cover, IGBP classification, for training.
varmodis=ee.Image('MODIS/006/MCD12Q1/2020_01_01')
.select('LC_Type1');
// Sample the input imagery to get a FeatureCollection of training data.
vartraining=input.addBands(modis).sample({
region:roi,
numPixels:5000,
seed:0
});
// Make a Random Forest classifier and train it.
varclassifier=ee.Classifier.smileRandomForest(10)
.train({
features:training,
classProperty:'LC_Type1',
inputProperties:['SR_B2','SR_B3','SR_B4','SR_B5','SR_B6','SR_B7']
});
// Classify the input imagery.
varclassified=input.classify(classifier);
// Get a confusion matrix representing resubstitution accuracy.
vartrainAccuracy=classifier.confusionMatrix();
print('Resubstitution error matrix: ',trainAccuracy);
print('Training overall accuracy: ',trainAccuracy.accuracy());
// Sample the input with a different random seed to get validation data.
varvalidation=input.addBands(modis).sample({
region:roi,
numPixels:5000,
seed:1
// Filter the result to get rid of any null pixels.
}).filter(ee.Filter.notNull(input.bandNames()));
// Classify the validation data.
varvalidated=validation.classify(classifier);
// Get a confusion matrix representing expected accuracy.
vartestAccuracy=validated.errorMatrix('LC_Type1','classification');
print('Validation error matrix: ',testAccuracy);
print('Validation overall accuracy: ',testAccuracy.accuracy());
// Define a palette for the IGBP classification.
varigbpPalette=[
'aec3d4',// water
'152106','225129','369b47','30eb5b','387242',// forest
'6a2325','c3aa69','b76031','d9903d','91af40',// shrub, grass
'111149',// wetlands
'cdb33b',// croplands
'cc0013',// urban
'33280d',// crop mosaic
'd7cdcc',// snow and ice
'f7e084',// barren
'6f6f6f'// tundra
];
// Display the input and the classification.
Map.centerObject(roi,10);
Map.addLayer(input.clip(roi),
{bands:['SR_B4','SR_B3','SR_B2'],min:0,max:0.25},
'landsat');
Map.addLayer(classified.clip(roi),
{palette:igbpPalette,min:0,max:17},
'classification');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Define a region of interest.
roi = ee.Geometry.BBox(-122.93, 36.99, -121.20, 38.16)
# Define a function that scales and masks Landsat 8 surface reflectance images.
defprep_sr_l8(image):
"""Scales and masks Landsat 8 surface reflectance images."""
 # Develop masks for unwanted pixels (fill, cloud, cloud shadow).
 qa_mask = image.select('QA_PIXEL').bitwiseAnd(0b1111).eq(0)
 saturation_mask = image.select('QA_RADSAT').eq(0)
 # Apply the scaling factors to the appropriate bands.
 def_get_factor_img(factor_names):
  factor_list = image.toDictionary().select(factor_names).values()
  return ee.Image.constant(factor_list)
 scale_img = _get_factor_img([
   'REFLECTANCE_MULT_BAND_.|TEMPERATURE_MULT_BAND_ST_B10'])
 offset_img = _get_factor_img([
   'REFLECTANCE_ADD_BAND_.|TEMPERATURE_ADD_BAND_ST_B10'])
 scaled = image.select('SR_B.|ST_B10').multiply(scale_img).add(offset_img)
 # Replace original bands with scaled bands and apply masks.
 return image.addBands(scaled, None, True).updateMask(
   qa_mask).updateMask(saturation_mask)

# Make a cloud-free Landsat 8 surface reflectance composite.
input_image = (
  ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
  .filterBounds(roi)
  .filterDate('2020-03-01', '2020-07-01')
  .map(prep_sr_l8)
  .median()
  .setDefaultProjection('EPSG:4326', None, 30)
  .select(['SR_B2', 'SR_B3', 'SR_B4', 'SR_B5', 'SR_B6', 'SR_B7'])
)
# Use MODIS land cover, IGBP classification, for training.
modis = ee.Image('MODIS/006/MCD12Q1/2020_01_01').select('LC_Type1')
# Sample the input imagery to get a FeatureCollection of training data.
training = input_image.addBands(modis).sample(
  region=roi, numPixels=5000, seed=0
)
# Make a Random Forest classifier and train it.
classifier = ee.Classifier.smileRandomForest(10).train(
  features=training,
  classProperty='LC_Type1',
  inputProperties=['SR_B2', 'SR_B3', 'SR_B4', 'SR_B5', 'SR_B6', 'SR_B7'],
)
# Classify the input imagery.
classified = input_image.classify(classifier)
# Get a confusion matrix representing resubstitution accuracy.
train_accuracy = classifier.confusionMatrix()
display('Resubstitution error matrix:', train_accuracy)
display('Training overall accuracy:', train_accuracy.accuracy())
# Sample the input with a different random seed to get validation data.
validation = (
  input_image.addBands(modis)
  .sample(
    region=roi,
    numPixels=5000,
    seed=1,
    # Filter the result to get rid of any null pixels.
  )
  .filter(ee.Filter.notNull(input_image.bandNames()))
)
# Classify the validation data.
validated = validation.classify(classifier)
# Get a confusion matrix representing expected accuracy.
test_accuracy = validated.errorMatrix('LC_Type1', 'classification')
display('Validation error matrix:', test_accuracy)
display('Validation overall accuracy:', test_accuracy.accuracy())
# Define a palette for the IGBP classification.
igbp_palette = [
  'aec3d4', # water
  '152106', '225129', '369b47', '30eb5b', '387242', # forest
  '6a2325', 'c3aa69', 'b76031', 'd9903d', '91af40', # shrub, grass
  '111149', # wetlands
  'cdb33b', # croplands
  'cc0013', # urban
  '33280d', # crop mosaic
  'd7cdcc', # snow and ice
  'f7e084', # barren
  '6f6f6f'  # tundra
]
# Display the input and the classification with geemap in a notebook.
m = geemap.Map()
m.center_object(roi, 10)
m.add_layer(
  input_image.clip(roi),
  {'bands': ['SR_B4', 'SR_B3', 'SR_B2'], 'min': 0, 'max': 0.25},
  'landsat',
)
m.add_layer(
  classified.clip(roi),
  {'palette': igbp_palette, 'min': 0, 'max': 17},
  'classification',
)
m
```
**Exercise:** To see the impact of the classifier model, try replacing `ee.Classifier.smileRandomForest` with `ee.Classifier.smileGradientTreeBoost` in the previous example. 
This example uses a random forest ([Breiman 2001](http://rd.springer.com/article/10.1023/A:1010933404324)) classifier with 10 trees to downscale MODIS data to Landsat resolution. The `sample()` method generates two random samples from the MODIS data: one for training and one for validation. The training sample is used to train the classifier. You can get resubstitution accuracy on the training data from `classifier.confusionMatrix()`. To get validation accuracy, classify the validation data. This adds a `classification` property to the validation `FeatureCollection`. Call `errorMatrix()` on the classified `FeatureCollection` to get a confusion matrix representing validation (expected) accuracy.
Inspect the output to see that the overall accuracy estimated from the training data is much higher than the validation data. The accuracy estimated from training data is an overestimate because the random forest is “fit” to the training data. The expected accuracy on unknown data is lower, as indicated by the estimate from the validation data.
You can also take a single sample and partition it with the [`randomColumn()`](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-randomcolumn) method on feature collections. Continuing the previous example: 
### Code Editor (JavaScript)
```
varsample=input.addBands(modis).sample({
region:roi,
numPixels:5000,
seed:0
});
// The randomColumn() method will add a column of uniform random
// numbers in a column named 'random' by default.
sample=sample.randomColumn();
varsplit=0.7;// Roughly 70% training, 30% testing.
vartraining=sample.filter(ee.Filter.lt('random',split));
varvalidation=sample.filter(ee.Filter.gte('random',split));
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
sample = input_image.addBands(modis).sample(region=roi, numPixels=5000, seed=0)
# The randomColumn() method will add a column of uniform random
# numbers in a column named 'random' by default.
sample = sample.randomColumn()
split = 0.7 # Roughly 70% training, 30% testing.
training = sample.filter(ee.Filter.lt('random', split))
validation = sample.filter(ee.Filter.gte('random', split))
```

You may also want to ensure that the training samples are uncorrelated with the evaluation samples. This might result from spatial autocorrelation of the phenomenon being predicted. One way to exclude samples that might be correlated in this manner is to remove samples that are within some distance to any other sample(s). This can be accomplished with a spatial join: 
### Code Editor (JavaScript)
```
// Sample the input imagery to get a FeatureCollection of training data.
varsample=input.addBands(modis).sample({
region:roi,
numPixels:5000,
seed:0,
geometries:true,
tileScale:16
});
// The randomColumn() method will add a column of uniform random
// numbers in a column named 'random' by default.
sample=sample.randomColumn();
varsplit=0.7;// Roughly 70% training, 30% testing.
vartraining=sample.filter(ee.Filter.lt('random',split));
print('Training size:',training.size());
varvalidation=sample.filter(ee.Filter.gte('random',split));
// Spatial join.
vardistFilter=ee.Filter.withinDistance({
distance:1000,
leftField:'.geo',
rightField:'.geo',
maxError:10
});
varjoin=ee.Join.inverted();
// Apply the join.
training=join.apply(training,validation,distFilter);
print('Training size after spatial filtering:',training.size());
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Sample the input imagery to get a FeatureCollection of training data.
sample = input_image.addBands(modis).sample(
  region=roi, numPixels=5000, seed=0, geometries=True, tileScale=16
)
# The randomColumn() method will add a column of uniform random
# numbers in a column named 'random' by default.
sample = sample.randomColumn()
split = 0.7 # Roughly 70% training, 30% testing.
training = sample.filter(ee.Filter.lt('random', split))
display('Training size:', training.size())
validation = sample.filter(ee.Filter.gte('random', split))
# Spatial join.
dist_filter = ee.Filter.withinDistance(
  distance=1000, leftField='.geo', rightField='.geo', maxError=10
)
join = ee.Join.inverted()
# Apply the join.
training = join.apply(training, validation, dist_filter)
display('Training size after spatial filtering:', training.size())
```

In the previous snippet, note that `geometries` is set to `true` in `sample()`. This is to retain the spatial information of the sample points needed for a spatial join. Also note that `tileScale` is set to `16`. This is to avoid the "User memory limit exceeded" error. 
##  Saving Classifiers 
Training a classifier on a large amount of input data may not be possible interactively because the input is too large (>99 MB) or because training takes too long (5 minutes). Use `Export.classifier.toAsset` to run the classifier training as a batch job, where it can run for longer with more memory. Expensive-to-train classifiers can be exported and reloaded to avoid the need to retrain. 
**NOTE** : Currently the only `ee.Classifiers`(s) that can be exported are `ee.Classifier.smileRandomForest`, `ee.Classifier.smileCart`, `ee.Classifier.DecisionTree` and `ee.Classifier.DecisionTreeEnsemble`. 
### Code Editor (JavaScript)
```
// Using the random forest classifier defined earlier, export the random
// forest classifier as an Earth Engine asset.
varclassifierAssetId='projects/<PROJECT-ID>/assets/upscaled_MCD12Q1_random_forest';
Export.classifier.toAsset(
classifier,
'Saved-random-forest-IGBP-classification',
classifierAssetId
);
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Using the random forest classifier defined earlier, export the random
# forest classifier as an Earth Engine asset.
classifier_asset_id = (
  'projects/<PROJECT-ID>/assets/upscaled_MCD12Q1_random_forest'
)
task = ee.batch.Export.classifier.toAsset(
  classifier, 'Saved-random-forest-IGBP-classification', classifier_asset_id
)
task.start()
```

To load the saved classifier, use the algorithm `ee.Classifier.load`, specify the exported classifier ID and use it just like any other trained classifier. 
### Code Editor (JavaScript)
```
// Once the classifier export finishes, we can load our saved classifier.
varsavedClassifier=ee.Classifier.load(classifierAssetId);
// We can perform classification just as before with the saved classifier now.
varclassified=input.classify(savedClassifier);
Map.addLayer(classified.clip(roi),
{palette:igbpPalette,min:0,max:17},
'classification');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Once the classifier export finishes, we can load our saved classifier.
saved_classifier = ee.Classifier.load(classifier_asset_id)
# We can perform classification just as before with the saved classifier now.
classified = input_image.classify(saved_classifier)
m = geemap.Map()
m.center_object(roi, 10)
m.add_layer(
  classified.clip(roi),
  {'palette': igbp_palette, 'min': 0, 'max': 17},
  'classification',
)
m
```

