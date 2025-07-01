 
#  ui.Chart
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
A chart widget. 
Usage| Returns  
---|---  
`ui.Chart( _dataTable_, _chartType_, _options_, _view_, _downloadable_)`| ui.Chart  
Argument| Type| Details  
---|---|---  
`dataTable`| List, optional| A 2-D array of data or a Google Visualization DataTable literal. See: http://developers.google.com/chart/interactive/docs/reference#DataTable  
`chartType`| String, optional| The chart type; e.g 'ScatterChart', 'LineChart', and 'ColumnChart'. For the complete list of charts, see: https://developers.google.com/chart/interactive/docs/gallery  
`options`| Object, optional| An object defining chart style options such as:  | ` title ` (string) The title of the chart.  
---  
` colors ` (Array) An array of colors used to draw the chart.  
Its format should follow the Google Visualization API's options: https://developers.google.com/chart/interactive/docs/customizing_charts  
`view`| Object, optional| Sets a DataView initializer object, which acts as a filter over the underlying data. See: https://developers.google.com/chart/interactive/docs/reference#DataView  
`downloadable`| Boolean, optional| Whether the chart can be downloaded as CSV, SVG, and PNG. Defaults to true.  
