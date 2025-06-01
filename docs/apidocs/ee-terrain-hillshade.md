 
#  ee.Terrain.hillshade 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-terrain-hillshade#examples)


Computes a simple hillshade from a DEM. 
Usage| Returns  
---|---  
`ee.Terrain.hillshade(input,  _azimuth_, _elevation_)`| Image  
Argument| Type| Details  
---|---|---  
`input`| Image| An elevation image, in meters.  
`azimuth`| Float, default: 270| The illumination azimuth in degrees from north.  
`elevation`| Float, default: 45| The illumination elevation in degrees.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-terrain-hillshade#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-terrain-hillshade#colab-python-sample) More
```
varelevation=ee.Image('NOAA/NGDC/ETOPO1').select('bedrock');
varexaggeration=20;
varhillshade=ee.Terrain.hillshade(elevation.multiply(exaggeration));
Map.addLayer(hillshade,null,'ETOPO1 Hillshade');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
elevation = ee.Image('NOAA/NGDC/ETOPO1').select('bedrock')
exaggeration = 20
hillshade = ee.Terrain.hillshade(elevation.multiply(exaggeration))
m = geemap.Map()
m.add_layer(hillshade, None, 'ETOPO1 Hillshade')
m
```

