 
#  Statistics of FeatureCollection Columns
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
To reduce properties of features in a `FeatureCollection`, use `featureCollection.reduceColumns()`. Consider the following toy example:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/reducers_reduce_columns#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/reducers_reduce_columns#colab-python-sample) More
```
// Make a toy FeatureCollection.
varaFeatureCollection=ee.FeatureCollection([
ee.Feature(null,{foo:1,weight:1}),
ee.Feature(null,{foo:2,weight:2}),
ee.Feature(null,{foo:3,weight:3}),
]);
// Compute a weighted mean and display it.
print(aFeatureCollection.reduceColumns({
reducer:ee.Reducer.mean(),
selectors:['foo'],
weightSelectors:['weight']
}));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Make a toy FeatureCollection.
a_feature_collection = ee.FeatureCollection([
  ee.Feature(None, {'foo': 1, 'weight': 1}),
  ee.Feature(None, {'foo': 2, 'weight': 2}),
  ee.Feature(None, {'foo': 3, 'weight': 3}),
])
# Compute a weighted mean and display it.
display(
  a_feature_collection.reduceColumns(
    reducer=ee.Reducer.mean(), selectors=['foo'], weightSelectors=['weight']
  )
)
```

Note that the inputs are weighted according to the specified `weight` property. The result is therefore:
```
mean: 2.333333333333333
  
```

As a more complex example, consider a `FeatureCollection` of US census blocks with census data as attributes. The variables of interest are total population and total housing units. You can get their sum(s) by supplying a summing reducer argument to `reduceColumns()` and printing the result:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/reducers_reduce_columns#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/reducers_reduce_columns#colab-python-sample) More
```
// Load US census data as a FeatureCollection.
varcensus=ee.FeatureCollection('TIGER/2010/Blocks');
// Filter the collection to include only Benton County, OR.
varbenton=census.filter(
ee.Filter.and(
ee.Filter.eq('statefp10','41'),
ee.Filter.eq('countyfp10','003')
)
);
// Display Benton County census blocks.
Map.setCenter(-123.27,44.57,13);
Map.addLayer(benton);
// Compute sums of the specified properties.
varproperties=['pop10','housing10'];
varsums=benton
.filter(ee.Filter.notNull(properties))
.reduceColumns({
reducer:ee.Reducer.sum().repeat(2),
selectors:properties
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
```
# Load US census data as a FeatureCollection.
census = ee.FeatureCollection('TIGER/2010/Blocks')
# Filter the collection to include only Benton County, OR.
benton = census.filter(
  ee.Filter.And(
    ee.Filter.eq('statefp10', '41'), ee.Filter.eq('countyfp10', '003')
  )
)
# Display Benton County census blocks.
m = geemap.Map()
m.set_center(-123.27, 44.57, 13)
m.add_layer(benton)
display(m)
# Compute sums of the specified properties.
properties = ['pop10', 'housing10']
sums = benton.filter(ee.Filter.notNull(properties)).reduceColumns(
  reducer=ee.Reducer.sum().repeat(2), selectors=properties
)
# Print the resultant Dictionary.
display(sums)
```

The output is a `Dictionary` representing the aggregated property according to the specified reducer:
```
sum: [85579,36245]
  
```

Note that the above example uses the `notNull()` filter to include only features with non-null entries for selected properties in the collection being reduced. It is good practice to check for null entries to catch unexpected missing data and avoid errors resulting from calculations that include null values. 
Also note that unlike `imageCollection.reduce()`, in which reducers are automatically repeated for each band, reducers on a `FeatureCollection` must be explicitly repeated using `repeat()`. Specifically, repeat the reducer _m_ times for _m_ inputs. The following error may be thrown as a result of not repeating the reducer:
Dictionary (Error) Collection.reduceColumns: Need 1 inputs for <Reducer>, got 2. 
