 
#  ee.ImageCollection.style 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Draw a vector collection for visualization using a simple style language. 
Usage| Returns  
---|---  
`ImageCollection.style( _color_, _pointSize_, _pointShape_, _width_, _fillColor_, _styleProperty_, _neighborhood_, _lineType_)`| Image  
Argument| Type| Details  
---|---|---  
this: `collection`| FeatureCollection| The collection to draw.  
`color`| String, default: "black"| A default color (CSS 3.0 color value e.g., 'FF0000' or 'red') to use for drawing the features. Supports opacity (e.g., 'FF000088' for 50% transparent red).  
`pointSize`| Integer, default: 3| The default size in pixels of the point markers.  
`pointShape`| String, default: "circle"| The default shape of the marker to draw at each point location. One of: `circle`, `square`, `diamond`, `cross`, `plus`, `pentagram`, `hexagram`, `triangle`, `triangle_up`, `triangle_down`, `triangle_left`, `triangle_right`, `pentagon`, `hexagon`, `star5`, `star6`. This argument also supports these Matlab marker abbreviations: `o`, `s`, `d`, `x`, `+`, `p`, `h`, `^`, `v`, `<`, `>`.  
`width`| Float, default: 2| The default line width for lines and outlines for polygons and point shapes.  
`fillColor`| String, default: null| The color for filling polygons and point shapes. Defaults to 'color' at 0.66 opacity.  
`styleProperty`| String, default: null| A per-feature property expected to contain a dictionary. Values in the dictionary override any default values for that feature.  
`neighborhood`| Integer, default: 5| If styleProperty is used and any feature has a pointSize or width larger than the defaults, tiling artifacts can occur. Specifies the maximum neighborhood (pointSize + width) needed for any feature.  
`lineType`| String, default: "solid"| The default line style for lines and outlines of polygons and point shapes. Defaults to 'solid'. One of: solid, dotted, dashed.  
