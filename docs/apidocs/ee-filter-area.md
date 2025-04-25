 
#  ee.Filter.area 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Returns a filter that passes if the specified geometry has an area within the given range (inclusive). 
Usage| Returns  
---|---  
`ee.Filter.area(min, max,  _maxError_, _geometrySelector_)`| Filter  
Argument| Type| Details  
---|---|---  
`min`| Float| Minimum area in square meters (inclusive).  
`max`| Float| Maximum area in square meters (inclusive).  
`maxError`| ErrorMargin, default: null| The maximum allowed error for computing the geometry's area.  
`geometrySelector`| String, default: null| The name of the geometry property to use for filtering. Leave blank or use '.geo' to operate on the object's geometry.  
