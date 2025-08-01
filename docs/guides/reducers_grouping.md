 
#  Grouped Reductions and Zonal Statistics
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
You can get statistics in each zone of an `Image` or `FeatureCollection` by using `reducer.group()` to group the output of a reducer by the value of a specified input. For example, to compute the total population and number of housing units in each state, this example groups the output of a reduction of a census block `FeatureCollection` as follows:
### Code Editor (JavaScript)
```
// Load a collection of US census blocks.
varblocks=ee.FeatureCollection('TIGER/2010/Blocks');

// Compute sums of the specified properties, grouped by state code.
varsums=blocks
.filter(ee.Filter.and(
ee.Filter.neq('pop10',null),
ee.Filter.neq('housing10',null)))
.reduceColumns({
selectors:['pop10','housing10','statefp10'],
reducer:ee.Reducer.sum().repeat(2).group({
groupField:2,
groupName:'state-code',
})
});

// Print the resultant Dictionary.
print(sums);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Load a collection of US census blocks.
blocks = ee.FeatureCollection('TIGER/2010/Blocks')

# Compute sums of the specified properties, grouped by state code.
sums = blocks.filter(
    ee.Filter.And(
        ee.Filter.neq('pop10', None), ee.Filter.neq('housing10', None)
    )
).reduceColumns(
    selectors=['pop10', 'housing10', 'statefp10'],
    reducer=ee.Reducer.sum()
    .repeat(2)
    .group(groupField=2, groupName='state-code'),
)

# Print the resultant Dictionary.
display(sums)
```

The `groupField` argument is the index of the input in the selectors array that contains the codes by which to group, the `groupName` argument specifies the name of the property to store the value of the grouping variable. Since the reducer is not automatically repeated for each input, the `repeat(2)` call is needed.
To group output of `image.reduceRegions()` you can specify a grouping band that defines groups by integer pixel values. This type of computation is sometimes called "zonal statistics" where the zones are specified as the grouping band and the statistic is determined by the reducer. In the following example, change in nightlights in the United States is grouped by land cover category:
### Code Editor (JavaScript)
```
// Load a region representing the United States
varregion=ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017')
.filter(ee.Filter.eq('country_na','United States'));

// Load MODIS land cover categories in 2001.
varlandcover=ee.Image('MODIS/051/MCD12Q1/2001_01_01')
// Select the IGBP classification band.
.select('Land_Cover_Type_1');

// Load nightlights image inputs.
varnl2001=ee.Image('NOAA/DMSP-OLS/NIGHTTIME_LIGHTS/F152001')
.select('stable_lights');
varnl2012=ee.Image('NOAA/DMSP-OLS/NIGHTTIME_LIGHTS/F182012')
.select('stable_lights');

// Compute the nightlights decadal difference, add land cover codes.
varnlDiff=nl2012.subtract(nl2001).addBands(landcover);

// Grouped a mean reducer: change of nightlights by land cover category.
varmeans=nlDiff.reduceRegion({
reducer:ee.Reducer.mean().group({
groupField:1,
groupName:'code',
}),
geometry:region.geometry(),
scale:1000,
maxPixels:1e8
});

// Print the resultant Dictionary.
print(means);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Load a region representing the United States
region = ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017').filter(
    ee.Filter.eq('country_na', 'United States')
)

# Load MODIS land cover categories in 2001.
landcover = ee.Image('MODIS/051/MCD12Q1/2001_01_01').select(
    # Select the IGBP classification band.
    'Land_Cover_Type_1'
)

# Load nightlights image inputs.
nl_2001 = ee.Image('NOAA/DMSP-OLS/NIGHTTIME_LIGHTS/F152001').select(
    'stable_lights'
)
nl_2012 = ee.Image('NOAA/DMSP-OLS/NIGHTTIME_LIGHTS/F182012').select(
    'stable_lights'
)

# Compute the nightlights decadal difference, add land cover codes.
nl_diff = nl_2012.subtract(nl_2001).addBands(landcover)

# Grouped a mean reducer: change of nightlights by land cover category.
means = nl_diff.reduceRegion(
    reducer=ee.Reducer.mean().group(groupField=1, groupName='code'),
    geometry=region.geometry(),
    scale=1000,
    maxPixels=1e8,
)

# Print the resultant Dictionary.
display(means)
```

Note that in this example, the `groupField` is the index of the band containing the zones by which to group the output. The first band is index 0, the second is index 1, etc.
