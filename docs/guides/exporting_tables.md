 
#  Exporting Table and Vector Data 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [to Drive](https://developers.google.com/earth-engine/guides/exporting_tables#to_drive)
  * [to Cloud Storage](https://developers.google.com/earth-engine/guides/exporting_tables#to_cloud_storage)
  * [to Asset](https://developers.google.com/earth-engine/guides/exporting_tables#to_asset)


You can export a `FeatureCollection` as CSV, SHP (shapefile), GeoJSON, KML, KMZ or TFRecord using `Export.table`. The `FeatureCollection` may represent vectors or simply a table of data. In the latter case, the features in the collection will have null geometry.
Note some additional constraints when working with some file formats, including:
  * **KML** : A `FeatureCollection` exported to a KML file will have all the geometries transformed to unprojected (WGS84) coordinates.
  * **SHP** : A `FeatureCollection` exported to a Shapefile must contain features with the same geometry type and projection and must fit within the [Shapefile size limits](https://support.esri.com/en/technical-article/000010813). Column names are truncated to 10 characters or fewer, and this must not create duplicate column names.
  * **TFRecord** : See [this page](https://developers.google.com/earth-engine/guides/tfrecord#exporting-tables).

**Note:** If you need control over the precision of geometries in your export, `map()` a function over the collection to be exported: `map(function(f) { return f.transform(targetProj, maxErr); })`
## to Drive
To export a `FeatureCollection` to your Drive account, use `Export.table.toDrive()`. For example:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/exporting_tables#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/exporting_tables#colab-python-sample) More
```
// Make a collection of points.
varfeatures=ee.FeatureCollection([
ee.Feature(ee.Geometry.Point(30.41,59.933),{name:'Voronoi'}),
ee.Feature(ee.Geometry.Point(-73.96,40.781),{name:'Thiessen'}),
ee.Feature(ee.Geometry.Point(6.4806,50.8012),{name:'Dirichlet'})
]);
// Export the FeatureCollection to a KML file.
Export.table.toDrive({
collection:features,
description:'vectorsToDriveExample',
fileFormat:'KML'
});
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Make a collection of points.
features = ee.FeatureCollection([
  ee.Feature(ee.Geometry.Point(30.41, 59.933), {'name': 'Voronoi'}),
  ee.Feature(ee.Geometry.Point(-73.96, 40.781), {'name': 'Thiessen'}),
  ee.Feature(ee.Geometry.Point(6.4806, 50.8012), {'name': 'Dirichlet'}),
])
# Export the FeatureCollection to a KML file.
task = ee.batch.Export.table.toDrive(
  collection=features, description='vectorsToDriveExample', fileFormat='KML'
)
task.start()
```

Note that the output format is specified as KML to handle geographic data (SHP would also be appropriate for exporting a table with geometry). To export just a table of data, without any geographic information, export features with null geometry in CSV format. The following demonstrates using `Export.table.toDrive()` to get the results of a potentially long running reduction:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/exporting_tables#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/exporting_tables#colab-python-sample) More
```
// Load a Landsat image.
varimage=ee.Image('LANDSAT/LC08/C02/T1_TOA/LC08_044034_20140318');
varprojection=image.select('B2').projection().getInfo();
// Create an arbitrary rectangle.
varregion=ee.Geometry.Rectangle(-122.2806,37.1209,-122.0554,37.2413);
// Get a dictionary of means in the region.
varmeans=image.reduceRegion({
reducer:ee.Reducer.mean(),
geometry:region,
crs:projection.crs,
crsTransform:projection.transform,
});
// Make a feature without geometry and set the properties to the dictionary of means.
varfeature=ee.Feature(null,means);
// Wrap the Feature in a FeatureCollection for export.
varfeatureCollection=ee.FeatureCollection([feature]);
// Export the FeatureCollection.
Export.table.toDrive({
collection:featureCollection,
description:'exportTableExample',
fileFormat:'CSV'
});
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Load a Landsat image.
image = ee.Image('LANDSAT/LC08/C02/T1_TOA/LC08_044034_20140318')
projection = image.select('B2').projection().getInfo()
# Create an arbitrary rectangle.
region = ee.Geometry.Rectangle(-122.2806, 37.1209, -122.0554, 37.2413)
# Get a dictionary of means in the region.
means = image.reduceRegion(
  reducer=ee.Reducer.mean(),
  geometry=region,
  crs=projection['crs'],
  crsTransform=projection['transform'],
)
# Make a feature without geometry and set the properties to the dictionary of means.
feature = ee.Feature(None, means)
# Wrap the Feature in a FeatureCollection for export.
feature_collection = ee.FeatureCollection([feature])
# Export the FeatureCollection.
task = ee.batch.Export.table.toDrive(
  collection=feature_collection,
  description='exportTableExample',
  fileFormat='CSV',
)
task.start()
```

Note that the format is set to 'CSV' in this example since there is no geometry in the output.
**Caution:** Depending on your Google Drive settings, CSV tables that you export from Earth Engine can be converted to XSLX files with unintended effects, such as data type conversions. The behavior can be modified with [Google Drive settings](https://developers.google.com/earth-engine/faq#tables_exported_to_drive_as_csv_format_are_converted_to_xslx_format).
## to Cloud Storage
To export a `FeatureCollection` to Cloud Storage, use `Export.table.toCloudStorage()`. For example, using the `features` defined previously:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/exporting_tables#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/exporting_tables#colab-python-sample) More
```
// Export a KML file to Cloud Storage.
Export.table.toCloudStorage({
collection:features,
description:'vectorsToCloudStorageExample',
bucket:'your-bucket-name',
fileNamePrefix:'exampleTableExport',
fileFormat:'KML'
});
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Export a KML file to Cloud Storage.
task = ee.batch.Export.table.toCloudStorage(
  collection=features,
  description='vectorsToCloudStorageExample',
  bucket='your-bucket-name',
  fileNamePrefix='exampleTableExport',
  fileFormat='KML',
)
task.start()
```

## to Asset
To export a `FeatureCollection` as an Earth Engine asset, use `Export.table.toAsset()`. For example, using the `features` defined previously:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/exporting_tables#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/exporting_tables#colab-python-sample) More
```
// Export an ee.FeatureCollection as an Earth Engine asset.
Export.table.toAsset({
collection:features,
description:'exportToTableAssetExample',
assetId:'exampleAssetId',
});
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Export an ee.FeatureCollection as an Earth Engine asset.
task = ee.batch.Export.table.toAsset(
  collection=features,
  description='exportToTableAssetExample',
  assetId='projects/your-project/assets/exampleAssetId',
)
task.start()
```

There are several limitations on the size and shape of Earth Engine table assets:
  * Maximum of 100 million features
  * Maximum of 1000 properties (columns)
  * Maximum of 100,000 vertices for each row's geometry
  * Maximum of 100,000 characters per string value


