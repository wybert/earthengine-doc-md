 
#  ee.FeatureCollection.errorMatrix
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-errormatrix#examples)


Computes a 2D error matrix for a collection by comparing two columns of a collection: one containing the actual values, and one containing predicted values. The values are expected to be small contiguous integers, starting from 0. Axis 0 (the rows) of the matrix correspond to the actual values, and Axis 1 (the columns) to the predicted values. 
Usage| Returns  
---|---  
`FeatureCollection.errorMatrix(actual, predicted,  _order_)`| ConfusionMatrix  
Argument| Type| Details  
---|---|---  
this: `collection`| FeatureCollection| The input collection.  
`actual`| String| The name of the property containing the actual value.  
`predicted`| String| The name of the property containing the predicted value.  
`order`| List, default: null| A list of the expected values. If this argument is not specified, the values are assumed to be contiguous and span the range 0 to maxValue. If specified, only values matching this list are used, and the matrix will have dimensions and order matching this list.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-errormatrix#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-errormatrix#colab-python-sample) More
```
/**
 * Classifies features in a FeatureCollection and computes an error matrix.
 */
// Combine Landsat and NLCD images using only the bands representing
// predictor variables (spectral reflectance) and target labels (land cover).
varspectral=
ee.Image('LANDSAT/LC08/C02/T1_L2/LC08_038032_20160820').select('SR_B[1-7]');
varlandcover=
ee.Image('USGS/NLCD_RELEASES/2016_REL/2016').select('landcover');
varsampleSource=spectral.addBands(landcover);
// Sample the combined images to generate a FeatureCollection.
varsample=sampleSource.sample({
region:spectral.geometry(),// sample only from within Landsat image extent
scale:30,
numPixels:2000,
geometries:true
})
// Add a random value column with uniform distribution for hold-out
// training/validation splitting.
.randomColumn({distribution:'uniform'});
print('Sample for classifier development',sample);
// Split out ~80% of the sample for training the classifier.
vartraining=sample.filter('random < 0.8');
print('Training set',training);
// Train a random forest classifier.
varclassifier=ee.Classifier.smileRandomForest(10).train({
features:training,
classProperty:landcover.bandNames().get(0),
inputProperties:spectral.bandNames()
});
// Classify the sample.
varpredictions=sample.classify(
{classifier:classifier,outputName:'predicted_landcover'});
print('Predictions',predictions);
// Split out the validation feature set.
varvalidation=predictions.filter('random >= 0.8');
print('Validation set',validation);
// Get a list of possible class values to use for error matrix axis labels.
varorder=sample.aggregate_array('landcover').distinct().sort();
print('Error matrix axis labels',order);
// Compute an error matrix that compares predicted vs. expected values.
varerrorMatrix=validation.errorMatrix({
actual:landcover.bandNames().get(0),
predicted:'predicted_landcover',
order:order
});
print('Error matrix',errorMatrix);
// Compute accuracy metrics from the error matrix.
print("Overall accuracy",errorMatrix.accuracy());
print("Consumer's accuracy",errorMatrix.consumersAccuracy());
print("Producer's accuracy",errorMatrix.producersAccuracy());
print("Kappa",errorMatrix.kappa());
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
frompprintimport pprint
# Classifies features in a FeatureCollection and computes an error matrix.
# Combine Landsat and NLCD images using only the bands representing
# predictor variables (spectral reflectance) and target labels (land cover).
spectral = ee.Image('LANDSAT/LC08/C02/T1_L2/LC08_038032_20160820').select(
  'SR_B[1-7]')
landcover = ee.Image('USGS/NLCD_RELEASES/2016_REL/2016').select('landcover')
sample_source = spectral.addBands(landcover)
# Sample the combined images to generate a FeatureCollection.
sample = sample_source.sample(**{
  # sample only from within Landsat image extent
  'region': spectral.geometry(),
  'scale': 30,
  'numPixels': 2000,
  'geometries': True
  })
# Add a random value column with uniform distribution for hold-out
# training/validation splitting.
sample = sample.randomColumn(**{'distribution': 'uniform'})
print('Sample for classifier development:', sample.getInfo())
# Split out ~80% of the sample for training the classifier.
training = sample.filter('random < 0.8')
print('Training set:', training.getInfo())
# Train a random forest classifier.
classifier = ee.Classifier.smileRandomForest(10).train(**{
  'features': training,
  'classProperty': landcover.bandNames().get(0),
  'inputProperties': spectral.bandNames()
  })
# Classify the sample.
predictions = sample.classify(
  **{'classifier': classifier, 'outputName': 'predicted_landcover'})
print('Predictions:', predictions.getInfo())
# Split out the validation feature set.
validation = predictions.filter('random >= 0.8')
print('Validation set:', validation.getInfo())
# Get a list of possible class values to use for error matrix axis labels.
order = sample.aggregate_array('landcover').distinct().sort()
print('Error matrix axis labels:')
pprint(order.getInfo())
# Compute an error matrix that compares predicted vs. expected values.
error_matrix = validation.errorMatrix(**{
  'actual': landcover.bandNames().get(0),
  'predicted': 'predicted_landcover',
  'order': order
  })
print('Error matrix:')
pprint(error_matrix.getInfo())
# Compute accuracy metrics from the error matrix.
print('Overall accuracy:', error_matrix.accuracy().getInfo())
print('Consumer\'s accuracy:')
pprint(error_matrix.consumersAccuracy().getInfo())
print('Producer\'s accuracy:')
pprint(error_matrix.producersAccuracy().getInfo())
print('Kappa:', error_matrix.kappa().getInfo())
```

Was this helpful?
