 
#  Image Visualization
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [RGB composites](https://developers.google.com/earth-engine/guides/image_visualization#rgb-composites)
  * [Color palettes](https://developers.google.com/earth-engine/guides/image_visualization#color-palettes)
    * [Saving default color palettes](https://developers.google.com/earth-engine/guides/image_visualization#saving-default-color-palettes)
  * [Masking](https://developers.google.com/earth-engine/guides/image_visualization#masking)
  * [Visualization images](https://developers.google.com/earth-engine/guides/image_visualization#visualization-images)
  * [Mosaicking](https://developers.google.com/earth-engine/guides/image_visualization#mosaicking)
  * [Clipping](https://developers.google.com/earth-engine/guides/image_visualization#clipping)
  * [Rendering categorical maps](https://developers.google.com/earth-engine/guides/image_visualization#rendering-categorical-maps)
  * [Styled Layer Descriptors](https://developers.google.com/earth-engine/guides/image_visualization#styled-layer-descriptors)
  * [Thumbnail images](https://developers.google.com/earth-engine/guides/image_visualization#thumbnail-images)


[ ![Colab logo](https://developers.google.com/static/earth-engine/images/colab_logo_32px.png) Run in Google Colab ](https://colab.research.google.com/github/google/earthengine-community/blob/master/guides/linked/generated/image_visualization.ipynb) |  [ ![GitHub logo](https://developers.google.com/static/earth-engine/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/earthengine-community/blob/master/guides/linked/generated/image_visualization.ipynb)  
---|---  
There are a number of `ee.Image` methods that produce RGB visual representations of image data, for example: `visualize()`, `getThumbURL()`, `getMap()`, `getMapId()` (used in Colab Folium map display) and, `Map.addLayer()` (used in Code Editor map display, not available for Python). By default these methods assign the first three bands to red, green and blue, respectively. The default stretch is based on the type of data in the bands (e.g. floats are stretched in [0, 1], 16-bit data are stretched to the full range of possible values), which may or may not be suitable. To achieve desired visualization effects, you can provide visualization parameters:
Image visualization parameters Parameter | Description | Type  
---|---|---  
_bands_ | Comma-delimited list of three band names to be mapped to RGB | list  
_min_ | Value(s) to map to 0 | number or list of three numbers, one for each band  
_max_ | Value(s) to map to 255 | number or list of three numbers, one for each band  
_gain_ | Value(s) by which to multiply each pixel value | number or list of three numbers, one for each band  
_bias_ | Value(s) to add to each DN | number or list of three numbers, one for each band  
_gamma_ | Gamma correction factor(s) | number or list of three numbers, one for each band  
_palette_ | List of CSS-style color strings (single-band images only) | comma-separated list of hex strings  
_opacity_ | The opacity of the layer (0.0 is fully transparent and 1.0 is fully opaque) | number  
_format_ | Either "jpg" or "png" | string  
## RGB composites
The following illustrates the use of parameters to style a Landsat 8 image as a false-color composite:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/image_visualization#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/image_visualization#colab-python-sample) More
```
// Load an image.
varimage=ee.Image('LANDSAT/LC08/C02/T1_TOA/LC08_044034_20140318');
// Define the visualization parameters.
varvizParams={
bands:['B5','B4','B3'],
min:0,
max:0.5,
gamma:[0.95,1.1,1]
};
// Center the map and display the image.
Map.setCenter(-122.1899,37.5010,10);// San Francisco Bay
Map.addLayer(image,vizParams,'false color composite');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Load an image.
image = ee.Image('LANDSAT/LC08/C02/T1_TOA/LC08_044034_20140318')
# Define the visualization parameters.
image_viz_params = {
  'bands': ['B5', 'B4', 'B3'],
  'min': 0,
  'max': 0.5,
  'gamma': [0.95, 1.1, 1],
}
# Define a map centered on San Francisco Bay.
map_l8 = geemap.Map(center=[37.5010, -122.1899], zoom=10)
# Add the image layer to the map and display it.
map_l8.add_layer(image, image_viz_params, 'false color composite')
display(map_l8)
```

In this example, band `'B5'` is assigned to red, `'B4'` is assigned to green, and `'B3'` is assigned to blue.
![false_color_sf](https://developers.google.com/static/earth-engine/images/Images_false_color_sf.png) Landsat 8 false color composite of San Francisco bay area, California, USA. 
## Color palettes
To display a single band of an image in color, set the `palette` parameter with a color ramp represented by a list of CSS-style color strings. (See [this reference](http://en.wikipedia.org/wiki/Web_colors) for more information). The following example illustrates how to use colors from cyan (`'00FFFF'`) to blue (`'0000FF'`) to render a [ Normalized Difference Water Index (NDWI)](http://www.tandfonline.com/doi/abs/10.1080/01431169608948714) image:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/image_visualization#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/image_visualization#colab-python-sample) More
```
// Load an image.
varimage=ee.Image('LANDSAT/LC08/C02/T1_TOA/LC08_044034_20140318');
// Create an NDWI image, define visualization parameters and display.
varndwi=image.normalizedDifference(['B3','B5']);
varndwiViz={min:0.5,max:1,palette:['00FFFF','0000FF']};
Map.addLayer(ndwi,ndwiViz,'NDWI',false);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Load an image.
image = ee.Image('LANDSAT/LC08/C02/T1_TOA/LC08_044034_20140318')
# Create an NDWI image, define visualization parameters and display.
ndwi = image.normalizedDifference(['B3', 'B5'])
ndwi_viz = {'min': 0.5, 'max': 1, 'palette': ['00FFFF', '0000FF']}
# Define a map centered on San Francisco Bay.
map_ndwi = geemap.Map(center=[37.5010, -122.1899], zoom=10)
# Add the image layer to the map and display it.
map_ndwi.add_layer(ndwi, ndwi_viz, 'NDWI')
display(map_ndwi)
```

In this example, note that the `min` and `max` parameters indicate the range of pixel values to which the palette should be applied. Intermediate values are linearly stretched.
Also note that the `show` parameter is set to `false` in the Code Editor example. This results in the visibility of the layer being off when it is added to the map. It can always be turned on again using the [Layer Manager](https://developers.google.com/earth-engine/guides/playground#layer-manager) in the upper right corner of the Code Editor map.
![ndwi_sf](https://developers.google.com/static/earth-engine/images/Images_NDWI_sf.png) Landsat 8 NDWI, San Francisco bay area, USA. Cyan are low values, blue are high values. 
### Saving default color palettes
To save color palettes on a classification image so that there is no need to remember to apply them, you can set two specially-named string image properties for each classification band.
For example, if your image has a band named `'landcover'` with three values 0, 1, and 2 corresponding to classes 'water', 'forest', and 'other', you can set the following properties to make the default visualization show a specified color for each class (the values used in the analysis will not be affected):
  * `landcover_class_values="0,1,2"`
  * `landcover_class_palette="0000FF,00FF00,AABBCD"`


See the [managing assets page](https://developers.google.com/earth-engine/guides/manage_assets#set_asset_metadata) to learn how to set asset metadata.
## Masking
You can use `image.updateMask()` to set the opacity of individual pixels based on where pixels in a mask image are non-zero. Pixels equal to zero in the mask are excluded from computations and the opacity is set to 0 for display. The following example uses an NDWI threshold (see the [ Relational Operations section](https://developers.google.com/earth-engine/guides/image_relational) for information on thresholds) to update the mask on the NDWI layer created previously:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/image_visualization#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/image_visualization#colab-python-sample) More
```
// Mask the non-watery parts of the image, where NDWI < 0.4.
varndwiMasked=ndwi.updateMask(ndwi.gte(0.4));
Map.addLayer(ndwiMasked,ndwiViz,'NDWI masked');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Mask the non-watery parts of the image, where NDWI < 0.4.
ndwi_masked = ndwi.updateMask(ndwi.gte(0.4))
# Define a map centered on San Francisco Bay.
map_ndwi_masked = geemap.Map(center=[37.5010, -122.1899], zoom=10)
# Add the image layer to the map and display it.
map_ndwi_masked.add_layer(ndwi_masked, ndwi_viz, 'NDWI masked')
display(map_ndwi_masked)
```

## Visualization images
Use the `image.visualize()` method to convert an image into an 8-bit RGB image for display or export. For example, to convert the false-color composite and NDWI to 3-band display images, use:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/image_visualization#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/image_visualization#colab-python-sample) More
```
// Create visualization layers.
varimageRGB=image.visualize({bands:['B5','B4','B3'],max:0.5});
varndwiRGB=ndwiMasked.visualize({
min:0.5,
max:1,
palette:['00FFFF','0000FF']
});
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
image_rgb = image.visualize(bands=['B5', 'B4', 'B3'], max=0.5)
ndwi_rgb = ndwi_masked.visualize(min=0.5, max=1, palette=['00FFFF', '0000FF'])
```

## Mosaicking
You can use masking and `imageCollection.mosaic()` (see the [Mosaicking section](https://developers.google.com/earth-engine/guides/ic_composite_mosaic) for information on mosaicking) to achieve various cartographic effects. The `mosaic()` method renders layers in the output image according to their order in the input collection. The following example uses `mosaic()` to combine the masked NDWI and the false color composite and obtain a new visualization:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/image_visualization#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/image_visualization#colab-python-sample) More
```
// Mosaic the visualization layers and display (or export).
varmosaic=ee.ImageCollection([imageRGB,ndwiRGB]).mosaic();
Map.addLayer(mosaic,{},'mosaic');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Mosaic the visualization layers and display (or export).
mosaic = ee.ImageCollection([image_rgb, ndwi_rgb]).mosaic()
# Define a map centered on San Francisco Bay.
map_mosaic = geemap.Map(center=[37.5010, -122.1899], zoom=10)
# Add the image layer to the map and display it.
map_mosaic.add_layer(mosaic, None, 'mosaic')
display(map_mosaic)
```

In this example, observe that a list of the two visualization images is provided to the `ImageCollection` constructor. The order of the list determines the order in which the images are rendered on the map.
![mosaic_sf](https://developers.google.com/static/earth-engine/images/Images_mosaic_sf.png) Mosaic of a Landsat 8 false color composite and NDWI. San Francisco bay area, USA. 
## Clipping
The `image.clip()` method is useful for achieving cartographic effects. The following example clips the mosaic created previously to an arbitrary buffer zone around the city of San Francisco:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/image_visualization#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/image_visualization#colab-python-sample) More
```
// Create a circle by drawing a 20000 meter buffer around a point.
varroi=ee.Geometry.Point([-122.4481,37.7599]).buffer(20000);
// Display a clipped version of the mosaic.
Map.addLayer(mosaic.clip(roi),null,'mosaic clipped');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Create a circle by drawing a 20000 meter buffer around a point.
roi = ee.Geometry.Point([-122.4481, 37.7599]).buffer(20000)
mosaic_clipped = mosaic.clip(roi)
# Define a map centered on San Francisco.
map_mosaic_clipped = geemap.Map(center=[37.7599, -122.4481], zoom=10)
# Add the image layer to the map and display it.
map_mosaic_clipped.add_layer(mosaic_clipped, None, 'mosaic clipped')
display(map_mosaic_clipped)
```

In the previous example, note that the coordinates are provided to the `Geometry` constructor and the buffer length is specified as 20,000 meters. Learn more about geometries on the [Geometries page](https://developers.google.com/earth-engine/guides/geometries).
![clipped_sf](https://developers.google.com/static/earth-engine/images/Images_clip_SF_map.png) The mosaic shown above, clipped to a buffer around San Francisco, California, USA. 
## Rendering categorical maps
Palettes are also useful for rendering discrete valued maps, for example a land cover map. In the case of multiple classes, use the palette to supply a different color for each class. (The `image.remap()` method may be useful in this context, to convert arbitrary labels to consecutive integers). The following example uses a palette to render land cover categories:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/image_visualization#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/image_visualization#colab-python-sample) More
```
// Load 2012 MODIS land cover and select the IGBP classification.
varcover=ee.Image('MODIS/051/MCD12Q1/2012_01_01')
.select('Land_Cover_Type_1');
// Define a palette for the 18 distinct land cover classes.
varigbpPalette=[
'aec3d4',// water
'152106','225129','369b47','30eb5b','387242',// forest
'6a2325','c3aa69','b76031','d9903d','91af40',// shrub, grass
'111149',// wetlands
'cdb33b',// croplands
'cc0013',// urban
'33280d',// crop mosaic
'd7cdcc',// snow and ice
'f7e084',// barren
'6f6f6f'// tundra
];
// Specify the min and max labels and the color palette matching the labels.
Map.setCenter(-99.229,40.413,5);
Map.addLayer(cover,
{min:0,max:17,palette:igbpPalette},
'IGBP classification');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Load 2012 MODIS land cover and select the IGBP classification.
cover = ee.Image('MODIS/051/MCD12Q1/2012_01_01').select('Land_Cover_Type_1')
# Define a palette for the 18 distinct land cover classes.
igbp_palette = [
  'aec3d4', # water
  '152106',
  '225129',
  '369b47',
  '30eb5b',
  '387242', # forest
  '6a2325',
  'c3aa69',
  'b76031',
  'd9903d',
  '91af40', # shrub, grass
  '111149', # wetlands
  'cdb33b', # croplands
  'cc0013', # urban
  '33280d', # crop mosaic
  'd7cdcc', # snow and ice
  'f7e084', # barren
  '6f6f6f', # tundra
]
# Define a map centered on the United States.
map_palette = geemap.Map(center=[40.413, -99.229], zoom=5)
# Add the image layer to the map and display it. Specify the min and max labels
# and the color palette matching the labels.
map_palette.add_layer(
  cover, {'min': 0, 'max': 17, 'palette': igbp_palette}, 'IGBP classes'
)
display(map_palette)
```
![landcover_palettized](https://developers.google.com/static/earth-engine/images/Images_landcover_palettized.png) MODIS 2012 land cover using the IGBP classification. 
## Styled Layer Descriptors
You can use a Styled Layer Descriptor ([SLD](http://www.opengeospatial.org/standards/sld)) to render imagery for display. Provide `image.sldStyle()` with an XML description of the symbolization and coloring of the image, specifically the `RasterSymbolizer` element. Learn more about the `RasterSymbolizer` element [here](http://docs.geoserver.org/stable/en/user/styling/sld/reference/rastersymbolizer.html). For example, to render the land cover map described in the Rendering categorical maps section with an SLD, use:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/image_visualization#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/image_visualization#colab-python-sample) More
```
varcover=ee.Image('MODIS/051/MCD12Q1/2012_01_01').select('Land_Cover_Type_1');
// Define an SLD style of discrete intervals to apply to the image.
varsld_intervals=
'<RasterSymbolizer>'+
'<ColorMap type="intervals" extended="false">'+
'<ColorMapEntry color="#aec3d4" quantity="0" label="Water"/>'+
'<ColorMapEntry color="#152106" quantity="1" label="Evergreen Needleleaf Forest"/>'+
'<ColorMapEntry color="#225129" quantity="2" label="Evergreen Broadleaf Forest"/>'+
'<ColorMapEntry color="#369b47" quantity="3" label="Deciduous Needleleaf Forest"/>'+
'<ColorMapEntry color="#30eb5b" quantity="4" label="Deciduous Broadleaf Forest"/>'+
'<ColorMapEntry color="#387242" quantity="5" label="Mixed Deciduous Forest"/>'+
'<ColorMapEntry color="#6a2325" quantity="6" label="Closed Shrubland"/>'+
'<ColorMapEntry color="#c3aa69" quantity="7" label="Open Shrubland"/>'+
'<ColorMapEntry color="#b76031" quantity="8" label="Woody Savanna"/>'+
'<ColorMapEntry color="#d9903d" quantity="9" label="Savanna"/>'+
'<ColorMapEntry color="#91af40" quantity="10" label="Grassland"/>'+
'<ColorMapEntry color="#111149" quantity="11" label="Permanent Wetland"/>'+
'<ColorMapEntry color="#cdb33b" quantity="12" label="Cropland"/>'+
'<ColorMapEntry color="#cc0013" quantity="13" label="Urban"/>'+
'<ColorMapEntry color="#33280d" quantity="14" label="Crop, Natural Veg. Mosaic"/>'+
'<ColorMapEntry color="#d7cdcc" quantity="15" label="Permanent Snow, Ice"/>'+
'<ColorMapEntry color="#f7e084" quantity="16" label="Barren, Desert"/>'+
'<ColorMapEntry color="#6f6f6f" quantity="17" label="Tundra"/>'+
'</ColorMap>'+
'</RasterSymbolizer>';
Map.addLayer(cover.sldStyle(sld_intervals),{},'IGBP classification styled');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
cover = ee.Image('MODIS/051/MCD12Q1/2012_01_01').select('Land_Cover_Type_1')
# Define an SLD style of discrete intervals to apply to the image.
sld_intervals = """
<RasterSymbolizer>
 <ColorMap type="intervals" extended="false" >
  <ColorMapEntry color="#aec3d4" quantity="0" label="Water"/>
  <ColorMapEntry color="#152106" quantity="1" label="Evergreen Needleleaf Forest"/>
  <ColorMapEntry color="#225129" quantity="2" label="Evergreen Broadleaf Forest"/>
  <ColorMapEntry color="#369b47" quantity="3" label="Deciduous Needleleaf Forest"/>
  <ColorMapEntry color="#30eb5b" quantity="4" label="Deciduous Broadleaf Forest"/>
  <ColorMapEntry color="#387242" quantity="5" label="Mixed Deciduous Forest"/>
  <ColorMapEntry color="#6a2325" quantity="6" label="Closed Shrubland"/>
  <ColorMapEntry color="#c3aa69" quantity="7" label="Open Shrubland"/>
  <ColorMapEntry color="#b76031" quantity="8" label="Woody Savanna"/>
  <ColorMapEntry color="#d9903d" quantity="9" label="Savanna"/>
  <ColorMapEntry color="#91af40" quantity="10" label="Grassland"/>
  <ColorMapEntry color="#111149" quantity="11" label="Permanent Wetland"/>
  <ColorMapEntry color="#cdb33b" quantity="12" label="Cropland"/>
  <ColorMapEntry color="#cc0013" quantity="13" label="Urban"/>
  <ColorMapEntry color="#33280d" quantity="14" label="Crop, Natural Veg. Mosaic"/>
  <ColorMapEntry color="#d7cdcc" quantity="15" label="Permanent Snow, Ice"/>
  <ColorMapEntry color="#f7e084" quantity="16" label="Barren, Desert"/>
  <ColorMapEntry color="#6f6f6f" quantity="17" label="Tundra"/>
 </ColorMap>
</RasterSymbolizer>"""
# Apply the SLD style to the image.
cover_sld = cover.sldStyle(sld_intervals)
# Define a map centered on the United States.
map_sld_categorical = geemap.Map(center=[40.413, -99.229], zoom=5)
# Add the image layer to the map and display it.
map_sld_categorical.add_layer(cover_sld, None, 'IGBP classes styled')
display(map_sld_categorical)
```

To create a visualization image with a color ramp, set the type of the `ColorMap` to 'ramp'. The following example compares the 'interval' and 'ramp' types for rendering a DEM:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/image_visualization#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/image_visualization#colab-python-sample) More
```
// Load SRTM Digital Elevation Model data.
varimage=ee.Image('CGIAR/SRTM90_V4');
// Define an SLD style of discrete intervals to apply to the image. Use the
// opacity keyword to set pixels less than 0 as completely transparent. Pixels
// with values greater than or equal to the final entry quantity are set to
// fully transparent by default.
varsld_intervals=
'<RasterSymbolizer>'+
'<ColorMap type="intervals" extended="false" >'+
'<ColorMapEntry color="#0000ff" quantity="0" label="0 ﹤ x" opacity="0" />'+
'<ColorMapEntry color="#00ff00" quantity="100" label="0 ≤ x ﹤ 100" />'+
'<ColorMapEntry color="#007f30" quantity="200" label="100 ≤ x ﹤ 200" />'+
'<ColorMapEntry color="#30b855" quantity="300" label="200 ≤ x ﹤ 300" />'+
'<ColorMapEntry color="#ff0000" quantity="400" label="300 ≤ x ﹤ 400" />'+
'<ColorMapEntry color="#ffff00" quantity="900" label="400 ≤ x ﹤ 900" />'+
'</ColorMap>'+
'</RasterSymbolizer>';
// Define an sld style color ramp to apply to the image.
varsld_ramp=
'<RasterSymbolizer>'+
'<ColorMap type="ramp" extended="false" >'+
'<ColorMapEntry color="#0000ff" quantity="0" label="0"/>'+
'<ColorMapEntry color="#00ff00" quantity="100" label="100" />'+
'<ColorMapEntry color="#007f30" quantity="200" label="200" />'+
'<ColorMapEntry color="#30b855" quantity="300" label="300" />'+
'<ColorMapEntry color="#ff0000" quantity="400" label="400" />'+
'<ColorMapEntry color="#ffff00" quantity="500" label="500" />'+
'</ColorMap>'+
'</RasterSymbolizer>';
// Add the image to the map using both the color ramp and interval schemes.
Map.setCenter(-76.8054,42.0289,8);
Map.addLayer(image.sldStyle(sld_intervals),{},'SLD intervals');
Map.addLayer(image.sldStyle(sld_ramp),{},'SLD ramp');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Load SRTM Digital Elevation Model data.
image = ee.Image('CGIAR/SRTM90_V4')
# Define an SLD style of discrete intervals to apply to the image.
sld_intervals = """
  <RasterSymbolizer>
   <ColorMap type="intervals" extended="false" >
    <ColorMapEntry color="#0000ff" quantity="0" label="0"/>
    <ColorMapEntry color="#00ff00" quantity="100" label="1-100" />
    <ColorMapEntry color="#007f30" quantity="200" label="110-200" />
    <ColorMapEntry color="#30b855" quantity="300" label="210-300" />
    <ColorMapEntry color="#ff0000" quantity="400" label="310-400" />
    <ColorMapEntry color="#ffff00" quantity="1000" label="410-1000" />
   </ColorMap>
  </RasterSymbolizer>"""
# Define an sld style color ramp to apply to the image.
sld_ramp = """
  <RasterSymbolizer>
   <ColorMap type="ramp" extended="false" >
    <ColorMapEntry color="#0000ff" quantity="0" label="0"/>
    <ColorMapEntry color="#00ff00" quantity="100" label="100" />
    <ColorMapEntry color="#007f30" quantity="200" label="200" />
    <ColorMapEntry color="#30b855" quantity="300" label="300" />
    <ColorMapEntry color="#ff0000" quantity="400" label="400" />
    <ColorMapEntry color="#ffff00" quantity="500" label="500" />
   </ColorMap>
  </RasterSymbolizer>"""
# Define a map centered on the United States.
map_sld_interval = geemap.Map(center=[40.413, -99.229], zoom=5)
# Add the image layers to the map and display it.
map_sld_interval.add_layer(
  image.sldStyle(sld_intervals), None, 'SLD intervals'
)
map_sld_interval.add_layer(image.sldStyle(sld_ramp), None, 'SLD ramp')
display(map_sld_interval)
```

SLDs are also useful for stretching pixel values to improve visualizations of continuous data. For example, the following code compares the results of an arbitrary linear stretch with a min-max 'Normalization' and a 'Histogram' equalization:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/image_visualization#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/image_visualization#colab-python-sample) More
```
// Load a Landsat 8 raw image.
varimage=ee.Image('LANDSAT/LC08/C02/T1/LC08_044034_20140318');
// Define a RasterSymbolizer element with '_enhance_' for a placeholder.
vartemplate_sld=
'<RasterSymbolizer>'+
'<ContrastEnhancement><_enhance_/></ContrastEnhancement>'+
'<ChannelSelection>'+
'<RedChannel>'+
'<SourceChannelName>B5</SourceChannelName>'+
'</RedChannel>'+
'<GreenChannel>'+
'<SourceChannelName>B4</SourceChannelName>'+
'</GreenChannel>'+
'<BlueChannel>'+
'<SourceChannelName>B3</SourceChannelName>'+
'</BlueChannel>'+
'</ChannelSelection>'+
'</RasterSymbolizer>';
// Get SLDs with different enhancements.
varequalize_sld=template_sld.replace('_enhance_','Histogram');
varnormalize_sld=template_sld.replace('_enhance_','Normalize');
// Display the results.
Map.centerObject(image,10);
Map.addLayer(image,{bands:['B5','B4','B3'],min:0,max:15000},'Linear');
Map.addLayer(image.sldStyle(equalize_sld),{},'Equalized');
Map.addLayer(image.sldStyle(normalize_sld),{},'Normalized');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Load a Landsat 8 raw image.
image = ee.Image('LANDSAT/LC08/C02/T1/LC08_044034_20140318')
# Define a RasterSymbolizer element with '_enhance_' for a placeholder.
template_sld = """
<RasterSymbolizer>
 <ContrastEnhancement><_enhance_/></ContrastEnhancement>
 <ChannelSelection>
  <RedChannel>
   <SourceChannelName>B5</SourceChannelName>
  </RedChannel>
  <GreenChannel>
   <SourceChannelName>B4</SourceChannelName>
  </GreenChannel>
  <BlueChannel>
   <SourceChannelName>B3</SourceChannelName>
  </BlueChannel>
 </ChannelSelection>
</RasterSymbolizer>"""
# Get SLDs with different enhancements.
equalize_sld = template_sld.replace('_enhance_', 'Histogram')
normalize_sld = template_sld.replace('_enhance_', 'Normalize')
# Define a map centered on San Francisco Bay.
map_sld_continuous = geemap.Map(center=[37.5010, -122.1899], zoom=10)
# Add the image layers to the map and display it.
map_sld_continuous.add_layer(
  image, {'bands': ['B5', 'B4', 'B3'], 'min': 0, 'max': 15000}, 'Linear'
)
map_sld_continuous.add_layer(image.sldStyle(equalize_sld), None, 'Equalized')
map_sld_continuous.add_layer(
  image.sldStyle(normalize_sld), None, 'Normalized'
)
display(map_sld_continuous)
```

Points of note in reference to using SLDs in Earth Engine:
  * OGC SLD 1.0 and OGC SE 1.1 are supported.
  * The XML document passed in can be complete, or just the RasterSymbolizer element and down.
  * Bands may be selected by their Earth Engine names or index ('1', '2', ...).
  * The Histogram and Normalize contrast stretch mechanisms are not supported for floating point imagery.
  * Opacity is only taken into account when it is 0.0 (transparent). Non-zero opacity values are treated as completely opaque.
  * The OverlapBehavior definition is currently ignored.
  * The ShadedRelief mechanism is not currently supported.
  * The ImageOutline mechanism is not currently supported.
  * The Geometry element is ignored.
  * The output image will have histogram_bandname metadata if histogram equalization or normalization is requested.


## Thumbnail images
Use the `ee.Image.getThumbURL()` method to generate a PNG or JPEG thumbnail image for an `ee.Image` object. Printing the outcome of an expression ending with a call to `getThumbURL()` results in a URL being printed. Visiting the URL sets Earth Engine servers to work on generating the requested thumbnail on-the-fly. The image is displayed in a browser when processing completes. It can be downloaded by selecting appropriate options from the image's right-click context menu.
**Note:** The authorization token to process the thumbnail lasts 2 hours. Until it expires, anyone with the authorization token can generate the image. ![thumbnail_in_browser](https://developers.google.com/static/earth-engine/images/Images_thumbnail.png) SRTM digital elevation model displayed as a PNG thumbnail in a browser. 
The `getThumbURL()` method includes parameters, described in the [visualization parameters table](https://developers.google.com/earth-engine/guides/image_visualization#mapVisParamTable) above. Additionally, it takes optional `dimensions`, `region`, and `crs` arguments that control the spatial extent, size, and display projection of the thumbnail. 
Additional parameters for `ee.Image.getThumbURL()` with note on _format_ Parameter | Description | Type  
---|---|---  
_dimensions_ | Thumbnail dimensions in pixel units. If a single integer is provided, it defines the size of the image's larger aspect dimension and scales the smaller dimension proportionally. Defaults to 512 pixels for the larger image aspect dimension. | A single integer or string in the format: 'WIDTHxHEIGHT'  
_region_ | The geospatial region of the image to render. The whole image by default, or the bounds of a provided geometry.  | GeoJSON or a 2-D list of at least three point coordinates that define a linear ring  
_crs_ | The target projection e.g. 'EPSG:3857'. Defaults to WGS84 ('EPSG:4326').  | String  
_format_ | Defines thumbnail format as either PNG or JPEG. The default PNG format is implemented as RGBA, where the alpha channel represents valid and invalid pixels, defined by the image's `mask()`. Invalid pixels are transparent. The optional JPEG format is implemented as RGB, where invalid image pixels are zero filled across RGB channels.  | String; either 'png' or 'jpg'  
**Caution:** The `'WIDTHxHEIGHT'` _dimensions_ argument can alter the original aspect ratio of the data or region extent.
A single-band image will default to grayscale unless a `palette` argument is supplied. A multi-band image will default to RGB visualization of the first three bands, unless a `bands` argument is supplied. If only two bands are provided, the first band will map to red, the second to blue, and the green channel will be zero filled. 
The following are a series of examples demonstrating various combinations of `getThumbURL()` parameter arguments. Click on the URLs printed when you run this script to view the thumbnails.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/image_visualization#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/image_visualization#colab-python-sample) More
```
// Fetch a digital elevation model.
varimage=ee.Image('CGIAR/SRTM90_V4');
// Request a default thumbnail of the DEM with defined linear stretch.
// Set masked pixels (ocean) to 1000 so they map as gray.
varthumbnail1=image.unmask(1000).getThumbURL({
'min':0,
'max':3000,
'dimensions':500,
});
print('Default extent:',thumbnail1);
// Specify region by rectangle, define palette, set larger aspect dimension size.
varthumbnail2=image.getThumbURL({
'min':0,
'max':3000,
'palette':['00A600','63C600','E6E600','E9BD3A','ECB176','EFC2B3','F2F2F2'],
'dimensions':500,
'region':ee.Geometry.Rectangle([-84.6,-55.9,-32.9,15.7]),
});
print('Rectangle region and palette:',thumbnail2);
// Specify region by a linear ring and set display CRS as Web Mercator.
varthumbnail3=image.getThumbURL({
'min':0,
'max':3000,
'palette':['00A600','63C600','E6E600','E9BD3A','ECB176','EFC2B3','F2F2F2'],
'region':ee.Geometry.LinearRing([[-84.6,15.7],[-84.6,-55.9],[-32.9,-55.9]]),
'dimensions':500,
'crs':'EPSG:3857'
});
print('Linear ring region and specified crs',thumbnail3);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Fetch a digital elevation model.
image = ee.Image('CGIAR/SRTM90_V4')
# Request a default thumbnail of the DEM with defined linear stretch.
# Set masked pixels (ocean) to 1000 so they map as gray.
thumbnail_1 = image.unmask(1000).getThumbURL({
  'min': 0,
  'max': 3000,
  'dimensions': 500,
})
print('Default extent:', thumbnail_1)
# Specify region by rectangle, define palette, set larger aspect dimension size.
thumbnail_2 = image.getThumbURL({
  'min': 0,
  'max': 3000,
  'palette': [
    '00A600',
    '63C600',
    'E6E600',
    'E9BD3A',
    'ECB176',
    'EFC2B3',
    'F2F2F2',
  ],
  'dimensions': 500,
  'region': ee.Geometry.Rectangle([-84.6, -55.9, -32.9, 15.7]),
})
print('Rectangle region and palette:', thumbnail_2)
# Specify region by a linear ring and set display CRS as Web Mercator.
thumbnail_3 = image.getThumbURL({
  'min': 0,
  'max': 3000,
  'palette': [
    '00A600',
    '63C600',
    'E6E600',
    'E9BD3A',
    'ECB176',
    'EFC2B3',
    'F2F2F2',
  ],
  'region': ee.Geometry.LinearRing(
    [[-84.6, 15.7], [-84.6, -55.9], [-32.9, -55.9]]
  ),
  'dimensions': 500,
  'crs': 'EPSG:3857',
})
print('Linear ring region and specified crs:', thumbnail_3)
```
**Note:** Thumbnail images are also available as UI elements (Code Editor only), see: [ `ui.Thumbnail`](https://developers.google.com/earth-engine/guides/ui_widgets#ui.thumbnail). **Note:** `getThumbURL` is intended as a method for producing preview images you might include in presentations, websites, and social media posts. Its size limitation is 100,000,000 pixels and the browser can timeout for complicated requests. If you want a large image or have a complex process, see the [Exporting Data](https://developers.google.com/earth-engine/guides/exporting) page.
