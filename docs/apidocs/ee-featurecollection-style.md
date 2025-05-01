 
#  ee.FeatureCollection.style 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Draw a vector collection for visualization using a simple style language. 
Usage| Returns  
---|---  
`FeatureCollection.style( _color_, _pointSize_, _pointShape_, _width_, _fillColor_, _styleProperty_, _neighborhood_, _lineType_)`| Image  
Argument| Type| Details  
---|---|---  
this: `collection`| FeatureCollection| The collection to draw.  
`color`| String, default: "black"| A default color (CSS 3.0 color value e.g., 'FF0000' or 'red') to use for drawing the features. Supports opacity (e.g., 'FF000088' for 50% transparent red).  
`pointSize`| Integer, default: 3| The default size in pixels of the point markers.  
`pointShape`| String, default: "circle"| The default shape of the marker to draw at each point location. One of: `circle`, `square`, `diamond`, `cross`, `plus`, `pentagram`, `hexagram`, `triangle`, `triangle_up`, `triangle_down`, `triangle_left`, `triangle_right`, `pentagon`, `hexagon`, `star5`, `star6`. This argument also supports these Matlab marker abbreviations: `o`, `s`, `d`, `x`, `+`, `p`, `h`, `^`, `v`, `<`, `>`.  
`width`| Float, default: 2| The default line width for lines and outlines for polygons and point shapes.  
`fillColor`| String, default: null| The color for filling polygons and point shapes. Defaults to 'color' at 0.66 opacity.  
`styleProperty`| String, default: null| A per-feature property expected to contain a dictionary. Values in the dictionary override any default values for that feature.  
`neighborhood`| Integer, default: 5| If styleProperty is used and any feature has a pointSize or width larger than the defaults, tiling artifacts can occur. Specifies the maximum neighborhood (pointSize + width) needed for any feature.  
`lineType`| String, default: "solid"| The default line style for lines and outlines of polygons and point shapes. Defaults to 'solid'. One of: solid, dotted, dashed.  
## Examples
### Code Editor (JavaScript)
```
// FeatureCollection of power plants in Belgium.
varfc=ee.FeatureCollection('WRI/GPPD/power_plants')
.filter('country_lg == "Belgium"');
// Paint FeatureCollection to an image using collection-wide style arguments.
varfcVis=fc.style({
color:'1e90ff',
width:2,
fillColor:'ff475788',// with alpha set for partial transparency
lineType:'dotted',
pointSize:10,
pointShape:'circle'
});
// Display the FeatureCollection visualization (ee.Image) on the map.
Map.setCenter(4.326,50.919,9);
Map.addLayer(fcVis,null,'Collection-wide style');
// Paint FeatureCollection to an image using feature-specific style arguments.
// A dictionary of style properties per power plant fuel type.
varfuelStyles=ee.Dictionary({
Wind:{color:'blue',pointSize:5,pointShape:'circle'},
Gas:{color:'yellow',pointSize:6,pointShape:'square'},
Oil:{color:'green',pointSize:3,pointShape:'diamond'},
Coal:{color:'red',pointSize:3,pointShape:'cross'},
Hydro:{color:'brown',pointSize:3,pointShape:'star5'},
Biomass:{color:'orange',pointSize:4,pointShape:'triangle'},
Nuclear:{color:'purple',pointSize:6,pointShape:'hexagram'},
});
// Add feature-specific style properties to each feature based on fuel type.
fc=fc.map(function(feature){
returnfeature.set('style',fuelStyles.get(feature.get('fuel1')));
});
// Style the FeatureCollection according to each feature's "style" property.
varfcVisCustom=fc.style({
styleProperty:'style',
neighborhood:8// maximum "pointSize" + "width" among features
});
// Display the FeatureCollection visualization (ee.Image) on the map.
Map.addLayer(fcVisCustom,null,'Feature-specific style');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# FeatureCollection of power plants in Belgium.
fc = ee.FeatureCollection('WRI/GPPD/power_plants').filter(
  'country_lg == "Belgium"'
)
# Paint FeatureCollection to an image using collection-wide style arguments.
fc_vis = fc.style(
  color='1e90ff',
  width=2,
  fillColor='ff475788', # with alpha set for partial transparency
  lineType='dotted',
  pointSize=10,
  pointShape='circle',
)
# Display the FeatureCollection visualization (ee.Image) on the map.
m = geemap.Map()
m.set_center(4.326, 50.919, 9)
m.add_layer(fc_vis, None, 'Collection-wide style')
# Paint FeatureCollection to an image using feature-specific style arguments.
# A dictionary of style properties per power plant fuel type.
fuel_styles = ee.Dictionary({
  'Wind': {'color': 'blue', 'pointSize': 5, 'pointShape': 'circle'},
  'Gas': {'color': 'yellow', 'pointSize': 6, 'pointShape': 'square'},
  'Oil': {'color': 'green', 'pointSize': 3, 'pointShape': 'diamond'},
  'Coal': {'color': 'red', 'pointSize': 3, 'pointShape': 'cross'},
  'Hydro': {'color': 'brown', 'pointSize': 3, 'pointShape': 'star5'},
  'Biomass': {'color': 'orange', 'pointSize': 4, 'pointShape': 'triangle'},
  'Nuclear': {'color': 'purple', 'pointSize': 6, 'pointShape': 'hexagram'},
})
# Add feature-specific style properties to each feature based on fuel type.
fc = fc.map(
  lambda feature: feature.set('style', fuel_styles.get(feature.get('fuel1')))
)
# Style the FeatureCollection according to each feature's "style" property.
fc_vis_custom = fc.style(
  styleProperty='style',
  neighborhood=8, # maximum "pointSize" + "width" among features
)
# Display the FeatureCollection visualization (ee.Image) on the map.
m.add_layer(fc_vis_custom, None, 'Feature-specific style')
m
```

