 
#  ee.FeatureCollection.getMapId
Stay organized with collections  Save and categorize content based on your preferences. 
Returns an object which may be passed to ee.data.getTileUrl or ui.Map.addLayer, including an additional 'image' field, containing a Collection.draw image wrapping a FeatureCollection containing this feature. Undefined if a callback was specified.
Usage | Returns  
---|---  
`FeatureCollection.getMapId(_visParams_, _callback_)`|  MapId|Object  
Argument | Type | Details  
---|---|---  
this: `featurecollection` | FeatureCollection | The FeatureCollection instance.  
`visParams` | Object, optional | The visualization parameters. Currently only one parameter, 'color', containing an RGB color string is allowed. If visParams is not specified, black ("000000") is used.  
`callback` | Function, optional | An async callback.  
