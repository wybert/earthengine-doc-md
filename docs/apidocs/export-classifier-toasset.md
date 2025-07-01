 
#  Export.classifier.toAsset
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/export-classifier-toasset#examples)


Creates a batch task to export an ee.Classifier as an Earth Engine asset. 
Only supported for ee.Classifier.smileRandomForest, ee.Classifier.smileCart, ee.Classifier.DecisionTree and ee.Classifier.DecisionTreeEnsemble.
Usage| Returns  
---|---  
`Export.classifier.toAsset(classifier,  _description_, _assetId_, _priority_)`|   
Argument|  Type| Details  
---|---|---  
`classifier`| ComputedObject| The classifier to export.  
`description`| String, optional| A human-readable name of the task. Defaults to "myExportClassifierTask".  
`assetId`| String, optional| The destination asset ID.  
`priority`| Number, optional| The priority of the task within the project. Higher priority tasks are scheduled sooner. Must be an integer between 0 and 9999. Defaults to 100.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/export-classifier-toasset#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/export-classifier-toasset#colab-python-sample) More
```
// First gather the training data for a random forest classifier.
// Let's use MCD12Q1 yearly landcover for the labels.
varlandcover=ee.ImageCollection('MODIS/061/MCD12Q1')
.filterDate('2022-01-01','2022-12-31')
.first()
.select('LC_Type1');
// A region of interest for training our classifier.
varregion=ee.Geometry.BBox(17.33,36.07,26.13,43.28);
// Training features will be based on a Landsat 8 composite.
varl8=ee.ImageCollection('LANDSAT/LC08/C02/T1')
.filterBounds(region)
.filterDate('2022-01-01','2023-01-01');
// Draw the Landsat composite, visualizing true color bands.
varlandsatComposite=ee.Algorithms.Landsat.simpleComposite({
collection:l8,
asFloat:true
});
Map.addLayer(landsatComposite,{
min:0,
max:0.3,
bands:['B3','B2','B1']
},'Landsat composite');
// Make a training dataset by sampling the stacked images.
vartraining=landcover.addBands(landsatComposite).sample({
region:region,
scale:30,
// With export to Classifier we can bump this higher to say 10,000.
numPixels:1000
});
varclassifier=ee.Classifier.smileRandomForest({
// We can also increase the number of trees higher to ~100 if needed.
numberOfTrees:3
}).train({features:training,classProperty:'LC_Type1'});
// Create an export classifier task to run.
varassetId='projects/<project-name>/assets/<asset-name>';// <> modify these
Export.classifier.toAsset({
classifier:classifier,
description:'classifier_export',
assetId:assetId
});
// Load the classifier after the export finishes and visualize.
varsavedClassifier=ee.Classifier.load(assetId)
varlandcoverPalette='05450a,086a10,54a708,78d203,009900,c6b044,dcd159,'+
'dade48,fbff13,b6ff05,27ff87,c24f44,a5a5a5,ff6d4c,69fff8,f9ffa4,1c0dff';
varlandcoverVisualization={
palette:landcoverPalette,
min:0,
max:16,
format:'png'
};
Map.addLayer(
landsatComposite.classify(savedClassifier),
landcoverVisualization,
'Upsampled landcover, saved');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# First gather the training data for a random forest classifier.
# Let's use MCD12Q1 yearly landcover for the labels.
landcover = (ee.ImageCollection('MODIS/061/MCD12Q1')
       .filterDate('2022-01-01', '2022-12-31')
       .first()
       .select('LC_Type1'))
# A region of interest for training our classifier.
region = ee.Geometry.BBox(17.33, 36.07, 26.13, 43.28)
# Training features will be based on a Landsat 8 composite.
l8 = (ee.ImageCollection('LANDSAT/LC08/C02/T1')
   .filterBounds(region)
   .filterDate('2022-01-01', '2023-01-01'))
# Draw the Landsat composite, visualizing true color bands.
landsatComposite = ee.Algorithms.Landsat.simpleComposite(
  collection=l8, asFloat=True)
Map = geemap.Map()
Map # Render the map in the notebook.
Map.addLayer(landsatComposite, {
  'min': 0,
  'max': 0.3,
  'bands': ['B3', 'B2', 'B1']
}, 'Landsat composite')
# Make a training dataset by sampling the stacked images.
training = landcover.addBands(landsatComposite).sample(
  region=region,
  scale=30,
  # With export to Classifier we can bump this higher to say 10,000.
  numPixels=1000
)
# We can also increase the number of trees higher to ~100 if needed.
classifier = ee.Classifier.smileRandomForest(
  numberOfTrees=3).train(features=training, classProperty='LC_Type1')
# Create an export classifier task to run.
asset_id = 'projects/<project-name>/assets/<asset-name>' # <> modify these
ee.batch.Export.classifier.toAsset(
  classifier=classifier,
  description='classifier_export',
  assetId=asset_id
)
# Load the classifier after the export finishes and visualize.
savedClassifier = ee.Classifier.load(asset_id)
landcover_palette = [
  '05450a', '086a10', '54a708', '78d203', '009900',
  'c6b044', 'dcd159', 'dade48', 'fbff13', 'b6ff05',
  '27ff87', 'c24f44', 'a5a5a5', 'ff6d4c', '69fff8',
  'f9ffa4', '1c0dff']
landcoverVisualization = {
  'palette': landcover_palette,
  'min': 0,
  'max': 16,
  'format': 'png'
}
Map.addLayer(
  landsatComposite.classify(savedClassifier),
  landcoverVisualization,
  'Upsampled landcover, saved')
```

