 
#  ui.Chart.feature.byFeature 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Generates a Chart from a set of features. Plots the value of one or more properties for each feature: 
- X-axis = Features labeled by xProperty (default: 'system:index').
- Y-axis = Values of yProperties (default: all properties).
- Series = Names of yProperties.
The values are ordered along the x-axis in the same order as the input features.
Returns a chart.
Usage| Returns  
---|---  
`ui.Chart.feature.byFeature(features,  _xProperty_, _yProperties_)`| ui.Chart  
Argument| Type| Details  
---|---|---  
`features`| Feature|FeatureCollection|List| The features to include in the chart.  
`xProperty`| String, optional| The property used as the value of each feature on the x-axis. Defaults to 'system:index'.  
`yProperties`| List, optional| Property or properties used on the y-axis. If omitted, all properties of all features will be charted on the y-axis (except xProperty).  
