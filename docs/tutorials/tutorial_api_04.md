 
#  Image Collections
Stay organized with collections  Save and categorize content based on your preferences. 
An image collection refers to a set of Earth Engine images. For example, the collection of all Landsat 8 images is an `ee.ImageCollection`. Like the SRTM image you have been working with, image collections also have an ID. As with single images, you can discover the ID of an image collection by searching the [Earth Engine data catalog](https://developers.google.com/earth-engine/datasets) from the Code Editor and looking at the details page of the dataset. For example, search for 'landsat 8 toa' and click on the first result, which should correspond to the [ USGS Landsat 8 Collection 1 Tier 1 TOA Reflectance](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C01_T1_TOA) dataset. Either import that dataset using the **Import** button and rename it to `l8`, or copy the ID into the image collection constructor:
### Code Editor (JavaScript)
```
varl8=ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA');
```

## Filtering image collections
It's worth noting that this collection represents _every_ Landsat 8 scene collected, all over the Earth. Often it is useful to extract a single image, or subset of images, on which to test algorithms. The way to limit the collection by time or space is by filtering it. For example, to filter the collection to images that cover a particular location, first define your area of interest with a point (or line or polygon) using the geometry drawing tools. Pan to your area of interest, hover on the **Geometry Imports** (if you already have one or more geometries defined) and click **+new layer** (if you don't have any imports, go to the next step). Get the point drawing tool (![](https://developers.google.com/static/earth-engine/images/Playground_button_placemark.png)) and make a point in your area of interest. Name the import `point`. Now, filter the `l8` collection to get _only_ the images that intersect the point, then add a second filter to limit the collection to only the images that were acquired in 2015:
### Code Editor (JavaScript)
```
varspatialFiltered=l8.filterBounds(point);
print('spatialFiltered',spatialFiltered);

vartemporalFiltered=spatialFiltered.filterDate('2015-01-01','2015-12-31');
print('temporalFiltered',temporalFiltered);
```

Here, `filterBounds()` and `filterDate()` are shortcut methods for the more general `filter()` method on image collections, which takes an `ee.Filter()` as its argument. Explore the **Docs** tab of the Code Editor to learn more about these methods. The argument to `filterBounds()` is the point you digitized and the arguments to `filterDate()` are two dates, expressed as strings.
Note that you can `print()` the filtered collections. You can't print more than 5000 things at once, so you couldn't, for example, print the entire `l8` collection. After executing the `print()` method, you can inspect the printed collections in the console. Note that when you expand the `ImageCollection` using the zippy (![](https://code.earthengine.google.com/images/zippy-tab.svg)), then expand the list of `features`, you will see a list of images, each of which also can be expanded and inspected. This is one way to discover the ID of an individual image. Another, more programmatic way to get individual images for analysis is to sort the collection in order to get the most recent, oldest, or optimal image relative to some metadata property. For example, by inspecting the image objects in the printed image collections, you may have observed a metadata property called `CLOUD_COVER`. You can use that property to get the least cloudy image in 2015 in your area of interest: 
### Code Editor (JavaScript)
```
// This will sort from least to most cloudy.
varsorted=temporalFiltered.sort('CLOUD_COVER');

// Get the first (least cloudy) image.
varscene=sorted.first();
```

You're now ready to display the image!
## Digression: Displaying RGB images
When a multi-band image is added to a map, Earth Engine chooses the first three bands of the image and displays them as red, green, and blue by default, stretching them according to the data type, [as described previously](https://developers.google.com/earth-engine/tutorials/tutorial_api_02#digression-images-in-earth-engine). Usually, this won't do. For example, if you add the Landsat image (`scene` in the previous example) to the map, the result is unsatisfactory:
### Code Editor (JavaScript)
```
Map.centerObject(scene,9);
Map.addLayer(scene,{},'default RGB');
```

Note that first, the map is centered on the image at zoom scale 9. Then the image is displayed with an empty object (`{}`) for the `visParams` parameter (see the `Map.addLayer()` docs for details). As a result, the image is displayed with the default visualization: first three bands map to R, G, B, respectively, and stretched to [0, 1] since the bands are `float` data type. This means that the coastal aerosol band ('B1') is rendered in red, the blue band ('B2') is rendered in green, and the green band ('B3') is rendered in blue. To render the image as a true-color composite, you need to tell Earth Engine to use the Landsat 8 bands 'B4', 'B3', and 'B2' for R, G, and B, respectively. Specify which bands to use with the `bands` property of the `visParams` object. Learn more about Landsat bands at [this reference](https://www.usgs.gov/faqs/what-are-band-designations-landsat-satellites).
You also need to provide `min` and `max` values suitable for displaying reflectance from typical Earth surface targets. Although lists can be used to specify different values for each band, here it's sufficient to specify `0.3` as `max` and use the default value of zero for the `min` parameter. Combining the visualization parameters into one object and displaying:
### Code Editor (JavaScript)
```
varvisParams={bands:['B4','B3','B2'],max:0.3};
Map.addLayer(scene,visParams,'true-color composite');
```

The result should look something like Figure 5. Note that this code assigns the object of visualization parameters to a variable for possible future use. As you'll soon discover, that object will be useful when you visualize image collections!
![Tutorial_api_05_true_color.png](https://developers.google.com/static/earth-engine/images/Tutorial_api_05_true_color.png) Figure 5. Landsat 8 TOA reflectance image as a true-color composite, stretched to [0, 0.3].
Try playing with visualizing different bands. Another favorite combination is 'B5', 'B4', and 'B3' which is called a false-color composite. Some other interesting false-color composites are described [here](https://www.usgs.gov/media/images/common-landsat-band-rgb-composites).
Since Earth Engine is designed to do large-scale analyses, you are not limited to working with just one scene. Now it's time to display a whole collection as an RGB composite!
## Displaying image collections
Adding an image collection to a map is similar to adding an image to a map. For example, using 2016 images in the `l8` collection and the `visParams` object defined previously,
### Code Editor (JavaScript)
```
varl8=ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA');
varlandsat2016=l8.filterDate('2016-01-01','2016-12-31');
Map.addLayer(landsat2016,visParams,'l8 collection');
```

Note that now you can zoom out and see a continuous mosaic where Landsat imagery is collected (i.e. over land). Also note that when you use the **Inspector** tab and click on the image, you'll see a list of pixel values (or a chart) in the **Pixels** section and a list of image objects in the **Objects** section of the inspector.
If you zoomed out enough, you probably noticed some clouds in the mosaic. When you add an `ImageCollection` to the map, it is displayed as a recent-value composite, meaning that only the most recent pixels are displayed (like calling `mosaic()` on the collection). That is why you can see discontinuities between [paths](http://landsat.gsfc.nasa.gov/?p=3231) which were acquired at different times. It's also why many areas may appear cloudy. In the next page, learn how to change the way the images are composited to get rid of those pesky clouds!
[ arrow_backPrevious page](https://developers.google.com/earth-engine/tutorials/tutorial_api_03) [ Next pagearrow_forward](https://developers.google.com/earth-engine/tutorials/tutorial_api_05)
