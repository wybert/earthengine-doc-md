 
#  Compositing, Masking, and Mosaicking 
Stay organized with collections  Save and categorize content based on your preferences. 
With the [Landsat 8 TOA reflectance collection](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC8_L1T_TOA) loaded into a variable called `l8`, you saw that the following code results in a recent-value composite:
### Code Editor (JavaScript)
```
varl8=ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA');
varlandsat2016=l8.filterDate('2016-01-01','2016-12-31');
Map.addLayer(landsat2016,visParams,'l8 collection');
```

One of the problems with this composite is that it's full of clouds. Instead of just taking the last pixel in the collection (when you add a collection to the map, Earth Engine implicitly calls [`mosaic()`](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-mosaic) on it), you can _reduce_ the `ImageCollection` ([Learn more about reducing image collections](https://developers.google.com/earth-engine/guides/reducers_image_collection)).
## Compositing with Reducers
You were first introduced to reducers for [getting statistics in an image region](https://developers.google.com/earth-engine/tutorials/tutorial_api_03#image-statistics). That was a _spatial_ reduction. Reducing an image collection to an image is a _temporal_ reduction when the collection represents images over time. The type of `Reducer` you use defines how Earth Engine handles overlapping pixels. Landsat 8 visits the same spot on the Earth every 16 days. That means that over a 6 month period, there will be approximately 12 images (and more where the scenes overlap). Each pixel on the map is derived from a stack of pixels - one from each image in the collection being displayed.
Merely adding the collection to the map results in selecting the most recent pixel - the one from the latest image in the stack. This behavior may be altered, using Earth Engine reducers. For example, rather than take the most recent pixel from the stack, Earth Engine can be instructed to pick the median value in the stack. This has the benefit of removing clouds (which have a high value) and shadows (which have a low value). When an image collection is reduced using the median reducer, the composite value is the median in each band, over time. For example, using Landsat scenes in 2016:
### Code Editor (JavaScript)
```
// Get the median over time, in each band, in each pixel.
varmedian=l8.filterDate('2016-01-01','2016-12-31').median();
// Make a handy variable of visualization parameters.
varvisParams={bands:['B4','B3','B2'],max:0.3};
// Display the median composite.
Map.addLayer(median,visParams,'median');
```

The new thing in this code is the `median()` method applied to an image collection. Like the filtering methods, this is a shortcut for the more general `reduce()` method on image collections which takes an `ee.Reducer()` as an argument. See the `ee.Reducer` package in the **Docs** tab of the Code Editor to see a list of all the Earth Engine reducers. When considering a reducer for an image collection, note that the output is an image, so reducers with non-numeric outputs, for example `histogram` or `toList` reducers, won't work with an image collection.
![Tutorial_api_06_median_composite](https://developers.google.com/static/earth-engine/images/Tutorial_api_06_median_composite.png) Figure 6. Landsat 8 median composite.
When you zoom out on the median composite, you should see something like Figure 6. This should look considerably better than the recent value composite you made previously. At this point, it's worth stepping back and considering what's been done to make that median composite. Earth Engine has loaded the entire Landsat 8 collection over the continental US, and has calculated the median for every pixel. That's a lot of data! Of course, you could compute annual medians, by first filtering the collection, [ as you've done previously](https://developers.google.com/earth-engine/tutorials/tutorial_api_04#filtering-image-collections). The point is that if you had to download all that imagery and make this composite, it would be a big project. With Earth Engine, you get a result in seconds!
Learn more about compositing and mosaicking [here](https://developers.google.com/earth-engine/guides/ic_composite_mosaic).
## Masking
Although the median composite is an improvement over the recent-value composite, you may want to mask parts of the image. Masking pixels in an image makes those pixels transparent and excludes them from analysis. Each pixel in each band of an image has a mask. Those with a mask value of 0 or below will be transparent. Those with a mask of any value above 0 will be rendered. The mask of an image is set using a call like `image1.mask(image2)`. This call takes the values of `image2` and makes them the mask of `image1`. Any pixels in `image2` that have the value 0 will be made transparent in `image1`.
For example, suppose you would like to mask all the water pixels in the median composite. A water mask can be created using the dataset described by [Hansen et al. (2013)](http://www.sciencemag.org/content/342/6160/850) which is in the Earth Engine data catalog. (Learn more about the Hansen et al. dataset in [this tutorial](https://developers.google.com/earth-engine/tutorials/tutorial_forest_01).) In this dataset, water has a value of 2, land has the value 1, and 'no data' has the value 0. Use a bit of logic to create a mask image that has zeros where there's no land:
### Code Editor (JavaScript)
```
// Load or import the Hansen et al. forest change dataset.
varhansenImage=ee.Image('UMD/hansen/global_forest_change_2015');
// Select the land/water mask.
vardatamask=hansenImage.select('datamask');
// Create a binary mask.
varmask=datamask.eq(1);
// Update the composite mask with the water mask.
varmaskedComposite=median.updateMask(mask);
Map.addLayer(maskedComposite,visParams,'masked');
```

There are a couple new things in this code that are worth mentioning in detail. First, the `select()` function is useful for extracting the bands of interest from an image. Here, we select only the band we care about: `datamask`. The next new thing is the logical operator `eq()` which stands for "equals." We use `eq(1)` to create a binary image in which all the pixels that do not have the value of 1 in the `datamask` band (those that are water or no data) get a value of 0 in the resulting image.
As a result of this masking, all the pixels in the median composite that are over land (according to the [Hansen et al. dataset](https://developers.google.com/earth-engine/datasets/catalog/UMD_hansen_global_forest_change_2015_v1_3)) are visible, but those over water (or nodata) are transparent and will be excluded from any analysis you do on the `maskedComposite` image.
## Mosaicking
By combining the concepts of image collections, logical operators, masking and compositing, you can achieve interesting cartographic results. For example, suppose you want an image in which land pixels are displayed in true-color and all the other pixels are displayed in blue, you can do something like:
### Code Editor (JavaScript)
```
// Make a water image out of the mask.
varwater=mask.not();
// Mask water with itself to mask all the zeros (non-water).
water=water.mask(water);
// Make an image collection of visualization images.
varmosaic=ee.ImageCollection([
median.visualize(visParams),
water.visualize({palette:'000044'}),
]).mosaic();
// Display the mosaic.
Map.addLayer(mosaic,{},'custom mosaic');
```

There's a lot going on in that code, so let's dissect it. First, we use the `not()` logical operator to invert the mask we made earlier. Specifically, `not()` turns all the zeros into ones and all the non-zeros into zeros. It's not completely correct to call that variable `water` because it includes some nodata pixels as well, but it's OK in the present cartographic context. The next thing is to mask the "water" with itself. This results in an image in which all the water pixels are 1's and everything else is masked. The final step is to combine the images with `mosaic()`. Since `mosaic()` works on an image collection, we pass a list of images that we want to combine into the image collection constructor, then call `mosaic()` as the final step. The order of the images in that list is important. Specifically, the output image will contain the last unmasked pixel from the stack of images in the input collection. In this case, that works because the water layer is the last (top) image in the collection, and only contains un-masked pixels where water occurs.
Note that the images in the collection are [visualization images](https://developers.google.com/earth-engine/guides/image_visualization#visualization-images). When you call [`visualize()`](https://developers.google.com/earth-engine/apidocs/ee-image-visualize) on an image, it gets turned into a 3-band, 8-bit image according to the visualization parameters you pass in. The default visualization parameters work fine for 3-band, 8-bit images, so you don't need visualization parameters when you add the image to the map. The result should look like Figure 7.
![Tutorial_api_07_mosaic.png](https://developers.google.com/static/earth-engine/images/Tutorial_api_07_mosaic.png) Figure 7. Custom mosaic that makes water areas a uniform color.
At this point, you've seen ways to visualize image collections as recent-value composites, methods for compositing image collections using reducers, and methods for making custom composites by masking and mosaicking a collection of images. In the next page, learn how to add a vegetation index to every image in a collection and use the index to make a "greenest pixel" composite.
[ arrow_backPrevious page](https://developers.google.com/earth-engine/tutorials/tutorial_api_04) [ Next pagearrow_forward](https://developers.google.com/earth-engine/tutorials/tutorial_api_06)
