 
#  ee.Image.reduceToVectors
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Convert an image to a feature collection by reducing homogeneous regions. Given an image containing a band of labeled segments and zero or more additional bands, runs a reducer over the pixels in each segment producing a feature per segment.
Either the reducer must have one fewer inputs than the image has bands, or it must have a single input and will be repeated for each band.
Usage | Returns  
---|---  
`Image.reduceToVectors(_reducer_, _geometry_, _scale_, _geometryType_, _eightConnected_, _labelProperty_, _crs_, _crsTransform_, _bestEffort_, _maxPixels_, _tileScale_, _geometryInNativeProjection_)`|  FeatureCollection  
Argument | Type | Details  
---|---|---  
this: `image` | Image | The input image. The first band is expected to be an integer type; adjacent pixels will be in the same segment if they have the same value in this band.  
`reducer` | Reducer, default: null | The reducer to apply. Its inputs will be taken from the image's bands after dropping the first band. Defaults to Reducer.countEvery().  
`geometry` | Geometry, default: null | The region over which to reduce data. Defaults to the footprint of the image's first band.  
`scale` | Float, default: null | A nominal scale in meters of the projection to work in.  
`geometryType` | String, default: "polygon" | How to choose the geometry of each generated feature; one of 'polygon' (a polygon enclosing the pixels in the segment), 'bb' (a rectangle bounding the pixels), or 'centroid' (the centroid of the pixels).  
`eightConnected` | Boolean, default: true | If true, diagonally-connected pixels are considered adjacent; otherwise only pixels that share an edge are.  
`labelProperty` | String, default: "label" | If non-null, the value of the first band will be saved as the specified property of each feature.  
`crs` | Projection, default: null | The projection to work in. If unspecified, the projection of the image's first band is used. If specified in addition to scale, rescaled to the specified scale.  
`crsTransform` | List, default: null | The list of CRS transform values. This is a row-major ordering of the 3x2 transform matrix. This option is mutually exclusive with 'scale', and replaces any transform already set on the projection.  
`bestEffort` | Boolean, default: false | If the polygon would contain too many pixels at the given scale, compute and use a larger scale which would allow the operation to succeed.  
`maxPixels` | Long, default: 10000000 | The maximum number of pixels to reduce.  
`tileScale` | Float, default: 1 | A scaling factor used to reduce aggregation tile size; using a larger tileScale (e.g., 2 or 4) may enable computations that run out of memory with the default.  
`geometryInNativeProjection` | Boolean, default: false | Create geometries in the pixel projection, rather than EPSG:4326.  
Was this helpful?
