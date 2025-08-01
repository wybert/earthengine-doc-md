 
#  ee.FeatureCollection.draw
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-draw#examples)


Paints a vector collection for visualization. Not intended for use as input to other algorithms.
Usage | Returns  
---|---  
`FeatureCollection.draw(color, _pointRadius_, _strokeWidth_)`|  Image  
Argument | Type | Details  
---|---|---  
this: `collection` | FeatureCollection | The collection to draw.  
`color` | String | A hex string in the format RRGGBB specifying the color to use for drawing the features.  
`pointRadius` | Integer, default: 3 | The radius in pixels of the point markers.  
`strokeWidth` | Integer, default: 2 | The width in pixels of lines and polygon borders.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-draw#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-draw#colab-python-sample) More
```
// FeatureCollection of power plants in Belgium.
varfc=ee.FeatureCollection('WRI/GPPD/power_plants')
.filter('country_lg == "Belgium"');

// Paint FeatureCollection to an image for visualization.
varfcVis=fc.draw({color:'800080',pointRadius:5,strokeWidth:3});
Map.setCenter(4.56,50.78,8);
Map.addLayer(fcVis);
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
    'country_lg == "Belgium"'
)

# Paint FeatureCollection to an image for visualization.
fc_vis = fc.draw(color='800080', pointRadius=5, strokeWidth=3)
m = geemap.Map()
m.set_center(4.56, 50.78, 8)
m.add_layer(fc_vis)
m
```

