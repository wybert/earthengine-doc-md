 
#  ee.Image.reduceConnectedComponents
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Applies a reducer to all of the pixels inside of each 'object'. Pixels are considered to belong to an object if they are connected (8-way) and have the same value in the 'label' band. The label band is only used to identify the connectedness; the rest are provided as inputs to the reducer.
Usage | Returns  
---|---  
`Image.reduceConnectedComponents(reducer, _labelBand_, _maxSize_)`|  Image  
Argument | Type | Details  
---|---|---  
this: `image` | Image | The input image.  
`reducer` | Reducer | The reducer to apply to pixels within the connected component.  
`labelBand` | String, default: null | The name of the band to use to detect connectedness. If unspecified, the first band is used.  
`maxSize` | Integer, default: 256 | Size of the neighborhood to consider when aggregating values. Any objects larger than maxSize in either the horizontal or vertical dimension will be masked, since portions of the object might be outside of the neighborhood.  
Was this helpful?
