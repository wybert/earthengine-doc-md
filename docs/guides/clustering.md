 
#  Unsupervised Classification (clustering)
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
The `ee.Clusterer` package handles unsupervised classification (or _clustering_) in Earth Engine. These algorithms are currently based on the algorithms with the same name in [Weka](http://www.cs.waikato.ac.nz/ml/weka/). More details about each `Clusterer` are available in the [reference docs](https://developers.google.com/earth-engine/apidocs).
Clusterers are used in the same manner as classifiers in Earth Engine. The general workflow for clustering is:
  1. Assemble features with numeric properties in which to find clusters.
  2. Instantiate a clusterer. Set its parameters if necessary.
  3. Train the clusterer using the training data.
  4. Apply the clusterer to an image or feature collection.
  5. Label the clusters.


The training data is a `FeatureCollection` with properties that will be input to the clusterer. Unlike classifiers, there is no input class value for an `Clusterer`. Like classifiers, the data for the train and apply steps are expected to have the same number of values. When a trained clusterer is applied to an image or table, it assigns an integer cluster ID to each pixel or feature.
Here is a simple example of building and using an `ee.Clusterer`:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/clustering#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/clustering#colab-python-sample) More
```
// Define a region in which to generate a segmented map.
varregion=ee.Geometry.Rectangle(29.7,30,32.5,31.7);
// Load a Landsat composite for input.
varinput=ee.ImageCollection('LANDSAT/COMPOSITES/C02/T1_L2_32DAY')
.filterDate('2001-05','2001-06')
.first()
.clip(region);
// Display the sample region.
Map.setCenter(31.5,31.0,8);
Map.addLayer(ee.Image().paint(region,0,2),{},'region');
// Make the training dataset.
vartraining=input.sample({
region:region,
scale:30,
numPixels:5000
});
// Instantiate the clusterer and train it.
varclusterer=ee.Clusterer.wekaKMeans(15).train(training);
// Cluster the input using the trained clusterer.
varresult=input.cluster(clusterer);
// Display the clusters with random colors.
Map.addLayer(result.randomVisualizer(),{},'clusters');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Define a region in which to generate a segmented map.
region = ee.Geometry.Rectangle(29.7, 30, 32.5, 31.7)
# Load a Landsat composite for input.
input = (
  ee.ImageCollection('LANDSAT/COMPOSITES/C02/T1_L2_32DAY')
  .filterDate('2001-05', '2001-06')
  .first()
  .clip(region)
)
# Display the sample region.
m = geemap.Map()
m.set_center(31.5, 31.0, 8)
m.add_layer(ee.Image().paint(region, 0, 2), {}, 'region')
# Make the training dataset.
training = input.sample(region=region, scale=30, numPixels=5000)
# Instantiate the clusterer and train it.
clusterer = ee.Clusterer.wekaKMeans(15).train(training)
# Cluster the input using the trained clusterer.
result = input.cluster(clusterer)
# Display the clusters with random colors.
m.add_layer(result.randomVisualizer(), {}, 'clusters')
m
```

Please note:
  * The same inputs should always produce the same outputs, but reordering the inputs can change the results.
  * Training with as few as 10 bands * 100k points can produce an Out Of Memory error.
  * Cobweb can take a long time to finish and can produce a large number of clusters.
  * The output clusters and their IDs are dependent on the algorithm and inputs.


Was this helpful?
