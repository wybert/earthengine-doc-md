 
#  ee.ImageCollection.errorMatrix
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Computes a 2D error matrix for a collection by comparing two columns of a collection: one containing the actual values, and one containing predicted values. The values are expected to be small contiguous integers, starting from 0. Axis 0 (the rows) of the matrix correspond to the actual values, and Axis 1 (the columns) to the predicted values.
Usage | Returns  
---|---  
`ImageCollection.errorMatrix(actual, predicted, _order_)`|  ConfusionMatrix  
Argument | Type | Details  
---|---|---  
this: `collection` | FeatureCollection | The input collection.  
`actual` | String | The name of the property containing the actual value.  
`predicted` | String | The name of the property containing the predicted value.  
`order` | List, default: null | A list of the expected values. If this argument is not specified, the values are assumed to be contiguous and span the range 0 to maxValue. If specified, only values matching this list are used, and the matrix will have dimensions and order matching this list.  
