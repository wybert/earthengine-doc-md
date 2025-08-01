 
#  ee.Image.pixelLonLat
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-pixellonlat#examples)


Creates an image with two bands named 'longitude' and 'latitude', containing the longitude and latitude at each pixel, in degrees.
Usage | Returns  
---|---  
`ee.Image.pixelLonLat()` | Image  
**No arguments.**
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image-pixellonlat#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image-pixellonlat#colab-python-sample) More
```
// https://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system
varlongitude=ee.Image.pixelLonLat().select('longitude');
varutmZones=longitude.add(180).divide(6).int();
Map.addLayer(utmZones,{min:0,max:60},'UTM zones');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# https://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system
longitude = ee.Image.pixelLonLat().select('longitude')
utm_zones = longitude.add(180).divide(6).int()
m = geemap.Map()
m.add_layer(utm_zones, {'min': 0, 'max': 60}, 'UTM zones')
m
```

Was this helpful?
