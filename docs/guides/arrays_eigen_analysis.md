 
#  Eigen Analysis 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
The [principal components (PC) transform](http://en.wikipedia.org/wiki/Principal_component_analysis) (also known as the Karhunen-Loeve transform) is a spectral rotation that takes spectrally correlated image data and outputs uncorrelated data. The PC transform accomplishes this by diagonalizing the input band correlation matrix through Eigen-analysis. To do this in Earth Engine, use a covariance reducer on an array image and the `eigen()` command on the resultant covariance array. Consider the following function for that purpose (an example of it in application is available as a [Code Editor script](https://code.earthengine.google.com/30c0e509da3a644fc4fea031b7649f87) and a [Colab notebook](https://github.com/google/earthengine-community/blob/master/guides/linked/Earth_Engine_PCA.ipynb)).
### Code Editor (JavaScript)
```
vargetPrincipalComponents=function(centered,scale,region){
// Collapse the bands of the image into a 1D array per pixel.
vararrays=centered.toArray();
// Compute the covariance of the bands within the region.
varcovar=arrays.reduceRegion({
reducer:ee.Reducer.centeredCovariance(),
geometry:region,
scale:scale,
maxPixels:1e9
});
// Get the 'array' covariance result and cast to an array.
// This represents the band-to-band covariance within the region.
varcovarArray=ee.Array(covar.get('array'));
// Perform an eigen analysis and slice apart the values and vectors.
vareigens=covarArray.eigen();
// This is a P-length vector of Eigenvalues.
vareigenValues=eigens.slice(1,0,1);
// This is a PxP matrix with eigenvectors in rows.
vareigenVectors=eigens.slice(1,1);
// Convert the array image to 2D arrays for matrix computations.
vararrayImage=arrays.toArray(1);
// Left multiply the image array by the matrix of eigenvectors.
varprincipalComponents=ee.Image(eigenVectors).matrixMultiply(arrayImage);
// Turn the square roots of the Eigenvalues into a P-band image.
varsdImage=ee.Image(eigenValues.sqrt())
.arrayProject([0]).arrayFlatten([getNewBandNames('sd')]);
// Turn the PCs into a P-band image, normalized by SD.
returnprincipalComponents
// Throw out an an unneeded dimension, [[]] -> [].
.arrayProject([0])
// Make the one band array image a multi-band image, [] -> image.
.arrayFlatten([getNewBandNames('pc')])
// Normalize the PCs by their SDs.
.divide(sdImage);
};
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
defget_principal_components(centered, scale, region):
 # Collapse bands into 1D array
 arrays = centered.toArray()
 # Compute the covariance of the bands within the region.
 covar = arrays.reduceRegion(
   reducer=ee.Reducer.centeredCovariance(),
   geometry=region,
   scale=scale,
   maxPixels=1e9,
 )
 # Get the 'array' covariance result and cast to an array.
 # This represents the band-to-band covariance within the region.
 covar_array = ee.Array(covar.get('array'))
 # Perform an eigen analysis and slice apart the values and vectors.
 eigens = covar_array.eigen()
 # This is a P-length vector of Eigenvalues.
 eigen_values = eigens.slice(1, 0, 1)
 # This is a PxP matrix with eigenvectors in rows.
 eigen_vectors = eigens.slice(1, 1)
 # Convert the array image to 2D arrays for matrix computations.
 array_image = arrays.toArray(1)
 # Left multiply the image array by the matrix of eigenvectors.
 principal_components = ee.Image(eigen_vectors).matrixMultiply(array_image)
 # Turn the square roots of the Eigenvalues into a P-band image.
 sd_image = (
   ee.Image(eigen_values.sqrt())
   .arrayProject([0])
   .arrayFlatten([get_new_band_names('sd')])
 )
 # Turn the PCs into a P-band image, normalized by SD.
 return (
   # Throw out an an unneeded dimension, [[]] -> [].
   principal_components.arrayProject([0])
   # Make the one band array image a multi-band image, [] -> image.
   .arrayFlatten([get_new_band_names('pc')])
   # Normalize the PCs by their SDs.
   .divide(sd_image)
 )
```

The input to the function is a mean zero image, a scale and a region over which to perform the analysis. Note that the input imagery first needs to be converted to a 1-D array image and then reduced using `ee.Reducer.centeredCovariance()`. The array returned by this reduction is the symmetric variance-covariance matrix of the input. Use the `eigen()` command to get the eigenvalues and eigenvectors of the covariance matrix. The matrix returned by `eigen()` contains the eigenvalues in the 0-th position of the 1-axis. As shown in the earlier function, use `slice()` to separate the eigenvalues and the eigenvectors. Each element along the 0-axis of the eigenVectors matrix is an eigenvector. As in the [tasseled cap (TC) example](https://developers.google.com/earth-engine/guides/arrays_array_images), perform the transformation by matrix multiplying the `arrayImage` by the eigenvectors. In this example, each eigenvector multiplication results in a PC.
