 
#  ee.Image.clip 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-clip#examples)


Clips an image to a Geometry or Feature. 
The output bands correspond exactly to the input bands, except data not covered by the geometry is masked. The output image retains the metadata of the input image.
Use clipToCollection to clip an image to a FeatureCollection.
Returns the clipped image.
Usage| Returns  
---|---  
`Image.clip(geometry)`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The Image instance.  
`geometry`| Feature|Geometry|Object| The Geometry or Feature to clip to.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image-clip#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image-clip#colab-python-sample) More
```
// A digital elevation model.
vardem=ee.Image('NASA/NASADEM_HGT/001');
vardemVis={bands:'elevation',min:0,max:1500};
// Clip the DEM by a polygon geometry.
vargeomPoly=ee.Geometry.BBox(-121.55,39.01,-120.57,39.38);
vardemClip=dem.clip(geomPoly);
print('Clipped image retains metadata and band names',demClip);
Map.setCenter(-121.12,38.13,8);
Map.addLayer(demClip,demVis,'Polygon clip');
Map.addLayer(geomPoly,{color:'green'},'Polygon geometry',false);
// Clip the DEM by a line geometry.
vargeomLine=ee.Geometry.LinearRing(
[[-121.19,38.10],[-120.53,38.54],[-120.22,37.83],[-121.19,38.10]]);
Map.addLayer(dem.clip(geomLine),demVis,'Line clip');
Map.addLayer(geomLine,{color:'orange'},'Line geometry',false);
// Images have geometry; clip the dem image by the geometry of an S2 image.
vars2Img=ee.Image('COPERNICUS/S2_SR/20210109T185751_20210109T185931_T10SEG');
vargeomS2Img=s2Img.geometry();
Map.addLayer(dem.clip(geomS2Img),demVis,'Image geometry clip');
Map.addLayer(geomS2Img,{color:'blue'},'Image geometry',false);
// Don't use ee.Image.clip prior to ee.Image.regionReduction, the "geometry"
// parameter handles it more efficiently.
varzonalMax=dem.select('elevation').reduceRegion({
reducer:ee.Reducer.max(),
geometry:geomPoly
});
print('Max elevation (m)',zonalMax.get('elevation'));
// Don't use ee.Image.clip to clip an image by a FeatureCollection, use
// ee.Image.clipToCollection(collection).
varwatersheds=ee.FeatureCollection('USGS/WBD/2017/HUC10')
.filterBounds(ee.Geometry.Point(-122.754,38.606).buffer(2e4));
Map.addLayer(dem.clipToCollection(watersheds),demVis,'Watersheds clip');
Map.addLayer(watersheds,{color:'red'},'Watersheds',false);
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
dem_vis = {'bands': 'elevation', 'min': 0, 'max': 1500}
# Clip the DEM by a polygon geometry.
geom_poly = ee.Geometry.BBox(-121.55, 39.01, -120.57, 39.38)
dem_clip = dem.clip(geom_poly)
display('Clipped image retains metadata and band names', dem_clip)
m = geemap.Map()
m.set_center(-121.12, 38.13, 8)
m.add_layer(dem_clip, dem_vis, 'Polygon clip')
m.add_layer(geom_poly, {'color': 'green'}, 'Polygon geometry', False)
# Clip the DEM by a line geometry.
geom_line = ee.Geometry.LinearRing(
  [[-121.19, 38.10], [-120.53, 38.54], [-120.22, 37.83], [-121.19, 38.10]]
)
m.add_layer(dem.clip(geom_line), dem_vis, 'Line clip')
m.add_layer(geom_line, {'color': 'orange'}, 'Line geometry', False)
# Images have geometry clip the dem image by the geometry of an S2 image.
s_2_img = ee.Image('COPERNICUS/S2_SR/20210109T185751_20210109T185931_T10SEG')
geom_s_2_img = s_2_img.geometry()
m.add_layer(dem.clip(geom_s_2_img), dem_vis, 'Image geometry clip')
m.add_layer(geom_s_2_img, {'color': 'blue'}, 'Image geometry', False)
# Don't use ee.Image.clip prior to ee.Image.regionReduction, the "geometry"
# parameter handles it more efficiently.
zonal_max = dem.select('elevation').reduceRegion(
  reducer=ee.Reducer.max(), geometry=geom_poly
)
display('Max elevation (m)', zonal_max.get('elevation'))
# Don't use ee.Image.clip to clip an image by a FeatureCollection, use
# ee.Image.clipToCollection(collection).
watersheds = ee.FeatureCollection('USGS/WBD/2017/HUC10').filterBounds(
  ee.Geometry.Point(-122.754, 38.606).buffer(2e4)
)
m.add_layer(dem.clipToCollection(watersheds), dem_vis, 'Watersheds clip')
m.add_layer(watersheds, {'color': 'red'}, 'Watersheds', False)
m
```

