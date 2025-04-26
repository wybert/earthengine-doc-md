 
#  ee.Geometry.fromS2CellToken 
Stay organized with collections  Save and categorize content based on your preferences. 
Constructs the Polygon corresponding to an S2 cell id as a hex string. 
Usage| Returns  
---|---  
`ee.Geometry.fromS2CellToken(cellToken)`| Geometry  
Argument| Type| Details  
---|---|---  
`cellToken`| String| The S2 cell id as a hex string. Trailing zeros are required, e.g., the top level face containing Antarctica is 0xb000000000000000.  
