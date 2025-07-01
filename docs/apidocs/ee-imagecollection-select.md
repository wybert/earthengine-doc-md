 
#  ee.ImageCollection.select
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-select#examples)


Select bands from each image in a collection. 
Returns the image collection with selected bands.
Usage| Returns  
---|---  
`ImageCollection.select(selectors,  _names_)`| ImageCollection  
Argument| Type| Details  
---|---|---  
this: `imagecollection`| ImageCollection| The ImageCollection instance.  
`selectors`| List| A list of names, regexes or numeric indices specifying the bands to select.  
`names`| List, optional| A list of new names for the output bands. Must match the number of bands selected.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-select#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-select#colab-python-sample) More
```
// A Sentinel-2 surface reflectance image collection.
varcol=ee.ImageCollection('COPERNICUS/S2_SR')
.filterBounds(ee.Geometry.Point(-122.152,37.336))
.filterDate('2021-01-01','2021-02-01');
print('All band names',col.first().bandNames());
print('Select a band by name',
col.select('B11').first().bandNames());
print('Select a band by index',
col.select(10).first().bandNames());
print('Select bands using a list',
col.select(['B11','B8','B3']).first().bandNames());
print('Select bands by an argument series',
col.select('B11','B8','B3').first().bandNames());
print('Mixing string and integer selectors is valid',
col.select(10,'B8',2).first().bandNames());
print('Rename selected bands using two corresponding lists',
col.select(['B11','B8','B3'],['SWIR1','NIR','Green'])
.first().bandNames());
// Use regular expressions to select bands.
print('Match "QA" followed by any two characters',
col.select('QA..').first().bandNames());
print('Match "B" followed by any character, any number of times',
col.select('B.*').first().bandNames());
print('Match "B" followed by any character, and any optional third character',
col.select('B..?').first().bandNames());
print('Match "B" followed by a character in the range 6-8',
col.select('B[6-8]').first().bandNames());
print('Match "B" followed by a character in the range 1-9 and then 1-2',
col.select('B[1-9][1-2]').first().bandNames());
print('Match "B" or "QA" each followed by any character, any number of times.',
col.select('B.*|QA.*').first().bandNames());
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# A Sentinel-2 surface reflectance image collection.
col = ee.ImageCollection('COPERNICUS/S2_SR').filterBounds(
  ee.Geometry.Point(-122.152, 37.336)
  ).filterDate('2021-01-01', '2021-02-01')
print('All band names', col.first().bandNames().getInfo())
print('Select a band by name:',
   col.select('B11').first().bandNames().getInfo())
print('Select a band by index:',
   col.select(10).first().bandNames().getInfo())
print('Select bands using a list:',
   col.select(['B11', 'B8', 'B3']).first().bandNames().getInfo())
print('Select bands by an argument series:',
   col.select('B11', 'B8', 'B3').first().bandNames().getInfo())
print('Mixing string and integer selectors is valid:',
   col.select(10, 'B8', 2).first().bandNames().getInfo())
print('Rename selected bands using two corresponding lists:',
   col.select(['B11', 'B8', 'B3'], ['SWIR1', 'NIR', 'Green'])
   .first().bandNames().getInfo())
# Use regular expressions to select bands.
print('Match "QA" followed by any two characters:',
   col.select('QA..').first().bandNames().getInfo())
print('Match "B" followed by any character, any number of times:',
   col.select('B.*').first().bandNames().getInfo())
print('Match "B" followed by any character, and any optional third character:',
   col.select('B..?').first().bandNames().getInfo())
print('Match "B" followed by a character in the range 6-8:',
   col.select('B[6-8]').first().bandNames().getInfo())
print('Match "B" followed by a character in the range 1-9 and then 1-2:',
   col.select('B[1-9][1-2]').first().bandNames().getInfo())
print('Match "B" or "QA" each followed by any character, any number of times:',
   col.select('B.*|QA.*').first().bandNames().getInfo())
```

