 
#  ui.Chart.setSeriesNames 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Returns a copy of this chart with updated series names. 
Usage| Returns  
---|---  
`Chart.setSeriesNames(seriesNames,  _seriesIndex_)`| ui.Chart  
Argument| Type| Details  
---|---|---  
this: `ui.chart`| ui.Chart| The ui.Chart instance.  
`seriesNames`| Dictionary|Dictionary| New series names. If it's a string, the name of the series at seriesIndex is set to seriesNames. If it's a list, the value at index i in the list is used as a label for series number i. If it's a dictionary or an object, it's treated as a map from existing series names to new series names. In the last two cases, seriesIndex is ignored.  
`seriesIndex`| Number, optional| The index of the series to rename. Ignored if seriesNames is a list or dictionary. Series are 0-indexed.  
