 
#  ee.Classifier.libsvm 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-classifier-libsvm#examples)


Creates an empty Support Vector Machine classifier. 
Usage| Returns  
---|---  
`ee.Classifier.libsvm( _decisionProcedure_, _svmType_, _kernelType_, _shrinking_, _degree_, _gamma_, _coef0_, _cost_, _nu_, _terminationEpsilon_, _lossEpsilon_, _oneClass_)`| Classifier  
Argument| Type| Details  
---|---|---  
`decisionProcedure`| String, default: "Voting"| The decision procedure to use for classification. Either 'Voting' or 'Margin'. Not used for regression.  
`svmType`| String, default: "C_SVC"| The SVM type. One of `C_SVC`, `NU_SVC`, `ONE_CLASS`, `EPSILON_SVR`, or `NU_SVR`.  
`kernelType`| String, default: "LINEAR"| The kernel type. One of LINEAR (u′×v), POLY ((γ×u′×v + coef₀)ᵈᵉᵍʳᵉᵉ), RBF (exp(-γ×|u-v|²)), or SIGMOID (tanh(γ×u′×v + coef₀)).  
`shrinking`| Boolean, default: true| Whether to use shrinking heuristics.  
`degree`| Integer, default: null| The degree of polynomial. Valid for POLY kernels.  
`gamma`| Float, default: null| The gamma value in the kernel function. Defaults to the reciprocal of the number of features. Valid for POLY, RBF, and SIGMOID kernels.  
`coef0`| Float, default: null| The coef₀ value in the kernel function. Defaults to 0. Valid for POLY and SIGMOID kernels.  
`cost`| Float, default: null| The cost (C) parameter. Defaults to 1. Only valid for C-SVC, epsilon-SVR, and nu-SVR.  
`nu`| Float, default: null| The nu parameter. Defaults to 0.5. Only valid for nu-SVC, one-class SVM, and nu-SVR.  
`terminationEpsilon`| Float, default: null| The termination criterion tolerance (e). Defaults to 0.001. Only valid for epsilon-SVR.  
`lossEpsilon`| Float, default: null| The epsilon in the loss function (p). Defaults to 0.1. Only valid for epsilon-SVR.  
`oneClass`| Integer, default: null| The class of the training data on which to train in a one-class SVM. Defaults to 0. Only valid for one-class SVM. Possible values are 0 and 1. The classifier output is binary (0/1) and will match this class value for the data determined to be in the class.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-classifier-libsvm#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-classifier-libsvm#colab-python-sample) More
```
// A Sentinel-2 surface reflectance image, reflectance bands selected,
// serves as the source for training and prediction in this contrived example.
varimg=ee.Image('COPERNICUS/S2_SR/20210109T185751_20210109T185931_T10SEG')
.select('B.*');
// ESA WorldCover land cover map, used as label source in classifier training.
varlc=ee.Image('ESA/WorldCover/v100/2020');
// Remap the land cover class values to a 0-based sequential series.
varclassValues=[10,20,30,40,50,60,70,80,90,95,100];
varremapValues=ee.List.sequence(0,10);
varlabel='lc';
lc=lc.remap(classValues,remapValues).rename(label).toByte();
// Add land cover as a band of the reflectance image and sample 100 pixels at
// 10 m scale from each land cover class within a region of interest.
varroi=ee.Geometry.Rectangle(-122.347,37.743,-122.024,37.838);
varsample=img.addBands(lc).stratifiedSample({
numPoints:100,
classBand:label,
region:roi,
scale:10,
geometries:true
});
// Add a random value field to the sample and use it to approximately split 80%
// of the features into a training set and 20% into a validation set.
sample=sample.randomColumn();
vartrainingSample=sample.filter('random <= 0.8');
varvalidationSample=sample.filter('random > 0.8');
// Train an SVM classifier (C-SVM classification, voting decision procedure,
// linear kernel) from the training sample.
vartrainedClassifier=ee.Classifier.libsvm().train({
features:trainingSample,
classProperty:label,
inputProperties:img.bandNames()
});
// Get information about the trained classifier.
print('Results of trained classifier',trainedClassifier.explain());
// Get a confusion matrix and overall accuracy for the training sample.
vartrainAccuracy=trainedClassifier.confusionMatrix();
print('Training error matrix',trainAccuracy);
print('Training overall accuracy',trainAccuracy.accuracy());
// Get a confusion matrix and overall accuracy for the validation sample.
validationSample=validationSample.classify(trainedClassifier);
varvalidationAccuracy=validationSample.errorMatrix(label,'classification');
print('Validation error matrix',validationAccuracy);
print('Validation accuracy',validationAccuracy.accuracy());
// Classify the reflectance image from the trained classifier.
varimgClassified=img.classify(trainedClassifier);
// Add the layers to the map.
varclassVis={
min:0,
max:10,
palette:['006400','ffbb22','ffff4c','f096ff','fa0000','b4b4b4',
'f0f0f0','0064c8','0096a0','00cf75','fae6a0']
};
Map.setCenter(-122.184,37.796,12);
Map.addLayer(img,{bands:['B11','B8','B3'],min:100,max:3500},'img');
Map.addLayer(lc,classVis,'lc');
Map.addLayer(imgClassified,classVis,'Classified');
Map.addLayer(roi,{color:'white'},'ROI',false,0.5);
Map.addLayer(trainingSample,{color:'black'},'Training sample',false);
Map.addLayer(validationSample,{color:'white'},'Validation sample',false);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# A Sentinel-2 surface reflectance image, reflectance bands selected,
# serves as the source for training and prediction in this contrived example.
img = ee.Image(
  'COPERNICUS/S2_SR/20210109T185751_20210109T185931_T10SEG'
).select('B.*')
# ESA WorldCover land cover map, used as label source in classifier training.
lc = ee.Image('ESA/WorldCover/v100/2020')
# Remap the land cover class values to a 0-based sequential series.
class_values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 100]
remap_values = ee.List.sequence(0, 10)
label = 'lc'
lc = lc.remap(class_values, remap_values).rename(label).toByte()
# Add land cover as a band of the reflectance image and sample 100 pixels at
# 10 m scale from each land cover class within a region of interest.
roi = ee.Geometry.Rectangle(-122.347, 37.743, -122.024, 37.838)
sample = img.addBands(lc).stratifiedSample(
  numPoints=100, classBand=label, region=roi, scale=10, geometries=True
)
# Add a random value field to the sample and use it to approximately split 80%
# of the features into a training set and 20% into a validation set.
sample = sample.randomColumn()
training_sample = sample.filter('random <= 0.8')
validation_sample = sample.filter('random > 0.8')
# Train an SVM classifier (C-SVM classification, voting decision procedure,
# linear kernel) from the training sample.
trained_classifier = ee.Classifier.libsvm().train(
  features=training_sample,
  classProperty=label,
  inputProperties=img.bandNames(),
)
# Get information about the trained classifier.
display('Results of trained classifier', trained_classifier.explain())
# Get a confusion matrix and overall accuracy for the training sample.
train_accuracy = trained_classifier.confusionMatrix()
display('Training error matrix', train_accuracy)
display('Training overall accuracy', train_accuracy.accuracy())
# Get a confusion matrix and overall accuracy for the validation sample.
validation_sample = validation_sample.classify(trained_classifier)
validation_accuracy = validation_sample.errorMatrix(label, 'classification')
display('Validation error matrix', validation_accuracy)
display('Validation accuracy', validation_accuracy.accuracy())
# Classify the reflectance image from the trained classifier.
img_classified = img.classify(trained_classifier)
# Add the layers to the map.
class_vis = {
  'min': 0,
  'max': 10,
  'palette': [
    '006400',
    'ffbb22',
    'ffff4c',
    'f096ff',
    'fa0000',
    'b4b4b4',
    'f0f0f0',
    '0064c8',
    '0096a0',
    '00cf75',
    'fae6a0',
  ],
}
m = geemap.Map()
m.set_center(-122.184, 37.796, 12)
m.add_layer(
  img, {'bands': ['B11', 'B8', 'B3'], 'min': 100, 'max': 3500}, 'img'
)
m.add_layer(lc, class_vis, 'lc')
m.add_layer(img_classified, class_vis, 'Classified')
m.add_layer(roi, {'color': 'white'}, 'ROI', False, 0.5)
m.add_layer(training_sample, {'color': 'black'}, 'Training sample', False)
m.add_layer(
  validation_sample, {'color': 'white'}, 'Validation sample', False
)
m
```

