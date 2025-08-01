 
#  ee.Algorithms.TemporalSegmentation.Verdet
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Vegetation Regeneration and Disturbance Estimates through Time, forest change detection algorithm. This algorithm generates a yearly clear-sky composite from satellite imagery, calculates a spectral vegetation index for each pixel in that composite, spatially segments the vegetation index image into patches, temporally divides the time series into differently sloped segments, and then labels those segments as disturbed, stable, or regenerating. Segmentation at both the spatial and temporal steps are performed using total variation regularization.
The output consists of a 1D array per pixel containing the slope of fitted trend lines. Negative values indicate disturbance and positive values regeneration.
See: Hughes, M.J., Kaylor, S.D. and Hayes, D.J., 2017. Patch-based forest change detection from Landsat time series. Forests, 8(5), p.166.
Usage | Returns  
---|---  
`ee.Algorithms.TemporalSegmentation.Verdet(timeSeries, _tolerance_, _alpha_, _nRuns_)`|  Image  
Argument | Type | Details  
---|---|---  
`timeSeries` | ImageCollection | Collection from which to extract VeRDET scores. This collection is expected to contain 1 image for each year, sorted temporally.  
`tolerance` | Float, default: 0.0001 | Convergence tolerance.  
`alpha` | Float, default: 0.03333333333333333 | Regularization parameter for segmentation.  
`nRuns` | Integer, default: 100 | Maximum number of runs for convergence.  
