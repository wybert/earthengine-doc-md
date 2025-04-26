 
#  ee.ImageCollection.filter 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-filter#examples)


Apply a filter to this collection. 
Returns the filtered collection.
Usage| Returns  
---|---  
`ImageCollection.filter(filter)`| Collection  
Argument| Type| Details  
---|---|---  
this: `collection`| Collection| The Collection instance.  
`filter`| Filter| A filter to apply to this collection.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-filter#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-filter#colab-python-sample) More
```
// The GOES Mesoscale images come in two domains.
// Separate the two groups using ee.Filter.eq.
vargoes17_mcmipm=ee.ImageCollection('NOAA/GOES/17/MCMIPM');
vargoes17_mcmipm_day=
goes17_mcmipm.filterDate('2020-09-26','2020-09-27');
vard1=goes17_mcmipm_day.filter('domain == 1');
vard2=goes17_mcmipm_day.filter('domain == 2');
// domain 3 does not exist.
vard3=goes17_mcmipm_day.filter('domain == 3');
print(goes17_mcmipm_day.size());
print(d1.size());
print(d2.size());
print(d3.size());
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# The GOES Mesoscale images come in two domains.
# Separate the two groups using ee.Filter.eq.
goes17_mcmipm = ee.ImageCollection('NOAA/GOES/17/MCMIPM')
goes17_mcmipm_day = goes17_mcmipm.filterDate('2020-09-26', '2020-09-27')
d1 = goes17_mcmipm_day.filter('domain == 1')
d2 = goes17_mcmipm_day.filter('domain == 2')
# domain 3 does not exist.
d3 = goes17_mcmipm_day.filter('domain == 3')
print(goes17_mcmipm_day.size().getInfo())
print(d1.size().getInfo())
print(d2.size().getInfo())
print(d3.size().getInfo())
```

