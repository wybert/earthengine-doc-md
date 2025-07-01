 
#  ee.FeatureCollection.merge
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-merge#examples)


Merges two collections into one. The result has all the elements that were in either collection. 
Elements from the first collection will have IDs prefixed with "1 _" and elements from the second collection will have IDs prefixed with "2_ ".
**Note:** If many collections need to be merged, consider placing them all in a collection and using FeatureCollection.flatten() instead. Repeated use of FeatureCollection.merge() will result in increasingly long element IDs and reduced performance.
Usage| Returns  
---|---  
`FeatureCollection.merge(collection2)`| FeatureCollection  
Argument| Type| Details  
---|---|---  
this: `collection1`| FeatureCollection| The first collection to merge.  
`collection2`| FeatureCollection| The second collection to merge.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-merge#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-merge#colab-python-sample) More
```
// FeatureCollection of points representing forest cover.
varfcForest=ee.FeatureCollection([
ee.Feature(ee.Geometry.Point([-122.248,37.238]),
{'id':0,'cover_class':'forest'}),
ee.Feature(ee.Geometry.Point([-122.204,37.222]),
{'id':1,'cover_class':'forest'}),
ee.Feature(ee.Geometry.Point([-122.110,37.199]),
{'id':2,'cover_class':'forest'})
]);
// FeatureCollection of points representing urban cover.
varfcUrban=ee.FeatureCollection([
ee.Feature(ee.Geometry.Point([-121.953,37.372]),
{'id':0,'cover_class':'urban'}),
ee.Feature(ee.Geometry.Point([-121.861,37.308]),
{'id':1,'cover_class':'urban'}),
ee.Feature(ee.Geometry.Point([-121.984,37.372]),
{'id':2,'cover_class':'urban'})
]);
// Merge the two FeatureCollections into one.
varfcMerged=fcForest.merge(fcUrban);
// Display FeatureCollections on the map.
Map.setCenter(-122.034,37.296,11);
Map.addLayer(fcForest,{color:'green'},'Forest points');
Map.addLayer(fcUrban,{color:'grey'},'Urban points');
Map.addLayer(fcMerged,{color:'yellow'},'Protected areas merged');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# FeatureCollection of points representing forest cover.
fc_forest = ee.FeatureCollection([
  ee.Feature(
    ee.Geometry.Point([-122.248, 37.238]),
    {
      'id': 0,
      'cover_class': 'forest',
      'id': 0,
      'cover_class': 'forest',
    },
  ),
  ee.Feature(
    ee.Geometry.Point([-122.204, 37.222]),
    {
      'id': 1,
      'cover_class': 'forest',
      'id': 1,
      'cover_class': 'forest',
    },
  ),
  ee.Feature(
    ee.Geometry.Point([-122.110, 37.199]),
    {
      'id': 2,
      'cover_class': 'forest',
      'id': 2,
      'cover_class': 'forest',
    },
  ),
])
# FeatureCollection of points representing urban cover.
fc_urban = ee.FeatureCollection([
  ee.Feature(
    ee.Geometry.Point([-121.953, 37.372]),
    {'id': 0, 'cover_class': 'urban', 'id': 0, 'cover_class': 'urban'},
  ),
  ee.Feature(
    ee.Geometry.Point([-121.861, 37.308]),
    {'id': 1, 'cover_class': 'urban', 'id': 1, 'cover_class': 'urban'},
  ),
  ee.Feature(
    ee.Geometry.Point([-121.984, 37.372]),
    {'id': 2, 'cover_class': 'urban', 'id': 2, 'cover_class': 'urban'},
  ),
])
# Merge the two FeatureCollections into one.
fc_merged = fc_forest.merge(fc_urban)
# Display FeatureCollections on the map.
m = geemap.Map()
m.set_center(-122.034, 37.296, 11)
m.add_layer(fc_forest, {'color': 'green'}, 'Forest points')
m.add_layer(fc_urban, {'color': 'grey'}, 'Urban points')
m.add_layer(fc_merged, {'color': 'yellow'}, 'Protected areas merged')
m
```

Was this helpful?
