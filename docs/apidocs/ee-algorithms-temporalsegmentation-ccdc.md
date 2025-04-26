 
#  ee.Algorithms.TemporalSegmentation.Ccdc 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Implements the Continuous Change Detection and Classification temporal breakpoint algorithm. This algorithm finds temporal breakpoints in an image collection by iteratively fitting harmonic functions to the data. Fit coefficients are produced for all input bands, but the bands used for breakpoint detection can be specified with the 'breakpointBands' argument. 
For more details, see Zhu, Z. and Woodcock, C.E., 2014. Continuous change detection and classification of land cover using all available Landsat data. Remote sensing of Environment, 144, pp.152-171.
Usage| Returns  
---|---  
`ee.Algorithms.TemporalSegmentation.Ccdc(collection,  _breakpointBands_, _tmaskBands_, _minObservations_, _chiSquareProbability_, _minNumOfYearsScaler_, _dateFormat_, _lambda_, _maxIterations_)`| Image  
Argument| Type| Details  
---|---|---  
`collection`| ImageCollection| Collection of images on which to run CCDC.  
`breakpointBands`| List, default: null| The name or index of the bands to use for change detection. If unspecified, all bands are used.  
`tmaskBands`| List, default: null| The name or index of the bands to use for iterative TMask cloud detection. These are typically the green band and the SWIR1 band. If unspecified, TMask is not used. If specified, 'tmaskBands' must be included in 'breakpointBands'.  
`minObservations`| Integer, default: 6| The number of observations required to flag a change.  
`chiSquareProbability`| Float, default: 0.99| The chi-square probability threshold for change detection in the range of [0, 1].  
`minNumOfYearsScaler`| Float, default: 1.33| Factors of minimum number of years to apply new fitting.  
`dateFormat`| Integer, default: 0| The time representation to use during fitting: 0 = jDays, 1 = fractional years, 2 = unix time in milliseconds. The start, end and break times for each temporal segment will be encoded this way.  
`lambda`| Float, default: 20| Lambda for LASSO regression fitting. If set to 0, regular OLS is used instead of LASSO.  
`maxIterations`| Integer, default: 25000| Maximum number of runs for LASSO regression convergence. If set to 0, regular OLS is used instead of LASSO.  
