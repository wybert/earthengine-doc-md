 
#  Image Information and Metadata
Stay organized with collections  Save and categorize content based on your preferences. 
[ ![Colab logo](https://developers.google.com/static/earth-engine/images/colab_logo_32px.png) Run in Google Colab ](https://colab.research.google.com/github/google/earthengine-community/blob/master/guides/linked/generated/image_info.ipynb) |  [ ![GitHub logo](https://developers.google.com/static/earth-engine/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/earthengine-community/blob/master/guides/linked/generated/image_info.ipynb)  
---|---  
Print image objects to explore band names, projection information, properties, and other metadata. The following examples demonstrate printing the entire set of image metadata as well as requesting specific metadata elements programmatically.
## Getting metadata
### Code Editor (JavaScript)
```
// Load an image.
varimage=ee.Image('LANDSAT/LC08/C02/T1/LC08_044034_20140318');
// Display all metadata.
print('All metadata:',image);
// Get information about the bands as a list.
varbandNames=image.bandNames();
print('Band names:',bandNames);// ee.List of band names
// Get projection information from band 1.
varb1proj=image.select('B1').projection();
print('Band 1 projection:',b1proj);// ee.Projection object
// Get scale (in meters) information from band 1.
varb1scale=image.select('B1').projection().nominalScale();
print('Band 1 scale:',b1scale);// ee.Number
// Note that different bands can have different projections and scale.
varb8scale=image.select('B8').projection().nominalScale();
print('Band 8 scale:',b8scale);// ee.Number
// Get a list of all metadata properties.
varproperties=image.propertyNames();
print('Metadata properties:',properties);// ee.List of metadata properties
// Get a specific metadata property.
varcloudiness=image.get('CLOUD_COVER');
print('CLOUD_COVER:',cloudiness);// ee.Number
// Get version number (ingestion timestamp as microseconds since Unix epoch).
varversion=image.get('system:version');
print('Version:',version);// ee.Number
print('Version (as ingestion date):',
ee.Date(ee.Number(version).divide(1000)));// ee.Date
// Get the timestamp and convert it to a date.
vardate=ee.Date(image.get('system:time_start'));
print('Timestamp:',date);// ee.Date
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Load an image.
image = ee.Image('LANDSAT/LC08/C02/T1/LC08_044034_20140318')
# All metadata.
display('All metadata:', image)
# Get information about the bands as a list.
band_names = image.bandNames()
display('Band names:', band_names) # ee.List of band names
# Get projection information from band 1.
b1_proj = image.select('B1').projection()
display('Band 1 projection:', b1_proj) # ee.Projection object
# Get scale (in meters) information from band 1.
b1_scale = image.select('B1').projection().nominalScale()
display('Band 1 scale:', b1_scale) # ee.Number
# Note that different bands can have different projections and scale.
b8_scale = image.select('B8').projection().nominalScale()
display('Band 8 scale:', b8_scale) # ee.Number
# Get a list of all metadata properties.
properties = image.propertyNames()
display('Metadata properties:', properties) # ee.List of metadata properties
# Get a specific metadata property.
cloudiness = image.get('CLOUD_COVER')
display('CLOUD_COVER:', cloudiness) # ee.Number
# Get version number (ingestion timestamp as microseconds since Unix epoch).
version = image.get('system:version')
display('Version:', version) # ee.Number
display(
  'Version (as ingestion date):',
  ee.Date(ee.Number(version).divide(1000)).format(),
) # ee.Date
# Get the timestamp.
ee_date = ee.Date(image.get('system:time_start'))
display('Timestamp:', ee_date) # ee.Date
# Date objects transferred to the client are milliseconds since UNIX epoch;
# convert to human readable date with ee.Date.format().
display('Datetime:', ee_date.format()) # ISO standard date string
```

