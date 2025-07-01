 
#  ee.Image.paint
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Paints the geometries of a collection onto an image, using the given 'color' value to replace each band's values where any geometry covers the image (or, if a line width is specified, where the perimeters do). 
This algorithm is most suitable for converting categorical data from feature properties to pixels in an image; if you wish to visualize a collection, consider using FeatureCollection.style instead, which supports RGB colors whereas this algorithm is strictly 'monochrome' (using single numeric values).
Usage| Returns  
---|---  
`Image.paint(featureCollection,  _color_, _width_)`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The image on which the collection is painted.  
`featureCollection`| FeatureCollection| The collection painted onto the image.  
`color`| Object, default: 0| The pixel value to paint into every band of the input image, either as a number which will be used for all features, or the name of a numeric property to take from each feature in the collection.  
`width`| Object, default: null| Line width, either as a number which will be the line width for all geometries, or the name of a numeric property to take from each feature in the collection. If unspecified, the geometries will be filled instead of outlined.  
