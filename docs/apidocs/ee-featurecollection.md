 
#  ee.FeatureCollection
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection#examples)


FeatureCollections can be constructed from the following arguments: 
- A string: assumed to be the name of a collection.
- A single geometry.
- A single feature.
- A list of features.
- A GeoJSON FeatureCollection
- A computed object: reinterpreted as a collection.
Usage| Returns  
---|---  
`ee.FeatureCollection(args,  _column_)`| FeatureCollection  
Argument| Type| Details  
---|---|---  
`args`| ComputedObject|Feature|FeatureCollection|Geometry|List| The constructor arguments.  
`column`| String, optional| The name of the geometry column to use. Only useful when working with a named collection.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection#colab-python-sample) More
```
// FeatureCollection from a string (collection name). Note that this only works
// with client-side strings, it won't accept computed, server-side strings.
varcollectionName='WRI/GPPD/power_plants';
varcollectionNameFc=ee.FeatureCollection(collectionName);
print('FeatureCollection from a string',collectionNameFc.limit(5));
// FeatureCollection from a single geometry.
varsingleGeometry=ee.Geometry.Point(-62.54,-27.32);
varsingleGeometryFc=ee.FeatureCollection(singleGeometry);
print('FeatureCollection from a single geometry',singleGeometryFc);
// FeatureCollection from a single feature.
varsingleFeature=ee.Feature(ee.Geometry.Point(-62.54,-27.32),{key:'val'});
varsingleFeatureFc=ee.FeatureCollection(singleFeature);
print('FeatureCollection from a single feature',singleFeatureFc);
// FeatureCollection from a list of features.
varlistOfFeatures=[
ee.Feature(ee.Geometry.Point(-62.54,-27.32),{key:'val1'}),
ee.Feature(ee.Geometry.Point(-69.18,-10.64),{key:'val2'}),
ee.Feature(ee.Geometry.Point(-45.98,-18.09),{key:'val3'})
];
varlistOfFeaturesFc=ee.FeatureCollection(listOfFeatures);
print('FeatureCollection from a list of features',listOfFeaturesFc);
// FeatureCollection from GeoJSON.
vargeojson={
"type":"FeatureCollection",
"columns":{
"key":"String",
"system:index":"String"
},
"features":[
{
"type":"Feature",
"geometry":{
"type":"Point",
"coordinates":[
-62.54,
-27.32
]
},
"id":"0",
"properties":{
"key":"val1"
}
}
]
};
vargeojsonFc=ee.FeatureCollection(geojson);
print('FeatureCollection from GeoJSON',geojsonFc);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# FeatureCollection from a string (collection name). Note that this only works
# with client-side strings, it won't accept computed, server-side strings.
collection_name = 'WRI/GPPD/power_plants'
collection_name_fc = ee.FeatureCollection(collection_name)
print('FeatureCollection from a string:', collection_name_fc.limit(5).getInfo())
# FeatureCollection from a single geometry.
single_geometry = ee.Geometry.Point(-62.54, -27.32)
single_geometry_fc = ee.FeatureCollection(single_geometry)
print('FeatureCollection from a single geometry:', single_geometry_fc.getInfo())
# FeatureCollection from a single feature.
single_feature = ee.Feature(ee.Geometry.Point(-62.54, -27.32), {'key': 'val'})
single_feature_fc = ee.FeatureCollection(single_feature)
print('FeatureCollection from a single feature:', single_feature_fc.getInfo())
# FeatureCollection from a list of features.
list_of_features = [
  ee.Feature(ee.Geometry.Point(-62.54, -27.32), {'key': 'val1'}),
  ee.Feature(ee.Geometry.Point(-69.18, -10.64), {'key': 'val2'}),
  ee.Feature(ee.Geometry.Point(-45.98, -18.09), {'key': 'val3'})
]
list_of_features_fc = ee.FeatureCollection(list_of_features)
print('FeatureCollection from a list of features:',
   list_of_features_fc.getInfo())
# FeatureCollection from GeoJSON.
geojson = {
  'type': 'FeatureCollection',
  'columns': {
    'key': 'String',
    'system:index': 'String'
    },
  'features': [
    {
      'type': 'Feature',
      'geometry': {
        'type': 'Point',
        'coordinates': [
          -62.54,
          -27.32
          ]
        },
      'id': '0',
      'properties': {
        'key': 'val1'
        }
      }
    ]
  }
geojson_fc = ee.FeatureCollection(geojson)
print('FeatureCollection from GeoJSON:', geojson_fc.getInfo())
```

