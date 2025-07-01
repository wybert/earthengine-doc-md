 
#  ui.Chart.image.doySeries
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Generates a Chart from an ImageCollection. Plots derived values of each band in a region for a each day of the year. 
- X-axis: Day of year (startDay to endDay, defaults to 1 to 366).
- Y-axis: Derived band value (reduced within the region and across years).
- Series: Band names.
Returns a chart.
Usage| Returns  
---|---  
`ui.Chart.image.doySeries(imageCollection,  _region_, _regionReducer_, _scale_, _yearReducer_, _startDay_, _endDay_)`| ui.Chart  
Argument| Type| Details  
---|---|---  
`imageCollection`| ImageCollection| The ImageCollection to chart.  
`region`| Feature|FeatureCollection|Geometry, optional| The region to reduce. Defaults to the union of all geometries in the image collection.  
`regionReducer`| Reducer, optional| Reducer for aggregating band values within the region. Must return a single value. Defaults to ee.Reducer.mean().  
`scale`| Number, optional| Scale to use with the region reducer in meters.  
`yearReducer`| Reducer, optional| Reducer for aggregating regionReducer outputs across years (for a given day). Must return a single value. Defaults to ee.Reducer.mean().  
`startDay`| Number, optional| Day of year to start the series. Must be between 1 and 366.  
`endDay`| Number, optional| Day of year to end the series. Must be between startDay and 366.  
Was this helpful?
