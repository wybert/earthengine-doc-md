 
#  ee.Algorithms.TemporalSegmentation.C2c
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
An implementation of the Composite 2 Change (C2C) algorithm. This algorithm segments a time series using a piecewise linear fit with the minimum of segments required to fit the data within the given maximum root mean squared error (RMSE). For every band given the algorithm will return the following bands:
changeDate:A 1D array of doubles representing pairs of start and end dates for each fitted segment. The date format is determined by the dateFormat argument.
value: A 1D array of doubles of the value of the band at the changeDate.
magnitude: A 1D array of doubles providing the absolute difference between the values before and after a change date. The first magnitude is always NaN.
duration: A 1D array of doubles of the duration of the segment preceding the change date. The first duration is always NaN.
rate: A 1D array of doubles of the rate of change of the data preceding the. change date. The first rate is always NaN.
postMagnitude: A 1D array of doubles of the absolute difference between the values after the change date and the value at the change date. The last postMagnitude is always NaN.
postDuration: The duration of the segment following the change date. The last postDuration is always NaN.
postRate: The rate of change of the data following the change date. The last postRate is always NaN.
See Hermosilla et al. (2015) dx.doi.org/10.1016/j.rse.2014.11.005 for further details on the original algorithm.
This algorithm is in preview and is subject to change.
Usage | Returns  
---|---  
`ee.Algorithms.TemporalSegmentation.C2c(collection, _dateFormat_, _maxError_, _maxSegments_, _startYear_, _endYear_, _infill_, _spikesTolerance_)`|  Image  
Argument | Type | Details  
---|---|---  
`collection` | ImageCollection | Collection of images on which to run C2C.  
`dateFormat` | Integer, default: 0 | The time representation to use during fitting: 0 = jDays, 1 = fractional years, 2 = unix time in milliseconds. The start, end and break times for each temporal segment will be encoded this way.  
`maxError` | Float, default: 75 |   
`maxSegments` | Integer, default: 6 |   
`startYear` | Integer, default: 1984 |   
`endYear` | Integer, default: 2019 |   
`infill` | Boolean, default: true |   
`spikesTolerance` | Float, default: 0.85 |   
