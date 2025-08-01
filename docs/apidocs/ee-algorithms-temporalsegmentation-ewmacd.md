 
#  ee.Algorithms.TemporalSegmentation.Ewmacd
Stay organized with collections  Save and categorize content based on your preferences. 
Exponentially Weighted Moving Average Change Detection. This algorithm computes a harmonic model for the 'training' portion of the input data and subtracts that from the original results. The residuals are then subjected to Shewhart X-bar charts and an exponentially weighted moving average. Disturbed pixels are indicated when the charts signal a deviation from the given control limits.
The output is a 5 band image containing the bands:
ewma: a 1D array of the EWMA score for each input image. Negative values represent disturbance and positive values represent recovery.
harmonicCoefficients: A 1-D array of the computed harmonic coefficient pairs. The coefficients are ordered as [constant, sin0, cos0, sin1, cos1...]
rmse: the RMSE from the harmonic regression.
rSquared: r-squared value from the harmonic regression.
residuals: 1D array of residuals from the harmonic regression.
See: Brooks, E.B., Wynne, R.H., Thomas, V.A., Blinn, C.E. and Coulston, J.W., 2014. On-the-fly massively multitemporal change detection using statistical quality control charts and Landsat data. IEEE Transactions on Geoscience and Remote Sensing, 52(6), pp.3316-3332.
Usage | Returns  
---|---  
`ee.Algorithms.TemporalSegmentation.Ewmacd(timeSeries, vegetationThreshold, trainingStartYear, trainingEndYear, _harmonicCount_, _xBarLimit1_, _xBarLimit2_, _lambda_, _lambdasigs_, _rounding_, _persistence_)`|  Image  
Argument | Type | Details  
---|---|---  
`timeSeries` | ImageCollection | Collection from which to extract EWMA. This collection is expected to contain 1 image for each year and be sorted temporally.  
`vegetationThreshold` | Float | Threshold for vegetation. Values below this are considered non-vegetation.  
`trainingStartYear` | Integer | Start year of training period, inclusive.  
`trainingEndYear` | Integer | End year of training period, exclusive.  
`harmonicCount` | Integer, default: 2 | Number of harmonic function pairs (sine and cosine) used.  
`xBarLimit1` | Float, default: 1.5 | Threshold for initial training xBar limit.  
`xBarLimit2` | Integer, default: 20 | Threshold for running xBar limit.  
`lambda` | Float, default: 0.3 | The 'lambda' tuning parameter weighting new years vs the running average.  
`lambdasigs` | Float, default: 3 | EWMA control bounds, in units of standard deviations.  
`rounding` | Boolean, default: true | Should rounding be performed for EWMA.  
`persistence` | Integer, default: 3 | Minimum number of observations needed to consider a change.  
