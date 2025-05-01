 
#  ee.Image.getDownloadURL 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-getdownloadurl#examples)


Get a download URL for small chunks of image data in GeoTIFF or NumPy format. Maximum request size is 32 MB, maximum grid dimension is 10000. 
Use getThumbURL for RGB visualization formats PNG and JPG.
Returns returns a download URL, or undefined if a callback was specified.
Usage| Returns  
---|---  
`Image.getDownloadURL(params,  _callback_)`| Object|String  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The Image instance.  
`params`| Object| An object containing download options with the following possible values:  | ` name: ` a base name to use when constructing filenames. Only applicable when format is "ZIPPED_GEO_TIFF" (default) or filePerBand is true. Defaults to the image id (or "download" for computed images) when format is "ZIPPED_GEO_TIFF" or filePerBand is true, otherwise a random character string is generated. Band names are appended when filePerBand is true.  
---  
` bands: ` a description of the bands to download. Must be an array of band names or an array of dictionaries, each with the following keys (optional parameters apply only when filePerBand is true):
  * ` id: ` the name of the band, a string, required. 
  * ` crs: ` an optional CRS string defining the band projection.
  * ` crs_transform: ` an optional array of 6 numbers specifying an affine transform from the specified CRS, in row-major order: [xScale, xShearing, xTranslation, yShearing, yScale, yTranslation]
  * ` dimensions: ` an optional array of two integers defining the width and height to which the band is cropped.
  * ` scale: ` an optional number, specifying the scale in meters of the band; ignored if crs and crs_transform are specified.

  
` crs: ` a default CRS string to use for any bands that do not explicitly specify one.  
` crs_transform: ` a default affine transform to use for any bands that do not specify one, of the same format as the `crs_transform` of bands.  
` dimensions: ` default image cropping dimensions to use for any bands that do not specify them.  
` scale: ` a default scale to use for any bands that do not specify one; ignored if `crs` and `crs_transform` are specified.  
` region: ` a polygon specifying a region to download; ignored if `crs` and `crs_transform` is specified.  
` filePerBand: ` whether to produce a separate GeoTIFF per band (boolean). Defaults to true. If false, a single GeoTIFF is produced and all band-level transformations will be ignored.  
` format: ` the download format. One of: 
  * "ZIPPED_GEO_TIFF" (GeoTIFF file(s) wrapped in a zip file, default)
  * "GEO_TIFF" (GeoTIFF file)
  * "NPY" (NumPy binary format)

If "GEO_TIFF" or "NPY", filePerBand and all band-level transformations will be ignored. Loading a NumPy output results in a structured array.  
`callback`| Function, optional| An optional callback. If not supplied, the call is made synchronously.  
## Examples
### Code Editor (JavaScript)
```
// A Sentinel-2 surface reflectance image.
varimg=ee.Image('COPERNICUS/S2_SR/20210109T185751_20210109T185931_T10SEG');
// A small region within the image.
varregion=ee.Geometry.BBox(-122.0859,37.0436,-122.0626,37.0586);
print('Single-band GeoTIFF files wrapped in a zip file',
img.getDownloadURL({
name:'single_band',
bands:['B3','B8','B11'],
region:region
}));
print('Multi-band GeoTIFF file wrapped in a zip file',
img.getDownloadURL({
name:'multi_band',
bands:['B3','B8','B11'],
region:region,
scale:20,
filePerBand:false
}));
print('Band-specific transformations',
img.getDownloadURL({
name:'custom_single_band',
bands:[
{id:'B3',scale:10},
{id:'B8',scale:10},
{id:'B11',scale:20}
],
region:region
}));
print('Multi-band GeoTIFF file',
img.getDownloadURL({
bands:['B3','B8','B11'],
region:region,
scale:20,
format:'GEO_TIFF'
}));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
"""Demonstrates the ee.Image.getDownloadURL method."""
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
url = img.getDownloadUrl({
  'bands': ['B3', 'B8', 'B11'],
  'region': region,
  'scale': 20,
  'format': 'NPY'
})
response = requests.get(url)
data = numpy.load(io.BytesIO(response.content))
print(data)
print(data.dtype)
# Single-band GeoTIFF files wrapped in a zip file.
url = img.getDownloadUrl({
  'name': 'single_band',
  'bands': ['B3', 'B8', 'B11'],
  'region': region
})
response = requests.get(url)
with open('single_band.zip', 'wb') as fd:
 fd.write(response.content)
# Multi-band GeoTIFF file wrapped in a zip file.
url = img.getDownloadUrl({
  'name': 'multi_band',
  'bands': ['B3', 'B8', 'B11'],
  'region': region,
  'scale': 20,
  'filePerBand': False
})
response = requests.get(url)
with open('multi_band.zip', 'wb') as fd:
 fd.write(response.content)
# Band-specific transformations.
url = img.getDownloadUrl({
  'name': 'custom_single_band',
  'bands': [
    {'id': 'B3', 'scale': 10},
    {'id': 'B8', 'scale': 10},
    {'id': 'B11', 'scale': 20}
  ],
  'region': region
})
response = requests.get(url)
with open('custom_single_band.zip', 'wb') as fd:
 fd.write(response.content)
# Multi-band GeoTIFF file.
url = img.getDownloadUrl({
  'bands': ['B3', 'B8', 'B11'],
  'region': region,
  'scale': 20,
  'format': 'GEO_TIFF'
})
response = requests.get(url)
with open('multi_band.tif', 'wb') as fd:
 fd.write(response.content)
```

