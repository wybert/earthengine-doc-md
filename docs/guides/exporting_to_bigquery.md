 
#  Exporting to BigQuery
Stay organized with collections  Save and categorize content based on your preferences. 
## Overview
Earth Engine's computational architecture is optimized for making image (pixel-based) computation fast and scalable. BigQuery is similarly optimized for scalable processing of tabular data (vectors), and it has many features which make it a nice complement to Earth Engine.
Example workflows include:
  * Performing large BigQuery joins on data generated in Earth Engine
  * Annotating vector data with statistics derived from imagery for further processing in BigQuery
  * Periodically exporting data from Earth Engine into an appendable BigQuery table


If you have other great use cases, we'd love to [hear about them](https://developers.google.com/earth-engine/help#help_others)!
## BigQuery basics
**Key Term:** _BigQuery dataset_ - a top-level container within a Cloud project that's used to organize and control access to your tables.
Earth Engine writes to BigQuery tables, and all tables are contained in datasets. Export tasks fail if the specified dataset isn't present in BigQuery. Find out more in the [BigQuery dataset introduction](https://developers.google.com/bigquery/docs/datasets-intro).
### Dataset creation
Datasets have a number of creation-time options, including the name, storage region, and expiration behavior (along with several other, more advanced options).
There are a variety of mechanisms to [create datasets](https://developers.google.com/bigquery/docs/datasets#create-dataset), but a simple way to get started is via the Cloud console:
  1. Navigate to the [BigQuery page in the Cloud console](https://console.cloud.google.com/bigquery).
  2. Click "Enable" to enable the API, if prompted.
  3. From the "SQL Workspace" tab, click the three-dot menu (more_vert) next to the project.
  4. Choose "Create dataset" option.
  5. Follow the configuration guide.


For all of the options to create and configure a dataset, see the [BigQuery documentation](https://developers.google.com/bigquery/docs/datasets#create-dataset).
### Permissions
In addition to the [standard roles and permissions](https://developers.google.com/earth-engine/cloud/roles_permissions) required to use Earth Engine, callers also need the correct [BigQuery permissions](https://developers.google.com/bigquery/docs/access-control) on the Cloud project or dataset.
  * `bigquery.tables.get`
  * `bigquery.tables.create`
  * `bigquery.tables.updateData`
  * `bigquery.tables.delete`
  * `bigquery.jobs.create`


Any of the following combinations of predefined Identity and Access Management (IAM) roles include the necessary permissions:
  * `bigquery.dataEditor` plus `bigquery.jobUser`
  * `bigquery.dataOwner` plus `bigquery.jobUser`
  * `bigquery.user`
  * `bigquery.admin`


### Pricing
BigQuery is a paid Google Cloud service, so you will incur [charges](https://developers.google.com/bigquery/pricing) for your usage of BigQuery, including storage and analysis of any Earth Engine data that you export to BigQuery.
For details on pricing for Earth Engine's BigQuery export feature, see the [pricing section](https://developers.google.com/earth-engine/guides/exporting_to_bigquery#pricing) below.
## Export configuration
### Syntax
### Code Editor (JavaScript)
```
Export.table.toBigQuery({
collection:features,
table:'myproject.mydataset.mytable',
description:'put_my_data_in_bigquery',
append:true,
overwrite:false
});
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
task = ee.batch.Export.table.toBigQuery(
    collection=features,
    table='myproject.mydataset.mytable',
    description='put_my_data_in_bigquery',
    append=True,
    overwrite=False,
)
task.start()
```

### Automatic or manual schema specification
If there's no table present in BigQuery, Earth Engine attempts to determine a [schema](https://developers.google.com/bigquery/docs/schemas) using the properties of the first `ee.Feature` in the collection. This is a best guess, and it's possible to construct a collection where the schema of the first feature is different from the schema of other features.
If you require a specific schema on your BigQuery table, configure it by [creating an empty table with the target schema](https://developers.google.com/bigquery/docs/tables#create_an_empty_table_with_a_schema_definition).
### Property names
The properties on Earth Engine features correspond to columns in BigQuery. Earth Engine uses the name "geo" to write the `ee.Feature` geometry (the ".geo" selector) to BigQuery.
To avoid any renaming, ensure that your `ee.Feature` objects have properties that are valid [column names](https://developers.google.com/bigquery/docs/schemas#flexible-column-names) and none are named "geo" (since this name is used for the feature's geometry, which has no name in Earth Engine).
Invalid characters in property names cause the export to fail, due to [restrictions on BigQuery column names](https://developers.google.com/bigquery/docs/schemas#flexible-column-names).
### Type conversion
Earth Engine (the values of `ee.Feature` properties) data are converted to an equivalent [BigQuery type](https://developers.google.com/bigquery/docs/reference/standard-sql/data-types) when possible. Note that nullability is controlled by the table schema, not the type.
**Earth Engine type** | **BigQuery type** | **Notes**  
---|---|---  
`ee.String` | `STRING` |   
`ee.Number` |  `FLOAT` or `INTEGER` |   
`ee.Geometry` | `GEOGRAPHY` |   
`ee.Date` | `TIMESTAMP` |   
`ee.ByteString` | `BYTES` |   
`ee.Array` |  `STRUCT<ARRAY<INT64>,` `ARRAY<INT64|FLOAT64>>` | See the section on [arrays](https://developers.google.com/earth-engine/guides/exporting_to_bigquery#arrays)  
Other `ee.*` types  | not supported  | See the section on [JSON values](https://developers.google.com/earth-engine/guides/exporting_to_bigquery#json-values)  
### Arrays
Earth Engine exports any multi-dimensional `ee.Array` to `STRUCT<ARRAY<INT64> dimensions, ARRAY<INT64|FLOAT64> values>`, similar to the format used by BigQuery's [ML.DECODE_IMAGE](https://developers.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-decode-image) function.
The first array in the struct, `dimensions`, contains the dimensions of the Earth Engine array, $d_1$ through $d_n$.
The second array in the struct, `values`, contains all of the values in the multi-dimensional array, flattened into a single BigQuery array. The total number of values in the flattened array is $\sum_{i=1}^n d_i$, and the value at index $(i_i, \ldots, i_n)$ in the original Earth Engine array corresponds to the value at the following index in the flattened array:
\\[ \sum_{j=1}^n \left( i_j \cdot \prod_{k=j+1}^n d_k \right) \\]
For common cases, the indexing expression for the `values` array is as follows:
**Array Size** | **Dimensions** | **Indexing Expression**  
---|---|---  
1-dimensional | `d1` | `[i1]`  
2-dimensional | `d1, d2` | `[(i1 * d2) + i2]`  
3-dimensional | `d1, d2, d3` | `[(i1 * d2 * d3) + (i2 * d3) + i3]`  
For example, consider a `2x3x4` Earth Engine array:
```
ee.Array([
[
[1,2,3,4],
[5,6,7,8],
[9,10,11,12]
],
[
[13,14,15,16],
[17,18,19,20],
[21,22,23,24]
]
]);

```

This array translates to a BigQuery `STRUCT` whose `dimensions` element is the array `[2, 3, 4]` and whose `values` element is the flattened array `[1, 2, 3, 4, 5, 6, 7, 8, ..., 21, 22, 23, 24]`. The indexes in the flattened array can be computed as `[(i1 * 12) + (i2 * 4) + i3]`.
### JSON values
To support more richly structured data within a cell, it's possible to encode Earth Engine values as [JSON](https://json.org) objects. BigQuery supports [SQL operations over JSON-encoded data](https://developers.google.com/bigquery/docs/json-data), allowing for queries which "look inside" the encoded JSON values you produce in Earth Engine.
### Code Editor (JavaScript)
```
varstates=ee.FeatureCollection('TIGER/2018/States');
varmod11a1=ee.ImageCollection('MODIS/061/MOD11A1');

// Find the max day and night temperatures per pixel for a given time.
varmaxTemp=mod11a1
.select(['LST_Day_1km','LST_Night_1km'])
.filterDate('2023-05-15','2023-05-25')
.max();

// Annotate each state with its max day/night temperatures.
varannotatedStates=states.map(function(e){
vardict=maxTemp.reduceRegion({
reducer:ee.Reducer.max(),
geometry:e.geometry(),
scale:10*1000,// 10 km
});
// Convert the dictionary to JSON and add it as a property.
returne.set('maxTemp',ee.String.encodeJSON(dict));
});

Export.table.toBigQuery(annotatedStates);
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
states = ee.FeatureCollection('TIGER/2018/States')
mod11a1 = ee.ImageCollection('MODIS/061/MOD11A1')

# Find the max day and night temperatures per pixel for a given time.
max_temp = (
    mod11a1.select(['LST_Day_1km', 'LST_Night_1km'])
    .filterDate('2023-05-15', '2023-05-25')
    .max()
)


defget_max_temp_for_state(e):
  max_temp_dict = max_temp.reduceRegion(
      reducer=ee.Reducer.max(),
      geometry=e.geometry(),
      scale=10 * 1000,  # 10 km
  )
  # Convert the dictionary to JSON and add it as a property.
  return e.set('maxTemp', ee.String.encodeJSON(max_temp_dict))


# Annotate each state with its max day/night temperatures.
annotated_states = states.map(get_max_temp_for_state)

task = ee.batch.Export.table.toBigQuery(
    collection=annotated_states, table='myproject.mydataset.mytable'
)
task.start()
```

### Geometry conversion
BigQuery has [limited support for different projections](https://developers.google.com/bigquery/docs/geospatial-data), so all Earth Engine geometries are transformed to geodesic `EPSG:4326` using an error margin of 1 meter.
To have finer control over this transformation process, you can manually map over the features and transform their geometries, e.g.:
### Code Editor (JavaScript)
```
vartransformedCollection=originalCollection.map(functiontransformGeo(e){
varmyErrorMargin=10*1000;// meters
returne.setGeometry(e.geometry(myErrorMargin,'EPSG:4326',true));
});
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
deftransform_geo(e):
  my_error_margin = 10 * 1000  # meters
  return e.setGeometry(e.geometry(my_error_margin, 'EPSG:4326', True))


transformed_collection = original_collection.map(transform_geo)
```
**Caution:** Polygons larger than a hemisphere may have their orientation reversed during export. See [known issues](https://developers.google.com/earth-engine/guides/exporting_to_bigquery#known_issue_orientation) for more detail.
## Performance
### Earth Engine performance
Earth Engine computation is often the bottleneck for `Export` operations. To this end, it's important to organize your processing for maximal parallelism. Any computation which bakes in serial processing (for example, `ee.FeatureCollection.iterate()`) can cause your export to run slowly or fail.
### Performance in BigQuery
Correctly structuring and [clustering](https://developers.google.com/bigquery/docs/clustered-tables) data is the best way to ensure that queries can be made efficient in BigQuery. If there isn't a table already present in BigQuery, tables exported from Earth Engine are clustered on the features' geometry (if it's present). Clustering by the geography field is very common for geospatial data. It improves performance and reduces cost for queries that use spatial filters, most commonly for BigQuery operations like:
```
WHEREST_DWithin(<table_column>,constant_geography>,distance>)

```
```
WHEREST_Intersects(<table_column>,constant_geography>)

```

Adding clustering to an unclustered table also does not generally harm anything, though it might slightly increase the time to load data to the table. For more on query optimization, see the [BigQuery documentation](https://developers.google.com/bigquery/docs/best-practices-performance-overview).
Note that clustering settings only affect _new_ data written to the table.
### Demo: using `reduceRegions`
In some cases, it's possible to use `reduceRegions` to get as much parallelism as possible from the Earth Engine processing infrastructure. This example demonstrates how to use a smaller number of `reduceRegions` calls (a few hundred) rather than tens of thousands of `reduceRegion` calls (the typical approach for mapping a function over a collection).
### Code Editor (JavaScript)
```
varlucas=ee.FeatureCollection('JRC/LUCAS_HARMO/COPERNICUS_POLYGONS/V1/2018');
vars2=ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED');

// Fetch the unique date values from the dataset.
vardates=lucas.aggregate_array('survey_date')
.distinct()
.map(function(date){
returnee.Date.parse('dd/MM/yy',date);
});

// For each date, annotate the LUCAS samples with the Sentinel-2 band values for
// a two-week window.
functiongetLucasSamplesForDate(date){
date=ee.Date(date);
varimageForDate=s2
.filterDate(
date.advance(-1,'week'),
date.advance(1,'week'))
.select('B.*');
varmedian=imageForDate.median();
varlucasForDate=lucas.filter(
ee.Filter.equals('survey_date',date.format('dd/MM/yy')));
varsample=median.reduceRegions({
collection:lucasForDate,
reducer:ee.Reducer.mean(),
scale:10,
tileScale:8,
});
returnsample;
}

// Flatten the collection.
varwithSamples=
ee.FeatureCollection(dates.map(getLucasSamplesForDate))
.flatten();

Export.table.toBigQuery({
collection:withSamples,
description:'lucas_s2_annotated'
});
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
lucas = ee.FeatureCollection('JRC/LUCAS_HARMO/COPERNICUS_POLYGONS/V1/2018')
s2 = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')

# Fetch the unique date values from the dataset.
dates = (
    lucas.aggregate_array('survey_date')
    .distinct()
    .map(lambda date: ee.Date.parse('dd/MM/yy', date))
)


# For each date, annotate the LUCAS samples with the Sentinel-2 band values for
# a two-week window.
defget_lucas_samples_for_date(date):
  date = ee.Date(date)
  image_for_date = s2.filterDate(
      date.advance(-1, 'week'), date.advance(1, 'week')
  ).select('B.*')
  median = image_for_date.median()
  lucas_for_date = lucas.filter(
      ee.Filter.equals('survey_date', date.format('dd/MM/yy'))
  )
  sample = median.reduceRegions(
      collection=lucas_for_date,
      reducer=ee.Reducer.mean(),
      scale=10,
      tileScale=8,
  )
  return sample


# Flatten the collection.
with_samples = ee.FeatureCollection(
    dates.map(get_lucas_samples_for_date)
).flatten()

task = ee.batch.Export.table.toBigQuery(
    collection=with_samples,
    table='myproject.mydataset.mytable',
    description='lucas_s2_annotated',
)
task.start()
```

### Task parallelization
With the `{append: true}` option, it's possible for multiple tasks to write data to a BigQuery table concurrently. This is a mechanism for writing data with a higher throughput, but it comes at the cost of increased complexity (managing the task queue, retrying, etc.).
### Performance differences between `append` and `overwrite` parameters
Note that overwriting is slower than appending because BigQuery must process the new data before overwriting the old. Setting the {overwrite: true} parameter when exporting to an existing BigQuery table triggers a safe overwrite process:
  1. Temporary table: data is exported to a new, temporary table within the destination dataset.
  2. Atomic overwrite: the temporary table's contents are copied to the final destination table, replacing existing data in a single, atomic transaction.
  3. Cleanup: the temporary table is deleted.


This ensures that errors during the export won't corrupt your existing data. For small tables, the delay is typically a few minutes.
### High-performance alternatives
For workflows which require very high throughput, consider using [GeoBeam to move data from Earth Engine to BigQuery](https://cloud.google.com/blog/products/data-analytics/ingest-geospatial-data-from-earth-engine-into-bigquery-using-geobeam). This requires more configuration and infrastructure, so we suggest starting with the built-in Earth Engine functionality.
## Pricing
**Caution:** Even if you use Earth Engine for free as a noncommercial or non-operational user, using BigQuery [generates charges](https://developers.google.com/bigquery/pricing) in your Cloud project's Google Cloud Billing account.
Exporting to BigQuery is a batch process which consumes batch EECU-time. If you use Earth Engine commercially or operationally, exporting data to BigQuery charges you for the EECU-time that the tasks use. All usage can be monitored with exactly the same [monitoring](https://developers.google.com/earth-engine/guides/monitoring_usage) tools that work for the rest of Earth Engine.
### Cloud billing accounts
To write data to BigQuery, the associated Cloud project needs to have a billing account enabled. To learn more about billing account configuration, see the [Cloud billing account docs](https://cloud.google.com/billing/docs/how-to/manage-billing-account).
### Egress
**Preview:** Writes from Earth Engine to BigQuery don't generate Cloud ingress or egress charges at this time, but they will in the future.
All ingress and egress costs are charged as standard network traffic.
Earth Engine is only hosted in the US, but BigQuery datasets can be hosted in a number of other [regions](https://cloud.google.com/about/locations). Depending on the regions and data volumes involved, writing data from Earth Engine to BigQuery can generate substantial network traffic.
## Known issues
### Orientation for large polygons
The BigQuery export function inverts polygons that are larger than a hemisphere by reversing their orientation (changing the polygon to its geometric complement). In rare cases, polygons larger than a hemisphere may fail to load.
If needed, polygons that have been inverted can be corrected within BigQuery by inverting them again, using the BigQuery expression `ST_Difference(ST_GeogFromText('fullglobe'), geo)`.
For more information, see [here](https://issuetracker.google.com/issues/296847446).
