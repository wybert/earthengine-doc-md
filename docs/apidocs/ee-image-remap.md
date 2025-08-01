 
#  ee.Image.remap
Stay organized with collections  Save and categorize content based on your preferences. 
Maps from input values to output values, represented by two parallel lists. Any input values not included in the input list are either set to defaultValue if it is given or masked if it isn't. Note that inputs containing floating point values might sometimes fail to match due to floating point precision errors. Usage | Returns  
---|---  
`Image.remap(from, to, _defaultValue_, _bandName_)`|  Image  
Argument | Type | Details  
---|---|---  
this: `image` | Image | The image to which the remapping is applied.  
`from` | List | The source values (numbers or ee.Array). All values in this list will be mapped to the corresponding value in 'to'.  
`to` | List | The destination values (numbers or ee.Array). These are used to replace the corresponding values in 'from'. Must have the same number of values as 'from'.  
`defaultValue` | Object, default: null | The default value to replace values that weren't matched by a value in 'from'. If not specified, unmatched values are masked out.  
`bandName` | String, default: null | The name of the band to remap. If not specified, the first band in the image is used.  
## Examples
### Code Editor (JavaScript)
```
// A land cover image.
varimg=ee.Image('ESA/WorldCover/v100/2020');

// A list of pixel values to replace.
varfromList=[10,20,30,40,50,60,70,80,90,95,100];

// A corresponding list of replacement values (10 becomes 1, 20 becomes 2, etc).
vartoList=[1,2,2,2,3,2,4,5,6,6,2];

// Replace pixel values in the image. If the image is multi-band, only the
// remapped band will be returned. The returned band name is "remapped".
// Input image properties are retained in the output image.
varimgRemap=img.remap({
from:fromList,
to:toList,
defaultValue:0,
bandName:'Map'
});

// Display the original and remapped images. Note that similar land cover
// classes in the original image are grouped into aggregate classes by
// from → to value mapping.
Map.addLayer(img,null,'Original image');
Map.addLayer(imgRemap,{
min:1,max:6,
palette:'darkgreen, lightgreen, red, white, blue, lightblue'
},'Remapped image');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# A land cover image.
img = ee.Image('ESA/WorldCover/v100/2020')

# A list of pixel values to replace.
from_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 100]

# A corresponding list of replacement values (10 becomes 1, 20 becomes 2, etc).
to_list = [1, 2, 2, 2, 3, 2, 4, 5, 6, 6, 2]

# Replace pixel values in the image. If the image is multi-band, only the
# remapped band will be returned. The returned band name is "remapped".
# Input image properties are retained in the output image.
img_remap = img.remap(from_list, to_list, defaultValue=0, bandName='Map')

# Display the original and remapped images. Note that similar land cover
# classes in the original image are grouped into aggregate classes by
# from → to value mapping.
m = geemap.Map()
m.add_layer(img, None, 'Original image')
m.add_layer(
    img_remap,
    {
        'min': 1,
        'max': 6,
        'palette': [
            'darkgreen',
            'lightgreen',
            'red',
            'white',
            'blue',
            'lightblue',
        ],
    },
    'Remapped image',
)
m
```

