 
#  Image Reductions
Stay organized with collections  Save and categorize content based on your preferences. 
To reduce an `Image`, use `image.reduce()`. Reducing an image functions in an analogous way to `imageCollection.reduce()`, except the bands of the image are input to the reducer rather than the images in the collection. The output is also an image with number of bands equal to number of reducer outputs. For example:
### Code Editor (JavaScript)
```
// Load an image and select some bands of interest.
varimage=ee.Image('LANDSAT/LC08/C02/T1/LC08_044034_20140318')
.select(['B4','B3','B2']);

// Reduce the image to get a one-band maximum value image.
varmaxValue=image.reduce(ee.Reducer.max());

// Display the result.
Map.centerObject(image,10);
Map.addLayer(maxValue,{max:13000},'Maximum value image');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Load an image and select some bands of interest.
image = ee.Image('LANDSAT/LC08/C02/T1/LC08_044034_20140318').select(
    ['B4', 'B3', 'B2']
)

# Reduce the image to get a one-band maximum value image.
max_value = image.reduce(ee.Reducer.max())

# Display the result.
m = geemap.Map()
m.center_object(image, 10)
m.add_layer(max_value, {'max': 13000}, 'Maximum value image')
m
```

