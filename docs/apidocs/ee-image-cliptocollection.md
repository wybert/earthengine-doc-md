 
#  ee.Image.clipToCollection
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-cliptocollection#examples)


Clips an image to a FeatureCollection. The output bands correspond exactly the input bands, except data not covered by the geometry of at least one feature from the collection is masked. The output image retains the metadata of the input image.
Usage | Returns  
---|---  
`Image.clipToCollection(collection)` | Image  
Argument | Type | Details  
---|---|---  
this: `input` | Image | The image to clip.  
`collection` | Object | The FeatureCollection to clip to.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image-cliptocollection#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image-cliptocollection#colab-python-sample) More
```
// A digital elevation model.
vardem=ee.Image('NASA/NASADEM_HGT/001');

// A FeatureCollection defining Southeast Asia boundary.
varfc=ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017')
.filter('wld_rgn == "SE Asia"');

// Clip the DEM by the Southeast Asia boundary FeatureCollection.
vardemClip=dem.clipToCollection(fc);
print('Clipped image retains metadata and band names',demClip);

// Add layers to the map.
Map.setCenter(110.64,9.16,4);
Map.addLayer(dem,{bands:'elevation',min:0,max:2500},'Original DEM');
Map.addLayer(fc,{color:'blue'},'FeatureCollection');
Map.addLayer(demClip,
{bands:'elevation',min:0,max:2500,palette:['green','yellow','brown']},
'Clipped DEM');
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

# A FeatureCollection defining Southeast Asia boundary.
fc = ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017').filter(
    'wld_rgn == "SE Asia"'
)

# Clip the DEM by the Southeast Asia boundary FeatureCollection.
dem_clip = dem.clipToCollection(fc)
display('Clipped image retains metadata and band names', dem_clip)

# Add layers to the map.
m = geemap.Map()
m.set_center(110.64, 9.16, 4)
m.add_layer(dem, {'bands': 'elevation', 'min': 0, 'max': 2500}, 'Original DEM')
m.add_layer(fc, {'color': 'blue'}, 'FeatureCollection')
m.add_layer(
    dem_clip,
    {
        'bands': 'elevation',
        'min': 0,
        'max': 2500,
        'palette': ['green', 'yellow', 'brown'],
    },
    'Clipped DEM',
)
m
```

Was this helpful?
