 
#  ee.Image.pixelLonLat
Stay organized with collections  Save and categorize content based on your preferences. 
Creates an image with two bands named 'longitude' and 'latitude', containing the longitude and latitude at each pixel, in degrees. Usage| Returns  
---|---  
`ee.Image.pixelLonLat()`| Image  
**No arguments.**
## Examples
### Code Editor (JavaScript)
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

### Colab (Python)
```
# https://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system
longitude = ee.Image.pixelLonLat().select('longitude')
utm_zones = longitude.add(180).divide(6).int()
m = geemap.Map()
m.add_layer(utm_zones, {'min': 0, 'max': 60}, 'UTM zones')
m
```

