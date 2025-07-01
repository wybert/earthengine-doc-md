 
#  Debugging guide
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Syntax errors](https://developers.google.com/earth-engine/guides/debugging#syntax-errors)
  * [Client-side errors](https://developers.google.com/earth-engine/guides/debugging#client-side-errors)
    * [Unknown object type casting](https://developers.google.com/earth-engine/guides/debugging#unknown-object-type-casting)
    * [Avoid mixing client and server functions](https://developers.google.com/earth-engine/guides/debugging#avoid-mixing)
    * [JavaScript Code Editor browser lock](https://developers.google.com/earth-engine/guides/debugging#browser-lock)
  * [Server-side errors](https://developers.google.com/earth-engine/guides/debugging#server-side-errors)
    * [Immutability](https://developers.google.com/earth-engine/guides/debugging#immutability)
    * [Mapped functions](https://developers.google.com/earth-engine/guides/debugging#mapped-functions)
  * [Procedural errors](https://developers.google.com/earth-engine/guides/debugging#procedural-errors)
    * [Pattern was applied to an Image with no bands](https://developers.google.com/earth-engine/guides/debugging#no-bands)
  * [Scaling errors](https://developers.google.com/earth-engine/guides/debugging#scaling-errors)
    * [reduceRegion()](https://developers.google.com/earth-engine/guides/debugging#reduceregion)
    * [Computation timed out](https://developers.google.com/earth-engine/guides/debugging#timed-out)
    * [Too many concurrent aggregations](https://developers.google.com/earth-engine/guides/debugging#too-many)
    * [User memory limit exceeded](https://developers.google.com/earth-engine/guides/debugging#user-memory-limit-exceeded)
    * [Internal errors](https://developers.google.com/earth-engine/guides/debugging#internal-errors)
  * [Debugging methods](https://developers.google.com/earth-engine/guides/debugging#debugging-methods)
    * [Inspect variables and map layers](https://developers.google.com/earth-engine/guides/debugging#inspect-variables-and-map-layers)
    * [aside()](https://developers.google.com/earth-engine/guides/debugging#aside)
    * [Running a function on first()](https://developers.google.com/earth-engine/guides/debugging#running-a-function-on-first)
    * [Profiler](https://developers.google.com/earth-engine/guides/debugging#profiler)


Algorithms you create in Earth Engine run in the Google cloud, distributed over many computers. Debugging can be challenging because errors can occur either in the client-side code or the server-side execution of the coded instructions, and result from scaling problems as well as syntactic or logical errors. The bits of the program that are running somewhere in the cloud are not available to inspect, unless you ask for them. This document presents debugging strategies, tools and solutions to help you resolve common errors and debug Earth Engine scripts.
## Syntax errors
Syntax errors happen when your code breaks the rules of the programming language (either JavaScript or Python in Earth Engine). These errors prevent your code from running and are usually caught before execution. If you encounter a syntax error, carefully review the highlighted line or error message, and consult resources like the [Python Language Reference](https://docs.python.org/3/reference/index.html) or [ Google JavaScript Style Guide](https://google.github.io/styleguide/jsguide.html). A code linter can also help identify and fix these issues.
## Client-side errors
Despite syntactically correct code, there may be errors associated with the consistency or logic of the script. The following examples demonstrate errors from using a variable and method that don't exist.
Error — this code doesn't work!
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/debugging#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/debugging#colab-python-sample) More
```
// Load a Sentinel-2 image.
varimage=ee.Image('USGS/SRTMGL1_003');
// Error: "bandNames" is not defined in this scope.
vardisplay=image.visualize({bands:bandNames,min:0,max:9000});
// Error: image.selfAnalyze is not a function
varsilly=image.selfAnalyze();
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Load a Sentinel-2 image.
image = ee.Image('USGS/SRTMGL1_003')
# NameError: name 'band_names' is not defined.
display = image.visualize(bands=band_names, min=0, max=9000)
# AttributeError: 'Image' object has no attribute 'selfAnalyze'.
silly = image.selfAnalyze()
```

The first error informs you that the `bandNames` variable is not defined in the scope in which it's referenced. As a solution, set the variable, or provide a list argument for the `bands` parameter. The second error demonstrates what happens when the non-existent `selfAnalyze()` function is called. Since that isn't a real method on images, the error tells you it's not a function. In both cases, the error is descriptive of the problem.
### Unknown object type casting
The "`...is not a function`" error may result from Earth Engine not knowing the type of a variable. Common manifestations of this problem result from:
  * Doing something to an object returned by `first()` (the type of the elements in a collection is unknown).
  * Doing something to an object returned by `get()` (the type of element stored in a property is unknown).
  * Doing something to a function argument (in the function) when the type of the argument is unknown.


For an example of the former:
Error — this code doesn't work!
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/debugging#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/debugging#colab-python-sample) More
```
varcollection=ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017');
// Error: collection.first(...).area is not a function
vararea=collection.first().area();
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
collection = ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017')
# AttributeError: 'Element' object has no attribute 'area'.
area = collection.first().area()
```

The solution in all cases is to cast the object of unknown type with the constructor of the known type. Continuing the previous example, the solution is to cast to `ee.Feature`:
Solution — use a cast!
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/debugging#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/debugging#colab-python-sample) More
```
vararea=ee.Feature(collection.first()).area();
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
area = ee.Feature(collection.first()).area()
```

(It's worth noting that you can safely call any method on `Element` here because that's what Earth Engine thinks it is).
### Avoid mixing client and server functions
The following example is less obvious:
Error — this code doesn't do what you want
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/debugging#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/debugging#colab-python-sample) More
```
// Don't mix EE objects and JavaScript objects.
varimage=ee.Image('USGS/SRTMGL1_003');
varnonsense=image+2;
// You can print this, but it's not what you were hoping for.
print(nonsense);
// Error: g.eeObject.name is not a function
Map.addLayer(nonsense);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Don't mix EE objects and Python objects.
image = ee.Image('USGS/SRTMGL1_003')
nonsense = image + 2
# TypeError: unsupported operand type(s) for +: 'Image' and 'int'.
display(nonsense)
# TypeError: unsupported operand type(s) for +: 'Image' and 'int'.
m = geemap.Map()
m.add_layer(nonsense)
m
```

Supposing the author of this code intended to add `2` to every pixel in the image, this is not the right way to do it. Specifically, this code wrongly mixes a server-side object (`image`) with a client-side operator (`+`). The results may be surprising. In the first case, printing of `nonsense` in the JavaScript Code Editor will perform the requested operation (`+`) by converting both `image` and `2` to strings, then concatenating them. The resultant string is unintended (in Python a TypeError is thrown). In the second case, adding `nonsense` to the map, the cryptic `g.eeObject.name is not a function` error is displayed in the JavaScript Code Editor because the object being added to the map, `nonsense`, is a string, not an EE object (in Python a TypeError is thrown). To avoid possibly unintended results and uninformative errors, don't mix server objects and functions with client objects, primitives or functions. The solution is this example is to use a server function.
Solution — use a server function!
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/debugging#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/debugging#colab-python-sample) More
```
Map.addLayer(image.add(2));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
m = geemap.Map()
m.add_layer(image.add(2))
m
```

See the [Client versus Server](https://developers.google.com/earth-engine/guides/client_server) page for more details.
### JavaScript Code Editor browser lock
Browser freeze or lock can occur when JavaScript running in the client takes too long, or when waiting for something from Earth Engine. Two common sources of this error are for-loops and/or `getInfo()` in your JavaScript Code Editor code, with the worst-case scenario of `getInfo()` inside a for-loop. For-loops can cause the browser to lock because the code runs on your machine. On the other hand, `getInfo()` synchronously requests the result of a computation from Earth Engine, blocking until the result is received. If the computation takes a long time, the blocking could cause your browser to lock. Avoid both for-loops and `getInfo()` while working in the Code Editor. See the [Client versus Server](https://developers.google.com/earth-engine/guides/client_server) page for more details.
## Server-side errors
Despite logical consistency in the client code, there may be bugs which only become apparent at run time on the server. The following example demonstrates what happens when trying to get a band that doesn't exist.
Error — this code doesn't work!
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/debugging#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/debugging#colab-python-sample) More
```
// Load a Sentinel-2 image.
vars2image=ee.Image(
'COPERNICUS/S2_HARMONIZED/20160625T100617_20160625T170310_T33UVR');
// Error: Image.select: Pattern 'nonBand' did not match any bands.
print(s2image.select(['nonBand']));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Load a Sentinel-2 image.
s2image = ee.Image(
  'COPERNICUS/S2_HARMONIZED/20160625T100617_20160625T170310_T33UVR'
)
# EEException: Image.select: Band pattern 'non_band' did not match any bands.
print(s2image.select(['non_band']).getInfo())
```

In this example, the error informs you that there is no band named `nonBand`. The possibly obvious solution is to specify a band name that _does_ exist. You can discover the band names by printing the image and inspecting it in the console, or by printing the list of band names returned by `image.bandNames()`.
### Immutability
Server-side objects you create in Earth Engine are [_immutable_](https://en.wikipedia.org/wiki/Immutable_object). (Any `ee.Object` is a server side `Object`). That means that if you want to make a change to the object, you have to save the changed state into a new variable. For example, this won't work to set a property on the Sentinel-2 image:
Error — this code doesn't do what you want!
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/debugging#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/debugging#colab-python-sample) More
```
vars2image=ee.Image(
'COPERNICUS/S2_HARMONIZED/20160625T100617_20160625T170310_T33UVR');
s2image.set('myProperty','This image is not assigned to a variable');
// This will not result in an error, but will not find 'myProperty'.
print(s2image.get('myProperty'));// null
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
s2image = ee.Image(
  'COPERNICUS/S2_HARMONIZED/20160625T100617_20160625T170310_T33UVR'
)
s2image.set('my_property', 'This image is not assigned to a variable')
# This will not result in an error, but will not find 'my_property'.
display(s2image.get('my_property')) # None
```

In this example, `s2image.set()` returns a copy of the image with the new property, but the image stored in the `s2image` variable is unchanged. You need to save the image returned by `s2image.set()` in a new variable. For example:
Solution — capture the result in a variable!
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/debugging#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/debugging#colab-python-sample) More
```
s2image=s2image.set('myProperty','OK');
print(s2image.get('myProperty'));// OK
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
s2image = s2image.set('my_property', 'OK')
display(s2image.get('my_property')) # OK
```

### Mapped functions
Another context in which client and server functions don't mix is in mapped functions. Specifically, the operations specified by the mapped function run in the cloud, so client functions such as `getInfo` and `Export` (as well as `print` and method on `Map` and `Chart` in the JavaScript Code Editor) won't work in mapped functions. For example:
Error — this code doesn't work!
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/debugging#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/debugging#colab-python-sample) More
```
varcollection=ee.ImageCollection('MODIS/006/MOD44B');
// Error: A mapped function's arguments cannot be used in client-side operations
varbadMap3=collection.map(function(image){
print(image);
returnimage;
});
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
collection = ee.ImageCollection('MODIS/006/MOD44B')
# Error: A mapped function's arguments cannot be used in client-side operations.
bad_map_3 = collection.map(lambda image: print(image.getInfo()))
```

This somewhat cryptic error results from the process Earth Engine uses to turn this code into a set of instructions that can be run on Google servers. Client-side functions and control structures cannot be used to operate on the argument image passed to the mapped function. To avoid this error, avoid the use of client-side functions in mapped functions. See the [Client versus Server](https://developers.google.com/earth-engine/guides/client_server) page to learn more about the distinction between client and server functions.
Mapped functions have additional requirements. For example, mapped functions must return something:
Error — this code doesn't work!
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/debugging#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/debugging#colab-python-sample) More
```
varcollection=ee.ImageCollection('MODIS/006/MOD44B');
// Error: User-defined methods must return a value.
varbadMap1=collection.map(function(image){
// Do nothing.
});
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
collection = ee.ImageCollection('MODIS/006/MOD44B')
# Error: User-defined methods must return a value.
bad_map_1 = collection.map(lambda image: None)
```

The possibly obvious solution is to return something. But it can't return just any type of thing. Specifically, functions mapped over an `ImageCollection` or `FeatureCollection` must return an `Image` or `Feature`. For example, you can't return a date from a function mapped over an `ImageCollection`:
Error — this code doesn't work!
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/debugging#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/debugging#colab-python-sample) More
```
varcollection=ee.ImageCollection('MODIS/006/MOD44B');
varbadMap2=collection.map(function(image){
returnimage.date();
});
// Error: Collection.map: A mapped algorithm must return a Feature or Image.
print(badMap2);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
collection = ee.ImageCollection('MODIS/006/MOD44B')
bad_map_2 = collection.map(lambda image: image.date())
# EEException: Collection.map:
# A mapped algorithm must return a Feature or Image.
print(bad_map_2.getInfo())
```

To avoid this, return the input image with a new property set. Then, if you need a list of the dates of the images in the collection, you can use `aggregate_array()`:
Solution — set a property!
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/debugging#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/debugging#colab-python-sample) More
```
varcollection=ee.ImageCollection('MODIS/006/MOD44B');
varokMap2=collection.map(function(image){
returnimage.set('date',image.date());
});
print(okMap2);
// Get a list of the dates.
vardatesList=okMap2.aggregate_array('date');
print(datesList);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
collection = ee.ImageCollection('MODIS/006/MOD44B')
ok_map_2 = collection.map(lambda image: image.set('date', image.date()))
print(ok_map_2.getInfo())
# Get a list of the dates.
dates_list = ok_map_2.aggregate_array('date')
print(dates_list.getInfo())
```

## Procedural errors
### Pattern was applied to an Image with no bands
The `"Pattern 'my_band' was applied to an Image with no bands"` error means there is an `ee.Image.select()` call for an Image with an empty band list. Here's what you can do to address this:
  * If the image is produced from an ImageCollection with a reducer or using the `first()` or `toBands()` calls, make sure the source collection is not empty.
  * If the image is produced from a dictionary using `ee.Dictionary().toImage()`, make sure the dictionary is not empty.
  * If the image is standalone, make sure it has data (and isn't just `ee.Image(0)`).


## Scaling errors
Though a script may be syntactically correct, without logical errors, and represent a valid set of instructions for the server, in parallelizing and executing the computation, the resultant objects may be too big, too numerous, or take too long to compute. In this case, you will get an error indicating that the algorithm can't be scaled. These errors are generally the most difficult to diagnose and resolve. Examples of this type of error include:
  * Computation timed out
  * Too many concurrent aggregations
  * User memory limit exceeded
  * An internal error has occurred

**Warning:** Quota restrictions exist to ensure the availability of computing resources for the entire Earth Engine community. Attempting to circumvent quota restrictions through the use of multiple Google accounts is a violation of the [Earth Engine Terms of Service.](https://earthengine.google.com/terms/)
Improving the scaling of your code will let you get results faster, and also improve the availability of computing resources for all users. Each type of error is discussed in the following sections, following a brief aside about `reduceRegion()`, a commonly used function that is notorious for being able to cause every type of scaling error.
### `reduceRegion()`
Although `reduceRegion()` greedily consumes enough pixels to trigger an exciting variety of errors, there are also parameters intended to control the computation, so you can overcome the errors. For example, consider the following inadvisable reduction:
Error — this code doesn't work!
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/debugging#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/debugging#colab-python-sample) More
```
varabsurdComputation=ee.Image(1).reduceRegion({
reducer:'count',
geometry:ee.Geometry.Rectangle([-180,-90,180,90],null,false),
scale:100,
});
// Error: Image.reduceRegion: Too many pixels in the region.
//    Found 80300348117, but only 10000000 allowed.
print(absurdComputation);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
absurd_computation = ee.Image(1).reduceRegion(
  reducer='count',
  geometry=ee.Geometry.Rectangle([-180, -90, 180, 90], None, False),
  scale=100,
)
# EEException: Image.reduceRegion: Too many pixels in the region.
#    Found 80300348117, but only 10000000 allowed.
print(absurd_computation.getInfo())
```

This silly example is just for demonstration. The purpose of this error is to ask you whether you _really_ want to reduce 80300348117 (that's 80 _billion_) pixels. If not, increase the `scale` (pixel size in meters) accordingly, or set `bestEffort` to true, to recompute a larger scale automatically. See the [`reduceRegion()`](https://developers.google.com/earth-engine/guides/reducers_reduce_region) page for more details about these parameters.
### Computation timed out
Suppose you need all those pixels in your computation. If so, you can increase the `maxPixels` parameter to allow the computation to succeed. However, it's going to take Earth Engine some time to finish the computation. As a result, a "computation timed out" error might be thrown:
Bad — don't do this!
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/debugging#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/debugging#colab-python-sample) More
```
varridiculousComputation=ee.Image(1).reduceRegion({
reducer:'count',
geometry:ee.Geometry.Rectangle([-180,-90,180,90],null,false),
scale:100,
maxPixels:1e11
});
// Error: Computation timed out.
print(ridiculousComputation);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
ridiculous_computation = ee.Image(1).reduceRegion(
  reducer='count',
  geometry=ee.Geometry.Rectangle([-180, -90, 180, 90], None, False),
  scale=100,
  maxPixels=int(1e11),
)
# Error: Computation timed out.
print(ridiculous_computation.getInfo())
```

What this error means is that Earth Engine waited about five minutes before stopping the computation. Exporting allows Earth Engine to perform the computation in an environment with longer allowable running times (but _not_ more memory). As the return value from `reduceRegion()` is a dictionary, you can use the dictionary to set the properties of a feature with null geometry:
Good — use `Export`!
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/debugging#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/debugging#colab-python-sample) More
```
Export.table.toDrive({
collection:ee.FeatureCollection([
ee.Feature(null,ridiculousComputation)
]),
description:'ridiculousComputation',
fileFormat:'CSV'
});
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
task = ee.batch.Export.table.toDrive(
  collection=ee.FeatureCollection([ee.Feature(None, ridiculous_computation)]),
  description='ridiculous_computation',
  fileFormat='CSV',
)
# task.start()
```

### Too many concurrent aggregations
The "aggregations" part of this error refers to operations that are spread out over multiple machines (such as reductions that span more than one tile). Earth Engine has limits in place to prevent too many such aggregations from being run concurrently. In this example, the "Too many concurrent aggregations" error is triggered by a reduction within a map:
Bad — don't do this!
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/debugging#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/debugging#colab-python-sample) More
```
varcollection=ee.ImageCollection('LANDSAT/LT05/C02/T1')
.filterBounds(ee.Geometry.Point([-123,43]));
varterribleAggregations=collection.map(function(image){
returnimage.set(image.reduceRegion({
reducer:'mean',
geometry:image.geometry(),
scale:30,
maxPixels:1e9
}));
});
// Error: Quota exceeded: Too many concurrent aggregations.
print(terribleAggregations);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
collection = ee.ImageCollection('LANDSAT/LT05/C02/T1').filterBounds(
  ee.Geometry.Point([-123, 43])
)

defapply_mean_aggregation(image):
 return image.set(
   image.reduceRegion(
     reducer='mean',
     geometry=image.geometry(),
     scale=30,
     maxPixels=int(1e9),
   )
 )

terrible_aggregations = collection.map(apply_mean_aggregation)
# EEException: Computation timed out.
print(terrible_aggregations.getInfo())
```

Assuming that the purpose of this code is to get image statistics for each image, one possible solution is to `Export` the result. For example, using the fact that an `ImageCollection` is also a `FeatureCollection`, the metadata associated with the images can be exported as a table:
Good — use `Export`!
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/debugging#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/debugging#colab-python-sample) More
```
Export.table.toDrive({
collection:terribleAggregations,
description:'terribleAggregations',
fileFormat:'CSV'
});
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
task = ee.batch.Export.table.toDrive(
  collection=terrible_aggregations,
  description='terrible_aggregations',
  fileFormat='CSV',
)
# task.start()
```

### User memory limit exceeded
One way your algorithms get parallelized in Earth Engine is by splitting the inputs into tiles, running the same computation separately on each tile, then combining the results. As a consequence, all of the inputs necessary to compute an output tile have to fit into memory. For example, when the input is an image with many bands, that could end up taking a lot of memory if all the bands are used in the computation. To demonstrate, this example uses too much memory by forcing (unnecessarily) an entire image collection into a tile:
Bad — don't do this!
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/debugging#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/debugging#colab-python-sample) More
```
varbands=['B1','B2','B3','B4','B5','B6','B7'];
varmemoryHog=ee.ImageCollection('LANDSAT/LT05/C02/T1').select(bands)
.toArray()
.arrayReduce(ee.Reducer.mean(),[0])
.arrayProject([1])
.arrayFlatten([bands])
.reduceRegion({
reducer:'mean',
geometry:ee.Geometry.Point([-122.27,37.87]).buffer(1000),
scale:1,
bestEffort:true,
});
// Error: User memory limit exceeded.
print(memoryHog);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
bands = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7']
memory_hog = (
  ee.ImageCollection('LANDSAT/LT05/C02/T1')
  .select(bands)
  .toArray()
  .arrayReduce(ee.Reducer.mean(), [0])
  .arrayProject([1])
  .arrayFlatten([bands])
  .reduceRegion(
    reducer=ee.Reducer.mean(),
    geometry=ee.Geometry.Point([-122.27, 37.87]).buffer(1000),
    scale=1,
    bestEffort=True,
  )
)
# EEException: User memory limit exceeded.
print(memory_hog.getInfo())
```

This very bad code demonstrates one reason to not use arrays unless you really need to (see also the 'Avoid converting type unnecessarily' section). When that collection is converted to a gigantic array, the array has to be loaded into memory all at once. Because it's a long time series of images, the array is large and won't fit in memory.
One possible solution is to set the `tileScale` parameter to a higher value. Higher values of tileScale result in tiles smaller by a factor of `tileScale^2`. For example, the following allows the computation to succeed:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/debugging#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/debugging#colab-python-sample) More
```
varbands=['B1','B2','B3','B4','B5','B6','B7'];
varsmallerHog=ee.ImageCollection('LANDSAT/LT05/C02/T1').select(bands)
.toArray()
.arrayReduce(ee.Reducer.mean(),[0])
.arrayProject([1])
.arrayFlatten([bands])
.reduceRegion({
reducer:'mean',
geometry:ee.Geometry.Point([-122.27,37.87]).buffer(1000),
scale:1,
bestEffort:true,
tileScale:16
});
print(smallerHog);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
bands = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7']
smaller_hog = (
  ee.ImageCollection('LANDSAT/LT05/C02/T1')
  .select(bands)
  .toArray()
  .arrayReduce(ee.Reducer.mean(), [0])
  .arrayProject([1])
  .arrayFlatten([bands])
  .reduceRegion(
    reducer=ee.Reducer.mean(),
    geometry=ee.Geometry.Point([-122.27, 37.87]).buffer(1000),
    scale=1,
    bestEffort=True,
    tileScale=16,
  )
)
print(smaller_hog.getInfo())
```

However, the much preferred solution is to not use arrays unnecessarily, so you don't need to fiddle with `tileScale` at all:
Good — avoid Arrays!
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/debugging#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/debugging#colab-python-sample) More
```
varbands=['B1','B2','B3','B4','B5','B6','B7'];
varokMemory=ee.ImageCollection('LANDSAT/LT05/C02/T1').select(bands)
.mean()
.reduceRegion({
reducer:'mean',
geometry:ee.Geometry.Point([-122.27,37.87]).buffer(1000),
scale:1,
bestEffort:true,
});
print(okMemory);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
bands = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7']
ok_memory = (
  ee.ImageCollection('LANDSAT/LT05/C02/T1')
  .select(bands)
  .mean()
  .reduceRegion(
    reducer=ee.Reducer.mean(),
    geometry=ee.Geometry.Point([-122.27, 37.87]).buffer(1000),
    scale=1,
    bestEffort=True,
  )
)
print(ok_memory.getInfo())
```

Unless necessary to resolve a memory error, you shouldn't set `tileScale` as smaller tiles also result in larger parallelization overhead.
### Internal errors
You may encounter an error that looks like:
An internal error has occurred.
If you get this error, click the "Report error" link which appears in the JavaScript Code Editor console. You can also **