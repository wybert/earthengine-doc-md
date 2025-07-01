 
#  Read from BigQuery
Stay organized with collections  Save and categorize content based on your preferences. 
**Note:** The [`ee.FeatureCollection.loadBigQueryTable()`](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-loadbigquerytable) and [`ee.FeatureCollection.runBigQuery()`](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-runbigquery) functions are in [**Preview**](https://cloud.google.com/products#product-launch-stages). To request support or provide feedback for them, email bigquery-earthengine-preview-support@google.com.
This page describes how to integrate BigQuery tables into Earth Engine workflows as `ee.FeatureCollection` objects, using the [`ee.FeatureCollection.loadBigQueryTable()`](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-loadbigquerytable) and [`ee.FeatureCollection.runBigQuery()`](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-runbigquery) methods.
## Load data from BigQuery
**Preview:** The [`ee.FeatureCollection.loadBigQueryTable()`](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-loadbigquerytable) function is in [**Preview**](https://cloud.google.com/products#product-launch-stages) and may change.
The [`ee.FeatureCollection.loadBigQueryTable()`](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-loadbigquerytable) function seamlessly reads a BigQuery table into an `ee.FeatureCollection` object. It connects to a specified table, converts all data types, [applies the necessary filters and selectors](https://developers.google.com/earth-engine/guides/read_from_bigquery#data_filtering), and adds indexing to the collection if necessary. The function uses Earth Engine's [interactive environment](https://developers.google.com/earth-engine/guides/processing_environments#interactive_environment), returning results directly to the client to be viewed or used as a component of a larger analysis.
### JavaScript
```
// Load the BigQuery table with a specified geometry column.
varfeatures=ee.FeatureCollection.loadBigQueryTable({
table:'my_project.my_dataset.my_table',
geometryColumn:'geo'
});
// Display features on the map.
Map.addLayer(features);

```

### Python
```
# Load the BigQuery table with a specified geometry column.
features = ee.FeatureCollection.loadBigQueryTable(
  table='my_project.my_dataset.my_table',
  geometryColumn='geo')
# Display the first feature.
display(features.first().getInfo())
   
```

### Billing
The cost of EECU-hours used during processing of the request is billed to the caller like for any other Earth Engine method (see [EECUs overview](https://developers.google.com/earth-engine/guides/computation_overview#eecus)).
There are no additional BigQuery costs associated with transferring the data to Earth Engine. Corresponding BigQuery usage will be visible in used project's [Google Cloud API Dashboard](https://console.cloud.google.com/apis/dashboard) (see [Monitoring API usage](https://cloud.google.com/apis/docs/monitoring)), but no cost will be incurred for reading BigQuery data this way.
## Query data from BigQuery
**Preview:** The [`ee.FeatureCollection.runBigQuery()`](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-runbigquery) function is in [**Preview**](https://cloud.google.com/products#product-launch-stages) and may change.
The [`ee.FeatureCollection.runBigQuery()`](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-runbigquery) method runs a BigQuery SQL query and returns the results as an `ee.FeatureCollection` object (see [Run a query doc](https://cloud.google.com/bigquery/docs/running-queries) to learn more about queries).
### JavaScript
```
// Construct a BigQuery query.
varquery='SELECT * FROM my_project.my_dataset.my_table WHERE column > 1000';
// Run the query and return the results as a FeatureCollection.
varfeatures=ee.FeatureCollection.runBigQuery(query);
// Print the first feature.
print(features.first());

```

### Python
```
# Construct a BigQuery query.
query = 'SELECT * FROM my_project.my_dataset.my_table WHERE column > 1000'
# Run the query and retrieve the results as a FeatureCollection.
features = ee.FeatureCollection.runBigQuery(query)
# Print the first feature.
print(features.first().getInfo())
   
```

### BigQuery queries
Each call to [`ee.FeatureCollection.runBigQuery()`](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-runbigquery) initiates a separate BigQuery query job (see more about queries in [Run a query documentation](https://cloud.google.com/bigquery/docs/running-queries)), allowing you to use key BigQuery capabilities:
  * **Job history** : Access a six-month history of your project's query executions (see more at [List jobs](https://cloud.google.com/bigquery/docs/managing-jobs#list_jobs_in_a_project)).
  * **Query caching** : BigQuery automatically caches query results when possible. Subsequent identical queries retrieve data from the cache, preventing redundant charges (see more at [Using cached query results](https://cloud.google.com/bigquery/docs/cached-results))


To learn about queries or how to use them in BigQuery see [BigQuery documentation](https://cloud.google.com/bigquery/docs/running-queries).
### Billing
Cost of EECUs used during processing of the request is billed to the caller like for any other Earth Engine method (see [EECUs overview](https://developers.google.com/earth-engine/guides/computation_overview#eecus)). Additionally **running a query is billed** to the caller according to [the BigQuery billing model](https://cloud.google.com/bigquery/pricing#overview_of_pricing).
There are no additional BigQuery costs associated with transferring the data to Earth Engine. Corresponding BigQuery usage will be visible in used project's [Google Cloud API Dashboard](https://console.cloud.google.com/apis/dashboard) (see [Monitoring API usage](https://cloud.google.com/apis/docs/monitoring)), but no cost will be incurred for reading BigQuery data this way.
To control potential costs associated with [`ee.FeatureCollection.runBigQuery()`](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-runbigquery), the `maxBytesBilled` parameter acts as a safeguard. Any BigQuery job that exceeds this limit will fail and won't be billed. The default value of `maxBytesBilled` is 100 GB. If your call is blocked by exceeding this limit, you can specify a different value in your script.
## Prerequisites and permissions
To use this feature, the caller's Cloud project needs to have BigQuery API and BigQuery Storage API enabled. Follow instructions [on the Enable API page](https://cloud.google.com/endpoints/docs/openapi/enable-api) to enable appropriate APIs.
In addition to [the standard Earth Engine roles and permissions](https://developers.google.com/earth-engine/guides/exporting_to_bigquery#permissions), you need to have read access on the referenced BigQuery table, permission to create read sessions and jobs in the target project. The specific BigQuery permissions required are:
  * `bigquery.tables.get` (on any accessed table)
  * `bigquery.tables.getData` (on any accessed table)
  * `bigquery.readSession.create`
  * `bigquery.jobs.create`


Refer to the [BigQuery access control documentation](https://cloud.google.com/bigquery/docs/access-control) for detailed information on managing permissions.
## Data filtering
Every `ee.FeatureCollection` can be filtered using the [`.filter(Filter)`](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-filter) method. To allow Google Earth Engine users to benefit from highly parallelized BigQuery tabular data processing, we translate Earth Engine filters to language understandable by BigQuery and send them together with a read table request. This approach indeed moves filter processing to BigQuery stack, but it also is subject to two limitations:
  1. Like every other query in BigQuery (see [BigQuery quotas](https://cloud.google.com/bigquery/quotas#query_jobs)) this request is limited to 10 MB in size. This means that passed filters cannot be overly complicated. Hitting the 10 MB limit results in the following error:
> `Filter sent to BigQuery is too long. This error may be caused by too complicated geometry in geometry filters. Consider simplifying the filter and used values.`
Filtering by geometries that contain many vertices is a common cause for this error. To solve this issue consider using [ee.Geometry.simplify()](https://developers.google.com/earth-engine/apidocs/ee-geometry-simplify) on the problematic object.
  2. Some more complicated Earth Engine filters can't be converted to their BigQuery equivalents. For example, BigQuery does not support ARRAY equality checks. In such cases, we don't translate the filter and instead apply it in Earth Engine after reading the data.


## Data indexing
Earth Engine collections rely on internal indexing, whereas BigQuery discourages keeping tables indexed. To make those two systems work together we create collection indexes in the following way:
  * If the BigQuery table contains a column named `system:index`, we use it for indexing FeatureCollection.
In such cases it is on the caller to make sure indexes are unique. Otherwise the collection may misbehave in an unexpected manner. Feature index must be a non-empty string, so loading BigQuery table with a non-string or `null` value for a `system:index` column will fail.
  * If the BigQuery table does not contain the `system:index` column, it is generated automatically.
Indexes in between two read requests are stable, but only if the requests are exactly the same, taking filters into account. Otherwise we cannot rely on indexes to correspond to the same features. Therefore if precisely unique data indexing is important for the caller, we recommend adding the `system:index` column in BigQuery manually.


## Limitations
  * The size of all selected columns of the table referenced in a [`ee.FeatureCollection.loadBigQueryTable()`](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-loadbigquerytable) call is limited to 400 GB. Hitting this limit will result in the following error:
> `Failed to read table from BigQuery: Requested data size is too large to read. Consider using selectors to specify only required columns.`
In such cases consider choosing more restrictive selectors to read-only necessary columns or consider using [`ee.FeatureCollection.runBigQuery()`](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-runbigquery) to preprocess the table in BigQuery and lower the amount of fetched data.
  * The [`ee.FeatureCollection.runBigQuery()`](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-runbigquery) method imposes a 10 GB limit on query result sizes. Although source tables can be of arbitrary size, processing larger data volumes will increase query costs.
  * Translated filter size is limited to 10 MB. See the [Data filtering](https://developers.google.com/earth-engine/guides/read_from_bigquery#data_filtering) section for details.
  * Using `ee.FeatureCollection.loadBigQueryTable()` or `ee.FeatureCollection.runBigQuery()` is not available with Earth Engine apps.


## Caveats
  * The [`ee.FeatureCollection.loadBigQueryTable()`](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-loadbigquerytable) does not support resources from [Linked Datasets](https://cloud.google.com/bigquery/docs/analytics-hub-introduction#linked_datasets). Trying to load data from such table results in "table not found" error.
As a workaround, consider running [`ee.FeatureCollection.runBigQuery()`](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-runbigquery) with a query specifying the requested table from the linked dataset. For example:
### JavaScript
```
varfeatures=ee.FeatureCollection.runBigQuery({
query:'SELECT * FROM my_project.my_linked_dataset.my_table',
geometryColumn:'geo'
});

```

### Python
```
features = ee.FeatureCollection.runBigQuery(
 query='SELECT * FROM my_project.my_linked_dataset.my_table',
 geometryColumn='geo')
   
```

  * Joining on `system:index` for BigQuery tables with auto-generated IDs may lead to unexpected behaviours. To prevent this from happening, consider adding `system:index` to BigQuery table manually or joining the table on a different property. Read more about indexing in the [Data indexing section](https://developers.google.com/earth-engine/guides/read_from_bigquery#data_indexing).
  * The [`ee.FeatureCollection.randomColumn()`](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-randomcolumn) method does not work with BigQuery auto-generated IDs. Consider specifying an alternative key using the `rowKeys` parameter in the [`ee.FeatureCollection.randomColumn()`](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-randomcolumn) method. You can also manually add `random` or `system:index` columns to the BigQuery source table. Read more about indexing in the [Data indexing section](https://developers.google.com/earth-engine/guides/read_from_bigquery#data_indexing).


