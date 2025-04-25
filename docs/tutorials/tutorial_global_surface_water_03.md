 
#  Water Occurrence Change Intensity 
Stay organized with collections  Save and categorize content based on your preferences. 
The Water Occurrence Change Intensity data layer provides a measure of how surface water has changed between two epochs: 1984-1999 and 2000-2015. The layer averages the change across homologous pairs of months taken from the two epochs. See the [ Data Users Guide (v2) ](https://storage.googleapis.com/global-surface-water/downloads_ancillary/DataUsersGuidev2.pdf) for additional details on this layer.
This section of the tutorial will:
  1. add a styled map layer for visualizing water occurrence change intensity, and 
  2. summarize the change intensity in a specified region-of-interest using a histogram. 


## Visualization
Similar to the water occurrence layer, we will start by adding a basic visualization of occurrence change intensity to the map and then improve upon it. Occurrence change intensity is provided in two ways, both as absolute and normalized values. We will use the absolute values in this tutorial. Start by selecting the absolute occurrence change intensity layer from the GSW image:
### Code Editor (JavaScript)
```
varchange=gsw.select("change_abs");
```

In the Constants section of the code, add a statement that creates a new variable that defines how the layer will be styled. This styling shows areas where the surface water occurrence has decreased/increased in red/green. Areas where surface water occurrence is relatively unchanged are shown in black.
### Code Editor (JavaScript)
```
varVIS_CHANGE={
min:-50,
max:50,
palette:['red','black','limegreen']
};
```

At the end of the Map Layers section of code, add a statement that adds a new layer to the map.
### Code Editor (JavaScript)
```
Map.setCenter(-74.4557,-8.4289,11);// Ucayali River, Peru
Map.addLayer({
eeObject:change,
visParams:VIS_CHANGE,
name:'occurrence change intensity'
});
```
![change intensity](https://developers.google.com/static/earth-engine/images/tutorial_global_surface_water_03_change_intensity.png) Figure 6. Screenshot of a surface water change intensity for the Ucayali River near Pucallpa, a city in the Amazonian rainforest of eastern Peru. Red/green indicates a decrease/increase in surface water occurrence between the epochs. 
## Summarizing Change within a Region of Interest
In this section, we will summarize the amount of change within a specified region of interest. To specify a region of interest, click on the polygon drawing tool, which is one of the [ Geometry tools](https://developers.google.com/earth-engine/guides/playground#geometry-tools). This will create a new Geometry Imports layer, which is named "geometry" by default. To change the name, click on the gear icon located to the right of the to the layer name. (Note that you may need to place your cursor on the layer name to make it appear.)
Change the layer name to `roi` (for region-of-interest or ROI). We then can click on a series of points on the map to define a polygon region of interest.
![region of interest](https://developers.google.com/static/earth-engine/images/tutorial_global_surface_water_03_roi.png) Figure 7. Screenshot of the Ucayali River near Pucallpa, Peru, with a region-of-interest created by using the polygon drawing tool. 
Now that our region-of-interest is defined and stored in a variable, we can use it to calculate a histogram of the change intensity for the ROI. Add the following code to the Calculations section of the script.
### Code Editor (JavaScript)
```
// Calculate a change intensity for the region of interest.
varhistogram=change.reduceRegion({
reducer:ee.Reducer.histogram(),
geometry:roi,
scale:30,
bestEffort:true,
});
print(histogram);
```

The first statement calculates a histogram of occurrence change intensity values within the ROI, sampling at a 30m scale. The second prints the resulting object to the Code Editor Console Tab. You can expand out the object tree to view the values of the histogram buckets. The numeric data is there, but there are better ways to visualize the results.
![histogram values](https://developers.google.com/static/earth-engine/images/tutorial_global_surface_water_03_histogram_values.png) Figure 8. Console tab results, showing histogram values of surface water change intensity. 
To improve upon this, we can generate a histogram chart instead. Replace the statement that defines the histogram object with the following statements:
### Code Editor (JavaScript)
```
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
```

These statements create a histogram chart object, which replaces the histogram object tree in the Console Tab with a chart. The chart method contains several arguments, including `scale` which defines the spatial scale, in meters, at which the region of interest' is sampled, and `minBucketWidth` which is used to control the width of the histogram buckets.
![histogram chart](https://developers.google.com/static/earth-engine/images/tutorial_global_surface_water_03_histogram_chart.png) Figure 9. Console tab results, showing a histogram chart of surface water change intensity. 
You can explore the chart values interactively by placing your cursor over the histogram bars.
## Final Script
The entire script for this section is listed below. Note that the script includes statements for defining a polygon geometry (`roi`), which is comparable to the geometry that you created using the Code Editor's geometry tools.
### Code Editor (JavaScript)
```
//////////////////////////////////////////////////////////////
// Asset List
//////////////////////////////////////////////////////////////
vargsw=ee.Image('JRC/GSW1_0/GlobalSurfaceWater');
varoccurrence=gsw.select('occurrence');
varchange=gsw.select("change_abs");
varroi=/* color: 0B4A8B */ee.Geometry.Polygon(
[[[-74.17213,-8.65569],
[-74.17419,-8.39222],
[-74.38362,-8.36980],
[-74.43031,-8.61293]]]);
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
// Calculations
//////////////////////////////////////////////////////////////
// Create a water mask layer, and set the image mask so that non-water areas are transparent.
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
//////////////////////////////////////////////////////////////
// Initialize Map Location
//////////////////////////////////////////////////////////////
// Uncomment one of the following statements to center the map on
// a particular location.
// Map.setCenter(-90.162, 29.8597, 10);  // New Orleans, USA
// Map.setCenter(-114.9774, 31.9254, 10); // Mouth of the Colorado River, Mexico
// Map.setCenter(-111.1871, 37.0963, 11); // Lake Powell, USA
// Map.setCenter(149.412, -35.0789, 11); // Lake George, Australia
// Map.setCenter(105.26, 11.2134, 9);   // Mekong River Basin, SouthEast Asia
// Map.setCenter(90.6743, 22.7382, 10);  // Meghna River, Bangladesh
// Map.setCenter(81.2714, 16.5079, 11);  // Godavari River Basin Irrigation Project, India
// Map.setCenter(14.7035, 52.0985, 12);  // River Oder, Germany & Poland
// Map.setCenter(-59.1696, -33.8111, 9); // Buenos Aires, Argentina\
Map.setCenter(-74.4557,-8.4289,11);// Ucayali River, Peru
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
name:'occurrence change intensity'
});
```

In the [next section](https://developers.google.com/earth-engine/tutorials/tutorial_global_surface_water_04), you will further explore how water changed over time, by working with the water class **transition** layer. 
