 
#  ee.Image.hersImage
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Computes the Histogram Error Ring Statistic (HERS) for each pair of pixels in each band present in both images. Only the bands for which HERS could be computed are returned.
Usage | Returns  
---|---  
`Image.hersImage(image2, radius, _buckets_, _peakWidthScale_)`|  Image  
Argument | Type | Details  
---|---|---  
this: `image` | Image | The input image.  
`image2` | Image | The image to compare.  
`radius` | Integer | The radius of the window.  
`buckets` | Integer, default: 100 | The number of HERS buckets.  
`peakWidthScale` | Float, default: 1 | The HERS peak width scale.  
Was this helpful?
