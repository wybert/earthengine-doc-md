 
#  ee.Filter.eq
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-filter-eq#examples)


Filter to metadata equal to the given value. 
Returns the constructed filter.
Usage| Returns  
---|---  
`ee.Filter.eq(name, value)`| Filter  
Argument| Type| Details  
---|---|---  
`name`| String| The property name to filter on.  
`value`| Object| The value to compare against.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-filter-eq#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-filter-eq#colab-python-sample) More
```
// The GOES Mesoscale images come in two domains.
// Separate the two groups using ee.Filter.eq.
vargoes17_mcmipm=ee.ImageCollection('NOAA/GOES/17/MCMIPM');
vargoes17_mcmipm_2019=
goes17_mcmipm.filterDate(ee.Date('2019-11-01'),ee.Date('2019-11-05'));
vard1=goes17_mcmipm_2019.filter(ee.Filter.eq('domain',1));
vard2=goes17_mcmipm_2019.filter(ee.Filter.eq('domain',2));
print(goes17_mcmipm_2019.size());
print(d1.size());
print(d2.size());
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
goes17_mcmipm_2019 = goes17_mcmipm.filterDate(
  ee.Date('2019-11-01'), ee.Date('2019-11-05')
)
d1 = goes17_mcmipm_2019.filter(ee.Filter.eq('domain', 1))
d2 = goes17_mcmipm_2019.filter(ee.Filter.eq('domain', 2))
print(goes17_mcmipm_2019.size().getInfo())
print(d1.size().getInfo())
print(d2.size().getInfo())
```

Was this helpful?
