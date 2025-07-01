 
#  ui.Chart.image.regions
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Generates a Chart from an image. Extracts and plots the value of each band in one or more regions. 
- X-axis = Band labeled by xProperty (default: band name).
- Y-axis = Reducer output.
- Series = Region labeled by seriesProperty (default: 'system:index').
Returns a chart.
Usage| Returns  
---|---  
`ui.Chart.image.regions(image,  _regions_, _reducer_, _scale_, _seriesProperty_, _xLabels_)`| ui.Chart  
Argument| Type| Details  
---|---|---  
`image`| Image| Image to extract band values from.  
`regions`| Feature|FeatureCollection|Geometry|List, optional| Regions to reduce. Defaults to the image's footprint.  
`reducer`| Reducer, optional| Reducer that generates the value(s) for the y-axis. Must return a single value per band.  
`scale`| Number, optional| The pixel scale in meters.  
`seriesProperty`| String, optional| Property to be used as the label for each region in the legend. Defaults to 'system:index'.  
`xLabels`| List, optional| A list of labels used for bands on the x-axis. Must have the same number of elements as the image bands. If omitted, bands will be labeled with their names. If the labels are numeric (e.g. wavelengths), x-axis will be continuous.  
