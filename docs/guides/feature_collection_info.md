 
#  FeatureCollection Information and Metadata 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Methods for getting information from feature collection metadata are the same as those for image collections. See the [ImageCollection Information and Metadata section](https://developers.google.com/earth-engine/guides/ic_info) for details.
## Metadata aggregation
You can use the aggregation shortcuts to count the number of features or summarize an attribute:
### Code Editor (JavaScript)
```
// Load watersheds from a data table.
varsheds=ee.FeatureCollection('USGS/WBD/2017/HUC06')
// Filter to the continental US.
.filterBounds(ee.Geometry.Rectangle(-127.18,19.39,-62.75,51.29))
// Convert 'areasqkm' property from string to number.
.map(function(feature){
varnum=ee.Number.parse(feature.get('areasqkm'));
returnfeature.set('areasqkm',num);
});
// Display the table and print its first element.
Map.addLayer(sheds,{},'watersheds');
print('First watershed',sheds.first());
// Print the number of watersheds.
print('Count:',sheds.size());
// Print stats for an area property.
print('Area stats:',sheds.aggregate_stats('areasqkm'));
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Load watersheds from a data table.
sheds = (
  ee.FeatureCollection('USGS/WBD/2017/HUC06')
  # Filter to the continental US.
  .filterBounds(ee.Geometry.Rectangle(-127.18, 19.39, -62.75, 51.29))
  # Convert 'areasqkm' property from string to number.
  .map(
    lambda feature: feature.set(
      'areasqkm', ee.Number.parse(feature.get('areasqkm'))
    )
  )
)
# Display the table and print its first element.
m = geemap.Map()
m.add_layer(sheds, {}, 'watersheds')
display(m)
display('First watershed:', sheds.first())
# Print the number of watersheds.
display('Count:', sheds.size())
# Print stats for an area property.
display('Area stats:', sheds.aggregate_stats('areasqkm'))
```

## Column information
Knowing the names and dataypes of `FeatureCollection` columns can be helpful (e.g., [filtering a collection by metadata](https://developers.google.com/earth-engine/guides/feature_collection_filtering)). The following example prints column names and datatypes for a collection of point features representing protected areas.
### Code Editor (JavaScript)
```
// Import a protected areas point feature collection.
varwdpa=ee.FeatureCollection("WCMC/WDPA/current/points");
// Define a function to print metadata column names and datatypes. This function
// is intended to be applied by the `evaluate` method which provides the
// function a client-side dictionary allowing the 'columns' object of the
// feature collection metadata to be subset by dot notation or bracket notation
// (`tableMetadata['columns']`).
functiongetCols(tableMetadata){
print(tableMetadata.columns);
}
// Fetch collection metadata (`.limit(0)`) and apply the
// previously defined function using `evaluate()`. The printed object is a
// dictionary where keys are column names and values are datatypes.
wdpa.limit(0).evaluate(getCols);
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Import a protected areas point feature collection.
wdpa = ee.FeatureCollection('WCMC/WDPA/current/points')
# Fetch collection metadata (`.limit(0)`). The printed object is a
# dictionary where keys are column names and values are datatypes.
wdpa.limit(0).getInfo()['columns']
```
**Note:** Computed collections may not have column information available as part of the collection metadata. Metadata exists for collections within the Data Catalog and those stored as assets. During some operations, however, metadata can be lost (joins, mapping, etc.). Additionally, collections not retrieved from disk ("computed collections", like those derived from lists or `reduceRegions()`) may lack meaningful type information.
For more general purpose `FeatureCollection` aggregation tools, see the [Reducing a FeatureCollection](https://developers.google.com/earth-engine/guides/feature_collection_reducing) page.
