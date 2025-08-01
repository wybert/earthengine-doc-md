 
#  ee.Algorithms.TemporalSegmentation.VCT
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Vegetation Change Tracker, an automated approach for reconstructing recent forest disturbance history using dense Landsat time series stacks.
The output is a 2D array per pixel containing 6 rows x N years. The output rows contain: input years, VCT landcover mask, magnitude in term of the UD composite, magnitude of distubance in B4, magnitude of distubance in NDVI, magnitude of distubance in dNBR.
See: Huang, C., Goward, S.N., Masek, J.G., Thomas, N., Zhu, Z. and Vogelmann, J.E., 2010. An automated approach for reconstructing recent forest disturbance history using dense Landsat time series stacks. Remote Sensing of Environment, 114(1), pp.183-198.
Usage | Returns  
---|---  
`ee.Algorithms.TemporalSegmentation.VCT(timeSeries, landCover, _maxUd_, _minNdvi_, _forThrMax_, _nYears_)`|  Image  
Argument | Type | Details  
---|---|---  
`timeSeries` | ImageCollection | Collection from which to extract VCT disturbances, containing the bands: B3, B4, B5, B7, thermal, NDVI, DNBR, and COMP. This collection is expected to contain 1 image for each year, sorted by time.  
`landCover` | ImageCollection | Collection from which to extract VCT masks. This collection is expected to contain 1 image for each image in the timeSeries, sorted by time.  
`maxUd` | Float, default: 4 | Maximum Z-score composite value for detecting forest.  
`minNdvi` | Float, default: 0.45 | Minimum NDVI value for forest.  
`forThrMax` | Float, default: 3 | Maximum threshold for forest.  
`nYears` | Integer, default: 30 | Maximum number of years.  
