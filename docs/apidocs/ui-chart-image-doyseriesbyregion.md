 
#  ui.Chart.image.doySeriesByRegion
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Generates a Chart from an ImageCollection. Plots the derived value of the given band in different regions at each day-of-year. 
- X-axis: Day of year (startDay to endDay, defaults to 1 to 366).
- Y-axis: Derived band value (reduced within the region and across years).
- Series: Regions.
Returns a chart.
Usage| Returns  
---|---  
`ui.Chart.image.doySeriesByRegion(imageCollection, bandName, regions,  _regionReducer_, _scale_, _yearReducer_, _seriesProperty_, _startDay_, _endDay_)`| ui.Chart  
Argument| Type| Details  
---|---|---  
`imageCollection`| ImageCollection| The ImageCollection to chart.  
`bandName`| Number|String| The name of the band to chart.  
`regions`| Feature|FeatureCollection|Geometry|List| The regions to reduce.  
`regionReducer`| Reducer, optional| Reducer for aggregating band values within the region. Must return a single value. Defaults to ee.Reducer.mean().  
`scale`| Number, optional| Scale to use with the region reducer in meters.  
`yearReducer`| Reducer, optional| Reducer for aggregating band values across years (for a given day of year). Must return a single value. Defaults to ee.Reducer.mean().  
`seriesProperty`| String, optional| Property of features in opt_regions to be used for series labels. Defaults to 'system:index'.  
`startDay`| Number, optional| Day of year to start the series. Must be between 1 and 366.  
`endDay`| Number, optional| Day of year to end the series. Must be between startDay and 366.  
Was this helpful?
