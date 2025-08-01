 
#  ui.Chart.feature.byProperty
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
- X-axis = Property name, labeled by xProperties (default: all properties).
- Y-axis = Property value (must be numeric).
- Series = Features, labeled by seriesProperty (default: 'system:index').
All properties except seriesProperty are included on the x-axis by default.
Returns a chart.
Usage | Returns  
---|---  
`ui.Chart.feature.byProperty(features, _xProperties_, _seriesProperty_)`|  ui.Chart  
Argument | Type | Details  
---|---|---  
`features` | Feature|FeatureCollection|List<Feature> | The features to include in the chart.  
`xProperties` | List<String>|Object|String, optional | One of (1) a property to be plotted on the x-axis; (2) a list of properties to be plotted on the x-axis; or (3) a (property, label) dictionary specifying labels for properties to be used as values on the x-axis. If omitted, all properties will be plotted on the x-axis, labeled with their names.  
`seriesProperty` | String, optional | The name of the property used to label each feature in the legend. Defaults to 'system:index'.  
Was this helpful?
