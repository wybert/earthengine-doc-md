 
#  ee.FeatureCollection.copyProperties
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-copyproperties#examples)


Copies metadata properties from one element to another. 
Usage| Returns  
---|---  
`FeatureCollection.copyProperties( _source_, _properties_, _exclude_)`| Element  
Argument| Type| Details  
---|---|---  
this: `destination`| Element, default: null| The object whose properties to override.  
`source`| Element, default: null| The object from which to copy the properties.  
`properties`| List, default: null| The properties to copy. If omitted, all ordinary (i.e. non-system) properties are copied.  
`exclude`| List, default: null| The list of properties to exclude when copying all properties. Must not be specified if properties is.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-copyproperties#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-copyproperties#colab-python-sample) More
```
// Import a Landsat 8 surface reflectance image to sample.
varimage=ee.Image('LANDSAT/LC08/C02/T1_L2/LC08_038032_20170722')
// Select the optical bands.
.select(['SR_B.']);
// Get the image geometry to define the geographical bounds of the sample.
varimageBounds=image.geometry();
// Sample the image at a set of random points; a feature collection is returned.
varpointSampleFc=image.sample(
{region:imageBounds,scale:30,numPixels:5,geometries:true});
// Copy image properties to the FeatureCollection; three options follow.
print('All non-system image properties copied to the FeatureCollection',
pointSampleFc.copyProperties(image));
print('Selected image properties copied to the FeatureCollection',
pointSampleFc.copyProperties({
source:image,
properties:['system:time_start','SPACECRAFT_ID']
}));
print('All but selected image properties copied to the FeatureCollection',
pointSampleFc.copyProperties({
source:image,
exclude:['TIRS_SSM_MODEL','TIRS_SSM_POSITION_STATUS']
}));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Import a Landsat 8 surface reflectance image to sample.
image = ee.Image('LANDSAT/LC08/C02/T1_L2/LC08_038032_20170722').select(
  # Select the optical bands.
  ['SR_B.'])
# Get the image geometry to define the geographical bounds of the sample.
image_bounds = image.geometry()
# Sample the image at a set of random points; a feature collection is returned.
point_sample_fc = image.sample(
  **{'region': image_bounds, 'scale': 30, 'numPixels': 5, 'geometries': True})
# Copy image properties to the FeatureCollection; three options follow.
print('All non-system image properties copied to the FeatureCollection:',
   point_sample_fc.copyProperties(image).getInfo())
print('Selected image properties copied to the FeatureCollection:',
   point_sample_fc.copyProperties(**{
     'source': image,
     'properties': ['system:time_start', 'SPACECRAFT_ID']
     }).getInfo())
print('All but selected image properties copied to the FeatureCollection:',
   point_sample_fc.copyProperties(**{
     'source': image,
     'exclude': ['TIRS_SSM_MODEL', 'TIRS_SSM_POSITION_STATUS']
   }).getInfo())
```

