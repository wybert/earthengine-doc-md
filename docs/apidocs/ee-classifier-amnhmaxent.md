 
#  ee.Classifier.amnhMaxent
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-classifier-amnhmaxent#examples)


Creates a Maximum Entropy classifier. Maxent is used to model species distribution probabilities using environmental data for locations of known presence and for a large number of 'background' locations. For more information and to cite, see: https://biodiversityinformatics.amnh.org/open_source/maxent/ and the reference publication: Phillips, et. al., 2004 A maximum entropy approach to species distribution modeling, Proceedings of the Twenty-First International Conference on Machine Learning. The output is a single band named 'probability', containing the modeled probability, and an additional band named 'clamp' when the 'writeClampGrid' argument is true. 
Usage| Returns  
---|---  
`ee.Classifier.amnhMaxent( _categoricalNames_, _outputFormat_, _autoFeature_, _linear_, _quadratic_, _product_, _threshold_, _hinge_, _hingeThreshold_, _l2lqThreshold_, _lq2lqptThreshold_, _addSamplesToBackground_, _addAllSamplesToBackground_, _betaMultiplier_, _betaHinge_, _betaLqp_, _betaCategorical_, _betaThreshold_, _extrapolate_, _doClamp_, _writeClampGrid_, _randomTestPoints_, _seed_)`| Classifier  
Argument| Type| Details  
---|---|---  
`categoricalNames`| List, default: null| A list of the names of the categorical inputs. Any inputs not listed in this argument are considered to be continuous.  
`outputFormat`| String, default: "cloglog"| Representation of probabilities in output.  
`autoFeature`| Boolean, default: true| Automatically select which feature classes to use, based on number of training samples.  
`linear`| Boolean, default: true| Allow linear features to be used. Ignored when autofeature is true.  
`quadratic`| Boolean, default: true| Allow quadratic features to be used. Ignored when autofeature is true.  
`product`| Boolean, default: true| Allow product features to be used. Ignored when autofeature is true.  
`threshold`| Boolean, default: false| Allow threshold features to be used. Ignored when autofeature is true.  
`hinge`| Boolean, default: true| Allow hinge features to be used. Ignored when autofeature is true.  
`hingeThreshold`| Integer, default: 15| Number of samples at which hinge features start being used. Ignored when autofeature is false.  
`l2lqThreshold`| Integer, default: 10| Number of samples at which quadratic features start being used. Ignored when autofeature is false.  
`lq2lqptThreshold`| Integer, default: 80| Number of samples at which product and threshold features start being used. Ignored when autofeature is false.  
`addSamplesToBackground`| Boolean, default: true| Add to the background any sample for which has a combination of environmental values that isn't already present in the background.  
`addAllSamplesToBackground`| Boolean, default: false| Add all samples to the background, even if they have combinations of environmental values that are already present in the background.  
`betaMultiplier`| Float, default: 1| Regularization multiplier. Multiply all automatic regularization parameters by this number. A higher number gives a more spread-out distribution.  
`betaHinge`| Float, default: -1| Regularization parameter to be applied to all hinge features; negative value enables automatic setting.  
`betaLqp`| Float, default: -1| Regularization parameter to be applied to all linear, quadratic and product features; negative value enables automatic setting.  
`betaCategorical`| Float, default: -1| Regularization parameter to be applied to all categorical features; negative value enables automatic setting.  
`betaThreshold`| Float, default: -1| Regularization parameter to be applied to all threshold features; negative value enables automatic setting.  
`extrapolate`| Boolean, default: true| Extrapolate. Predict to regions of environmental space outside the limits encountered during training.  
`doClamp`| Boolean, default: true| Apply clamping to output.  
`writeClampGrid`| Boolean, default: true| Adds a band to the output ('clamp') showing the spatial distribution of clamping. At each point, the value is the absolute difference between prediction values with and without clamping.  
`randomTestPoints`| Integer, default: 0| Random test percentage. The percentage of training points to hold aside as test points, used to compute AUX, omission, etc.  
`seed`| Long, default: 0| A seed used when generating random numbers.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-classifier-amnhmaxent#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-classifier-amnhmaxent#colab-python-sample) More
```
// Create some sample species presence/absence training data.
vartrainingData=ee.FeatureCollection([
// Species present points.
ee.Feature(ee.Geometry.Point([-122.39567,38.02740]),{presence:1}),
ee.Feature(ee.Geometry.Point([-122.68560,37.83690]),{presence:1}),
// Species absent points.
ee.Feature(ee.Geometry.Point([-122.59755,37.92402]),{presence:0}),
ee.Feature(ee.Geometry.Point([-122.47137,37.99291]),{presence:0}),
ee.Feature(ee.Geometry.Point([-122.52905,37.85642]),{presence:0}),
ee.Feature(ee.Geometry.Point([-122.03010,37.66660]),{presence:0})
]);
// Import a Landsat 8 surface reflectance image.
varimage=ee.Image('LANDSAT/LC08/C02/T1_L2/LC08_044034_20200606')
// Select the optical and thermal bands.
.select(['.._B.*']);
// Sample the image at the location of the points.
vartraining=image.sampleRegions({collection:trainingData,scale:30});
// Define and train a Maxent classifier from the image-sampled points.
varclassifier=ee.Classifier.amnhMaxent().train({
features:training,
classProperty:'presence',
inputProperties:image.bandNames()
});
// Classify the image using the Maxent classifier.
varimageClassified=image.classify(classifier);
// Display the layers on the map.
// Species presence probability [0, 1] grades from black to white.
Map.centerObject(image,9);
Map.addLayer(
image.select(['SR_B4','SR_B3','SR_B2']).multiply(0.0000275).add(-0.2),
{min:0,max:0.3},'Image');
Map.addLayer(
imageClassified,{bands:'probability',min:0,max:1},'Probability');
Map.addLayer(
trainingData.filter('presence == 0'),{color:'red'},
'Training data (species absent)');
Map.addLayer(
trainingData.filter('presence == 1'),{color:'blue'},
'Training data (species present)');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
"""Demonstrates the ee.Classifier.amnhMaxent method."""
importee

# Authenticates to the Earth Engine servers.
ee.Authenticate()
# Initializes the client library.
ee.Initialize()

# Create some sample species presence/absence training data.
training_data = ee.FeatureCollection([
  # Species present points.
  ee.Feature(ee.Geometry.Point([-122.39567, 38.02740]), {'presence': 1}),
  ee.Feature(ee.Geometry.Point([-122.68560, 37.83690]), {'presence': 1}),
  # Species absent points.
  ee.Feature(ee.Geometry.Point([-122.59755, 37.92402]), {'presence': 0}),
  ee.Feature(ee.Geometry.Point([-122.47137, 37.99291]), {'presence': 0}),
  ee.Feature(ee.Geometry.Point([-122.52905, 37.85642]), {'presence': 0}),
  ee.Feature(ee.Geometry.Point([-122.03010, 37.66660]), {'presence': 0})
])
# Import a Landsat 8 image and select the reflectance bands.
image = (ee.Image('LANDSAT/LC08/C02/T1_L2/LC08_044034_20200606')
     .select(['SR_B[1-7]'])
     .multiply(0.0000275).add(-0.2)) # Apply scaling factors.
# Sample the image at the location of the points.
training = image.sampleRegions(**{
  'collection': training_data,
  'scale': 30
})
# Define and train a Maxent classifier from the image-sampled points.
classifier = ee.Classifier.amnhMaxent().train(**{
  'features': training,
  'classProperty': 'presence',
  'inputProperties': image.bandNames()
})
# Classify the image using the Maxent classifier.
image_classified = image.classify(classifier)
```

