 
#  ee.Algorithms.TemporalSegmentation.LandTrendrFit 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Interpolates a time series using a set of LandTrendr breakpoint years. For each input band in the timeSeries, outputs a new 1D array-valued band containing the input values interpolated between the breakpoint times identified by the vertices image. See the LandTrendr Algorithm for more details. 
Usage| Returns  
---|---  
`ee.Algorithms.TemporalSegmentation.LandTrendrFit(timeSeries, vertices,  _spikeThreshold_, _minObservationsNeeded_)`| Image  
Argument| Type| Details  
---|---|---  
`timeSeries`| ImageCollection| Time series to interpolate.  
`vertices`| Image| Vertices image. A 1D array of LandTrendr breakpoint years.  
`spikeThreshold`| Float, default: 0.9| Threshold for dampening input spikes (1.0 means no dampening).  
`minObservationsNeeded`| Integer, default: 6| Min observations needed.  
Was this helpful?
