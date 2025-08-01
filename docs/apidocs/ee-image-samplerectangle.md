 
#  ee.Image.sampleRectangle
Stay organized with collections  Save and categorize content based on your preferences. 
Extracts a rectangular region of pixels from an image into a ND array per band. The arrays are returned in a feature retaining the same properties as the image and a geometry the same as that used to sample the image (or the image footprint if unspecified). Each band is sampled in its input projection, and if no geometry is specified, sampled using its footprint. For scalar bands, the output array is 2D. For array bands the output array is (2+N)D where N is the number of dimensions in the original band. If sampling array bands, all arrays must have the same number of elements. If a band's sampled region is entirely masked and a default array value is specified, the default array value is used in-lieu of sampling the image. Usage | Returns  
---|---  
`Image.sampleRectangle(_region_, _properties_, _defaultValue_, _defaultArrayValue_)`|  Feature  
Argument | Type | Details  
---|---|---  
this: `image` | Image | The image to sample.  
`region` | Geometry, default: null | The region whose projected bounding box is used to sample the image. Defaults to the footprint in each band.  
`properties` | List, default: null | The properties to copy over from the sampled image. Defaults to all non-system properties.  
`defaultValue` | Float, default: null | A default value used when a sampled pixel is masked or outside a band's footprint.  
`defaultArrayValue` | Array, default: null | A default value used when a sampled array pixel is masked or outside a band's footprint.  
