 
#  FeatureCollection Overview 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [The FeatureCollection constructor](https://developers.google.com/earth-engine/guides/feature_collections#the-featurecollection-constructor)
    * [Table Datasets](https://developers.google.com/earth-engine/guides/feature_collections#table-datasets)
    * [Random Samples](https://developers.google.com/earth-engine/guides/feature_collections#random-samples)


Groups of related features can be combined into a `FeatureCollection`, to enable additional operations on the entire set such as filtering, sorting and rendering. Besides just simple features (geometry + properties), feature collections can also contain other collections.
## The `FeatureCollection` constructor
One way to create a `FeatureCollection` is to provide the constructor with a list of features. The features don't need to have the same geometry type or the same properties. For example:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/feature_collections#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/feature_collections#colab-python-sample) More
```
// Make a list of Features.
varfeatures=[
ee.Feature(ee.Geometry.Rectangle(30.01,59.80,30.59,60.15),{name:'Voronoi'}),
ee.Feature(ee.Geometry.Point(-73.96,40.781),{name:'Thiessen'}),
ee.Feature(ee.Geometry.Point(6.4806,50.8012),{name:'Dirichlet'})
];
// Create a FeatureCollection from the list and print it.
varfromList=ee.FeatureCollection(features);
print(fromList);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Make a list of Features.
features = [
  ee.Feature(
    ee.Geometry.Rectangle(30.01, 59.80, 30.59, 60.15), {'name': 'Voronoi'}
  ),
  ee.Feature(ee.Geometry.Point(-73.96, 40.781), {'name': 'Thiessen'}),
  ee.Feature(ee.Geometry.Point(6.4806, 50.8012), {'name': 'Dirichlet'}),
]
# Create a FeatureCollection from the list and print it.
from_list = ee.FeatureCollection(features)
display(from_list)
```

Individual geometries can also be turned into a `FeatureCollection` of just one `Feature`:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/feature_collections#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/feature_collections#colab-python-sample) More
```
// Create a FeatureCollection from a single geometry and print it.
varfromGeom=ee.FeatureCollection(ee.Geometry.Point(16.37,48.225));
print(fromGeom);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Create a FeatureCollection from a single geometry and print it.
from_geom = ee.FeatureCollection(ee.Geometry.Point(16.37, 48.225))
display(from_geom)
```

### Table Datasets
Earth Engine hosts a variety of table datasets. To load a table dataset, provide the table ID to the `FeatureCollection` constructor. For example, to load RESOLVE Ecoregions data:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/feature_collections#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/feature_collections#colab-python-sample) More
```
varfc=ee.FeatureCollection('RESOLVE/ECOREGIONS/2017');
Map.setCenter(12.17,20.96,3);
Map.addLayer(fc,{},'ecoregions');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
fc = ee.FeatureCollection('RESOLVE/ECOREGIONS/2017')
m = geemap.Map()
m.set_center(12.17, 20.96, 3)
m.add_layer(fc, {}, 'ecoregions')
display(m)
```

Note that as with image datasets, you can search for table datasets in the [Earth Engine Data Catalog](https://developers.google.com/earth-engine/datasets).
### Random Samples
To get a collection of random points in a specified region, you can use:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/feature_collections#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/feature_collections#colab-python-sample) More
```
// Define an arbitrary region in which to compute random points.
varregion=ee.Geometry.Rectangle(-119.224,34.669,-99.536,50.064);
// Create 1000 random points in the region.
varrandomPoints=ee.FeatureCollection.randomPoints(region);
// Display the points.
Map.centerObject(randomPoints);
Map.addLayer(randomPoints,{},'random points');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Define an arbitrary region in which to compute random points.
region = ee.Geometry.Rectangle(-119.224, 34.669, -99.536, 50.064)
# Create 1000 random points in the region.
random_points = ee.FeatureCollection.randomPoints(region)
# Display the points.
m = geemap.Map()
m.center_object(random_points)
m.add_layer(random_points, {}, 'random points')
display(m)
```

