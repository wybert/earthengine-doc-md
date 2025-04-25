 
#  ui.Chart.image.byRegion 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Generates a Chart from an image. Extracts and plots band values in one or more regions in the image, with each band in a separate series. 
- X-axis = Region labeled by xProperty (default: 'system:index')
- Y-axis = Reducer output.
- Series = Band name.
Returns a chart.
Usage| Returns  
---|---  
`ui.Chart.image.byRegion(image,  _regions_, _reducer_, _scale_, _xProperty_)`| ui.Chart  
Argument| Type| Details  
---|---|---  
`image`| Image| Image to extract band values from.  
`regions`| Feature|FeatureCollection|Geometry|List, optional| Regions to reduce. Defaults to the image's footprint.  
`reducer`| Reducer, optional| Reducer that generates the value(s) for the y-axis. Must return a single value per band. Defaults to ee.Reducer.mean().  
`scale`| Number, optional| Scale to use with the reducer in meters.  
`xProperty`| String, optional| Property to be used as the label for each Region on the x-axis. Defaults to 'system:index'.  
Was this helpful?
