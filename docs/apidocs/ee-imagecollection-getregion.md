 
#  ee.ImageCollection.getRegion 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-getregion#examples)


Output an array of values for each [pixel, band, image] tuple in an ImageCollection. The output contains rows of id, lon, lat, time, and all bands for each image that intersects each pixel in the given region. Attempting to extract more than 1048576 values will result in an error. 
Usage| Returns  
---|---  
`ImageCollection.getRegion(geometry,  _scale_, _crs_, _crsTransform_)`| List  
Argument| Type| Details  
---|---|---  
this: `collection`| ImageCollection| The image collection to extract data from.  
`geometry`| Geometry| The region over which to extract data.  
`scale`| Float, default: null| A nominal scale in meters of the projection to work in.  
`crs`| Projection, optional| The projection to work in. If unspecified, defaults to EPSG:4326. If specified in addition to scale, the projection is rescaled to the specified scale.  
`crsTransform`| List, default: null| The array of CRS transform values. This is a row-major ordering of a 3x2 affine transform. This option is mutually exclusive with the scale option, and will replace any transform already set on the given projection.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-getregion#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-getregion#colab-python-sample) More
```
// A Landsat 8 TOA image collection (3 months at a specific point, RGB bands).
varcol=ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA')
.filterBounds(ee.Geometry.Point(-90.70,34.71))
.filterDate('2020-07-01','2020-10-01')
.select('B[2-4]');
print('Collection',col);
// Define a region to get pixel values for. This is a small rectangle region
// that intersects 2 image pixels at 30-meter scale.
varroi=ee.Geometry.BBox(-90.496353,34.851971,-90.495749,34.852197);
// Display the region of interest overlaid on an image representative. Note
// the ROI intersection with 2 pixels.
varvisParams={
bands:['B4','B3','B2'],
min:0.128,
max:0.163
};
Map.setCenter(-90.49605,34.85211,19);
Map.addLayer(col.first(),visParams,'Image representative');
Map.addLayer(roi,{color:'white'},'ROI');
// Fetch pixel-level information from all images in the collection for the
// pixels intersecting the ROI.
varpixelInfoBbox=col.getRegion({
geometry:roi,
scale:30
});
// The result is a table (a list of lists) where the first row is column
// labels and subsequent rows are image pixels. Columns contain values for
// the image ID ('system:index'), pixel longitude and latitude, image
// observation time ('system:time_start'), and bands. In this example, note
// that there are 5 images and the region intersects 2 pixels, so n rows
// equals 11 (5 * 2 + 1). All collection images must have the same number of
// bands with the same names.
print('Extracted pixel info',pixelInfoBbox);
// The function accepts all geometry types (e.g., points, lines, polygons).
// Here, a multi-point geometry with two points is used.
varpoints=ee.Geometry.MultiPoint([[-90.49,34.85],[-90.48,34.84]]);
varpixelInfoPoints=col.getRegion({
geometry:points,
scale:30
});
print('Point geometry example',pixelInfoPoints);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# A Landsat 8 TOA image collection (3 months at a specific point, RGB bands).
col = (
  ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA')
  .filterBounds(ee.Geometry.Point(-90.70, 34.71))
  .filterDate('2020-07-01', '2020-10-01')
  .select('B[2-4]')
)
display('Collection', col)
# Define a region to get pixel values for. This is a small rectangle region
# that intersects 2 image pixels at 30-meter scale.
roi = ee.Geometry.BBox(-90.496353, 34.851971, -90.495749, 34.852197)
# Display the region of interest overlaid on an image representative. Note
# the ROI intersection with 2 pixels.
vis_params = {'bands': ['B4', 'B3', 'B2'], 'min': 0.128, 'max': 0.163}
m = geemap.Map()
m.set_center(-90.49605, 34.85211, 19)
m.add_layer(col.first(), vis_params, 'Image representative')
m.add_layer(roi, {'color': 'white'}, 'ROI')
display(m)
# Fetch pixel-level information from all images in the collection for the
# pixels intersecting the ROI.
pixel_info_bbox = col.getRegion(geometry=roi, scale=30)
# The result is a table (a list of lists) where the first row is column
# labels and subsequent rows are image pixels. Columns contain values for
# the image ID ('system:index'), pixel longitude and latitude, image
# observation time ('system:time_start'), and bands. In this example, note
# that there are 5 images and the region intersects 2 pixels, so n rows
# equals 11 (5 * 2 + 1). All collection images must have the same number of
# bands with the same names.
display('Extracted pixel info', pixel_info_bbox)
# The function accepts all geometry types (e.g., points, lines, polygons).
# Here, a multi-point geometry with two points is used.
points = ee.Geometry.MultiPoint([[-90.49, 34.85], [-90.48, 34.84]])
pixel_info_points = col.getRegion(geometry=points, scale=30)
display('Point geometry example', pixel_info_points)
```

