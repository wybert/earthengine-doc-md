 
#  ee.data.makeDownloadUrl 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-data-makedownloadurl#examples)


Create a download URL from a docid and token. 
Returns the download URL.
Usage| Returns  
---|---  
`ee.data.makeDownloadUrl(id)`| String  
Argument| Type| Details  
---|---|---  
`id`| DownloadId| A download id and token.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-data-makedownloadurl#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-data-makedownloadurl#colab-python-sample) More
```
// A Sentinel-2 surface reflectance image.
varimg=ee.Image('COPERNICUS/S2_SR/20210109T185751_20210109T185931_T10SEG');
// A small region within the image.
varregion=ee.Geometry.BBox(-122.0859,37.0436,-122.0626,37.0586);
vardownloadId=ee.data.getDownloadId({
image:img,
name:'single_band',
bands:['B3','B8','B11'],
region:region
});
print('Single-band GeoTIFF files wrapped in a zip file',
ee.data.makeDownloadUrl(downloadId));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
"""Demonstrates the ee.data.makeDownloadUrl method."""
importio
importrequests
importee

ee.Authenticate()
ee.Initialize()
# A Sentinel-2 surface reflectance image.
img = ee.Image('COPERNICUS/S2_SR/20210109T185751_20210109T185931_T10SEG')
# A small region within the image.
region = ee.Geometry.BBox(-122.0859, 37.0436, -122.0626, 37.0586)
# Image chunk as a NumPy structured array.
importnumpy
download_id = ee.data.getDownloadId({
  'image': img,
  'bands': ['B3', 'B8', 'B11'],
  'region': region,
  'scale': 20,
  'format': 'NPY'
})
response = requests.get(ee.data.makeDownloadUrl(download_id))
data = numpy.load(io.BytesIO(response.content))
print(data)
print(data.dtype)
# Single-band GeoTIFF files wrapped in a zip file.
download_id = ee.data.getDownloadId({
  'image': img,
  'name': 'single_band',
  'bands': ['B3', 'B8', 'B11'],
  'region': region
})
response = requests.get(ee.data.makeDownloadUrl(download_id))
with open('single_band.zip', 'wb') as fd:
 fd.write(response.content)
```

Was this helpful?
