 
#  ee.Algorithms.TemporalSegmentation.LandTrendr
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Landsat-based detection of Trends in Disturbance and Recovery: temporally segments a time-series of images by extracting the spectral trajectories of change over time. The first band of each image is used to find breakpoints, and those breakpoints are used to perform fitting on all subsequent bands. The breakpoints are returned as a 2-D matrix of 4 rows and as many columns as images. The first two rows are the original X and Y values. The third row contains the Y values fitted to the estimated segments, and the 4th row contains a 1 if the corresponding point was used as a segment vertex or 0 if not. Any additional fitted bands are appended as rows in the output. Breakpoint fitting assumes that increasing values represent disturbance and decreasing values represent recovery. 
See: Kennedy, R.E., Yang, Z. and Cohen, W.B., 2010. Detecting trends in forest disturbance and recovery using yearly Landsat time series: 1. LandTrendr - Temporal segmentation algorithms. Remote Sensing of Environment, 114(12), pp.2897-2910.
Usage| Returns  
---|---  
`ee.Algorithms.TemporalSegmentation.LandTrendr(timeSeries, maxSegments,  _spikeThreshold_, _vertexCountOvershoot_, _preventOneYearRecovery_, _recoveryThreshold_, _pvalThreshold_, _bestModelProportion_, _minObservationsNeeded_)`| Image  
Argument| Type| Details  
---|---|---  
`timeSeries`| ImageCollection| Yearly time-series from which to extract breakpoints. The first band is usedto find breakpoints, and all subsequent bands are fitted using those breakpoints.  
`maxSegments`| Integer| Maximum number of segments to be fitted on the time series.  
`spikeThreshold`| Float, default: 0.9| Threshold for dampening the spikes (1.0 means no dampening).  
`vertexCountOvershoot`| Integer, default: 3| The initial model can overshoot the maxSegments + 1 vertices by this amount. Later, it will be pruned down to maxSegments + 1.  
`preventOneYearRecovery`| Boolean, default: false| Prevent segments that represent one year recoveries.  
`recoveryThreshold`| Float, default: 0.25| If a segment has a recovery rate faster than 1/recoveryThreshold (in years), then the segment is disallowed.  
`pvalThreshold`| Float, default: 0.1| If the p-value of the fitted model exceeds this threshold, then the current model is discarded and another one is fitted using the Levenberg-Marquardt optimizer.  
`bestModelProportion`| Float, default: 0.75| Allows models with more vertices to be chosen if their p-value is no more than (2 - bestModelProportion) times the p-value of the best model.  
`minObservationsNeeded`| Integer, default: 6| Min observations needed to perform output fitting.  
