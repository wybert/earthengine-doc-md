 
#  ee.FeatureCollection.cluster 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Clusters each feature in a collection, adding a new column to each feature containing the cluster number to which it has been assigned. Usage| Returns  
---|---  
`FeatureCollection.cluster(clusterer,  _outputName_)`| FeatureCollection  
Argument| Type| Details  
---|---|---  
this: `features`| FeatureCollection| The collection of features to cluster. Each feature must contain all the properties in the clusterer's schema.  
`clusterer`| Clusterer| The clusterer to use.  
`outputName`| String, default: "cluster"| The name of the output property to be added.  
## Examples
### Code Editor (JavaScript)
```
// Import a Sentinel-2 surface reflectance image.
varimage=ee.Image('COPERNICUS/S2_SR/20210109T185751_20210109T185931_T10SEG');
// Get the image geometry to define the geographical bounds of a point sample.
varimageBounds=image.geometry();
// Sample the image at a set of random points; a feature collection is returned.
varpointSampleFc=image.sample(
{region:imageBounds,scale:20,numPixels:1000,geometries:true});
// Instantiate a k-means clusterer and train it.
varclusterer=ee.Clusterer.wekaKMeans(5).train(pointSampleFc);
// Cluster the input using the trained clusterer; optionally specify the name
// of the output cluster ID property.
varclusteredFc=pointSampleFc.cluster(clusterer,'spectral_cluster');
print('Note added "spectral_cluster" property for an example feature',
clusteredFc.first().toDictionary());
// Visualize the clusters by applying a unique color to each cluster ID.
varpalette=ee.List(['8dd3c7','ffffb3','bebada','fb8072','80b1d3']);
varclusterVis=clusteredFc.map(function(feature){
returnfeature.set('style',{
color:palette.get(feature.get('spectral_cluster')),
});
}).style({styleProperty:'style'});
// Display the points colored by cluster ID with the S2 image.
Map.setCenter(-122.35,37.47,9);
Map.addLayer(image,{bands:['B4','B3','B2'],min:0,max:1500},'S2 image');
Map.addLayer(clusterVis,null,'Clusters');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Import a Sentinel-2 surface reflectance image.
image = ee.Image('COPERNICUS/S2_SR/20210109T185751_20210109T185931_T10SEG')
# Get the image geometry to define the geographical bounds of a point sample.
image_bounds = image.geometry()
# Sample the image at a set of random points a feature collection is returned.
point_sample_fc = image.sample(
  region=image_bounds, scale=20, numPixels=1000, geometries=True
)
# Instantiate a k-means clusterer and train it.
clusterer = ee.Clusterer.wekaKMeans(5).train(point_sample_fc)
# Cluster the input using the trained clusterer optionally specify the name
# of the output cluster ID property.
clustered_fc = point_sample_fc.cluster(clusterer, 'spectral_cluster')
display(
  'Note added "spectral_cluster" property for an example feature',
  clustered_fc.first().toDictionary(),
)
# Visualize the clusters by applying a unique color to each cluster ID.
palette = ee.List(['8dd3c7', 'ffffb3', 'bebada', 'fb8072', '80b1d3'])
cluster_vis = clustered_fc.map(
  lambda feature: feature.set(
    'style', {'color': palette.get(feature.get('spectral_cluster'))}
  )
).style(styleProperty='style')
# Display the points colored by cluster ID with the S2 image.
m = geemap.Map()
m.set_center(-122.35, 37.47, 9)
m.add_layer(
  image, {'bands': ['B4', 'B3', 'B2'], 'min': 0, 'max': 1500}, 'S2 image'
)
m.add_layer(cluster_vis, None, 'Clusters')
m
```

