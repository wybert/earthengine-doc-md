 
#  ee.FeatureCollection.getDownloadURL
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-getdownloadurl#examples)


Returns a download URL or undefined if a callback was specified.
Usage | Returns  
---|---  
`FeatureCollection.getDownloadURL(_format_, _selectors_, _filename_, _callback_)`|  Object|String  
Argument | Type | Details  
---|---|---  
this: `featurecollection` | FeatureCollection | The FeatureCollection instance.  
`format` | String, optional | The format of download, one of: "csv", "json", "geojson", "kml", "kmz" ("json" outputs GeoJSON). If unspecified, defaults to "csv".  
`selectors` | List<String>|String, optional | Feature property names used to select the attributes to be downloaded. If unspecified, all properties are included.  
`filename` | String, optional | Name of the file to be downloaded; extension is appended by default. If unspecified, defaults to "table".  
`callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-getdownloadurl#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-getdownloadurl#colab-python-sample) More
```
// FeatureCollection of power plants in Belgium.
varfc=ee.FeatureCollection('WRI/GPPD/power_plants')
.filter('country_lg == "Belgium"');

// Get a download URL for the FeatureCollection.
vardownloadUrl=fc.getDownloadURL({
format:'CSV',
selectors:['capacitymw','fuel1'],
filename:'belgian_power_plants'
});
print('URL for downloading FeatureCollection as CSV',downloadUrl);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# FeatureCollection of power plants in Belgium.
fc = ee.FeatureCollection('WRI/GPPD/power_plants').filter(
    'country_lg == "Belgium"')

# Get a download URL for the FeatureCollection.
download_url = fc.getDownloadURL(**{
  'filetype': 'CSV',
  'selectors': ['capacitymw', 'fuel1'],
  'filename': 'belgian_power_plants',
})
print('URL for downloading FeatureCollection as CSV:', download_url)
```

