 
#  ee.Geometry.fromS2CellId
Stay organized with collections  Save and categorize content based on your preferences. 
Constructs the Polygon corresponding to an S2 cell id. Usage | Returns  
---|---  
`ee.Geometry.fromS2CellId(cellId)` | Geometry  
Argument | Type | Details  
---|---|---  
`cellId` | Long | The S2 cell id as 64 bit integer. From Javascript, which does not support integers larger than 53 bits, use fromS2CellToken instead.  
