 
#  ee.Image.clipToBoundsAndScale 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-cliptoboundsandscale#examples)


Clips an image to the bounds of a Geometry, and scales the clipped image to a particular size or scale. **Caution:** providing a large or complex collection as the `geometry` argument can result in poor performance. Collating the geometry of collections does not scale well; use the smallest collection (or geometry) that is required to achieve the desired outcome.
Usage| Returns  
---|---  
`Image.clipToBoundsAndScale( _geometry_, _width_, _height_, _maxDimension_, _scale_)`| Image  
Argument| Type| Details  
---|---|---  
this: `input`| Image| The image to clip and scale.  
`geometry`| Geometry, default: null| The Geometry to clip the image to. The image will be clipped to the bounding box, in the image's projection, of this geometry.  
`width`| Integer, default: null| The width to scale the image to, in pixels. Must be provided along with "height". Exclusive with "maxDimension" and "scale".  
`height`| Integer, default: null| The height to scale the image to, in pixels. Must be provided along with "width". Exclusive with "maxDimension" and "scale".  
`maxDimension`| Integer, default: null| The maximum dimension to scale the image to, in pixels. Exclusive with "width", "height" and "scale".  
`scale`| Float, default: null| If scale is specified, then the projection is scaled by dividing the specified scale value by the nominal size of a meter in the image's projection. Exclusive with "width", "height", and "maxDimension".  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image-cliptoboundsandscale#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image-cliptoboundsandscale#colab-python-sample) More
```
// A digital elevation model.
vardem=ee.Image('NASA/NASADEM_HGT/001');
vardemVis={bands:'elevation',min:0,max:2000};
print('DEM',dem);
Map.setCenter(-121.38,46.51,8);
Map.addLayer(dem,demVis,'DEM');
// Clip DEM by a single polygon geometry, specify width and height parameters.
vargeom1=ee.Geometry.BBox(-123.55,46.61,-122.57,46.98);
vardemClip1=dem.clipToBoundsAndScale({
geometry:geom1,
width:20,// pixels
height:10// pixels
});
print('Clipped image retains metadata and band names',demClip1);
Map.addLayer(demClip1,demVis,'Single geometry clip (width, height)');
Map.addLayer(geom1,{color:'red'},'Single geometry (width, height)');
// Clip DEM by a single polygon geometry, specify maxDimension parameter.
vargeom2=ee.Geometry.BBox(-120.79,46.58,-120.16,46.81);
vardemClip2=dem.clipToBoundsAndScale({
geometry:geom2,
maxDimension:5,// pixels
});
Map.addLayer(demClip2,demVis,'Single polygon clip (maxDimension)');
Map.addLayer(geom2,{color:'yellow'},'Single polygon (maxDimension)');
// Clip DEM by a single polygon geometry, specify scale parameter.
vargeom3=ee.Geometry.BBox(-120.79,46.18,-120.16,46.41);
vardemClip3=dem.clipToBoundsAndScale({
geometry:geom3,
scale:1e4,// meters
});
Map.addLayer(demClip3,demVis,'Single polygon clip (scale)');
Map.addLayer(geom3,{color:'blue'},'Single polygon (scale)');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# A digital elevation model.
dem = ee.Image('NASA/NASADEM_HGT/001')
dem_vis = {'bands': 'elevation', 'min': 0, 'max': 2000}
display('DEM', dem)
m = geemap.Map()
m.set_center(-121.38, 46.51, 8)
m.add_layer(dem, dem_vis, 'DEM')
# Clip DEM by a single polygon geometry, specify width and height parameters.
geom_1 = ee.Geometry.BBox(-123.55, 46.61, -122.57, 46.98)
dem_clip_1 = dem.clipToBoundsAndScale(geometry=geom_1, width=20, height=10)
display('Clipped image retains metadata and band names', dem_clip_1)
m.add_layer(dem_clip_1, dem_vis, 'Single geometry clip (width, height)')
m.add_layer(geom_1, {'color': 'red'}, 'Single geometry (width, height)')
# Clip DEM by a single polygon geometry, specify maxDimension parameter.
geom_2 = ee.Geometry.BBox(-120.79, 46.58, -120.16, 46.81)
dem_clip_2 = dem.clipToBoundsAndScale(geometry=geom_2, maxDimension=5)
m.add_layer(dem_clip_2, dem_vis, 'Single polygon clip (maxDimension)')
m.add_layer(geom_2, {'color': 'yellow'}, 'Single polygon (maxDimension)')
# Clip DEM by a single polygon geometry, specify scale parameter.
geom_3 = ee.Geometry.BBox(-120.79, 46.18, -120.16, 46.41)
dem_clip_3 = dem.clipToBoundsAndScale(geometry=geom_3, scale=1e4)
m.add_layer(dem_clip_3, dem_vis, 'Single polygon clip (scale)')
m.add_layer(geom_3, {'color': 'blue'}, 'Single polygon (scale)')
m
```

Was this helpful?
