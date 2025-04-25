 
#  ee.FeatureCollection.kriging 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-kriging#examples)


Returns the results of sampling a Kriging estimator at each pixel. 
Usage| Returns  
---|---  
`FeatureCollection.kriging(propertyName, shape, range, sill, nugget,  _maxDistance_, _reducer_)`| Image  
Argument| Type| Details  
---|---|---  
this: `collection`| FeatureCollection| Feature collection to use as source data for the estimation.  
`propertyName`| String| Property to be estimated (must be numeric).  
`shape`| String| Semivariogram shape (one of {exponential, gaussian, spherical}).  
`range`| Float| Semivariogram range, in meters.  
`sill`| Float| Semivariogram sill.  
`nugget`| Float| Semivariogram nugget.  
`maxDistance`| Float, default: null| Radius which determines which features are included in each pixel's computation, in meters. Defaults to the semivariogram's range.  
`reducer`| Reducer, default: null| Reducer used to collapse the 'propertyName' value of overlapping points into a single value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-kriging#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-kriging#colab-python-sample) More
```
/**
 * This example generates an interpolated surface using kriging from a
 * FeatureCollection of random points that simulates a table of air temperature
 * at ocean weather buoys.
 */
// Average air temperature at 2m height for June, 2020.
varimg=ee.Image('ECMWF/ERA5/MONTHLY/202006')
.select(['mean_2m_air_temperature'],['tmean']);
// Region of interest: South Pacific Ocean.
varroi=ee.Geometry.Polygon(
[[[-156.053,-16.240],
[-156.053,-44.968],
[-118.633,-44.968],
[-118.633,-16.240]]],null,false);
// Sample the mean June 2020 temperature surface at random points in the ROI.
vartmeanFc=img.sample(
{region:roi,scale:25000,numPixels:50,geometries:true});//250
// Generate an interpolated surface from the points using kriging; parameters
// are set according to interpretation of an unshown semivariogram. See section
// 2.1 of https://doi.org/10.14214/sf.369 for information on semivariograms.
vartmeanImg=tmeanFc.kriging({
propertyName:'tmean',
shape:'gaussian',
range:2.8e6,
sill:164,
nugget:0.05,
maxDistance:1.8e6,
reducer:ee.Reducer.mean()
});
// Display the results on the map.
Map.setCenter(-137.47,-30.47,3);
Map.addLayer(tmeanImg,{min:279,max:300},'Temperature (K)');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# This example generates an interpolated surface using kriging from a
# FeatureCollection of random points that simulates a table of air temperature
# at ocean weather buoys.
# Average air temperature at 2m height for June, 2020.
img = ee.Image('ECMWF/ERA5/MONTHLY/202006').select(
  ['mean_2m_air_temperature'], ['tmean']
)
# Region of interest: South Pacific Ocean.
roi = ee.Geometry.Polygon(
  [[
    [-156.053, -16.240],
    [-156.053, -44.968],
    [-118.633, -44.968],
    [-118.633, -16.240],
  ]],
  None,
  False,
)
# Sample the mean June 2020 temperature surface at random points in the ROI.
tmean_fc = img.sample(region=roi, scale=25000, numPixels=50, geometries=True)
# Generate an interpolated surface from the points using kriging parameters
# are set according to interpretation of an unshown semivariogram. See section
# 2.1 of https://doi.org/10.14214/sf.369 for information on semivariograms.
tmean_img = tmean_fc.kriging(
  propertyName='tmean',
  shape='gaussian',
  range=2.8e6,
  sill=164,
  nugget=0.05,
  maxDistance=1.8e6,
  reducer=ee.Reducer.mean(),
)
# Display the results on the map.
m = geemap.Map()
m.set_center(-137.47, -30.47, 3)
m.add_layer(
  tmean_img,
  {'min': 279, 'max': 300, 'min': 279, 'max': 300},
  'Temperature (K)',
)
m
```

