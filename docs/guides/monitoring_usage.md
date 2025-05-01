 
#  Monitoring usage 
Stay organized with collections  Save and categorize content based on your preferences. 
This page describes how to create charts to monitor Earth Engine compute and storage consumption using Cloud Monitoring.
There are other ways to monitor Earth Engine usage from the Cloud Console, which are not the focus of the document but include:
  * The **APIs & Services > Metrics** [page](https://console.cloud.google.com/apis/api/earthengine.googleapis.com/metrics), which shows basic metrics including traffic (number of requests), errors and latency (per API method, response code or credentials).
  * The **APIs & Services > Quotas & System Limits** [page](https://console.cloud.google.com/apis/api/earthengine.googleapis.com/quotas), which shows the amount of stored assets in bytes and the number of read requests for the assets.
  * The **APIs & Services > Credentials** [page](https://console.cloud.google.com/apis/api/earthengine.googleapis.com/credentials), which shows which credentials (e.g, service accounts) have been used to access the API.


## View consumption in Cloud Monitoring
### Chart metrics in Metrics Explorer
  1. Go to the **Monitoring > Metrics Explorer** page in the Cloud Console.
[Go to Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer)
  2. Select the name of your project if it is not already selected at the top of the page.
     * Note: You must have the [appropriate Identity and Access Management (IAM) permissions](https://cloud.google.com/monitoring/access-control#grant-monitoring-access) to access monitoring data.
  3. Click **Select a metric** to choose a metric to add to the chart.
     * Earth Engine metrics are under the **Earth Engine Cloud Project** resource.
     * By default, only resources and metrics that were active in the past hour are visible. Adjust the time range or un-check the "Active" filter to see more metrics.
  4. Once you've selected a metric, click **Apply**.
  5. In the top pane, configure the drop-down filters to set how to visualize the data.
     * By default, the explorer will show a rate aggregation for compute metrics. See the [Units and Aligners](https://developers.google.com/earth-engine/guides/monitoring_usage#units-and-aligners) section for details on choosing a different Aligner and showing explicit units.
     * For example, to see the total completed batch compute used per `workload_tag` (see [Workload tags](https://developers.google.com/earth-engine/guides/monitoring_usage#workload-tags) section) over the past week, you could choose the following settings. Here, each data point represents the total amount of EECU-hours each completed batch task used. ![Example Metrics Explorer
configuration](https://developers.google.com/static/earth-engine/images/Monitoring_completed_eecus.png)


The [Cloud Monitoring documentation](https://cloud.google.com/monitoring/docs) provides more guides on using Cloud Monitoring. In particular, the [Select the metrics to chart](https://cloud.google.com/monitoring/charts/metrics-selector) page provides a detailed overview of different ways to build queries, and the [Filtering and aggregation](https://cloud.google.com/monitoring/api/v3/aggregation) page provides more information about configuring the time series.
### Available Metrics
Earth Engine metrics are in preview and are subject to change.  Metric | Description | Available labels  
---|---|---  
Completed EECU-seconds |  Earth Engine compute usage of successful requests in [ EECU-seconds](https://developers.google.com/earth-engine/guides/computation_overview#eecus). Usage is reported when a request completes and is not reported for failed requests.  |  **`compute_type`**: The type of compute, based on the[ processing environment](https://developers.google.com/earth-engine/guides/processing_environments) of the request. One of [`online`, `batch`, `highvolume`]. **`client_type`**: The client type (if known), for example:`ee-js/latest` or `python/v0.1.300`. Client type is not set for batch compute. **`workload_tag`**: The workload tag (if supplied in the client), for example:`my-export1`. See the [ Workload tags ](https://developers.google.com/earth-engine/guides/monitoring_usage#workload-tags) section for how to set this label.   
In-progress EECU-seconds |  Earth Engine compute usage of all requests in [ EECU-seconds](https://developers.google.com/earth-engine/guides/computation_overview#eecus). Usage is reported periodically as a request is running.  |  **`compute_type`**: The type of compute, based on the[ processing environment](https://developers.google.com/earth-engine/guides/processing_environments) of the request. One of [`online`, `batch`, `highvolume`]. **`client_type`**: The client type (if known), for example:`ee-js/latest` or `python/v0.1.300`. Client type is not set for batch compute. **`workload_tag`**: The workload tag (if supplied in the client), for example:`my-export1`. See the [ Workload tags ](https://developers.google.com/earth-engine/guides/monitoring_usage#workload-tags) section for how to set this label.   
Used Bytes | The number of bytes of Earth Engine asset storage used. Sampled every 30 minutes. | N/A  
For a complete list of available metrics in Cloud Monitoring, see [Google Cloud metrics](https://cloud.google.com/monitoring/api/metrics_gcp).
### Units and Aligners
By default, compute metrics will be displayed as a unitless rate of the average EECU-seconds used per-second over the **Min interval** (default 1 minute).
To see the raw EECU-time used with explicit units, click the **Aggregation** field in your query and choose "Configure aligner" from the resulting menu. This replaces the aggregation operation with two new operations: **Grouping** and **Alignment function**. Choosing "Grouping: `Sum`" and "Alignment function: `Sum`" will construct a graph with explicit units, representing the total EECU-time being used at each data point. See the [Aligner reference](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#aligner) for a list of possible Aligners.
### Workload Tags
Workload tags are labels for monitoring specific computations within Earth Engine. Use `setDefaultWorkloadTag` to bind all computations in the script to a default workload tag unless one is explicitly set with [](https://developers.google.com/earth-engine/apidocs/ee-data-setworkloadtag)`ee.data.setWorkloadTag`, in which case the default is overridden. These methods set the `workload_tag` label for specific computations and export tasks.
You can then monitor and track tagged computations in the [Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer) using the **Earth Engine Cloud Project > Project > Used EECUs** metric, and grouping or filtering by `workload_tag`.
**Note:** the name passed to `ee.data.setWorkloadTag` must be under 64 characters long, begin and ending with an alphanumeric character (`[a-zA-Z0-9]`) with dashes (`-`), underscores (`_`), and alphanumerics between, and not be empty.
For example, to monitor the EECUs used for an image computation and/or and export:
### Code Editor (JavaScript)
```
// Set a default workload tag.
ee.data.setDefaultWorkloadTag('landsat-compositing')
varcomposite=ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
.filterDate('2020-01-01','2021-01-01')
.median();
// Set a workload tag for export.
ee.data.setWorkloadTag('export-jobs');
Export.image.toAsset(composite);
ee.data.resetWorkloadTag();// Reset to landsat-compositing
ee.data.resetWorkloadTag(true);// Reset back to empty
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Authenticate, then initialize with your Cloud Project.
ee.Initialize(project='your-project')
# Set a default workload tag.
ee.data.setDefaultWorkloadTag('landsat-compositing')
composite = (
  ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
  .filterDate('2020-01-01', '2021-01-01')
  .median()
)
# Set a workload tag for export.
ee.data.setWorkloadTag('export-jobs')
ee.batch.Export.image.toAsset(composite).start()
ee.data.resetWorkloadTag() # Reset to landsat-compositing
ee.data.resetWorkloadTag(True) # Reset back to empty
# Alternatively, use a workload tag with the `with` context manager.
with ee.data.workloadTagContext('export-jobs'):
 ee.batch.Export.image.toAsset(composite).start()
```

In this example, all computations are annotated with the `landsat-compositing` tag (set as default), and the export gets its own workload tag since [](https://developers.google.com/earth-engine/apidocs/ee-data-setworkloadtag)`ee.data.setWorkloadTag` is called before running it. Use [](https://developers.google.com/earth-engine/apidocs/ee-data-resetworkloadtag)`ee.data.resetWorkloadTag` to set back to the default tag or to set the default tag back to an empty string.
