 
#  Feature Overview
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Creating Feature objects](https://developers.google.com/earth-engine/guides/features#creating-feature-objects)


A `Feature` in Earth Engine is defined as a GeoJSON Feature. Specifically, a `Feature` is an object with a `geometry` property storing a `Geometry` object (or null) and a `properties` property storing a dictionary of other properties.
## Creating Feature objects
To create a `Feature`, provide the constructor with a `Geometry` and (optionally) a dictionary of other properties. For example:
### Code Editor (JavaScript)
```
// Create an ee.Geometry.
varpolygon=ee.Geometry.Polygon([
[[-35,-10],[35,-10],[35,10],[-35,10],[-35,-10]]
]);

// Create a Feature from the Geometry.
varpolyFeature=ee.Feature(polygon,{foo:42,bar:'tart'});
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Create an ee.Geometry.
polygon = ee.Geometry.Polygon(
    [[[-35, -10], [35, -10], [35, 10], [-35, 10], [-35, -10]]]
)

# Create a Feature from the Geometry.
poly_feature = ee.Feature(polygon, {'foo': 42, 'bar': 'tart'})
```

As with a `Geometry`, a `Feature` may be printed or added to the map for inspection and visualization:
### Code Editor (JavaScript)
```
print(polyFeature);
Map.addLayer(polyFeature,{},'feature');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
display(poly_feature)
m = geemap.Map()
m.add_layer(poly_feature, {}, 'feature')
display(m)
```

A `Feature` need not have a `Geometry` and may simply wrap a dictionary of properties. For example:
### Code Editor (JavaScript)
```
// Create a dictionary of properties, some of which may be computed values.
vardict={foo:ee.Number(8).add(88),bar:'nihao'};

// Create a null geometry feature with the dictionary of properties.
varnowhereFeature=ee.Feature(null,dict);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Create a dictionary of properties, some of which may be computed values.
dic = {'foo': ee.Number(8).add(88), 'bar': 'nihao'}

# Create a null geometry feature with the dictionary of properties.
nowhere_feature = ee.Feature(None, dic)
```

In this example, note that the dictionary supplied to the `Feature` contains a computed value. Creating features in this manner is useful for exporting long-running computations with a `Dictionary` result (e.g. `image.reduceRegion()`). See the [FeatureCollections](https://developers.google.com/earth-engine/guides/feature_collections) and [Importing Table Data](https://developers.google.com/earth-engine/guides/table_upload) or [Exporting](https://developers.google.com/earth-engine/guides/exporting) guides for details.
Each `Feature` has one primary `Geometry` stored in the `geometry` property. Additional geometries may be stored in other properties. `Geometry` methods such as intersection and buffer also exist on `Feature` as a convenience for getting the primary `Geometry`, applying the operation, and setting the result as the new primary `Geometry`. The result will retain all the other properties of the `Feature` on which the method is called. There are also methods for getting and setting the non-geometry properties of the `Feature`. For example:
### Code Editor (JavaScript)
```
// Make a feature and set some properties.
varfeature=ee.Feature(ee.Geometry.Point([-122.22599,37.17605]))
.set('genus','Sequoia').set('species','sempervirens');

// Get a property from the feature.
varspecies=feature.get('species');
print(species);

// Set a new property.
feature=feature.set('presence',1);

// Overwrite the old properties with a new dictionary.
varnewDict={genus:'Brachyramphus',species:'marmoratus'};
varfeature=feature.set(newDict);

// Check the result.
print(feature);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Make a feature and set some properties.
feature = (
    ee.Feature(ee.Geometry.Point([-122.22599, 37.17605]))
    .set('genus', 'Sequoia')
    .set('species', 'sempervirens')
)

# Get a property from the feature.
species = feature.get('species')
display(species)

# Set a new property.
feature = feature.set('presence', 1)

# Overwrite the old properties with a new dictionary.
new_dic = {'genus': 'Brachyramphus', 'species': 'marmoratus'}
feature = feature.set(new_dic)

# Check the result.
display(feature)
```

In the previous example, note that properties can be set with either a key-value pair, or with a dictionary. Also note that `feature.set()` overwrites existing properties.
