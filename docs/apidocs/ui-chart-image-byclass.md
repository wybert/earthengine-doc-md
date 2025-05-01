 
#  ui.Chart.image.byClass 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Generates a Chart from an image. Plots derived band values in classified regions in an image. 
- X-axis = Band name (all bands except the class band are charted).
- Y-axis = Band value.
- Series = Class label.
Returns a chart.
Usage| Returns  
---|---  
`ui.Chart.image.byClass(image, classBand,  _region_, _reducer_, _scale_, _classLabels_, _xLabels_)`| ui.Chart  
Argument| Type| Details  
---|---|---  
`image`| Image| Classified image to derive band values from.  
`classBand`| Number|String| The class label band in this image.  
`region`| Feature|FeatureCollection|Geometry, optional| The region to reduce. If omitted, uses the entire image.  
`reducer`| Reducer, optional| Reducer that generates the value(s) for the y-axis. Must return a single value per band. Defaults to ee.Reducer.mean().  
`scale`| Number, optional| Scale to use with the reducer in meters.  
`classLabels`| List., optional| A dictionary of labels used to identify classes in the series legend. If omitted, classes will be labeled with the value of classBand.  
`xLabels`| List, optional| A list of labels used to label bands on the xAxis. Must have one fewer elements than the number of image bands. If omitted, bands will be labeled with their names. If the labels are numeric (e.g. wavelengths), x-axis will be continuous.  
