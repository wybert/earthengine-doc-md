 
#  Forest Cover and Loss Estimation
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
[ Edit on GitHub ](https://github.com/google/earthengine-community/edit/master/tutorials/forest-cover-loss-estimation/index.md "Contribute to this article on GitHub.")
[ Report issue ](https://github.com/google/earthengine-community/issues/new?title=Issue%20with%20tutorials/forest-cover-loss-estimation/index.md&body=Issue%20Description "Report an issue with this article on GitHub.")
[ Page history ](https://github.com/google/earthengine-community/commits/master/tutorials/forest-cover-loss-estimation/index.md "View changes to this article over time.")
Author(s): [ nkeikon ](https://github.com/nkeikon "View the profile for nkeikon on GitHub")
Tutorials contributed by the Earth Engine developer community are not part of the official Earth Engine product documentation. 
[Open In Code Editor](https://code.earthengine.google.com/09a2542381c5d7d79a772ba049b4b63d)
When estimating forest cover, deforestation, or emissions from land-use change at the national level, countries use forest definitions. In this tutorial, you will learn how to extract forest area by applying technical thresholds of canopy cover and minimum area requirements.
## Context
The Food and Agriculture Organization of the United Nations (FAO) defines forests as "Land spanning more than 0.5 hectares with trees higher than 5 meters and a canopy cover of more than 10 percent, or trees able to reach these thresholds in situ. It does not include land that is predominantly under agricultural or urban land use" (FAO 2015).
In various reporting of forest and/or land-use related data, countries may have different forest definitions, including these parameters, forest types or land use categories.
## Instructions
### Select a country and set parameters
This tutorial selected Bolivia as an example, with the minimum canopy cover of 10% and minimum forest area of 0.5 ha (the national definition may be different).
```
// Selected country (e.g. Bolivia).
varcountry='Bolivia';
// Canopy cover percentage (e.g. 10%).
varcc=ee.Number(10);
// Minimum forest area in pixels (e.g. 6 pixels, ~ 0.5 ha in this example).
varpixels=ee.Number(6);
// Minimum mapping area for tree loss (usually same as the minimum forest area).
varlossPixels=ee.Number(6);

// Load country features from Large Scale International Boundary (LSIB) dataset.
varcountries=ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017');
varselected=countries.filter(ee.Filter.eq('country_na',ee.String(country)));

```

Depending on the location of the country, the number of pixels that make up for 0.5 ha would differ. You can adjust this by calculating the actual minimum areas you were using (see step 6 below).
### Tree cover
We need a tree cover map to start this analysis. It is important to select a tree cover map that is appropriate for the purpose and scope of your research. In this tutorial, we select one from the Google Earth Engine catalogue, which currently has several tree cover datasets, including the Global Forest Change (GFC) (year 2000) and GLCF: Landsat Tree Cover Continuous Fields (2000, 2005, and 2010). Here, we use the Global Forest Change dataset. Note that the dataset is not intended for inter-year comparison because of variation in methods to produce the data; the dataset is used here to demonstrate analyses and introduce Earth Engine concepts and not rigorous or valid interpretation of results.
```
vargfc2018=ee.Image('UMD/hansen/global_forest_change_2018_v1_6');

```

1. Select 'treecover2000' in the Global Forest Change dataset.
```
varcanopyCover=gfc2018.select(['treecover2000']);

```

2. Apply the minimum canopy cover percentage (e.g. greater than or equal to 10%). Use `selfMask()` to set other other areas transparent by assigning value zero.
```
varcanopyCover10=canopyCover.gte(cc).selfMask();

```

3. Apply the minimum area requirement using `connectedPixelCount` (e.g. greater than or equal to 6 pixels). Note that if no kernel is passed to `connectedPixelCount`, 8 neighbor adjacency is used to determine connectivity.
```
// Use connectedPixelCount() to get contiguous area.
varcontArea=canopyCover10.connectedPixelCount();
// Apply the minimum area requirement.
varminArea=contArea.gte(pixels).selfMask();

```

4. Scale the results in nominal value based on to the dataset's projection to display on the map. Reprojecting with a specified scale ensures that pixel area does not change with zoom.
```
varprj=gfc2018.projection();
varscale=prj.nominalScale();
Map.addLayer(minArea.reproject(prj.atScale(scale)),{
palette:['#96ED89']
},'tree cover: >= min canopy cover & area (light green)');

```

5. Calculate the tree cover area (ha). Use `pixelArea()` to get the value of each pixel in square metres, divide by 10,000 to convert to hectare, and sum over the result for a measure of area.
```
varforestArea=minArea.multiply(ee.Image.pixelArea()).divide(10000);
varforestSize=forestArea.reduceRegion({
reducer:ee.Reducer.sum(),
geometry:selected.geometry(),
scale:30,
maxPixels:1e13
});
print(
'Year 2000 tree cover (ha) \nmeeting minimum canopy cover and \nforest area thresholds \n ',
forestSize.get('treecover2000'));

```

6. Calculate the actual average minimum forest area used (ha). This is to make sure if the selected number of pixels for minimum area (e.g. 6) matches or comes close to the minimum area intended in hectare (e.g. 0.5 ha).
```
varpixelCount=minArea.reduceRegion({
reducer:ee.Reducer.count(),
geometry:selected.geometry(),
scale:30,
maxPixels:1e13
});
varonePixel=forestSize.getNumber('treecover2000')
.divide(pixelCount.getNumber('treecover2000'));
varminAreaUsed=onePixel.multiply(pixels);
print('Minimum forest area used (ha)\n ',minAreaUsed);

```

The GFC dataset uses 30x30m pixels. Therefore, 6 pixels (>5,000/(30x30)) is used for this exercise. This can be used for countries near the equator. For countries in higher or lower latitudes, you would need to increase the number of pixels.
![](https://developers.google.com/static/earth-engine/tutorials/community/forest-cover-loss-estimation/alltrees.png) | ![](https://developers.google.com/static/earth-engine/tutorials/community/forest-cover-loss-estimation/cc10.png) | ![](https://developers.google.com/static/earth-engine/tutorials/community/forest-cover-loss-estimation/treecover00.png)  
---|---|---  
All trees (yellow) | >= min canopy cover (orange) | >= min canopy cover & tree area (light green)  
### Tree loss
We use the Global Forest Change dataset (year 2001) to demonstrate how to estimate tree loss based on forest definition.
1. Select tree loss pixels that are inside the derived tree cover.
```
vartreeLoss=gfc2018.select(['lossyear']);
vartreeLoss01=treeLoss.eq(1).selfMask();// tree loss in year 2001
// Select the tree loss within the derived tree cover
// (>= canopy cover and area requirements).
vartreecoverLoss01=minArea.and(treeLoss01).rename('loss2001').selfMask();

```

2. Apply the minimum mapping unit using `connectedPixelCount()`.
```
// Create connectedPixelCount() to get contiguous area.
varcontLoss=treecoverLoss01.connectedPixelCount();
// Apply the minimum area requirement.
varminLoss=contLoss.gte(lossPixels).selfMask();

```

3. Calculate the tree loss area (ha).
```
varlossArea=minLoss.multiply(ee.Image.pixelArea()).divide(10000);
varlossSize=lossArea.reduceRegion({
reducer:ee.Reducer.sum(),
geometry:selected.geometry(),
scale:30,
maxPixels:1e13
});
print(
'Year 2001 tree loss (ha) \nmeeting minimum canopy cover and \nforest area thresholds \n ',
lossSize.get('loss2001'));

```

![](https://developers.google.com/static/earth-engine/tutorials/community/forest-cover-loss-estimation/allloss.png) | ![](https://developers.google.com/static/earth-engine/tutorials/community/forest-cover-loss-estimation/losstreecover.png) | ![](https://developers.google.com/static/earth-engine/tutorials/community/forest-cover-loss-estimation/lossmin.png)  
---|---|---  
All tree loss (black), tree cover (green) | Loss inside tree cover (purple) | Loss inside tree cover & >= min tree area (red)  
### Subsequent tree cover
You can estimate the tree cover after the loss by subtracting the loss from the previous tree cover. You can also add tree gain if you have data.
1. Use the derived tree cover and tree loss from the previous steps.
2. Create a new tree cover by removing the tree loss.
```
// Unmask the derived loss.
varminLossUnmask=minLoss.unmask();
// Switch the binary value of the loss (0, 1) to (1, 0).
varnotLoss=minLossUnmask.select('loss2001').eq(0);
// Combine the derived tree cover and not-loss with 'and'.
vartreecoverLoss01=minArea.and(notLoss).selfMask();

```

3. Apply the minimum area requirement to the above tree cover (minimum canopy cover threshold is already applied by using the derived tree cover). Reproject in nominal scale when displaying on the map.
```
varcontArea01=treecoverLoss01.connectedPixelCount();
varminArea01=contArea01.gte(pixels);
Map.addLayer(minArea01.reproject(prj.atScale(scale)),{
palette:['#168039']
},'tree cover 2001 (gain not considered) (light green)');

```

4. Calculate the new tree cover area (ha).
```
varforestArea01=minArea01.multiply(ee.Image.pixelArea()).divide(10000);
varforestSize01=forestArea01.reduceRegion({
reducer:ee.Reducer.sum(),
geometry:selected.geometry(),
scale:30,
maxPixels:1e13
});
print(
'Year 2001 tree cover (ha) \nmeeting minimum canopy cover and \nforest area thresholds \n ',
forestSize01.get('treecover2000'));

```

![](https://developers.google.com/static/earth-engine/tutorials/community/forest-cover-loss-estimation/treecover2000.png) | ![](https://developers.google.com/static/earth-engine/tutorials/community/forest-cover-loss-estimation/treeloss2001.png) | ![](https://developers.google.com/static/earth-engine/tutorials/community/forest-cover-loss-estimation/treecover2001.png)  
---|---|---  
Tree cover 2000 (light green) | Tree loss 2001 (red) | Tree cover 2001 (dark green)  
## Land use categories
You can also exclude certain tree areas such as tree plantations or agricultural plantations with tree crops if you have spatial data for these areas (e.g. masking, assigning values, etc. - not included in this tutorial).
## References
  * GOFC-GOLD 2013 A sourcebook of methods and procedures for monitoring and reporting anthropogenic greenhouse gas emissions and removals associated with deforestation, gains and losses of carbon stocks in forests remaining forests, and forestation p 126 GOFC-GOLD Report (version COP22-1)
  * FAO 2018 From reference levels to results reporting: REDD+ under the UNFCCC 2018 update (Food and Agriculture Organization of the United Nations) (http://fao.org/3/CA0176EN/ca0176en.pdf)
  * Forest Resources Assessment Programme (FAO) 2015 Global forest resources assessment 2015 (http://fao.org/3/a-i4808e.pdf)
  * Nomura, K., Mitchard, E.T., Bowers, S.J. and Patenaude, G., 2019. Missed carbon emissions from forests: comparing countries' estimates submitted to UNFCCC to biophysical estimates. Environmental Research Letters (https://iopscience.iop.org/article/10.1088/1748-9326/aafc6b)


