 
#  Export.table.toDrive
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Creates a batch task to export a FeatureCollection as a table to Drive. Tasks can be started from the Tasks tab. Usage| Returns  
---|---  
`Export.table.toDrive(collection,  _description_, _folder_, _fileNamePrefix_, _fileFormat_, _selectors_, _maxVertices_, _priority_)`|   
Argument|  Type| Details  
---|---|---  
`collection`| FeatureCollection| The feature collection to export.  
`description`| String, optional| A human-readable name of the task. May contain letters, numbers, -, _ (no spaces). Defaults to "myExportTableTask".  
`folder`| String, optional| The Google Drive Folder that the export will reside in. Note: (a) if the folder name exists at any level, the output is written to it, (b) if duplicate folder names exist, output is written to the most recently modified folder, (c) if the folder name does not exist, a new folder will be created at the root, and (d) folder names with separators (e.g. 'path/to/file') are interpreted as literal strings, not system paths. Defaults to Drive root.  
`fileNamePrefix`| String, optional| The filename prefix. May contain letters, numbers, -, _ (no spaces). Defaults to the description.  
`fileFormat`| String, optional| The output format: "CSV" (default), "GeoJSON", "KML", "KMZ", or "SHP", or "TFRecord".  
`selectors`| List, optional| A list of properties to include in the export; either a single string with comma-separated names or a list of strings.  
`maxVertices`| Number, optional| Max number of uncut vertices per geometry; geometries with more vertices will be cut into pieces smaller than this size.  
`priority`| Number, optional| The priority of the task within the project. Higher priority tasks are scheduled sooner. Must be an integer between 0 and 9999. Defaults to 100.  
## Examples
### Code Editor (JavaScript)
```
// A Sentinel-2 surface reflectance image.
varimg=ee.Image('COPERNICUS/S2_SR/20210109T185751_20210109T185931_T10SEG');
Map.setCenter(-122.359,37.428,9);
Map.addLayer(img,{bands:['B11','B8','B3'],min:100,max:3500},'img');
// Sample the image at 20 m scale, a point feature collection is returned.
varsamp=img.sample({scale:20,numPixels:50,geometries:true});
Map.addLayer(samp,{color:'white'},'samp');
print('Image sample feature collection',samp);
// Export the image sample feature collection to Drive as a CSV file.
Export.table.toDrive({
collection:samp,
description:'image_sample_demo_csv',
folder:'earth_engine_demos',
fileFormat:'CSV'
});
// Export a subset of collection properties: three bands and the geometry
// as GeoJSON.
Export.table.toDrive({
collection:samp,
description:'image_sample_demo_prop_subset',
folder:'earth_engine_demos',
fileFormat:'GeoJSON',
selectors:['B8','B11','B12','.geo']
});
// Export the image sample feature collection to Drive as a shapefile.
Export.table.toDrive({
collection:samp,
description:'image_sample_demo_shp',
folder:'earth_engine_demos',
fileFormat:'SHP'
});
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# A Sentinel-2 surface reflectance image.
img = ee.Image('COPERNICUS/S2_SR/20210109T185751_20210109T185931_T10SEG')
m = geemap.Map()
m.set_center(-122.359, 37.428, 9)
m.add_layer(
  img, {'bands': ['B11', 'B8', 'B3'], 'min': 100, 'max': 3500}, 'img'
)
# Sample the image at 20 m scale, a point feature collection is returned.
samp = img.sample(scale=20, numPixels=50, geometries=True)
m.add_layer(samp, {'color': 'white'}, 'samp')
display(m)
display('Image sample feature collection', samp)
# Export the image sample feature collection to Drive as a CSV file.
task = ee.batch.Export.table.toDrive(
  collection=samp,
  description='image_sample_demo_csv',
  folder='earth_engine_demos',
  fileFormat='CSV',
)
task.start()
# Export a subset of collection properties: three bands and the geometry
# as GeoJSON.
task = ee.batch.Export.table.toDrive(
  collection=samp,
  description='image_sample_demo_prop_subset',
  folder='earth_engine_demos',
  fileFormat='GeoJSON',
  selectors=['B8', 'B11', 'B12', '.geo'],
)
task.start()
# Export the image sample feature collection to Drive as a shapefile.
task = ee.batch.Export.table.toDrive(
  collection=samp,
  description='image_sample_demo_shp',
  folder='earth_engine_demos',
  fileFormat='SHP',
)
task.start()
```

