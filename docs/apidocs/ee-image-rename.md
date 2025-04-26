 
#  ee.Image.rename 
Stay organized with collections  Save and categorize content based on your preferences. 
Rename the bands of an image. 
Returns the renamed image.
Usage| Returns  
---|---  
`Image.rename(var_args)`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The Image instance.  
`var_args`| List| The new names for the bands. Must match the number of bands in the Image.  
## Examples
### Code Editor (JavaScript)
```
// A Sentinel-2 surface reflectance image.
varimg=ee.Image('COPERNICUS/S2_SR/20210109T185751_20210109T185931_T10SEG')
.select(['B11','B8','B3']);
print('Original selected S2 image band names',img.bandNames());
print('Rename bands using a list (JavaScript array or ee.List)',
img.rename(['SWIR1','NIR','GREEN']).bandNames());
print('Rename bands using a series of string arguments',
img.rename('swir1','nir','green').bandNames());
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# A Sentinel-2 surface reflectance image.
img = ee.Image(
  'COPERNICUS/S2_SR/20210109T185751_20210109T185931_T10SEG'
).select(['B11', 'B8', 'B3'])
print('Original selected S2 image band names:', img.bandNames().getInfo())
print('Rename bands using a list (Python list or ee.List):',
   img.rename(['SWIR1', 'NIR', 'GREEN']).bandNames().getInfo())
print('Rename bands using a series of string arguments:',
   img.rename('swir1', 'nir', 'green').bandNames().getInfo())
```

