 
#  Earth Engine quotas 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Types of quota](https://developers.google.com/earth-engine/guides/usage#types_of_quota)
  * [Adjustable quota limits](https://developers.google.com/earth-engine/guides/usage#adjustable_quota_limits)
    * [Concurrent interactive requests](https://developers.google.com/earth-engine/guides/usage#concurrent_interactive_requests)
    * [Rate of requests (QPS)](https://developers.google.com/earth-engine/guides/usage#rate_of_requests_qps)
    * [Concurrent batch tasks](https://developers.google.com/earth-engine/guides/usage#concurrent_batch_tasks)
    * [Asset storage quota](https://developers.google.com/earth-engine/guides/usage#asset_storage_quota)
    * [User seats](https://developers.google.com/earth-engine/guides/usage#user_seats)
  * [Fixed quota limits](https://developers.google.com/earth-engine/guides/usage#fixed_quota_limits)
    * [Computation time](https://developers.google.com/earth-engine/guides/usage#computation_time)
    * [Per-request memory footprint](https://developers.google.com/earth-engine/guides/usage#per-request_memory_footprint)
    * [Aggregations](https://developers.google.com/earth-engine/guides/usage#aggregations)
    * [Table import limits](https://developers.google.com/earth-engine/guides/usage#table_import_limits)
    * [Request payload size](https://developers.google.com/earth-engine/guides/usage#request_payload_size)
    * [Task queue length](https://developers.google.com/earth-engine/guides/usage#task_queue_length)
  * [BigQuery raster functions quota limits](https://developers.google.com/earth-engine/guides/usage#bigquery_raster_functions_quota_limits)
    * [BigQuery slot-time per day](https://developers.google.com/earth-engine/guides/usage#bigquery_slot-time_per_day)


## Types of quota
The Earth Engine platform has a number of quota limits in place to ensure that resources are distributed fairly across users. Since there are many different types of resources available in Earth Engine (computation, storage, etc.), there are many different types of quota limits.
The primary distinction between different quota types is whether they're adjustable. For some types of quota, we're able to change the limits on a per-user or per-project basis, while other types are system-wide limits which can't be changed.
**Warning:** Quota restrictions exist to ensure the availability of computing resources for the entire Earth Engine community. Attempting to circumvent quota restrictions through the use of multiple Google Accounts is a violation of the [Earth Engine Terms of Service](https://earthengine.google.com/terms/).
## Adjustable quota limits
The following limits **may be adjusted** on a per-project basis. See [the help page](https://developers.google.com/earth-engine/help#additional_quota) for how to request additional quota.
Quota type | Default value (per project)  
---|---  
Max concurrent requests (standard endpoint) | 40 concurrent requests   
Max concurrent requests (high-volume endpoint) | 40 concurrent requests   
Max rate of requests (per project) | 100 requests/s (6000 requests/min)  
Max rate of requests (per account) | 100 requests/s (6000 requests/min)  
Average concurrent batch tasks | 2 tasks (on average)  
Max asset storage space | 250 GB  
Max number of assets | 10,000  
### Concurrent interactive requests
Each project can make [interactive requests](https://developers.google.com/earth-engine/guides/processing_environments#interactive-environment) in parallel, up to a quota limit. If the limit is exceeded, Earth Engine will return ["HTTP 429: Too Many Requests" errors](https://www.rfc-editor.org/rfc/rfc6585#section-4). Generally, these errors are handled by the Earth Engine client library, which wraps requests in exponential backoff, retrying the query until it succeeds. The Earth Engine client library will retry the request up to five times.
To help avoid receiving these 429 errors, you may want to enable caching for your application, for example using memcache, to avoid redundant queries when possible. If using an older version of the Earth Engine client library that does not retry queries automatically, or if a query is still not completed after five retries, you may need to implement exponential backoff around requests.
### Rate of requests (QPS)
In addition to the [concurrency limits](https://developers.google.com/earth-engine/guides/usage#concurrent_interactive_requests), Earth Engine limits the rate of [interactive requests](https://developers.google.com/earth-engine/guides/processing_environments#interactive-environment) at the project and user level. These settings can be adjusted in the [Cloud Console](https://console.cloud.google.com/iam-admin/quotas?r&pageState=\(%22allQuotasTable%22:\(%22p%22:0,%22f%22:%22%255B%257B_22k_22_3A_22Service_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22Google%2520Earth%2520Engine%2520API_5C_22_22_2C_22s_22_3Atrue_2C_22i_22_3A_22serviceTitle_22%257D%255D%22\)\))
### Concurrent batch tasks
[Batch tasks](https://developers.google.com/earth-engine/guides/processing_environments#batch-environment) are limited to a small amount of parallelism, since they use more resources than [interactive requests](https://developers.google.com/earth-engine/guides/processing_environments#interactive-environment).
When using Earth Engine noncommercially, the maximum number of batch tasks that you're able to run concurrently is set to the default unless you've been granted a [quota uplift](https://developers.google.com/earth-engine/help#additional_quota).
When using Earth Engine commercially, the maximum number of batch tasks that you're able to run concurrently is determined by the [pricing plan](https://cloud.google.com/earth-engine/pricing), though it may be further lowered by setting the per-project batch task concurrency limit. By default, the batch task concurrency limit on a project is set to the maximum allowed by the payment plan configured on the project's billing account. To view or update this limit on a project, see the [documentation for the command line tool](https://developers.google.com/earth-engine/guides/command_line#project_config).
### Asset storage quota
Each [Earth Engine asset](https://developers.google.com/earth-engine/cloud/assets) has a corresponding data storage size measured in bytes. Assets can be owned by Cloud Projects or by individuals (legacy assets), and each asset counts against its owner's Earth Engine limit on overall storage and asset count.
### User seats
When using Earth Engine commercially, each [subscription tier](https://cloud.google.com/earth-engine/pricing) comes with a number of user seats, though it's also possible to purchase a number of additional seats.
Service admins are expected to purchase a seat count to accommodate the number of Code Editor users within a given billing cycle.
#### FAQ
**Q: Who counts towards a seat?** **A:** Only distinct human users who perform Earth Engine compute usage using the Code Editor (view map tiles, send computation queries, etc.) count towards the seat limit. 
**Q: What if users change from one month to the next?** **A:** Seats aren't allocated to specific individuals - they're not named slots. As long as you don't exceed the count in a given month, the individual user identities don't matter. 
**Q: What about service accounts?** **A:** Service accounts are exempt from seat counts. They don't count as human users performing compute. 
**Q: What about users accessing Earth Engine via Python?** **A:** Users who only access Earth Engine through the Python API and don't use the Code Editor don't count towards seat usage. Seat counts are tied to Code Editor usage. 
**Q: Where are seats counted?** **A:** Seat counts apply at the billing account level. All human users across your organization who use the Code Editor contribute to the total seat count for your billing account. 
**Q: What happens if we exceed our seat limit?** **A:** We monitor for consistent violations and enforce limits at the billing account level. 
**Q: How do I purchase more or fewer seats?** **A:** See the [Earth Engine pricing](https://cloud.google.com/earth-engine/pricing) page for details.
## Fixed quota limits
These types of quota limits are set at the platform level, so they **can't be adjusted** on a per-user or per-project basis. They're unlikely to change significantly over time.
### Computation time
Different types of requests have different maximum durations, which are detailed in detail in the [Processing Environments documentation](https://developers.google.com/earth-engine/guides/processing_environments#interactive-environment).
For help fixing timeout errors, see [the debugging guide](https://developers.google.com/earth-engine/guides/debugging#timed-out).
### Per-request memory footprint
When a request fails with "User memory limit exceeded", this means that Earth Engine was unable to compute the answer within the allowed memory footprint. The EE computation platform has a finite amount of RAM available, and, to ensure that the system remains stable, each request can only use a certain amount. The maximum amount of memory available depends on the type of request (e.g., more for a batch task than a map tile), but these are system-wide limits.
For help fixing memory errors, see [the debugging guide](https://developers.google.com/earth-engine/guides/debugging#user-memory-limit-exceeded).
### Aggregations
When processing Earth Engine requests, we separate off certain types of sub-computations which we know are computationally intensive. These sub-computations are called "aggregations," and they're handled specially in the EE system. The results of aggregations are cached to avoid recomputation.
#### Concurrent aggregations
To avoid uncontrolled computational fanout, we limit the number of aggregations that an individual user can run simultaneously, and this is unchangeable. When a request fails with "Too many concurrent aggregations", it means that the requester had too many aggregations running at the same time.
For help fixing concurrent aggregation errors, see [the debugging guide](https://developers.google.com/earth-engine/guides/debugging#too-many).
#### Large aggregation results
When a request fails with "Computed value too large", it means that the aggregation returned a result which is too large to fit in our cache. The size limit on computed results is 100 MiB, and this is a system-wide limit.
### Table import limits
Table upload limits are explained in the [the guide to importing table data](https://developers.google.com/earth-engine/guides/table_upload).
### Request payload size
A single query to Earth Engine is limited to 10MB in size. This limit is usually only exceeded when some large piece of additional data gets included directly in the query, like a shapefile or GeoJSON structure that's been inlined into the query. These objects should instead be uploaded and turned into a FeatureCollection asset, and referenced by the asset ID.
### Task queue length
Tasks that are waiting to be scheduled (in the `READY` state) form the "task queue." Each project's queue supports a maximum of 3,000 tasks. This means that it's not possible to have more than 3,000 tasks in the `READY` state.
## BigQuery raster functions quota limits
The following quotas apply to calls to Earth Engine from BigQuery, such as when using the [`ST_REGIONSTATS`](https://developers.google.com/bigquery/docs/reference/standard-sql/geography_functions#st_regionstats) SQL function.
Quota type | Default value (per project)  
---|---  
BigQuery slot-time per day | 1,260,000 slot-seconds (350 slot-hours)  
### BigQuery slot-time per day
The BigQuery slot-time per day quota is a custom quota that lets you limit the amount of slot-time that BigQuery raster functions are allowed to consume on Earth Engine on a given day for a given project. You can [view this quota in the Cloud Console](https://console.cloud.google.com/iam-admin/quotas?service=earthengine.googleapis.com&metric=earthengine.googleapis.com/bigquery_slot_usage_time) under the `earthengine.googleapis.com/bigquery_slot_usage_time` metric, and the value can be adjusted up or down by a Quota Administrator. To increase the value above the default value, [create a quota increase request](https://cloud.google.com/docs/quotas/view-manage#requesting_higher_quota), which will be automatically approved.
If you exceed this quota, BigQuery will return the following error message:
> `From Earth Engine: Custom quota exceeded: Your usage exceeded the custom quota for 'earthengine.googleapis.com/bigquery_slot_usage_time', which is adjustable by your administrator in the Google Cloud console: https://console.cloud.google.com/quotas/?project=_.`
Once the quota is exceeded, `ST_REGIONSTATS` calls will fail until the quota is reset the next day or the limit is increased by an administrator.
**Note:** Like [BigQuery custom query quotas](https://cloud.google.com/bigquery/docs/custom-quotas), this quota is approximate. It provides a safeguard against excessive spending, but is not designed to strictly limit slot time. BigQuery might occasionally run a query that exceeds the quota limit, and you might exhaust your quota without being billed for the entire consumed amount.
