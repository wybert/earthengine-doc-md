 
#  ImageCollection Overview
Stay organized with collections  Save and categorize content based on your preferences. 
An `ImageCollection` is a stack or sequence of images.
## Construct from a collection ID
An `ImageCollection` can be loaded by pasting an Earth Engine asset ID into the `ImageCollection` constructor. You can find `ImageCollection` IDs in the [data catalog](https://developers.google.com/earth-engine/datasets). For example, to load the [Sentinel-2 surface reflectance collection](https://developers.google.com/earth-engine/guides/datasets/catalog/COPERNICUS_S2_SR):
### Code Editor (JavaScript)
```
varsentinelCollection=ee.ImageCollection('COPERNICUS/S2_SR');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
sentinel_collection = ee.ImageCollection('COPERNICUS/S2_SR')
```

This collection contains every Sentinel-2 image in the public catalog. There are a lot. Usually you want to filter the collection as shown [here](https://developers.google.com/earth-engine/guides/ic_info) or [here](https://developers.google.com/earth-engine/guides/ic_filtering).
## Construct from an image list
The constructor `ee.ImageCollection()` or the convenience method `ee.ImageCollection.fromImages()` create image collections from lists of images. You can also create new image collections by merging existing collections. For example:
### Code Editor (JavaScript)
```
// Create arbitrary constant images.
varconstant1=ee.Image(1);
varconstant2=ee.Image(2);

// Create a collection by giving a list to the constructor.
varcollectionFromConstructor=ee.ImageCollection([constant1,constant2]);
print('collectionFromConstructor: ',collectionFromConstructor);

// Create a collection with fromImages().
varcollectionFromImages=ee.ImageCollection.fromImages(
[ee.Image(3),ee.Image(4)]);
print('collectionFromImages: ',collectionFromImages);

// Merge two collections.
varmergedCollection=collectionFromConstructor.merge(collectionFromImages);
print('mergedCollection: ',mergedCollection);

// Create a toy FeatureCollection
varfeatures=ee.FeatureCollection(
[ee.Feature(null,{foo:1}),ee.Feature(null,{foo:2})]);

// Create an ImageCollection from the FeatureCollection
// by mapping a function over the FeatureCollection.
varimages=features.map(function(feature){
returnee.Image(ee.Number(feature.get('foo')));
});

// Print the resultant collection.
print('Image collection: ',images);
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Create arbitrary constant images.
constant_1 = ee.Image(1)
constant_2 = ee.Image(2)

# Create a collection by giving a list to the constructor.
collection_from_constructor = ee.ImageCollection([constant_1, constant_2])
display('Collection from constructor:', collection_from_constructor)

# Create a collection with fromImages().
collection_from_images = ee.ImageCollection.fromImages(
    [ee.Image(3), ee.Image(4)]
)
display('Collection from images:', collection_from_images)

# Merge two collections.
merged_collection = collection_from_constructor.merge(collection_from_images)
display('Merged collection:', merged_collection)

# Create a toy FeatureCollection
features = ee.FeatureCollection(
    [ee.Feature(None, {'foo': 1}), ee.Feature(None, {'foo': 2})]
)

# Create an ImageCollection from the FeatureCollection
# by mapping a function over the FeatureCollection.
images = features.map(lambda feature: ee.Image(ee.Number(feature.get('foo'))))

# Display the resultant collection.
display('Image collection:', images)
```

Note that in this example an `ImageCollection` is created by mapping a function that returns an `Image` over a `FeatureCollection`. Learn more about mapping in the [Mapping over an ImageCollection section](https://developers.google.com/earth-engine/guides/ic_mapping). Learn more about feature collections from the [FeatureCollection section](https://developers.google.com/earth-engine/guides/feature_collections).
## Construct from a COG list
Create an `ImageCollection` from GeoTiffs in Cloud Storage. For example:
### Code Editor (JavaScript)
```
// All the GeoTiffs are in this folder.
varuriBase='gs://gcp-public-data-landsat/LC08/01/001/002/'+
'LC08_L1GT_001002_20160817_20170322_01_T2/';

// List of URIs, one for each band.
varuris=ee.List([
uriBase+'LC08_L1GT_001002_20160817_20170322_01_T2_B2.TIF',
uriBase+'LC08_L1GT_001002_20160817_20170322_01_T2_B3.TIF',
uriBase+'LC08_L1GT_001002_20160817_20170322_01_T2_B4.TIF',
uriBase+'LC08_L1GT_001002_20160817_20170322_01_T2_B5.TIF',
]);

// Make a collection from the list of images.
varimages=uris.map(ee.Image.loadGeoTIFF);
varcollection=ee.ImageCollection(images);

// Get an RGB image from the collection of bands.
varrgb=collection.toBands().rename(['B2','B3','B4','B5']);
Map.centerObject(rgb);
Map.addLayer(rgb,{bands:['B4','B3','B2'],min:0,max:20000},'rgb');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# All the GeoTiffs are in this folder.
uri_base = (
    'gs://gcp-public-data-landsat/LC08/01/001/002/'
    + 'LC08_L1GT_001002_20160817_20170322_01_T2/'
)

# List of URIs, one for each band.
uris = ee.List([
    uri_base + 'LC08_L1GT_001002_20160817_20170322_01_T2_B2.TIF',
    uri_base + 'LC08_L1GT_001002_20160817_20170322_01_T2_B3.TIF',
    uri_base + 'LC08_L1GT_001002_20160817_20170322_01_T2_B4.TIF',
    uri_base + 'LC08_L1GT_001002_20160817_20170322_01_T2_B5.TIF',
])

# Make a collection from the list of images.
images = uris.map(lambda uri: ee.Image.loadGeoTIFF(uri))
collection = ee.ImageCollection(images)

# Get an RGB image from the collection of bands.
rgb = collection.toBands().rename(['B2', 'B3', 'B4', 'B5'])
m = geemap.Map()
m.center_object(rgb)
m.add_layer(rgb, {'bands': ['B4', 'B3', 'B2'], 'min': 0, 'max': 20000}, 'rgb')
m
```

[Learn more about loading images from Cloud GeoTiffs](https://developers.google.com/earth-engine/guides/image_overview#images-from-cloud-geotiffs).
## Construct from a Zarr v2 array
Create an `ImageCollection` from a Zarr v2 array in Cloud Storage by taking image slices along a higher dimension. For example:
### Code Editor (JavaScript)
```
vartimeStart=1000000;
vartimeEnd=1000048;
varzarrV2ArrayImages=ee.ImageCollection.loadZarrV2Array({
uri:
'gs://gcp-public-data-arco-era5/ar/full_37-1h-0p25deg-chunk-1.zarr-v3/evaporation/.zarray',
proj:'EPSG:4326',
axis:0,
starts:[timeStart],
ends:[timeEnd]
});

print(zarrV2ArrayImages);

Map.addLayer(zarrV2ArrayImages,{min:-0.0001,max:0.00005},'Evaporation');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
time_start = 1000000
time_end = 1000048
zarr_v2_array_images = ee.ImageCollection.loadZarrV2Array(
    uri='gs://gcp-public-data-arco-era5/ar/full_37-1h-0p25deg-chunk-1.zarr-v3/evaporation/.zarray',
    proj='EPSG:4326',
    axis=0,
    starts=[time_start],
    ends=[time_end],
)

display(zarr_v2_array_images)

m = geemap.Map()
m.add_layer(
    zarr_v2_array_images, {'min': -0.0001, 'max': 0.00005}, 'Evaporation'
)
m
```

