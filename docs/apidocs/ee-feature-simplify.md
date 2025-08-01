 
#  ee.Feature.simplify
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Simplifies the geometry of a feature to within a given error margin. Note that this does not respect the error margin requested by the consumer of this algorithm, unless maxError is explicitly specified to be null.
This overrides the default Earth Engine policy for propagating error margins, so regardless of the geometry accuracy requested from the output, the inputs will be requested with the error margin specified in the arguments to this algorithm. This results in consistent rendering at all zoom levels of a rendered vector map, but at lower zoom levels (i.e. zoomed out), the geometry won't be simplified, which may harm performance.
Usage | Returns  
---|---  
`Feature.simplify(maxError, _proj_)`|  Feature  
Argument | Type | Details  
---|---|---  
this: `feature` | Element | The feature whose geometry is being simplified.  
`maxError` | ErrorMargin | The maximum amount of error by which the result may differ from the input.  
`proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in the same projection as the input. If the error margin is in projected units, the margin will be interpreted as units of this projection.  
Was this helpful?
