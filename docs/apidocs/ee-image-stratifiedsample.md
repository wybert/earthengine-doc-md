 
#  ee.Image.stratifiedSample
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Extracts a stratified random sample of points from an image. Extracts the specified number of samples for each distinct value discovered within the 'classBand'. Returns a FeatureCollection of 1 Feature per extracted point, with each feature having 1 property per band in the input image. If there are less than the specified number of samples available for a given class value, then all of the points for that class will be included. Requires that the classBand contain integer values. 
Usage| Returns  
---|---  
`Image.stratifiedSample(numPoints,  _classBand_, _region_, _scale_, _projection_, _seed_, _classValues_, _classPoints_, _dropNulls_, _tileScale_, _geometries_)`| FeatureCollection  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The image to sample.  
`numPoints`| Integer| The default number of points to sample in each class. Can be overridden for specific classes using the 'classValues' and 'classPoints' properties.  
`classBand`| String, default: null| The name of the band containing the classes to use for stratification. If unspecified, the first band of the input image is used.  
`region`| Geometry, default: null| The region to sample from. If unspecified, the input image's whole footprint is used.  
`scale`| Float, default: null| A nominal scale in meters of the projection to sample in. Defaults to the scale of the first band of the input image.  
`projection`| Projection, default: null| The projection in which to sample. If unspecified, the projection of the input image's first band is used. If specified in addition to scale, rescaled to the specified scale.  
`seed`| Integer, default: 0| A randomization seed to use for subsampling.  
`classValues`| List, default: null| A list of class values for which to override the numPoints parameter. Must be the same size as classPoints or null.  
`classPoints`| List, default: null| A list of the per-class maximum number of pixels to sample for each class in the classValues list. Must be the same size as classValues or null.  
`dropNulls`| Boolean, default: true| Skip pixels in which any band is masked.  
`tileScale`| Float, default: 1| A scaling factor used to reduce aggregation tile size; using a larger tileScale (e.g., 2 or 4) may enable computations that run out of memory with the default.  
`geometries`| Boolean, default: false| If true, the results will include a geometry per sampled pixel. Otherwise, geometries will be omitted (saving memory).  
Was this helpful?
