 
#  Cost controls
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Limit daily EECU-time](https://developers.google.com/earth-engine/guides/cost_controls#daily-limits)
    * [Set a daily limit](https://developers.google.com/earth-engine/guides/cost_controls#set_a_daily_limit)
    * [Returned error messages](https://developers.google.com/earth-engine/guides/cost_controls#returned_error_messages)
  * [Fine-grained monitoring and alerting](https://developers.google.com/earth-engine/guides/cost_controls#fine-grained_monitoring_and_alerting)
    * [Configure alerts](https://developers.google.com/earth-engine/guides/cost_controls#configure_alerts)
    * [Cancel resource-heavy tasks](https://developers.google.com/earth-engine/guides/cost_controls#cancel_resource-heavy_tasks)


This page describes how to set daily limits and monitor in-progress EECU-time to help control computational costs in Earth Engine.
## Limit daily EECU-time
To help control your Earth Engine costs, you can set a limit on the amount of EECU-time that your project is allowed to consume in a day by updating the following Cloud Quota:
  * `Earth Engine compute time (EECU-time) per day in seconds`: A project-level quota that limits the aggregate EECU-time of all users in a project.


For more information about Earth Engine quotas you can set, see [Earth Engine quotas](https://developers.google.com/earth-engine/guides/usage).
**Note:** This quota is approximate. It provides a safeguard against excessive spending, but is not designed to strictly limit EECU-time. Earth Engine might occasionally run a query that exceeds the quota limit.
### Set a daily limit
You can view and edit quotas in the [**Quotas & System Limits**](https://console.cloud.google.com/iam-admin/quotas) page of the Google Cloud console. When you adjust a quota, the change takes effect within a few minutes. To set or update a daily limit, do the following:
  1. Verify you have the [Permissions for changing project quota](https://cloud.google.com/docs/quotas/permissions#permissions_changing) on your selected project.
  2. Navigate to the [Quotas](https://console.cloud.google.com/iam-admin/quotas) page of Google Cloud console.
  3. Use the **Metric** filter in the **Filter** search box to filter for `earthengine.googleapis.com/daily_eecu_usage_time`. If you don't see the `Earth Engine compute time (EECU-time) per day in seconds` quota, verify that you have enabled the Earth Engine API for the selected project.
  4. Click **Edit quota** from the three-dot menu.
  5. If the **Unlimited** checkbox is selected, deselect it.
  6. Enter the limit in EECU-seconds you want in the **New value** field. Click **Submit Request**.


For more information about viewing and managing quotas, see [View and manage quotas](https://cloud.google.com/docs/quotas/view-manage).
### Returned error messages
After you set a daily limit, Earth Engine returns the following error message when you exceed it:
> Your usage exceeded the custom quota for 'earthengine.googleapis.com/daily_eecu_usage_time', which is adjustable by your administrator in the Google Cloud console: https://console.cloud.google.com/quotas/?project=_.
Once the quota is exceeded, Earth Engine requests will fail until the quota is reset the next day or the limit is increased by an administrator.
## Fine-grained monitoring and alerting
If you need to control and monitor costs at a finer-grain than the [daily limit](https://developers.google.com/earth-engine/guides/cost_controls#daily-limits), the following recipes require more set-up but enable alerting and cancelation at the [`workload_tag`](https://developers.google.com/earth-engine/guides/monitoring_usage#workload-tags) and batch task level.
These recipes use the in-progress EECU-time monitoring that's surfaced for running requests. See the [Monitoring usage](https://developers.google.com/earth-engine/guides/monitoring_usage) guide for more information about in-progress EECU-time reporting in Cloud Monitoring.
### Configure alerts
You can configure alerts in Cloud Monitoring to warn you when a metric hits a certain threshold. The Cloud Monitoring alerting system is very flexible. We've collected a few of our favorite recipes here, but feel free to cook with custom configurations that suit your needs.
#### Recipe: Chat notification for `workload_tag` usage
This example shows how to wire up a chat notification (e.g., a Google Chat message or a Slack message) if the Earth Engine compute usage for a given [`workload_tag`](https://developers.google.com/earth-engine/guides/monitoring_usage#workload-tags) exceeds a threshold. This could be useful in the case that you have a set of export tasks which create data for your production service, and you want to be notified if they collectively consume more than a certain amount of EECU-time.
  1. Visit the [Alerting page](https://console.cloud.google.com/monitoring/alerting) in the Cloud Monitoring section of the Cloud console.
  2. Choose "Create policy" to configure a new alerting policy.
  3. Select the metric: 
     * [**In-progress EECU-seconds**](https://developers.google.com/earth-engine/guides/monitoring_usage#available_metrics) represents the number of pending (not yet successful) compute seconds.
     * You may need to deselect the "Active" filter to see the metric.
  4. Add a filter: 
     * Use `workload_tag == your_workload_tag_value` to filter to a particular workload tag.
     * Use `compute_type = batch` or `compute_type = online` to filter to a particular type of computation.
  5. Choose an appropriate "Rolling window" value. If you're not sure, use `5 min`.
  6. Select "Sum" from the "Rolling window function" menu. ![Configuration of a
metric for an alert](https://developers.google.com/static/earth-engine/images/alerting-metric-configuration.png)
  7. Choose the alert trigger and give it a name.
  8. Select the notification channels. 
     * For this recipe, we'll choose "Manage Notification Channels" from the modal window, then "Add New" to paste in the Space ID of your Google Chat. This ID can be found in the URL of the Gmail or Chat page when viewing the chat.
     * If using Google Chat, you'll also need to type `@Google Cloud Monitoring` and select the app to add the Alerting app to your Space (if your organization allows).
  9. Choose the relevant policy and severity labels.
  10. Write a short documentation snippet.
  11. Publish your new alerting policy!


Once set, you'll get alerts in your chat space any time that the threshold is exceeded for your project.
#### Recipe: Get email alerts for total in-progress EECU-time
Follow the recipe for chat notifications, but make two changes:
  1. Skip the step for adding a `workload_tag` filter, so that you can see all values.
  2. When selecting a notification channel, instead of configuring a chat channel, add your email address instead.


#### Alert latency and timing
Note that there's a small delay in the propagation of Monitoring reports, so you shouldn't expect instantaneous notifications.
### Cancel resource-heavy tasks
Given a limit, it's possible to use the Earth Engine API to periodically check the list of pending tasks and request cancellation for any running task that exceeds the EECU-seconds limit.
#### Recipe: Run a snippet of code in a notebook or local Python shell
```
eecu_seconds_limit = 50 * 60 * 60  # 50 hours
print("Watching for operations to cancel...")
while(True):
  for op in ee.data.listOperations():
    if op['metadata']['state'] == 'RUNNING':
      if op['metadata'].get('batchEecuUsageSeconds', 0) > eecu_seconds_limit:
        print(f"Cancelling operation {op['name']}")
        ee.data.cancelOperation(op['name'])
  time.sleep(10)  # 10 seconds

```

