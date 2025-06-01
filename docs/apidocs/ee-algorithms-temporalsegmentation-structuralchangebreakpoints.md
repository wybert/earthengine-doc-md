 
#  ee.Algorithms.TemporalSegmentation.StructuralChangeBreakpoints 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Runs breakpoint detection, similar to R's strucchange::breakpoints function. 
Each pixel is fit by a piecewise linear/harmonic model, of the form
Y = A + B * t + C * cos(2 * pi * season(t)) + D * sin(2 * pi * season(t)) + E * cos(4 * pi * season(t)) + F * sin(4 * pi * season(t)) + ...
In this equation, 't' is the start time of the image in the format specified by 'dateFormat', and 'season(t)' is the fractional year of that start time (see the description of dateFormat for details). The maximum order of the harmonic terms is determined by 'seasonalModelOrder'.
The result is an image containing two bands, plus two bands per band in the input:
`tStart`, `tEnd`: each of these holds a 1D array, with one entry per segment in the piecewise linear fit; each entry contains the start time of the first or last images in that segment. By default the values here are in fractional years, for easy use with the coefficients.
`coefs_BANDNAME`: there will be one such output band per input band. Each of these holds a 2D array, with one row per segment. The values in that row are the coefficients of the linear fit for that segment - that is, the values of A, B, C, ... for that segment. As described above, the values here are affected by 'dateFormat'
.`rmse_BANDNAME`: there will be one such output band per input band. This holds a 1D array, with one entry per segment. The value for each segment is the RMSE for the linear fit residuals for that segment.
Usage| Returns  
---|---  
`ee.Algorithms.TemporalSegmentation.StructuralChangeBreakpoints(collection,  _breakpointBand_, _seasonalModelOrder_, _minSpacing_, _maxBreaks_, _dateFormat_)`| Image  
Argument| Type| Details  
---|---|---  
`collection`| ImageCollection| Collection of images on which to detect breakpoints.  
`breakpointBand`| String, default: null| The name of the band to use for breakpoint detection. Optional only if the images have only a single band.  
`seasonalModelOrder`| Integer, default: 3| The order of the harmonic seasonal model.  
`minSpacing`| Float, default: 0.15| The minimum spacing between breakpoints. If this is between 0 and 1 (exclusive), it will be interpreted as a fraction of the number of images in the collection. Otherwise, it will be interpreted as a number of samples.  
`maxBreaks`| Integer, default: 0| The maximum number of breakpoints.  
`dateFormat`| Integer, default: 1| The time representation to use in the results: 1 = fractional years, 2 = unix time in milliseconds. This affects the values in the tStart and tEnd bands and the 't' values used in the harmonic model. The fractional years used here and in that model are defined as the fractional number of 365.25-day years since 1 Jan 1970.  
