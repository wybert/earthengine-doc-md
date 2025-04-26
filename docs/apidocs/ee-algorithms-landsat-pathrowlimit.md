 
#  ee.Algorithms.Landsat.pathRowLimit 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Limits requests to an ImageCollection of Landsat scenes to return a controllable number of the best scenes for each request. This is intended for use with statistical algorithms like median composites that need a certain amount of good data to perform well, but that do not benefit substantially from additional data beyond that while becoming needlessly expensive. The default arguments select approximately one year's worth of good data. 
Note that in rare circumstances, when the tile boundary aligns with a Landsat WRS cell boundary, queries for adjacent tiles may yield conflicting results. This is why it is important that this algorithm only be used with statistical methods that can tolerate these inconsistencies.
Usage| Returns  
---|---  
`ee.Algorithms.Landsat.pathRowLimit(collection,  _maxScenesPerPathRow_, _maxScenesTotal_)`| ImageCollection  
Argument| Type| Details  
---|---|---  
`collection`| ImageCollection| The Landsat ImageCollection to limit.  
`maxScenesPerPathRow`| Integer, default: 25| The max number of scenes to return per path/row.  
`maxScenesTotal`| Integer, default: 100| The max number of scenes to return per request total.  
