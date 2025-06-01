 
#  ee.Image.changeProj 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-changeproj#examples)


Tweaks the projection of the input image, moving each pixel from its location in srcProj to the same coordinates in dstProj. 
Usage| Returns  
---|---  
`Image.changeProj(srcProj, dstProj)`| Image  
Argument| Type| Details  
---|---|---  
this: `input`| Image|   
`srcProj`| Projection| The original projection.  
`dstProj`| Projection| The new projection.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image-changeproj#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image-changeproj#colab-python-sample) More
```
// A DEM image object.
varimg=ee.Image('MERIT/DEM/v1_0_3');
// Construct a projection object from a WKT string or EPSG code, for example,
// the Robinson projection (https://epsg.io/54030).
varproj=ee.Projection(
'PROJCS["World_Robinson",'+
'GEOGCS["GCS_WGS_1984",'+
'DATUM["WGS_1984",'+
'SPHEROID["WGS_1984",6378137,298.257223563]],'+
'PRIMEM["Greenwich",0],'+
'UNIT["Degree",0.017453292519943295]],'+
'PROJECTION["Robinson"],'+
'UNIT["Meter",1]]'
)
// Optionally adjust projection scale; stretch layer larger in this case.
.scale(0.9,0.9);
// "Paint" the image in the desired projection onto the projection of
// the map canvas ('EPSG:3857').
varimgProj=img.changeProj(proj,'EPSG:3857');
// Add an overlay image to the map to cover the default base layers.
Map.setCenter(0,0,2);
Map.addLayer(ee.Image(1),{palette:'grey'},'Grey background',false);
// Add the projection-tweaked image to the map.
Map.addLayer(imgProj,{min:0,max:3000},'DEM in Robinson projection');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# A DEM image object.
img = ee.Image('MERIT/DEM/v1_0_3')
# Construct a projection object from a WKT string or EPSG code, for example,
# the Robinson projection (https://epsg.io/54030).
proj = (
  ee.Projection(
    'PROJCS["World_Robinson",'
    + 'GEOGCS["GCS_WGS_1984",'
    + 'DATUM["WGS_1984",'
    + 'SPHEROID["WGS_1984",6378137,298.257223563]],'
    + 'PRIMEM["Greenwich",0],'
    + 'UNIT["Degree",0.017453292519943295]],'
    + 'PROJECTION["Robinson"],'
    + 'UNIT["Meter",1]]'
  )
  # Optionally adjust projection scale stretch layer larger in this case.
  .scale(0.9, 0.9)
)
# "Paint" the image in the desired projection onto the projection of
# the map canvas ('EPSG:3857').
img_proj = img.changeProj(proj, 'EPSG:3857')
# Add an overlay image to the map to cover the default base layers.
m = geemap.Map()
m.set_center(0, 0, 2)
m.add_layer(ee.Image(1), {'palette': 'grey'}, 'Grey background', False)
# Add the projection-tweaked image to the map.
m.add_layer(
  img_proj,
  {'min': 0, 'max': 3000},
  'DEM in Robinson projection',
)
m
```

Was this helpful?
