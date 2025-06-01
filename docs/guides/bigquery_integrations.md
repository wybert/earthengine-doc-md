 
#  BigQuery integrations 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Query raster data within BigQuery](https://developers.google.com/earth-engine/guides/bigquery_integrations#query_raster_data_within_bigquery)
  * [Read BigQuery data from Earth Engine](https://developers.google.com/earth-engine/guides/bigquery_integrations#read_bigquery_data_from_earth_engine)
  * [Write Earth Engine vector data to BigQuery](https://developers.google.com/earth-engine/guides/bigquery_integrations#write_earth_engine_vector_data_to_bigquery)


BigQuery excels as a serverless data warehouse for petabyte-scale SQL analysis, including vector data using the `GEOGRAPHY` data type. Google Earth Engine provides a planetary-scale platform specializing in geospatial raster analysis and offers a vast data catalog. Their combination creates a uniquely comprehensive environment for tackling complex geospatial challenges that involve both vector and raster data.
The integration of BigQuery and Earth Engine enables efficient workflows where BigQuery's vector data can be enriched with Earth Engine's raster insights, and Earth Engine analyses can access data stored and managed in BigQuery. By using both, you gain access to:
  * **BigQuery** : Scalable storage and SQL-based analysis for large vector datasets.
  * **Earth Engine** : Powerful processing of petabytes of raster data and access to a rich geospatial catalog.


The primary ways these platforms interoperate are:
  * **Querying raster data within BigQuery** : Using the `ST_REGIONSTATS` SQL function to perform zonal statistics directly in BigQuery.
  * **Reading BigQuery data into Earth Engine** : Accessing BigQuery tables or query results as `ee.FeatureCollection` objects for use in Earth Engine scripts.
  * **Writing Earth Engine data to BigQuery** : Exporting `ee.FeatureCollection` results from Earth Engine analyses to BigQuery tables for storage and further analysis.


The following sections provide additional details about each of these features.
## Query raster data within BigQuery
The BigQuery `ST_REGIONSTATS` function brings Earth Engine's raster analysis to BigQuery SQL. It calculates regional statistics on raster data for BigQuery tables with `GEOGRAPHY` data.
  * **Key use:** Zonal statistics and raster analysis within BigQuery.
  * **Data sources:** Analytics Hub, Cloud Storage GeoTIFF, Earth Engine assets.


This function lets you query Earth Engine's 100+ PB geospatial [data catalog](https://developers.google.com/earth-engine/datasets) directly within BigQuery. You can also apply this function to your own Earth Engine assets as well as GeoTIFFs in Cloud Storage.
Learn more about `ST_REGIONSTATS` in BigQuery's [Work with raster data](https://cloud.google.com/bigquery/docs/raster-data) page.
## Read BigQuery data from Earth Engine
Earth Engine can directly access BigQuery data as `ee.FeatureCollection` objects, allowing you to visualize and incorporate BigQuery data in Earth Engine analyses.
  * `ee.FeatureCollection.loadBigQueryTable()`: Reads a BigQuery table into Earth Engine.
  * `ee.FeatureCollection.runBigQuery()`: Executes a BigQuery SQL query and retrieves results into Earth Engine.


These functions enable seamless use of BigQuery's vector data within Earth Engine's raster-centric geospatial analysis platform.
Learn more about these functions in the [Read from BigQuery](https://developers.google.com/earth-engine/guides/read_from_bigquery) page.
## Write Earth Engine vector data to BigQuery
Earth Engine can export vector data to BigQuery using the [`Export.table.toBigQuery()`](https://developers.google.com/earth-engine/apidocs/export-table-tobigquery) function.
  * **Functionality:** Exports `ee.FeatureCollection` objects to BigQuery tables.
  * **Benefits:** Enables further analysis, integration, and storage of Earth Engine results in BigQuery.


This facilitates a workflow where vector data results from Earth Engine's processing are readily available in BigQuery.
Learn more about writing Earth Engine vector data to BigQuery in the [Exporting to BigQuery](https://developers.google.com/earth-engine/guides/exporting_to_bigquery) page.
