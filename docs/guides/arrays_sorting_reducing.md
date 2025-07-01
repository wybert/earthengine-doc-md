 
#  Array Sorting and Reducing
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Array sorting is useful for obtaining custom quality mosaics which involve reducing a subset of image bands according to the values in a different band. The following example sorts by NDVI, then gets the mean of a subset of observations in the collection with the highest NDVI values:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/arrays_sorting_reducing#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/arrays_sorting_reducing#colab-python-sample) More
```
// Define a function that scales and masks Landsat 8 surface reflectance images
// and adds an NDVI band.
functionprepSrL8(image){
// Develop masks for unwanted pixels (fill, cloud, cloud shadow).
varqaMask=image.select('QA_PIXEL').bitwiseAnd(parseInt('11111',2)).eq(0);
varsaturationMask=image.select('QA_RADSAT').eq(0);
// Apply the scaling factors to the appropriate bands.
varopticalBands=image.select('SR_B.').multiply(0.0000275).add(-0.2);
varthermalBands=image.select('ST_B.*').multiply(0.00341802).add(149.0);
// Calculate NDVI.
varndvi=opticalBands.normalizedDifference(['SR_B5','SR_B4'])
.rename('NDVI');
// Replace original bands with scaled bands, add NDVI band, and apply masks.
returnimage.addBands(opticalBands,null,true)
.addBands(thermalBands,null,true)
.addBands(ndvi)
.updateMask(qaMask)
.updateMask(saturationMask);
}
// Define an arbitrary region of interest as a point.
varroi=ee.Geometry.Point(-122.26032,37.87187);
// Load a Landsat 8 surface reflectance collection.
varcollection=ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
// Filter to get only imagery at a point of interest.
.filterBounds(roi)
// Filter to get only six months of data.
.filterDate('2021-01-01','2021-07-01')
// Prepare images by mapping the prepSrL8 function over the collection.
.map(prepSrL8)
// Select the bands of interest to avoid taking up unneeded memory.
.select('SR_B.|NDVI');
// Convert the collection to an array.
vararray=collection.toArray();
// Label of the axes.
varimageAxis=0;
varbandAxis=1;
// Get the NDVI slice and the bands of interest.
varbandNames=collection.first().bandNames();
varbands=array.arraySlice(bandAxis,0,bandNames.length());
varndvi=array.arraySlice(bandAxis,-1);
// Sort by descending NDVI.
varsorted=bands.arraySort(ndvi.multiply(-1));
// Get the highest 20% NDVI observations per pixel.
varnumImages=sorted.arrayLength(imageAxis).multiply(0.2).int();
varhighestNdvi=sorted.arraySlice(imageAxis,0,numImages);
// Get the mean of the highest 20% NDVI observations by reducing
// along the image axis.
varmean=highestNdvi.arrayReduce({
reducer:ee.Reducer.mean(),
axes:[imageAxis]
});
// Turn the reduced array image into a multi-band image for display.
varmeanImage=mean.arrayProject([bandAxis]).arrayFlatten([bandNames]);
Map.centerObject(roi,12);
Map.addLayer(meanImage,{bands:['SR_B6','SR_B5','SR_B4'],min:0,max:0.4});
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Define a function that scales and masks Landsat 8 surface reflectance images
# and adds an NDVI band.
defprep_sr_l8(image):
 # Develop masks for unwanted pixels (fill, cloud, cloud shadow).
 qa_mask = image.select('QA_PIXEL').bitwiseAnd(int('11111', 2)).eq(0)
 saturation_mask = image.select('QA_RADSAT').eq(0)
 # Apply the scaling factors to the appropriate bands.
 optical_bands = image.select('SR_B.').multiply(0.0000275).add(-0.2)
 thermal_bands = image.select('ST_B.*').multiply(0.00341802).add(149.0)
 # Calculate NDVI.
 ndvi = optical_bands.normalizedDifference(['SR_B5', 'SR_B4']).rename('NDVI')
 # Replace the original bands with the scaled ones and apply the masks.
 return (
   image.addBands(optical_bands, None, True)
   .addBands(thermal_bands, None, True)
   .addBands(ndvi)
   .updateMask(qa_mask)
   .updateMask(saturation_mask)
 )

# Define an arbitrary region of interest as a point.
roi = ee.Geometry.Point(-122.26032, 37.87187)
# Load a Landsat 8 surface reflectance collection.
collection = (
  ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
  # Filter to get only imagery at a point of interest.
  .filterBounds(roi)
  # Filter to get only six months of data.
  .filterDate('2021-01-01', '2021-07-01')
  # Prepare images by mapping the prep_sr_l8 function over the collection.
  .map(prep_sr_l8)
  # Select the bands of interest to avoid taking up unneeded memory.
  .select('SR_B.|NDVI')
)
# Convert the collection to an array.
array = collection.toArray()
# Label of the axes.
image_axis = 0
band_axis = 1
# Get the NDVI slice and the bands of interest.
band_names = collection.first().bandNames()
bands = array.arraySlice(band_axis, 0, band_names.length())
ndvi = array.arraySlice(band_axis, -1)
# Sort by descending NDVI.
sorted = bands.arraySort(ndvi.multiply(-1))
# Get the highest 20% NDVI observations per pixel.
num_images = sorted.arrayLength(image_axis).multiply(0.2).int()
highest_ndvi = sorted.arraySlice(image_axis, 0, num_images)
# Get the mean of the highest 20% NDVI observations by reducing
# along the image axis.
mean = highest_ndvi.arrayReduce(reducer=ee.Reducer.mean(), axes=[image_axis])
# Turn the reduced array image into a multi-band image for display.
mean_image = mean.arrayProject([band_axis]).arrayFlatten([band_names])
m = geemap.Map()
m.center_object(roi, 12)
m.add_layer(
  mean_image, {'bands': ['SR_B6', 'SR_B5', 'SR_B4'], 'min': 0, 'max': 0.4}
)
m
```

As in the linear modeling example, separate the bands of interest from the sort index (NDVI) using `arraySlice()` along the band axis. Then sort the bands of interest by sort index using `arraySort()`. After the pixels have been sorted by descending NDVI, use `arraySlice()` along the `imageAxis` to get 20% of the highest NDVI pixels. Lastly, apply `arrayReduce()` along the `imageAxis` with a mean reducer to get the mean of the highest NDVI pixels. The final step converts the array image back to a multi-band image for display.
