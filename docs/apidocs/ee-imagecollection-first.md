 
#  ee.ImageCollection.first 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Returns the first entry from a given collection. 
Usage| Returns  
---|---  
`ImageCollection.first()`| Image  
Argument| Type| Details  
---|---|---  
this: `imagecollection`| ImageCollection| The ImageCollection instance.  
## Examples
### Code Editor (JavaScript)
```
varimage=ee.ImageCollection('COPERNICUS/S2_SR').first();
Map.centerObject(image,8);
varvis={bands:['B4','B3','B2'],min:0,max:5000};
Map.addLayer(image,vis,'first of S2_SR');
// Display the image metadata.
print(image);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
image = ee.ImageCollection('COPERNICUS/S2_SR').first()
m = geemap.Map()
m.center_object(image, 8)
vis = {'bands': ['B4', 'B3', 'B2'], 'min': 0, 'max': 5000}
m.add_layer(image, vis, 'first of S2_SR')
display(m)
# Display the image metadata.
display(image)
```

