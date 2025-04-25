 
#  Feature and FeatureCollection Visualization 
Stay organized with collections  Save and categorize content based on your preferences. 
As with images, geometries and features, feature collections can be added to the map directly with `Map.addLayer()`. The default visualization will display the vectors with solid black lines and semi-opaque black fill. To render the vectors in color, specify the `color` parameter. The following displays the 'RESOLVE' ecoregions ([Dinerstein et al. 2017](https://academic.oup.com/bioscience/article/67/6/534/3102935)) as the default visualization and in red:
### Code Editor (JavaScript)
```
// Load a FeatureCollection from a table dataset: 'RESOLVE' ecoregions.
varecoregions=ee.FeatureCollection('RESOLVE/ECOREGIONS/2017');
// Display as default and with a custom color.
Map.addLayer(ecoregions,{},'default display');
Map.addLayer(ecoregions,{color:'FF0000'},'colored');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Load a FeatureCollection from a table dataset: 'RESOLVE' ecoregions.
ecoregions = ee.FeatureCollection('RESOLVE/ECOREGIONS/2017')
# Display as default and with a custom color.
m = geemap.Map()
m.set_center(-76.2486, 44.8988, 8)
m.add_layer(ecoregions, {}, 'default display')
m.add_layer(ecoregions, {'color': 'FF0000'}, 'colored')
m
```

For additional display options, use `featureCollection.draw()`. Specifically, parameters `pointRadius` and `strokeWidth` control the size of points and lines, respectively, in the rendered `FeatureCollection`:
### Code Editor (JavaScript)
```
Map.addLayer(ecoregions.draw({color:'006600',strokeWidth:5}),{},'drawn');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
m.add_layer(ecoregions.draw(color='006600', strokeWidth=5), {}, 'drawn')
```

The output of `draw()` is an image with red, green and blue bands set according to the specified `color` parameter.
For more control over how a `FeatureCollection` is displayed, use `image.paint()` with the `FeatureCollection` as an argument. Unlike `draw()`, which outputs a three-band, 8-bit display image, `image.paint()` outputs an image with the specified numeric value 'painted' into it. Alternatively, you can supply the name of a property in the `FeatureCollection` which contains the numbers to paint. The `width` parameter behaves the same way: it can be a constant or the name of a property with a number for the line width. For example:
### Code Editor (JavaScript)
```
// Create an empty image into which to paint the features, cast to byte.
varempty=ee.Image().byte();
// Paint all the polygon edges with the same number and width, display.
varoutline=empty.paint({
featureCollection:ecoregions,
color:1,
width:3
});
Map.addLayer(outline,{palette:'FF0000'},'edges');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Create an empty image into which to paint the features, cast to byte.
empty = ee.Image().byte()
# Paint all the polygon edges with the same number and width, display.
outline = empty.paint(featureCollection=ecoregions, color=1, width=3)
m.add_layer(outline, {'palette': 'FF0000'}, 'edges')
```

Note that the empty image into which you paint the features needs to be cast prior to painting. This is because a constant image behaves as a constant: it is clamped to the initialization value. To color the feature edges with values set from a property of the features, set the color parameter to the name of the property with numeric values:
### Code Editor (JavaScript)
```
// Paint the edges with different colors, display.
varoutlines=empty.paint({
featureCollection:ecoregions,
color:'BIOME_NUM',
width:4
});
varpalette=['FF0000','00FF00','0000FF'];
Map.addLayer(outlines,{palette:palette,max:14},'different color edges');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Paint the edges with different colors, display.
outlines = empty.paint(featureCollection=ecoregions, color='BIOME_NUM', width=4)
palette = ['FF0000', '00FF00', '0000FF']
m.add_layer(outlines, {'palette': palette, 'max': 14}, 'different color edges')
```

Both the color and width with which the boundaries are drawn can be set with properties. For example:
### Code Editor (JavaScript)
```
// Paint the edges with different colors and widths.
varoutlines=empty.paint({
featureCollection:ecoregions,
color:'BIOME_NUM',
width:'NNH'
});
Map.addLayer(outlines,{palette:palette,max:14},'different color, width edges');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Paint the edges with different colors and widths.
outlines = empty.paint(
  featureCollection=ecoregions, color='BIOME_NUM', width='NNH'
)
m.add_layer(
  outlines, {'palette': palette, 'max': 14}, 'different color, width edges'
)
```

If the `width` parameter is not provided, the interior of the features is painted:
### Code Editor (JavaScript)
```
// Paint the interior of the polygons with different colors.
varfills=empty.paint({
featureCollection:ecoregions,
color:'BIOME_NUM',
});
Map.addLayer(fills,{palette:palette,max:14},'colored fills');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Paint the interior of the polygons with different colors.
fills = empty.paint(featureCollection=ecoregions, color='BIOME_NUM')
m.add_layer(fills, {'palette': palette, 'max': 14}, 'colored fills')
```

To render both the interior and edges of the features, paint the empty image twice:
### Code Editor (JavaScript)
```
// Paint both the fill and the edges.
varfilledOutlines=empty.paint(ecoregions,'BIOME_NUM').paint(ecoregions,0,2);
Map.addLayer(filledOutlines,{palette:['000000'].concat(palette),max:14},'edges and fills');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Paint both the fill and the edges.
filled_outlines = empty.paint(ecoregions, 'BIOME_NUM').paint(ecoregions, 0, 2)
m.add_layer(
  filled_outlines,
  {'palette': ['000000'] + palette, 'max': 14},
  'edges and fills',
)
```

