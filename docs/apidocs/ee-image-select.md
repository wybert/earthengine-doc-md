 
#  ee.Image.select
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-select#examples)


Selects bands from an image. 
Returns an image with the selected bands.
Usage| Returns  
---|---  
`Image.select(var_args)`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The Image instance.  
`var_args`| VarArgs| One of two possibilities: 
  * Any number of non-list arguments. All of these will be interpreted as band selectors. These can be band names, regexes, or numeric indices. E.g. selected = image.select('a', 'b', 3, 'd');
  * Two lists. The first will be used as band selectors and the second as new names for the selected bands. The number of new names must match the number of selected bands. E.g. selected = image.select(['a', 4], ['newA', 'newB']);

  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image-select#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image-select#colab-python-sample) More
```
// A Sentinel-2 surface reflectance image.
varimg=ee.Image('COPERNICUS/S2_SR/20210109T185751_20210109T185931_T10SEG');
print('All band names',img.bandNames());
print('Select a band by name',
img.select('B11').bandNames());
print('Select a band by index',
img.select(10).bandNames());
print('Select bands using a list',
img.select(['B11','B8','B3']).bandNames());
print('Select bands by an argument series',
img.select('B11','B8','B3').bandNames());
print('Mixing string and integer selectors is valid',
img.select(10,'B8',2).bandNames());
print('Rename selected bands using two corresponding lists',
img.select(['B11','B8','B3'],['SWIR1','NIR','Green']).bandNames());
// Use regular expressions to select bands.
print('Match "QA" followed by any two characters',
img.select('QA..').bandNames());
print('Match "B" followed by any character, any number of times',
img.select('B.*').bandNames());
print('Match "B" followed by any character, and any optional third character',
img.select('B..?').bandNames());
print('Match "B" followed by a character in the range 6-8',
img.select('B[6-8]').bandNames());
print('Match "B" followed by a character in the range 1-9 and then 1-2',
img.select('B[1-9][1-2]').bandNames());
print('Match "B" or "QA" each followed by any character, any number of times.',
img.select('B.*|QA.*').bandNames());
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# A Sentinel-2 surface reflectance image.
img = ee.Image('COPERNICUS/S2_SR/20210109T185751_20210109T185931_T10SEG')
print('All band names:', img.bandNames().getInfo())
print('Select a band by name:', img.select('B11').bandNames().getInfo())
print('Select a band by index:', img.select(10).bandNames().getInfo())
print('Select bands using a list:',
   img.select(['B11', 'B8', 'B3']).bandNames().getInfo())
print('Select bands by an argument series:',
   img.select('B11', 'B8', 'B3').bandNames().getInfo())
print('Mixing string and integer selectors is valid:',
   img.select(10, 'B8', 2).bandNames().getInfo())
print('Rename selected bands using two corresponding lists:',
   img.select(['B11', 'B8', 'B3'], ['SWIR1', 'NIR', 'Green'])
   .bandNames().getInfo())
# Use regular expressions to select bands.
print('Match "QA" followed by any two characters:',
   img.select('QA..').bandNames().getInfo())
print('Match "B" followed by any character, any number of times:',
   img.select('B.*').bandNames().getInfo())
print('Match "B" followed by any character, and any optional third character',
   img.select('B..?').bandNames().getInfo())
print('Match "B" followed by a character in the range 6-8',
   img.select('B[6-8]').bandNames().getInfo())
print('Match "B" followed by a character in the range 1-9 and then 1-2',
   img.select('B[1-9][1-2]').bandNames().getInfo())
print('Match "B" or "QA" each followed by any character, any number of times.',
   img.select('B.*|QA.*').bandNames().getInfo())
```

