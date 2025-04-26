 
#  ee.Blob.string 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-blob-string#examples)


Returns the contents of the blob as a String. 
Usage| Returns  
---|---  
`Blob.string( _encoding_)`| String  
Argument| Type| Details  
---|---|---  
this: `blob`| Blob|   
`encoding`| String, default: null| The character set encoding to use when decoding the blob. Options include, but are not limited to, 'US-ASCII', 'UTF-8', and 'UTF-16'.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-blob-string#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-blob-string#colab-python-sample) More
```
// Parse a SpatioTemporal Asset Catalog (STAC) entry from Google Cloud
// Storage (GCS). This is a non-traditional use of ee.Blob.
varurl='gs://ee-docs-demos/vector/geojson/point.json';
varblob=ee.Blob(url);
varentry=ee.Dictionary(blob.string().decodeJSON());
print(entry);// Point (1.00, 2.00)...
print(entry.get('a_field'));// "a demo field"
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Parse a SpatioTemporal Asset Catalog (STAC) entry from Google Cloud
# Storage (GCS). This is a non-traditional use of ee.Blob.
url = 'gs://ee-docs-demos/vector/geojson/point.json'
blob = ee.Blob(url)
entry = ee.Dictionary(blob.string().decodeJSON())
print(entry.getInfo()) # Point (1.00, 2.00)...
print(entry.get('a_field').getInfo()) # "a demo field"
```

Was this helpful?
