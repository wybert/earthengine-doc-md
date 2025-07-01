 
#  ee.Image.pixelArea
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-pixelarea#examples)


Generate an image in which the value of each pixel is the area of that pixel in square meters. The returned image has a single band called "area." 
Usage| Returns  
---|---  
`ee.Image.pixelArea()`| Image  
**No arguments.**
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image-pixelarea#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image-pixelarea#colab-python-sample) More
```
// Create a pixel area image. Pixel values are square meters based on
// a given CRS and scale (or CRS transform).
varpixelArea=ee.Image.pixelArea();
// The default projection is WGS84 with 1-degree scale.
print('Pixel area default projection',pixelArea.projection());
// When inspecting the output in the Code Editor map, the scale of analysis is
// determined by the zoom level. As you zoom in and out, you'll notice that the
// area of the clicked pixel changes. To set a specific pixel scale when
// performing a computation, provide an argument to the `scale` or
// `crsTransform` parameters whenever a function gives you the option.
Map.addLayer(pixelArea,null,'Pixel area for inspection',false);
// The "area" band produced by the `pixelArea` function can be useful for
// calculating the area of a certain condition of another image. For example,
// here we use the sum reducer to determine the area above 2250m in the North
// Cascades ecoregion, according to a 30m digital elevation model.
// Import a DEM and subset the "elevation" band.
varelev=ee.Image('NASA/NASADEM_HGT/001').select('elevation');
// Define a high elevation mask where pixels with elevation greater than 2250m
// are set to 1, otherwise 0.
varhighElevMask=elev.gt(2250);
// Apply the high elevation mask to the pixel area image.
varhighElevArea=pixelArea.updateMask(highElevMask);
// Import an ecoregion feature collection and filter it by ecoregion name.
varecoregion=ee.FeatureCollection('RESOLVE/ECOREGIONS/2017')
.filter('ECO_NAME == "North Cascades conifer forests"');
// Display the ecoregion and high elevation area.
Map.setCenter(-121.127,48.389,7);
Map.addLayer(ecoregion,null,'North Cascades ecoregion');
Map.addLayer(highElevArea.clip(ecoregion),
{palette:'yellow'},'High elevation area');
// Sum the area of high elevation pixels in the North Cascades ecoregion.
vararea=highElevArea.reduceRegion({
reducer:ee.Reducer.sum(),
geometry:ecoregion,
crs:elev.projection(),// DEM coordinate reference system
crsTransform:elev.projection().getInfo().transform,// DEM grid alignment
maxPixels:1e8
});
// Fetch the summed area property from the resulting dictionary and convert
// square meters to square kilometers.
varsquareMeters=area.getNumber('area');
varsquareKilometers=squareMeters.divide(1e6);
print('Square meters above 2250m elevation',squareMeters);
print('Square kilometers above 2250m elevation',squareKilometers);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Create a pixel area image. Pixel values are square meters based on
# a given CRS and scale (or CRS transform).
pixel_area = ee.Image.pixelArea()
# The default projection is WGS84 with 1-degree scale.
display('Pixel area default projection', pixel_area.projection())
# When inspecting the output in the Code Editor map, the scale of analysis is
# determined by the zoom level. As you zoom in and out, you'll notice that the
# area of the clicked pixel changes. To set a specific pixel scale when
# performing a computation, provide an argument to the `scale` or
# `crsTransform` parameters whenever a function gives you the option.
m = geemap.Map()
m.add_layer(pixel_area, None, 'Pixel area for inspection', False)
# The "area" band produced by the `pixel_area` function can be useful for
# calculating the area of a certain condition of another image. For example,
# here we use the sum reducer to determine the area above 2250m in the North
# Cascades ecoregion, according to a 30m digital elevation model.
# Import a DEM and subset the "elevation" band.
elev = ee.Image('NASA/NASADEM_HGT/001').select('elevation')
# Define a high elevation mask where pixels with elevation greater than 2250m
# are set to 1, otherwise 0.
high_elev_mask = elev.gt(2250)
# Apply the high elevation mask to the pixel area image.
high_elev_area = pixel_area.updateMask(high_elev_mask)
# Import an ecoregion feature collection and filter it by ecoregion name.
ecoregion = ee.FeatureCollection('RESOLVE/ECOREGIONS/2017').filter(
  'ECO_NAME == "North Cascades conifer forests"'
)
# Display the ecoregion and high elevation area.
m.set_center(-121.127, 48.389, 7)
m.add_layer(ecoregion, None, 'North Cascades ecoregion')
m.add_layer(
  high_elev_area.clip(ecoregion), {'palette': 'yellow'}, 'High elevation area'
)
display(m)
# Sum the area of high elevation pixels in the North Cascades ecoregion.
area = high_elev_area.reduceRegion(
  reducer=ee.Reducer.sum(),
  geometry=ecoregion,
  crs=elev.projection(), # DEM coordinate reference system
  crsTransform=elev.projection().getInfo()['transform'], # DEM grid alignment
  maxPixels=1e8,
)
# Fetch the summed area property from the resulting dictionary and convert
# square meters to square kilometers.
square_meters = area.getNumber('area')
square_kilometers = square_meters.divide(1e6)
display('Square meters above 2250m elevation', square_meters)
display('Square kilometers above 2250m elevation', square_kilometers)
```

Was this helpful?
