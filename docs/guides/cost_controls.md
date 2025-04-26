 
#  Cost controls 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
## Configure alerts
In order to control your Earth Engine resource usage and costs, you can configure alerts in Cloud Monitoring to warn you when a metric hits a certain threshold.
The Cloud Monitoring alerting system is very flexible. We've collected a few of our favorite recipes here, but feel free to experiment with custom configurations that suit your needs.
### Recipe: Chat notification for `workload_tag` usage
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
### Recipe: Get email alerts for total in-progress EECU-time
Follow the recipe for chat notifications, but make two changes:
  1. Skip the step for adding a `workload_tag` filter, so that you can see all values.
  2. When selecting a notification channel, instead of configuring a chat channel, add your email address instead.


### Alert latency and timing
Note that there's a small delay in the propagation of Monitoring reports, so you shouldn't expect instantaneous notifications.
## Cancel resource-heavy tasks
Given a limit, it's possible to use the Earth Engine API to periodically check the list of pending tasks and request cancellation for any running task that exceeds the EECU-seconds limit.
### Recipe: Run a snippet of code in a notebook or local Python shell
```
eecu_seconds_limit = 50 * 60 * 60 # 50 hours
print("Watching for operations to cancel...")
while(True):
 for op in ee.data.listOperations():
  if op['metadata']['state'] == 'RUNNING':
   if op['metadata'].get('batchEecuUsageSeconds', 0) > eecu_seconds_limit:
    print(f"Cancelling operation {op['name']}")
    ee.data.cancelOperation(op['name'])
 time.sleep(10) # 10 seconds

```

