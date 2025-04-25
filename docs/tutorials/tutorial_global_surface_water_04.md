 
#  Water Class Transition 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Basic Visualization](https://developers.google.com/earth-engine/tutorials/tutorial_global_surface_water_04#basic-visualization)
  * [Summarizing Area by Transition Class](https://developers.google.com/earth-engine/tutorials/tutorial_global_surface_water_04#summarizing-area-by-transition-class)
  * [Creating a Summary Chart](https://developers.google.com/earth-engine/tutorials/tutorial_global_surface_water_04#creating-a-summary-chart)
    * [Code Editor (JavaScript)](https://developers.google.com/earth-engine/tutorials/tutorial_global_surface_water_04#code-editor-javascript_6)
  * [Final Script](https://developers.google.com/earth-engine/tutorials/tutorial_global_surface_water_04#final-script)


The water transition layer captures changes between three classes of water occurrence (not water, seasonal water, and permanent water) along with two additional classes for ephemeral water (ephemeral permanent and ephemeral seasonal).
This section of the tutorial will: 
  1. add a map layer for visualizing water transition, 
  2. create a grouped reducer for summing the area of each transition class within a specified region-of-interest, and 
  3. create a chart that summarizes the area by transition class. 


## Basic Visualization
In the Asset List section of the script, add the following statement which creates a single band image object called `transition`:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/tutorials/tutorial_global_surface_water_04#code-editor-javascript-sample) More
```
vartransition=gsw.select('transition');
```

The GSW images contain metadata on the transition class numbers and names, and a default palette for styling the transition classes. When the transition layer is added to the map, these visualization parameters will be used automatically.
At the bottom of the Map Layers section of your script, add the following statement which adds a new map layer that displays the transition classes:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/tutorials/tutorial_global_surface_water_04#code-editor-javascript-sample) More
```
Map.setCenter(105.26,11.2134,9);// Mekong River Basin, SouthEast Asia
Map.addLayer({
eeObject:transition,
name:'Transition classes (1984-2015)',
});
```

When you run the script, the transition layer will be displayed.
![Surface Water Transition Classes](https://developers.google.com/static/earth-engine/images/tutorial_global_surface_water_04_default_vis.png) Figure 10. Screenshot of the Mekong River delta, showing a wide variation in surface water class transitions. 
The map key for the transition classes is:
Value | Symbol | Label  
---|---|---  
0 | Not water  
1 | Permanent  
2 | New permanent  
3 | Lost permanent  
4 | Seasonal  
5 | New seasonal  
6 | Lost seasonal  
7 | Seasonal to permanent  
8 | Permanent to seasonal  
9 | Ephemeral permanent  
10 | Ephemeral seasonal  
## Summarizing Area by Transition Class
In this section we will once again use the geometry polygon tool to define a region-of-interest. If you want to analyze a new location, you will want to first select and delete the original polygon that you drew so that you don't get results from the combined areas. See the [ Geometry tools](https://developers.google.com/earth-engine/guides/playground#geometry-tools) section of the Code Editor docs from information on how to modify geometries.
For this example we will draw a new polygon within the Mekong River delta.
![Transition Classes with ROI](https://developers.google.com/static/earth-engine/images/tutorial_global_surface_water_04_roi.png) Figure 11. The Mekong River delta in Vietnam, with a region-of-interest created by using the Code Editor's polygon drawing tool. 
In order to calculate the area covered by parts of an image, we will add an additional band to the transition image object that identifies the size of each pixel in square meters using the [ ee.Image.pixelArea](https://developers.google.com/earth-engine/apidocs/ee-image-pixelarea) method. 
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/tutorials/tutorial_global_surface_water_04#code-editor-javascript-sample) More
```
vararea_image_with_transition_class=ee.Image.pixelArea().addBands(transition);
```

The resulting image object (`area_image_with_transition_class`) is a two band image where the first band contains the area information in units of square meters (produced by the [ `ee.Image.pixelArea`code> ](https://developers.google.com/earth-engine/apidocs/ee-image-pixelarea) method), and the second band contains the transition class information.
We then summarize the class transitions within a region of interest (`roi`) using the [ `ee.Image.reduceRegion` ](https://developers.google.com/earth-engine/apidocs/ee-image-reduceregion) method and a [ grouped reducer ](https://developers.google.com/earth-engine/guides/reducers_grouping) which acts to sum up the area within each transition class:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/tutorials/tutorial_global_surface_water_04#code-editor-javascript-sample) More
```
varreduction_results=area_image_with_transition_class.reduceRegion({
reducer:ee.Reducer.sum().group({
groupField:1,
groupName:'transition_class_value',
}),
geometry:roi,
scale:30,
bestEffort:true,
});
print('reduction_results',reduction_results);
```

The console tab output now displays the `reduction_results`. Note that you will need to expand the tree a few levels to see the area summary data.
![Grouped Reduction Results](https://developers.google.com/static/earth-engine/images/tutorial_global_surface_water_04_roi_reduction_results.png) Figure 12. Console tab output, showing the results of the grouped reduction. 
While the `reduction_results` object does contain information on the area covered by each transition class, it is not particularly easy to read. In the next section we will make it easier to view the results. 
## Creating a Summary Chart
In this section we will make a chart to better summarize the results. To get started, we first extract out the list of transition classes with areas as follows: 
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/tutorials/tutorial_global_surface_water_04#code-editor-javascript-sample) More
```
varroi_stats=ee.List(reduction_results.get('groups'));
```

The result of the grouped reducer (`reduction_results`) is a dictionary containing a list of dictionaries. There is one dictionary in the list for each transition class. These statements use the [ ee.Dictionary.get ](https://developers.google.com/earth-engine/apidocs/ee-dictionary-get) method to extract the grouped reducer results from that dictionary and casts the results to an [ee.List](https://developers.google.com/earth-engine/apidocs/ee-list) data type, so we can access the individual dictionaries.
In order to make use of the [ charting functions of the Code Editor](https://developers.google.com/earth-engine/guides/charts), we will build a FeatureCollection that contains the necessary information. To do this we first create two lookup dictionaries and two helper functions. The code that creates the lookup dictionaries can be placed at the top of the "Calculations" section as follows: 
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/tutorials/tutorial_global_surface_water_04#code-editor-javascript-sample) More
```
//////////////////////////////////////////////////////////////
// Calculations
//////////////////////////////////////////////////////////////
// Create a dictionary for looking up names of transition classes.
varlookup_names=ee.Dictionary.fromLists(
ee.List(gsw.get('transition_class_values')).map(numToString),
gsw.get('transition_class_names')
);
// Create a dictionary for looking up colors of transition classes.
varlookup_palette=ee.Dictionary.fromLists(
ee.List(gsw.get('transition_class_values')).map(numToString),
gsw.get('transition_class_palette')
);
```

The `lookup_names` dictionary associates transition class values with their names, while the `lookup_palette` dictionary associates the transition class values with color definitions.
The two helper functions can be placed in a new code section called "Helper functions". 
More
### Code Editor (JavaScript)
```
//////////////////////////////////////////////////////////////
// Helper functions
//////////////////////////////////////////////////////////////
// Create a feature for a transition class that includes the area covered.
functioncreateFeature(transition_class_stats){
transition_class_stats=ee.Dictionary(transition_class_stats);
varclass_number=transition_class_stats.get('transition_class_value');
varresult={
transition_class_number:class_number,
transition_class_name:lookup_names.get(class_number),
transition_class_palette:lookup_palette.get(class_number),
area_m2:transition_class_stats.get('sum')
};
returnee.Feature(null,result);// Creates a feature without a geometry.
}
// Create a JSON dictionary that defines piechart colors based on the
// transition class palette.
// https://developers.google.com/chart/interactive/docs/gallery/piechart
functioncreatePieChartSliceDictionary(fc){
returnee.List(fc.aggregate_array("transition_class_palette"))
.map(function(p){return{'color':p};}).getInfo();
}
// Convert a number to a string. Used for constructing dictionary key lists
// from computed number objects.
functionnumToString(num){
returnee.Number(num).format();
}
```

The function `createFeature` takes a dictionary (containing the area and the water transition class) and returns a Feature suitable for charting. The function `createPieChartSliceDictionary` creates a list of colors that correspond to the transition classes, using the format expected by the pie chart. 
Next, we will apply the `createFeature` function over each dictionary in the list (`roi_stats`), using [ee.List.map](https://developers.google.com/earth-engine/apidocs/ee-list-map) to apply the helper function to each element of the list.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/tutorials/tutorial_global_surface_water_04#code-editor-javascript-sample) More
```
vartransition_fc=ee.FeatureCollection(roi_stats.map(createFeature));
print('transition_fc',transition_fc);
```

Now that we have a FeatureCollection containing the attributes we want to display on the chart, we can create a chart object and print it to the console.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/tutorials/tutorial_global_surface_water_04#code-editor-javascript-sample) More
```
// Add a summary chart.
vartransition_summary_chart=ui.Chart.feature.byFeature({
features:transition_fc,
xProperty:'transition_class_name',
yProperties:['area_m2','transition_class_number']
})
.setChartType('PieChart')
.setOptions({
title:'Summary of transition class areas',
slices:createPieChartSliceDictionary(transition_fc),
sliceVisibilityThreshold:0// Don't group small slices.
});
print(transition_summary_chart);
```

The `slices` option colors the pie chart slices so that they use the default palette defined for the transition classes (shown earlier in the map key table). The `sliceVisibilityThreshold` option prevents small slices from being grouped together into an "other" category. The resulting chart should be something similar to the one shown in Figure 13.
![Water transition class summary chart](https://developers.google.com/static/earth-engine/images/tutorial_global_surface_water_04_summary_chart.png) Figure 13. Chart summarizing the relatives size of the water transition classes. 
## Final Script
The entire script for this section is:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/tutorials/tutorial_global_surface_water_04#code-editor-javascript-sample) More
```
//////////////////////////////////////////////////////////////
// Asset List
//////////////////////////////////////////////////////////////
vargsw=ee.Image('JRC/GSW1_0/GlobalSurfaceWater');
varoccurrence=gsw.select('occurrence');
varchange=gsw.select("change_abs");
vartransition=gsw.select('transition');
varroi=ee.Geometry.Polygon(
[[[105.531921,10.412183],
[105.652770,10.285193],
[105.949401,10.520218],
[105.809326,10.666006]]]);
//////////////////////////////////////////////////////////////
// Constants
//////////////////////////////////////////////////////////////
varVIS_OCCURRENCE={
min:0,
max:100,
palette:['red','blue']
};
varVIS_CHANGE={
min:-50,
max:50,
palette:['red','black','limegreen']
};
varVIS_WATER_MASK={
palette:['white','black']
};
//////////////////////////////////////////////////////////////
// Helper functions
//////////////////////////////////////////////////////////////
// Create a feature for a transition class that includes the area covered.
functioncreateFeature(transition_class_stats){
transition_class_stats=ee.Dictionary(transition_class_stats);
varclass_number=transition_class_stats.get('transition_class_value');
varresult={
transition_class_number:class_number,
transition_class_name:lookup_names.get(class_number),
transition_class_palette:lookup_palette.get(class_number),
area_m2:transition_class_stats.get('sum')
};
returnee.Feature(null,result);// Creates a feature without a geometry.
}
// Create a JSON dictionary that defines piechart colors based on the
// transition class palette.
// https://developers.google.com/chart/interactive/docs/gallery/piechart
functioncreatePieChartSliceDictionary(fc){
returnee.List(fc.aggregate_array("transition_class_palette"))
.map(function(p){return{'color':p};}).getInfo();
}
// Convert a number to a string. Used for constructing dictionary key lists
// from computed number objects.
functionnumToString(num){
returnee.Number(num).format();
}
//////////////////////////////////////////////////////////////
// Calculations
//////////////////////////////////////////////////////////////
// Create a dictionary for looking up names of transition classes.
varlookup_names=ee.Dictionary.fromLists(
ee.List(gsw.get('transition_class_values')).map(numToString),
gsw.get('transition_class_names')
);
// Create a dictionary for looking up colors of transition classes.
varlookup_palette=ee.Dictionary.fromLists(
ee.List(gsw.get('transition_class_values')).map(numToString),
gsw.get('transition_class_palette')
);
// Create a water mask layer, and set the image mask so that non-water areas
// are transparent.
varwater_mask=occurrence.gt(90).mask(1);
// Generate a histogram object and print it to the console tab.
varhistogram=ui.Chart.image.histogram({
image:change,
region:roi,
scale:30,
minBucketWidth:10
});
histogram.setOptions({
title:'Histogram of surface water change intensity.'
});
print(histogram);
// Summarize transition classes in a region of interest.
vararea_image_with_transition_class=ee.Image.pixelArea().addBands(transition);
varreduction_results=area_image_with_transition_class.reduceRegion({
reducer:ee.Reducer.sum().group({
groupField:1,
groupName:'transition_class_value',
}),
geometry:roi,
scale:30,
bestEffort:true,
});
print('reduction_results',reduction_results);
varroi_stats=ee.List(reduction_results.get('groups'));
vartransition_fc=ee.FeatureCollection(roi_stats.map(createFeature));
print('transition_fc',transition_fc);
// Add a summary chart.
vartransition_summary_chart=ui.Chart.feature.byFeature({
features:transition_fc,
xProperty:'transition_class_name',
yProperties:['area_m2','transition_class_number']
})
.setChartType('PieChart')
.setOptions({
title:'Summary of transition class areas',
slices:createPieChartSliceDictionary(transition_fc),
sliceVisibilityThreshold:0// Don't group small slices.
});
print(transition_summary_chart);
//////////////////////////////////////////////////////////////
// Initialize Map Location
//////////////////////////////////////////////////////////////
// Uncomment one of the following statements to center the map on
// a particular location.
// Map.setCenter(-90.162, 29.8597, 10);  // New Orleans, USA
// Map.setCenter(-114.9774, 31.9254, 10); // Mouth of the Colorado River, Mexico
// Map.setCenter(-111.1871, 37.0963, 11); // Lake Powell, USA
// Map.setCenter(149.412, -35.0789, 11); // Lake George, Australia
Map.setCenter(105.26,11.2134,9);// Mekong River Basin, SouthEast Asia
// Map.setCenter(90.6743, 22.7382, 10);  // Meghna River, Bangladesh
// Map.setCenter(81.2714, 16.5079, 11);  // Godavari River Basin Irrigation Project, India
// Map.setCenter(14.7035, 52.0985, 12);  // River Oder, Germany & Poland
// Map.setCenter(-59.1696, -33.8111, 9); // Buenos Aires, Argentina
// Map.setCenter(-74.4557, -8.4289, 11); // Ucayali River, Peru
//////////////////////////////////////////////////////////////
// Map Layers
//////////////////////////////////////////////////////////////
Map.addLayer({
eeObject:water_mask,
visParams:VIS_WATER_MASK,
name:'90% occurrence water mask',
shown:false
});
Map.addLayer({
eeObject:occurrence.updateMask(occurrence.divide(100)),
name:"Water Occurrence (1984-2015)",
visParams:VIS_OCCURRENCE,
shown:false
});
Map.addLayer({
eeObject:change,
visParams:VIS_CHANGE,
name:'occurrence change intensity',
shown:false
});
Map.addLayer({
eeObject:transition,
name:'Transition classes (1984-2015)',
});
```

This concludes the tutorial on the Global Surface Water dataset. Note that this tutorial has shown how to work with just three of the data layers (occurrence, change intensity, and transition) that are available in the Global Surface Water dataset. You can read about the other data layers that are available in the [ Data Users Guide (v2)](https://storage.googleapis.com/global-surface-water/downloads_ancillary/DataUsersGuidev2.pdf). 
Happy analyzing!
