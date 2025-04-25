 
#  Beginner's Cookbook 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Introduction](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#introduction)
  * [Vector data](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#vector_data)
    * [Point data](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#point_data)
    * [Lines](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#lines)
    * [Polygons](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#polygons)
  * [Raster data](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#raster_data)
    * [Layers and bands](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#layers_and_bands)
  * [The Google Earth Engine platform](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#the_google_earth_engine_platform)
  * [Basic functions](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#basic_functions)
    * [Declaring variables](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#declaring_variables)
    * [Centering the map](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#centering_the_map)
    * [Displaying metadata](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#displaying_metadata)
    * [Adding a layer to the map](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#adding_a_layer_to_the_map)
  * [Common Earth Engine data types](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#common_earth_engine_data_types)
    * [Strings](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#strings)
    * [Numbers](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#numbers)
    * [Arrays](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#arrays)
    * [Lists](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#lists)
    * [Dictionaries](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#dictionaries)
    * [And the fun stuff...](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#and_the_fun_stuff)
  * [Declaring geometries](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#declaring_geometries)
    * [Points](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#points)
    * [Multi points](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#multi_points)
    * [Line string](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#line_string)
    * [Multi-line string](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#multi-line_string)
    * [Linear ring](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#linear_ring)
    * [Rectangle](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#rectangle)
    * [Polygon](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#polygon)
    * [Multi-polygon](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#multi-polygon)
  * [Features and FeatureCollections](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#features_and_featurecollections)
  * [Functions and mapping](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#functions_and_mapping)
    * [Calling a function](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#calling_a_function)
    * [Mapping a function over a collection](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#mapping_a_function_over_a_collection)
  * [Common operations on geometries](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#common_operations_on_geometries)
    * [Finding the area of a geometry](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#finding_the_area_of_a_geometry)
    * [Finding the length of a line](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#finding_the_length_of_a_line)
    * [Finding the perimeter of a geometry](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#finding_the_perimeter_of_a_geometry)
    * [Reducing number of vertices in geometry](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#reducing_number_of_vertices_in_geometry)
    * [Finding the centroid of a geometry](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#finding_the_centroid_of_a_geometry)
    * [Creating buffer around a geometry](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#creating_buffer_around_a_geometry)
    * [Finding the bounding rectangle of a geometry](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#finding_the_bounding_rectangle_of_a_geometry)
    * [Finding the smallest polygon that can envelope a geometry](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#finding_the_smallest_polygon_that_can_envelope_a_geometry)
    * [Finding common areas between two or more geometries](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#finding_common_areas_between_two_or_more_geometries)
    * [Finding the area that includes two or more geometries](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#finding_the_area_that_includes_two_or_more_geometries)
  * [Operations on features](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#operations_on_features)
    * [Creating a feature with a specific property value](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#creating_a_feature_with_a_specific_property_value)
    * [Creating a feature from an existing feature, renaming a property](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#creating_a_feature_from_an_existing_feature_renaming_a_property)
    * [Extracting values of a property from a Feature](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#extracting_values_of_a_property_from_a_feature)
  * [Filtering](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#filtering)
    * [Filtering by property values](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#filtering_by_property_values)
    * [Filtering based on maximum difference from a threshold](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#filtering_based_on_maximum_difference_from_a_threshold)
    * [Filtering by text property](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#filtering_by_text_property)
    * [Filtering by a value range](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#filtering_by_a_value_range)
    * [Filtering by specific property values](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#filtering_by_specific_property_values)
    * [Filtering by date range](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#filtering_by_date_range)
    * [Filtering by particular days of the year](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#filtering_by_particular_days_of_the_year)
    * [Filtering by a bounding area](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#filtering_by_a_bounding_area)
    * [Combining and inversing filters](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#combining_and_inversing_filters)
  * [Operations on images](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#operations_on_images)
    * [Selecting the bands of an image](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#selecting_the_bands_of_an_image)
    * [Creating masks](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#creating_masks)
    * [Applying image masks](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#applying_image_masks)
    * [Performing pixelwise calculations](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#performing_pixelwise_calculations)
    * [Shift pixels of an image](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#shift_pixels_of_an_image)
  * [Reducers](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#reducers)
    * [Reducing an image collection to an image](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#reducing_an_image_collection_to_an_image)
    * [Reducing an image to a statistic for an area of interest](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#reducing_an_image_to_a_statistic_for_an_area_of_interest)
    * [Applying a reducer to each element of a collection](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#applying_a_reducer_to_each_element_of_a_collection)
    * [Applying a reducer to the neighborhoods of each pixel](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#applying_a_reducer_to_the_neighborhoods_of_each_pixel)
    * [Applying a reducer to each element of an array pixel](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#applying_a_reducer_to_each_element_of_an_array_pixel)
    * [Convert the properties of a vector into a raster](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#convert_the_properties_of_a_vector_into_a_raster)
    * [Convert a raster into a vector](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#convert_a_raster_into_a_vector)
  * [Operations on image collections](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#operations_on_image_collections)
    * [Selecting the first n images in a collection (based on property)](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#selecting_the_first_n_images_in_a_collection_based_on_property)
    * [Selecting images based on particular properties](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#selecting_images_based_on_particular_properties)
    * [Selecting images within a date range](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#selecting_images_within_a_date_range)
    * [Selecting images within a bounding geometry](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#selecting_images_within_a_bounding_geometry)
    * [Performing pixelwise calculations for all images in a collection](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#performing_pixelwise_calculations_for_all_images_in_a_collection)
    * [Compositing images in collection with the last image on top](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#compositing_images_in_collection_with_the_last_image_on_top)
  * [Exporting data](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#exporting_data)
    * [Exporting a collection to Google Drive, Earth Engine Asset, or Google Cloud](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#exporting_a_collection_to_google_drive_earth_engine_asset_or_google_cloud)
  * [Bonus: Timelapse example](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#bonus_timelapse_example)
  * [Example applications](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#example_applications)
  * [Additional resources](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook#additional_resources)


[ Edit on GitHub ](https://github.com/google/earthengine-community/edit/master/tutorials/beginners-cookbook/index.md)
[ Report issue ](https://github.com/google/earthengine-community/issues/new?title=Issue%20with%20tutorials/beginners-cookbook/index.md&body=Issue%20Description)
[ Page history ](https://github.com/google/earthengine-community/commits/master/tutorials/beginners-cookbook/index.md)
Author(s): [ TC25 ](https://github.com/TC25)
Tutorials contributed by the Earth Engine developer community are not part of the official Earth Engine product documentation. 
In this tutorial, we will introduce several types of geospatial data, and enumerate key Earth Engine functions for analyzing and visualizing them. This cookbook was originally created as a workshop during Yale-NUS Data 2.0 hackathon, and later updated for Yale GIS Day 2018 and 2019. 
## Introduction
GIS or Geographic Information System is the collection, visualization, and analysis of geographical or spatial data. In this section, we will cover the data types commonly used in GIS applications.
## Vector data
Vector data represent objects on the Earth's surface using their longitude and latitude, as well as combinations of the pairs of coordinates (lines, polylines, polygons, etc.).
### Point data
A pair of coordinates (longitude, latitude), that represents the location of points on the Earth's surface.
Example: Location of drop boxes, landmarks, etc.
![Points](https://developers.google.com/static/earth-engine/tutorials/community/beginners-cookbook/points.png)
### Lines
A series of points that represents a line (straight or otherwise) on the Earth's surface.
Example: Center of roads, rivers, etc.
![Lines](https://developers.google.com/static/earth-engine/tutorials/community/beginners-cookbook/line-vector.png)
### Polygons
A series of points (vertices) that define the outer edge of a region. Example: Outlines of cities, countries, continents, etc.
![Polygons](https://developers.google.com/static/earth-engine/tutorials/community/beginners-cookbook/polygon-vector.png)
## Raster data
Raster data represent objects/variables on the Earth's surface as a matrix of values, in the form of pixels, cells, or grids.
### Layers and bands
A raster is an image with a matrix of values representing the values of some observed attribute. Bands of a raster correspond to different variables, usually using the same matrix structure.
Example: Spatial variability of temperature, elevation, rainfall, etc. over a region.
![Raster](https://developers.google.com/static/earth-engine/tutorials/community/beginners-cookbook/map-algebra.png)
Conceptual figures sourced from [GISGeography](https://gisgeography.com/spatial-data-types-vector-raster/)
## The Google Earth Engine platform
[Introductory video](https://www.youtube.com/watch?v=gKGOeTFHnKY&feature=youtu.be)
[Code editor](https://code.earthengine.google.com/)
What is Earth Engine?
  * A cloud-based platform for planetary scale geospatial analysis
  * Uses Google's computational resources to reduce processing time
  * A massive [archive](https://developers.google.com/earth-engine/datasets/catalog/) of remote sensing data


![The Earth Engine Code Editor \(source: developers.google.com\)](https://developers.google.com/static/earth-engine/tutorials/community/beginners-cookbook/ee-editor.png)
## Basic functions
### Declaring variables
```
varvariableName=ee.ContainerType(value);

```

A container object (usually in the form `ee.SomeVariableType`) is used to wrap a native JavaScript object so that Google's servers can perform operations on it.
### Centering the map
```
Map.setCenter(long,lat,zoomLevel);

```

> Zoom level varies from 0 (no zoom) to 20 (highest zoom level)
### Displaying metadata
```
print(variableName);

```

The `print` operation is also useful for printing data and getting debugging info. Note: You cannot print more than 5,000 elements at once.
### Adding a layer to the map
```
Map.addLayer(variableName);

```

## Common Earth Engine data types
### Strings
```
varstr=ee.String('This is a string. Or is it? It is.');

```

### Numbers
```
varnum=ee.Number(5);

```

### Arrays
```
vararr=ee.Array([[5,2,3],[-2,7,10],[6,6,9]]);

```

### Lists
```
varlis=ee.List([5,'five',6,'six']);

```

### Dictionaries
```
vardict=ee.Dictionary({five:5,six:6});

```

### And the fun stuff...
  * `ee.Geometry`
  * `ee.Feature`
  * `ee.FeatureCollection`
  * `ee.Image`
  * `ee.ImageCollection`


## Declaring geometries
### Points
```
varpoi=ee.Geometry.Point(0,45);

```

### Multi points
```
varmulti=ee.Geometry.MultiPoint(0,45,5,6,70,-56);

```

### Line string
```
varlineStr=ee.Geometry.LineString([[0,45],[5,6],[70,-56]]);

```

### Multi-line string
```
varmLineStr=
ee.Geometry.MultiLineString(
[[[0,45],[5,6],[70,-56]],[[0,-45],[-5,-6],[-70,56]]]);

```

### Linear ring
```
varlinRin=ee.Geometry.LinearRing(0,45,5,6,70,-56,0,45);

```

### Rectangle
```
varrect=ee.Geometry.Rectangle(0,0,60,30);

```

### Polygon
```
varpoly=ee.Geometry.Polygon([[[0,0],[6,3],[5,5],[-30,2],[0,0]]]);

```

### Multi-polygon
```
varmultiPoly=
ee.Geometry.MultiPolygon(
[ee.Geometry.Polygon([[0,0],[6,3],[5,5],[-30,2],[0,0]]),
ee.Geometry.Polygon([[0,0],[-6,-3],[-5,-5],[30,-2],[0,0]])]);

```

## Features and FeatureCollections
  * Features are geometries associated with specific properties.
  * Feature collections are groups of features.


![Counties in the contiguous United States](https://developers.google.com/static/earth-engine/tutorials/community/beginners-cookbook/county-features.png)
## Functions and mapping
A function is a set of instructions to perform a specific task:
```
functionfunctionName(Arguments){
statements;
};

```

### Calling a function
```
varresult=functionName(input);

```

### Mapping a function over a collection
```
varresult=input.map(functionName);

```

Mapping a function over a collection applies the function to every element in the collection.
## Common operations on geometries
### Finding the area of a geometry
```
vargeoArea=geometry.area(maxError);

```

By default, all units in Earth Engine are in meters.
### Finding the length of a line
```
varlinLen=lineString.length(maxError);

```

### Finding the perimeter of a geometry
```
vargeoPeri=geometry.perimeter(maxError);

```

### Reducing number of vertices in geometry
```
varsimpGeo=geometry.simplify(maxError);

```

### Finding the centroid of a geometry
```
varcentrGeo=geometry.centroid(maxError);

```

### Creating buffer around a geometry
```
varbuffGeo=geometry.buffer(radius,maxError);

```

### Finding the bounding rectangle of a geometry
```
varbounGeo=geometry.bounds(maxError);

```

### Finding the smallest polygon that can envelope a geometry
```
varconvexGeo=geometry.convexHull(maxError);

```

### Finding common areas between two or more geometries
```
varinterGeo=geometry1.intersection(geometry2,maxError);

```

### Finding the area that includes two or more geometries
```
varunGeo=geometry1.union(geometry2,maxError);

```

#### Example: Geometry operations
Let's run some these operations over the state of Connecticut, US using geometries of the public US counties feature collection available on Earth Engine:
**1.** We begin by zooming to the region of interest and loading/creating the geometries of interest by extracting them from the corresponding features.
```
// Set map center over the state of CT.
Map.setCenter(-72.6978,41.6798,8);
// Load US county dataset.
varcountyData=ee.FeatureCollection('TIGER/2018/Counties');
// Filter the counties that are in Connecticut (more on filters later).
varcountyConnect=countyData.filter(ee.Filter.eq('STATEFP','09'));
// Get the union of all the county geometries in Connecticut.
varcountyConnectDiss=countyConnect.union(100);
// Create a circular area using the first county in the Connecticut
// FeatureCollection.
varcircle=ee.Feature(countyConnect.first())
.geometry().centroid(100).buffer(50000,100);
// Add the layers to the map with a specified color and layer name.
Map.addLayer(countyConnectDiss,{color:'red'},'CT dissolved');
Map.addLayer(circle,{color:'orange'},'Circle');

```

**2.** Using the `bounds()` function, we can find the rectangle that emcompasses the southernmost, westernmost, easternmost, and northernmost points of the geometry.
```
varbound=countyConnectDiss.geometry().bounds(100);
// Add the layer to the map with a specified color and layer name.
Map.addLayer(bound,{color:'yellow'},'Bounds');

```

**3.** In the same vein, but not restricting ourselves to a rectangle, a convex hull (`convexHull()`) is a polygon covering the extremities of the geometry.
```
varconvex=countyConnectDiss.geometry().convexHull(100);
// Add the layer to the map with a specified color and layer name.
Map.addLayer(convex,{color:'blue'},'Convex Hull');

```

**4.** Moving on to some basic operations to combine multiple geometries, the intersection (`intersection()`) is the area common to two or more geometries.
```
varintersect=convex.intersection(circle,100);
// Add the layer to the map with a specified color and layer name.
Map.addLayer(intersect,{color:'green'},'Circle and convex intersection');

```

**5.** The union (`union()`) is the area encompassing two or more features.
```
// number is the maximum error in meters.
varunion=convex.union(circle,100);
// Add the layer to the map with a specified color and layer name.
Map.addLayer(union,{color:'purple'},'Circle and convex union');

```

**6.** We can also find the spatial difference (`difference()`) between two geometries.
```
vardiff=convex.difference(circle,100);
// Add the layer to the map with a specified color and layer name.
Map.addLayer(diff,{color:'brown'},'Circle and convex difference');

```

Difference | Union | Intersection  
---|---|---  
![](https://developers.google.com/static/earth-engine/tutorials/community/beginners-cookbook/difference.png) | ![](https://developers.google.com/static/earth-engine/tutorials/community/beginners-cookbook/union.png) | ![](https://developers.google.com/static/earth-engine/tutorials/community/beginners-cookbook/intersection.png)  
**7.** Finally, we can calculate and display the area, length, perimeter, etc. of our geometries.
```
// Find area of feature.
varar=countyConnectDiss.geometry().area(100);
print(ar);
// Find length of line geometry (You get zero since this is a polygon).
varlength=countyConnectDiss.geometry().length(100);
print(length);
// Find perimeter of feature.
varperi=countyConnectDiss.geometry().perimeter(100);
print(peri);

```

#### Example: Mapping over a feature collection
By mapping over a collection, one can apply the same operation on every element in a collection. For instance, let's run the same geometry operations on every county in Connecticut:
**1.** Similar to the previous example, we start by zooming into the map and loading the feature collection of CT counties.
```
// Set map center over the state of CT.
Map.setCenter(-72.6978,41.6798,8);
// Load US county dataset.
varcountyData=ee.FeatureCollection('TIGER/2018/Counties');
// Filter the counties that are in Connecticut.
varcountyConnect=countyData.filter(
ee.Filter.eq('STATEFP','09'));
// Add the layer to the map with a specified color and layer name.
Map.addLayer(countyConnect,{color:'red'},'Original Collection');

```

**2.** We define the function, which will perform the geometry operation on a feature. Try changing the operation being performed within the function to test what it does to the final output.
```
functionperformMap(feature){
// Reduce number of vertices in geometry; the number is to specify maximum
// error in meters. This is only for illustrative purposes, since Earth Engine
// can handle up to 1 million vertices.
varsimple=feature.simplify(10000);
// Find centroid of geometry.
varcenter=simple.centroid(100);
// Return buffer around geometry; the number represents the width of buffer,
// in meters.
returncenter.buffer(5000,100);
}

```

**3.** Finally, we map the defined function over all the features in the collection. This parallelization is generally much faster than performing operations sequentially over each element of the collection.
```
varmappedCentroid=countyConnect.map(performMap);
// Add the layer to the map with a specified color and layer name.
Map.addLayer(mappedCentroid,{color:'blue'},'Mapped buffed centroids');

```

## Operations on features
### Creating a feature with a specific property value
```
varfeat=ee.Feature(geometry,{Name:'featureName',Size:500});

```

### Creating a feature from an existing feature, renaming a property
```
varfeatNew=feature.select(['name'],['descriptor']);

```

### Extracting values of a property from a Feature
```
varfeatVal=feature.get('size');

```

#### Example: Feature operations
Let's create a feature from scratch and play around with its properties:
```
// Create geometry.
varvarGeometry=ee.Geometry.Polygon(0,0,40,30,20,20,0,0);
// Create feature from geometry.
varvarFeature=ee.Feature(varGeometry,{
name:['Feature name','Supreme'],
size:[500,1000]
});
// Get values of a property.
vararr=varFeature.get('size');
// Print variable.
print(arr);
// Select a subset of properties and rename them.
varvarFeaturenew=varFeature.select(['name'],['descriptor']);
// Print variable.
print(varFeaturenew);

```

## Filtering
### Filtering by property values
```
varbFilter=ee.Filter.eq(propertyName,value);

```

> or .neq , .gt , .gte , .lt , and .lte
### Filtering based on maximum difference from a threshold
```
vardiffFilter=ee.Filter.maxDifference(threshold,propertyName,value);

```

### Filtering by text property
```
vartxtFilter=ee.Filter.stringContains(propertyName,stringValue);

```

> or .stringStartsWith, and .stringEndsWith
### Filtering by a value range
```
varrangeFilter=ee.Filter.rangeContains(
propertyName,stringValue,minValue,maxValue);

```

### Filtering by specific property values
```
varlistFilter=ee.Filter.listContains(
propertyName,value1,propertyName2,value2);

```

> .inList to test against a list of values
### Filtering by date range
```
vardateFilter=ee.Filter.calendarRange(startDate,stopDate);

```

### Filtering by particular days of the year
```
vardayFilter=ee.Filter.dayOfYear(startDay,stopDay);

```

### Filtering by a bounding area
```
varboundsFilter=ee.Filter.bounds(geometryOrFeature);

```

### Combining and inversing filters
```
varnewFilterAnd=ee.Filter.and(listOfFilters);
varnewFilterOr=ee.Filter.or(listOfFilters);
varinverseFilter=ee.Filter.not(filter);

```

## Operations on images
### Selecting the bands of an image
```
varband=image.select(bandName);

```

### Creating masks
```
varmask=image.eq(value);

```

> or .neq or .gt or .gte or .lt or .lte
### Applying image masks
```
varmasked=image.updateMask(mask);

```

### Performing pixelwise calculations
```
varresults=image.add(value);

```

> or .subtract , .multiply , .divide , .max , .min , .abs , .round , .floor , .ceil , .sqrt , .exp, .log, .log10, .sin , .cos , .tan , .sinh , .cosh , .tanh , .acos, .asin
### Shift pixels of an image
```
newImage=oldImage.leftShift(valueOfShift);

```

> or .rightShift
## Reducers
Reducers are objects in Earth Engine for data aggregation. They can be used for aggregating across time, space, bands, properties, etc. Reducers range from basic statistical indices (like `ee.Reducer.mean()`, `ee.Reducer.stdDev()`, `ee.Reducer.max()`, etc.), to standard measures of covariance (like `ee.Reducer.linearFit()`,`ee.Reducer.spearmansCorrelation()`, `ee.Reducer.spearmansCorrelation()`, etc.), to descriptors of variable distributions (like `ee.Reducer.skew()`, `ee.Reducer.frequencyHistogram()`, `ee.Reducer.kurtosis()`, etc.). To get the first (or only) value for a property, use `ee.Reducer.first()`.
### Reducing an image collection to an image
```
varoutputImage=imCollection.reduce(reducer);

```

### Reducing an image to a statistic for an area of interest
```
varoutputDictionary=varImage.reduceRegion(reducer,geometry,scale);

```

Alternatively, `reduceRegions` can be used to compute image statistics for all elements of a collection at once:
```
varoutputCollection=varImage.reduceRegions(reducer,collection,scale);

```

Note that for large collections, this may be less efficient than mapping over the collection and using `reduceRegion`.
### Applying a reducer to each element of a collection
```
varoutputDictionary=reduceColumns(reducer,selectors);

```

### Applying a reducer to the neighborhoods of each pixel
```
varoutputImage=reduceNeighborhood(reducer,kernel);

```

### Applying a reducer to each element of an array pixel
```
varoutputImage=arrayAccum(axis,reducer);

```

### Convert the properties of a vector into a raster
```
varoutputImage=reduceToImage(properties,reducer);

```

### Convert a raster into a vector
```
varoutputCollection=reduceToVectors(reducer);

```

## Operations on image collections
### Selecting the first n images in a collection (based on property)
```
varselectedImages=imCollection.limit(n,propertyName,order);

```

### Selecting images based on particular properties
```
varselectedIm=imCollection.filterMetadata(propertyName,operator,value);

```

> Operators include: "equals", "less_than", "greater_than", "not_equals", "not_less_than", "not_greater_than", "starts_with", "ends_with", "not_starts_with", "not_ends_with", "contains", "not_contains".
### Selecting images within a date range
```
varselectedIm=imCollection.filterDate(startDate,stopDate);

```

### Selecting images within a bounding geometry
```
varselectedIm=imCollection.filterBounds(geometry);

```

### Performing pixelwise calculations for all images in a collection
```
varsumOfImages=imCollection.sum();

```

> or `product()`, `max()`, `min()`, `mean()`, `mode()`, `median()`, `count()`.
Alternatively, using reducers:
```
varsumOfImages=imCollection.reduce(ee.Reducer.sum());

```

### Compositing images in collection with the last image on top
```
varmosaicOfImages=imCollection.mosaic();

```

Alternatively, using reducers:
```
varsumOfImages=imCollection.reduce(ee.Reducer.first());

```

#### Example: Image and image collection operations
Let's analyze images over a region of interest (the counties of Connecticut):
**1.** As before, we start by loading in the feature and image collections of interest.
```
// Set map center over the state of CT.
Map.setCenter(-72.6978,41.6798,8);
// Load the MODIS MYD11A2 (8-day LST) image collection.
varraw=ee.ImageCollection('MODIS/006/MYD11A2');
// Load US county dataset.
varcountyData=ee.FeatureCollection('TIGER/2018/Counties');
// Filter the counties that are in Connecticut.
// This will be the region of interest for the image operations.
varroi=countyData.filter(ee.Filter.eq('STATEFP','09'));
// Examine image collection.
print(raw);

```

**2.** We select the bands and images in the collection we are interested in.
```
// Select a band of the image collection using either indexing or band name.
varbandSel1=raw.select(0);
varbandSel2=raw.select('LST_Day_1km');
// Filter the image collection by a date range.
varfiltered=raw.filterDate('2002-12-30','2004-4-27');
// Print filtered collection.
print(filtered);
// Limit the image collection to the first 50 elements.
varlimited=raw.limit(50);
// Print collections.
print(limited);
print(bandSel1);

```

**3.** We calculate the mean of all the images in the collection, clip it to the geometry of interest and scale it to convert it from digital number to degree Celsius.
```
// Calculate mean of all images (pixel-by-pixel) in the collection.
varmean=bandSel1.mean();
// Isolate image to region of interest.
varclipped=mean.clip(roi);
// mathematical operation on image pixels to convert from digital number
// of satellite observations to degree Celsius.
varcalculate=clipped.multiply(0.02).subtract(273.15);
// Add the layer to the map with a specified color palette and layer name.
Map.addLayer(
calculate,{min:15,max:20,palette:['blue','green','red']},'LST');

```

**4.** We mask out parts of the image to display regions above and below certain temperature thresholds.
```
// Select pixels in the image that are greater than 30.8.
varmask=calculate.gt(18);
// Add the mask to the map with a layer name.
Map.addLayer(mask,{},'mask');
// Use selected pixels to update the mask of the whole image.
varmasked=calculate.updateMask(mask);
// Add the final layer to the map with a specified color palette and layer name.
Map.addLayer(masked,
{min:18,max:25,palette:['blue','green','red']},'LST_masked');

```

![Masked LST image](https://developers.google.com/static/earth-engine/tutorials/community/beginners-cookbook/masked-image.png)
## Exporting data
### Exporting a collection to Google Drive, Earth Engine Asset, or Google Cloud
```
Export.image.toDrive({
collection:varImage,description:'fileName',region:geometry,scale:1000
});

```

> or `Export.image.toCloudStorage()`, `Export.image.toAsset()`, `Export.table.toDrive()`, `Export.table.toCloudStorage()`, `Export.video.toCloudStorage()`, `Export.video.toDrive()`.
#### Example: Exporting data
**1.** Define a function to find the mean value of pixels in each feature of a collection.
```
// Function to find mean of pixels in region of interest.
vargetRegions=function(image){
// Load US county dataset.
varcountyData=ee.FeatureCollection('TIGER/2018/Counties');
// Filter the counties that are in Connecticut.
// This will be the region of interest for the operations.
varroi=countyData.filter(ee.Filter.eq('STATEFP','09'));
returnimage.reduceRegions({
// Collection to run operation over.
collection:roi,
// Calculate mean of all pixels in region.
reducer:ee.Reducer.mean(),
// Pixel resolution used for the calculations.
scale:1000
});
};

```

**2.** Load image collection, filter collection to date range, select band of interest, calculate mean of all images in collection, and multiply by scaling factor.
```
varimage=ee.ImageCollection('MODIS/MYD13A1')
.filterDate('2002-07-08','2017-07-08')
.select('NDVI')
.mean()
.multiply(.0001);
// Print final image.
print(image);
// Call function.
varcoll=getRegions(image);

```

**3.** Export the table created to your Google Drive.
```
Export.table.toDrive({
collection:coll,
description:'NDVI_all',
fileFormat:'CSV'
});
// Print final collection.
print(coll);

```

## Bonus: Timelapse example
```
// Timelapse example (based on google API example);
// Create rectangle over Dubai.
vargeometry=ee.Geometry.Rectangle([55.1,25,55.4,25.4]);
// Add layer to map.
Map.addLayer(geometry);
// Load Landsat image collection.
varallImages=ee.ImageCollection('LANDSAT/LT05/C02/T1_TOA')
// Filter row and path such that they cover Dubai.
.filter(ee.Filter.eq('WRS_PATH',160))
.filter(ee.Filter.eq('WRS_ROW',43))
// Filter cloudy scenes.
.filter(ee.Filter.lt('CLOUD_COVER',30))
// Get required years of imagery.
.filterDate('1984-01-01','2012-12-30')
// Select 3-band imagery for the video.
.select(['B4','B3','B2'])
// Make the data 8-bit.
.map(function(image){
returnimage.multiply(512).uint8();
});
Export.video.toDrive({
collection:allImages,
// Name of file.
description:'dubaiTimelapse',
// Quality of video.
dimensions:720,
// FPS of video.
framesPerSecond:8,
// Region of export.
region:geometry
});

```

[Dubai timelapse](https://www.youtube.com/watch?v=6gK4Fd-WSM4&feature=youtu.be)
![Urban growth in Dubai](https://developers.google.com/static/earth-engine/tutorials/community/beginners-cookbook/dubai-change.png)
## Example applications
What can you do with Google Earth Engine?
  * [EE Population Explorer](https://google.earthengine.app/view/population-explorer)
  * [EE Ocean Time Series Investigator](https://google.earthengine.app/view/ocean)
  * [Global Surface UHI Explorer](https://yceo.users.earthengine.app/view/uhimap)
  * [Stratifi - cloud-based stratification](https://sabrinaszeto.users.earthengine.app/view/stratifi)
  * [And hundreds more...](https://philippgaertner.github.io/2019/04/earth-engine-apps-inventory/)


## Additional resources
  * [Google Earth Engine API documentation](https://developers.google.com/earth-engine/)
  * [Google Earth Engine Developers forum](https://groups.google.com/forum/#!forum/google-earth-engine-developers)
  * [Example scripts from Prof. Dana Tomlin's handouts for his course on Geospatial Software Design](https://github.com/EEYale/example-scripts)


Was this helpful?
