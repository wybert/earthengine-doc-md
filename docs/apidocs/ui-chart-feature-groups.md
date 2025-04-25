 
#  ui.Chart.feature.groups 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Generates a Chart from a set of features. Plots the value of a given property across groups of features. Features with the same value of groupProperty will be grouped and plotted as a single series. 
- X-axis = xProperty values.
- Y-axis = yProperty values.
- Series = Feature groups, by seriesProperty.
Returns a chart.
Usage| Returns  
---|---  
`ui.Chart.feature.groups(features, xProperty, yProperty, seriesProperty)`| ui.Chart  
Argument| Type| Details  
---|---|---  
`features`| Feature|FeatureCollection|List| The features to include in the chart.  
`xProperty`| String| Property to be used as the label for each feature on the x-axis.  
`yProperty`| String| Property to be plotted on the y-axis.  
`seriesProperty`| String| Property used to determine feature groups. Features with the same value of groupProperty will be plotted as a single series on the chart.  
