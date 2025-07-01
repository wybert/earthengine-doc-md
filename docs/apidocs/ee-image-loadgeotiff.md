 
#  ee.Image.loadGeoTIFF
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-loadgeotiff#examples)


Loads a GeoTIFF as an Image. 
Usage| Returns  
---|---  
`ee.Image.loadGeoTIFF(uri)`| Image  
Argument| Type| Details  
---|---|---  
`uri`| String| The Cloud Storage URI of the GeoTIFF to load. The bucket metadata must be accessible (requires the `storage.buckets.get` permission which is provided by the role "Storage Legacy Bucket Reader" among others, see https://cloud.google.com/storage/docs/access-control/iam-roles) and the bucket must be located in the US multi-region, a dual-region including US-CENTRAL1, or the US-CENTRAL1 region.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image-loadgeotiff#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image-loadgeotiff#colab-python-sample) More
```
varuri='gs://gcp-public-data-landsat/LC08/01/001/002/'+
'LC08_L1GT_001002_20160817_20170322_01_T2/'+
'LC08_L1GT_001002_20160817_20170322_01_T2_B5.TIF';
varcloudImage=ee.Image.loadGeoTIFF(uri);
print(cloudImage);
Map.addLayer(cloudImage,{min:0,max:20000});
Map.centerObject(cloudImage,6);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
uri = (
  'gs://gcp-public-data-landsat/'
  + 'LC08/01/001/002/'
  + 'LC08_L1GT_001002_20160817_20170322_01_T2/'
  + 'LC08_L1GT_001002_20160817_20170322_01_T2_B5.TIF'
)
cloud_image = ee.Image.loadGeoTIFF(uri)
display(cloud_image)
m = geemap.Map()
m.add_layer(cloud_image, {'min': 0, 'max': 20000})
m.center_object(cloud_image, 6)
m
```

