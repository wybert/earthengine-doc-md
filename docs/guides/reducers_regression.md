 
#  Linear Regression 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [ee.ImageCollection](https://developers.google.com/earth-engine/guides/reducers_regression#eeimagecollection)
    * [linearFit()](https://developers.google.com/earth-engine/guides/reducers_regression#linearfit)
    * [linearRegression()](https://developers.google.com/earth-engine/guides/reducers_regression#linearregression)
  * [ee.Image](https://developers.google.com/earth-engine/guides/reducers_regression#eeimage)
    * [linearFit()](https://developers.google.com/earth-engine/guides/reducers_regression#linearfit_2)
    * [linearRegression()](https://developers.google.com/earth-engine/guides/reducers_regression#linearregression_2)
  * [ee.FeatureCollection](https://developers.google.com/earth-engine/guides/reducers_regression#eefeaturecollection)
  * [ee.List](https://developers.google.com/earth-engine/guides/reducers_regression#eelist)
    * [linearFit()](https://developers.google.com/earth-engine/guides/reducers_regression#linearfit_3)
    * [linearRegression()](https://developers.google.com/earth-engine/guides/reducers_regression#linearregression_3)


Earth Engine has several methods for performing linear regression using reducers:
  * `ee.Reducer.linearFit()`
  * `ee.Reducer.linearRegression()`
  * `ee.Reducer.robustLinearRegression()`
  * `ee.Reducer.ridgeRegression()`


The simplest linear regression reducer is `linearFit()` which computes the least squares estimate of a linear function of one variable with a constant term. For a more flexible approach to linear modelling, use one of the linear regression reducers which allow for a variable number of independent and dependent variables. `linearRegression()` implements ordinary least squares regression(OLS). `robustLinearRegression()` uses a cost function based on regression residuals to iteratively de-weight outliers in the data ([O’Leary, 1990](http://epubs.siam.org/doi/abs/10.1137/0611032)). `ridgeRegression()` does linear regression with L2 regularization.
Regression analysis with these methods is suitable for reducing `ee.ImageCollection`, `ee.Image`, `ee.FeatureCollection`, and `ee.List` objects. The following examples demonstrate an application for each. Note that `linearRegression()`, `robustLinearRegression()`, and `ridgeRegression()` all have the same input and output structures, but `linearFit()` expects a two-band input (X followed by Y) and `ridgeRegression()` has an additional parameter (`lambda`, _optional_) and output (`pValue`).
**Note:** [`matrixSolve()`](https://developers.google.com/earth-engine/apidocs/ee-image-matrixsolve) provides an alternative method for least squares regression that is not implemented as an `ee.Reducer`.
## ee.ImageCollection
### `linearFit()`
The data should be set up as a two-band input image, where the first band is the independent variable and the second band is the dependent variable. The following example shows estimation of the linear trend of future precipitation (after 2006 in the [NEX-DCP30 data](https://developers.google.com/earth-engine/guides/earth-engine/datasets/catalog/NASA_NEX-DCP30)) projected by climate models. The dependent variable is projected precipitation and the independent variable is time, added prior to calling `linearFit()`:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/reducers_regression#code-editor-javascript-sample) More
```
// This function adds a time band to the image.
varcreateTimeBand=function(image){
// Scale milliseconds by a large constant to avoid very small slopes
// in the linear regression output.
returnimage.addBands(image.metadata('system:time_start').divide(1e18));
};
// Load the input image collection: projected climate data.
varcollection=ee.ImageCollection('NASA/NEX-DCP30_ENSEMBLE_STATS')
.filter(ee.Filter.eq('scenario','rcp85'))
.filterDate(ee.Date('2006-01-01'),ee.Date('2050-01-01'))
// Map the time band function over the collection.
.map(createTimeBand);
// Reduce the collection with the linear fit reducer.
// Independent variable are followed by dependent variables.
varlinearFit=collection.select(['system:time_start','pr_mean'])
.reduce(ee.Reducer.linearFit());
// Display the results.
Map.setCenter(-100.11,40.38,5);
Map.addLayer(linearFit,
{min:0,max:[-0.9,8e-5,1],bands:['scale','offset','scale']},'fit');
```

Observe that the output contains two bands, the ‘offset’ (intercept) and the ‘scale’ ('scale' in this context refers to the slope of the line and is not to be confused with the scale parameter input to many reducers, which is the spatial scale). The result, with areas of increasing trend in blue, decreasing trend in red and no trend in green should look something like Figure 1.
![](https://developers.google.com/static/earth-engine/images/Reducers_linearFit.png) Figure 1. The output of `linearFit()` applied to projected precipitation. Areas projected to be increased precipitation are shown in blue and decreased precipitation in red.
### `linearRegression()`
For example, suppose there are two dependent variables: precipitation and maximum temperature, and two independent variables: a constant and time. The collection is identical to the previous example, but the constant band must be manually added prior to the reduction. The first two bands of the input are the ‘X’ (independent) variables and the next two bands are the ‘Y’ (dependent) variables. In this example, first get the regression coefficients, then flatten the array image to extract the bands of interest:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/reducers_regression#code-editor-javascript-sample) More
```
// This function adds a time band to the image.
varcreateTimeBand=function(image){
// Scale milliseconds by a large constant.
returnimage.addBands(image.metadata('system:time_start').divide(1e18));
};
// This function adds a constant band to the image.
varcreateConstantBand=function(image){
returnee.Image(1).addBands(image);
};
// Load the input image collection: projected climate data.
varcollection=ee.ImageCollection('NASA/NEX-DCP30_ENSEMBLE_STATS')
.filterDate(ee.Date('2006-01-01'),ee.Date('2099-01-01'))
.filter(ee.Filter.eq('scenario','rcp85'))
// Map the functions over the collection, to get constant and time bands.
.map(createTimeBand)
.map(createConstantBand)
// Select the predictors and the responses.
.select(['constant','system:time_start','pr_mean','tasmax_mean']);
// Compute ordinary least squares regression coefficients.
varlinearRegression=collection.reduce(
ee.Reducer.linearRegression({
numX:2,
numY:2
}));
// Compute robust linear regression coefficients.
varrobustLinearRegression=collection.reduce(
ee.Reducer.robustLinearRegression({
numX:2,
numY:2
}));
// The results are array images that must be flattened for display.
// These lists label the information along each axis of the arrays.
varbandNames=[['constant','time'],// 0-axis variation.
['precip','temp']];// 1-axis variation.
// Flatten the array images to get multi-band images according to the labels.
varlrImage=linearRegression.select(['coefficients']).arrayFlatten(bandNames);
varrlrImage=robustLinearRegression.select(['coefficients']).arrayFlatten(bandNames);
// Display the OLS results.
Map.setCenter(-100.11,40.38,5);
Map.addLayer(lrImage,
{min:0,max:[-0.9,8e-5,1],bands:['time_precip','constant_precip','time_precip']},'OLS');
// Compare the results at a specific point:
print('OLS estimates:',lrImage.reduceRegion({
reducer:ee.Reducer.first(),
geometry:ee.Geometry.Point([-96.0,41.0]),
scale:1000
}));
print('Robust estimates:',rlrImage.reduceRegion({
reducer:ee.Reducer.first(),
geometry:ee.Geometry.Point([-96.0,41.0]),
scale:1000
}));
```

Inspect the results to discover that `linearRegression()` output is equivalent to the coefficients estimated by the `linearFit()` reducer, though the `linearRegression()` output also has coefficients for the other dependent variable, `tasmax_mean`. Robust linear regression coefficients are different from the OLS estimates. The example compares the coefficients from the different regression methods at a specific point.
## ee.Image
In the context of an `ee.Image` object, regression reducers can be used with `reduceRegion` or `reduceRegions` to perform linear regression on the pixels in the region(s). The following examples demonstrate how to calculate regression coefficients between Landsat bands in an arbitrary polygon.
### `linearFit()`
The guide section describing [array data charts](https://developers.google.com/earth-engine/guides/charts_array_values) shows a scatter plot of the correlation between Landsat 8 SWIR1 and SWIR2 bands. Here, the linear regression coefficients for this relationship are calculated. A dictionary containing the properties `'offset'` (y-intercept) and `'scale'` (slope) are returned.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/reducers_regression#code-editor-javascript-sample) More
```
// Define a rectangle geometry around San Francisco.
varsanFrancisco=ee.Geometry.Rectangle([-122.45,37.74,-122.4,37.8]);
// Import a Landsat 8 TOA image for this region.
varimg=ee.Image('LANDSAT/LC08/C02/T1_TOA/LC08_044034_20140318');
// Subset the SWIR1 and SWIR2 bands. In the regression reducer, independent
// variables come first followed by the dependent variables. In this case,
// B5 (SWIR1) is the independent variable and B6 (SWIR2) is the dependent
// variable.
varimgRegress=img.select(['B5','B6']);
// Calculate regression coefficients for the set of pixels intersecting the
// above defined region using reduceRegion with ee.Reducer.linearFit().
varlinearFit=imgRegress.reduceRegion({
reducer:ee.Reducer.linearFit(),
geometry:sanFrancisco,
scale:30,
});
// Inspect the results.
print('OLS estimates:',linearFit);
print('y-intercept:',linearFit.get('offset'));
print('Slope:',linearFit.get('scale'));
```

### `linearRegression()`
The same analysis from the previous `linearFit` section is applied here, except this time the `ee.Reducer.linearRegression` function is used. Note that a regression image is constructed from three separate images: a constant image and images representing SWIR1 and SWIR2 bands from the same Landsat 8 image. Keep in mind that you can combine any set of bands to construct an input image for region reduction by `ee.Reducer.linearRegression`, they do not have to belong to the same source image.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/reducers_regression#code-editor-javascript-sample) More
```
// Define a rectangle geometry around San Francisco.
varsanFrancisco=ee.Geometry.Rectangle([-122.45,37.74,-122.4,37.8]);
// Import a Landsat 8 TOA image for this region.
varimg=ee.Image('LANDSAT/LC08/C02/T1_TOA/LC08_044034_20140318');
// Create a new image that is the concatenation of three images: a constant,
// the SWIR1 band, and the SWIR2 band.
varconstant=ee.Image(1);
varxVar=img.select('B5');
varyVar=img.select('B6');
varimgRegress=ee.Image.cat(constant,xVar,yVar);
// Calculate regression coefficients for the set of pixels intersecting the
// above defined region using reduceRegion. The numX parameter is set as 2
// because the constant and the SWIR1 bands are independent variables and they
// are the first two bands in the stack; numY is set as 1 because there is only
// one dependent variable (SWIR2) and it follows as band three in the stack.
varlinearRegression=imgRegress.reduceRegion({
reducer:ee.Reducer.linearRegression({
numX:2,
numY:1
}),
geometry:sanFrancisco,
scale:30,
});
// Convert the coefficients array to a list.
varcoefList=ee.Array(linearRegression.get('coefficients')).toList();
// Extract the y-intercept and slope.
varb0=ee.List(coefList.get(0)).get(0);// y-intercept
varb1=ee.List(coefList.get(1)).get(0);// slope
// Extract the residuals.
varresiduals=ee.Array(linearRegression.get('residuals')).toList().get(0);
// Inspect the results.
print('OLS estimates',linearRegression);
print('y-intercept:',b0);
print('Slope:',b1);
print('Residuals:',residuals);
```

A dictionary containing properties `'coefficients'` and `'residuals'` are returned. The `'coefficients'` property is an array with dimensions (numX, numY); each column contains the coefficients for the corresponding dependent variable. In this case, the array has two rows and one column; row one, column one is the y-intercept and row two, column one is the slope. The `'residuals'` property is the vector of the root mean square of the residuals of each dependent variable. Extract the coefficients by casting the result as an array and then slicing out the desired elements or converting the array to a list and selecting coefficients by index position.
## ee.FeatureCollection
Suppose you want to know the linear relationship between Sentinel-2 and Landsat 8 SWIR1 reflectance. In this example, a random sample of pixels formatted as a feature collection of points are used to calculate the relationship. A scatter plot of the pixel pairs along with the least squares line of best fit are generated (Figure 2).
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/reducers_regression#code-editor-javascript-sample) More
```
// Import a Sentinel-2 TOA image.
vars2ImgSwir1=ee.Image('COPERNICUS/S2/20191022T185429_20191022T185427_T10SEH');
// Import a Landsat 8 TOA image from 12 days earlier than the S2 image.
varl8ImgSwir1=ee.Image('LANDSAT/LC08/C02/T1_TOA/LC08_044033_20191010');
// Get the intersection between the two images - the area of interest (aoi).
varaoi=s2ImgSwir1.geometry().intersection(l8ImgSwir1.geometry());
// Get a set of 1000 random points from within the aoi. A feature collection
// is returned.
varsample=ee.FeatureCollection.randomPoints({
region:aoi,
points:1000
});
// Combine the SWIR1 bands from each image into a single image.
varswir1Bands=s2ImgSwir1.select('B11')
.addBands(l8ImgSwir1.select('B6'))
.rename(['s2_swir1','l8_swir1']);
// Sample the SWIR1 bands using the sample point feature collection.
varimgSamp=swir1Bands.sampleRegions({
collection:sample,
scale:30
})
// Add a constant property to each feature to be used as an independent variable.
.map(function(feature){
returnfeature.set('constant',1);
});
// Compute linear regression coefficients. numX is 2 because
// there are two independent variables: 'constant' and 's2_swir1'. numY is 1
// because there is a single dependent variable: 'l8_swir1'. Cast the resulting
// object to an ee.Dictionary for easy access to the properties.
varlinearRegression=ee.Dictionary(imgSamp.reduceColumns({
reducer:ee.Reducer.linearRegression({
numX:2,
numY:1
}),
selectors:['constant','s2_swir1','l8_swir1']
}));
// Convert the coefficients array to a list.
varcoefList=ee.Array(linearRegression.get('coefficients')).toList();
// Extract the y-intercept and slope.
varyInt=ee.List(coefList.get(0)).get(0);// y-intercept
varslope=ee.List(coefList.get(1)).get(0);// slope
// Gather the SWIR1 values from the point sample into a list of lists.
varprops=ee.List(['s2_swir1','l8_swir1']);
varregressionVarsList=ee.List(imgSamp.reduceColumns({
reducer:ee.Reducer.toList().repeat(props.size()),
selectors:props
}).get('list'));
// Convert regression x and y variable lists to an array - used later as input
// to ui.Chart.array.values for generating a scatter plot.
varx=ee.Array(ee.List(regressionVarsList.get(0)));
vary1=ee.Array(ee.List(regressionVarsList.get(1)));
// Apply the line function defined by the slope and y-intercept of the
// regression to the x variable list to create an array that will represent
// the regression line in the scatter plot.
vary2=ee.Array(ee.List(regressionVarsList.get(0)).map(function(x){
vary=ee.Number(x).multiply(slope).add(yInt);
returny;
}));
// Concatenate the y variables (Landsat 8 SWIR1 and predicted y) into an array
// for input to ui.Chart.array.values for plotting a scatter plot.
varyArr=ee.Array.cat([y1,y2],1);
// Make a scatter plot of the two SWIR1 bands for the point sample and include
// the least squares line of best fit through the data.
print(ui.Chart.array.values({
array:yArr,
axis:0,
xLabels:x})
.setChartType('ScatterChart')
.setOptions({
legend:{position:'none'},
hAxis:{'title':'Sentinel-2 SWIR1'},
vAxis:{'title':'Landsat 8 SWIR1'},
series:{
0:{
pointSize:0.2,
dataOpacity:0.5,
},
1:{
pointSize:0,
lineWidth:2,
}
}
})
);
```

![](https://developers.google.com/static/earth-engine/images/Reducers_scatterplot.png) Figure 2. Scatter plot and least squares linear regression line for a sample of pixels representing Sentinel-2 and Landsat 8 SWIR1 TOA reflectance.
## ee.List
**Columns** of 2-D `ee.List` objects can be inputs to regression reducers. The following examples provide simple proofs; the independent variable is a copy of the dependent variable producing a y-intercept equal to 0 and a slope equal to 1.
**Note:** that the result of `ee.List` reduction is an object. Cast it to an `ee.Dictionary` to make accessing the properties easier.**Caution:** lengths among rows and columns must be equal. Use `null` to represent missing data entries.
### `linearFit()`
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/reducers_regression#code-editor-javascript-sample) More
```
// Define a list of lists, where columns represent variables. The first column
// is the independent variable and the second is the dependent variable.
varlistsVarColumns=ee.List([
[1,1],
[2,2],
[3,3],
[4,4],
[5,5]
]);
// Compute the least squares estimate of a linear function. Note that an
// object is returned; cast it as an ee.Dictionary to make accessing the
// coefficients easier.
varlinearFit=ee.Dictionary(listsVarColumns.reduce(ee.Reducer.linearFit()));
// Inspect the result.
print(linearFit);
print('y-intercept:',linearFit.get('offset'));
print('Slope:',linearFit.get('scale'));
```

**Transpose the list if variables are represented by rows** by converting to an `ee.Array`, transposing it, then converting back to an `ee.List`.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/reducers_regression#code-editor-javascript-sample) More
```
// If variables in the list are arranged as rows, you'll need to transpose it.
// Define a list of lists where rows represent variables. The first row is the
// independent variable and the second is the dependent variable.
varlistsVarRows=ee.List([
[1,2,3,4,5],
[1,2,3,4,5]
]);
// Cast the ee.List as an ee.Array, transpose it, and cast back to ee.List.
varlistsVarColumns=ee.Array(listsVarRows).transpose().toList();
// Compute the least squares estimate of a linear function. Note that an
// object is returned; cast it as an ee.Dictionary to make accessing the
// coefficients easier.
varlinearFit=ee.Dictionary(listsVarColumns.reduce(ee.Reducer.linearFit()));
// Inspect the result.
print(linearFit);
print('y-intercept:',linearFit.get('offset'));
print('Slope:',linearFit.get('scale'));
```

### `linearRegression()`
Application of `ee.Reducer.linearRegression()` is similar to the above [linearFit()](https://developers.google.com/earth-engine/guides/reducers_regression#linearfit_3) example, except that a constant independent variable is included.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/reducers_regression#code-editor-javascript-sample) More
```
// Define a list of lists where columns represent variables. The first column
// represents a constant term, the second an independent variable, and the third
// a dependent variable.
varlistsVarColumns=ee.List([
[1,1,1],
[1,2,2],
[1,3,3],
[1,4,4],
[1,5,5]
]);
// Compute ordinary least squares regression coefficients. numX is 2 because
// there is one constant term and an additional independent variable. numY is 1
// because there is only a single dependent variable. Cast the resulting
// object to an ee.Dictionary for easy access to the properties.
varlinearRegression=ee.Dictionary(
listsVarColumns.reduce(ee.Reducer.linearRegression({
numX:2,
numY:1
})));
// Convert the coefficients array to a list.
varcoefList=ee.Array(linearRegression.get('coefficients')).toList();
// Extract the y-intercept and slope.
varb0=ee.List(coefList.get(0)).get(0);// y-intercept
varb1=ee.List(coefList.get(1)).get(0);// slope
// Extract the residuals.
varresiduals=ee.Array(linearRegression.get('residuals')).toList().get(0);
// Inspect the results.
print('OLS estimates',linearRegression);
print('y-intercept:',b0);
print('Slope:',b1);
print('Residuals:',residuals);
```

