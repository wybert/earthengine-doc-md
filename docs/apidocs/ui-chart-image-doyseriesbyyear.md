 
#  ui.Chart.image.doySeriesByYear 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Generates a Chart from an ImageCollection. Plots the derived value of the given band in a region for each day-of-year across different years. 
- X-axis: Day of year (startDay to endDay, defaults to 1 to 366).
- Y-axis: Derived band value (reduced within the region).
- Series: Years.
Returns a chart.
Usage| Returns  
---|---  
`ui.Chart.image.doySeriesByYear(imageCollection, bandName,  _region_, _regionReducer_, _scale_, _sameDayReducer_, _startDay_, _endDay_)`| ui.Chart  
Argument| Type| Details  
---|---|---  
`imageCollection`| ImageCollection| The ImageCollection to chart.  
`bandName`| Number|String| The name of the band to chart.  
`region`| Feature|FeatureCollection|Geometry, optional| The region to reduce. Defaults to the union of all geometries in the image collection.  
`regionReducer`| Reducer, optional| Reducer for aggregating band values within the region. Must return a single value. Defaults to ee.Reducer.mean().  
`scale`| Number, optional| Scale to use with the region reducer in meters.  
`sameDayReducer`| Reducer, optional| Reducer for aggregating band values across images with the same (DoY, year) pair. Must return a single value. Defaults to ee.Reducer.mean().  
`startDay`| Number, optional| Day of year to start the series. Must be between 1 and 366.  
`endDay`| Number, optional| Day of year to end the series. Must be between startDay and 366.  
