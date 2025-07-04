 
#  ee.Algorithms.GeometryConstructors.Rectangle
Stay organized with collections  Save and categorize content based on your preferences. 
Constructs a rectangular polygon from the given corner points. Usage| Returns  
---|---  
`ee.Algorithms.GeometryConstructors.Rectangle(coordinates,  _crs_, _geodesic_, _evenOdd_)`| Geometry  
Argument| Type| Details  
---|---|---  
`coordinates`| List| The low and then high corners of the Rectangle, as a list of Points or pairs of Numbers in x,y order.  
`crs`| Projection, default: null| The coordinate reference system of the coordinates. The default is the projection of the inputs, where Numbers are assumed to be EPSG:4326.  
`geodesic`| Boolean, default: null| If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth. The default is the geodesic state of the inputs, or true if the inputs are numbers.  
`evenOdd`| Boolean, default: true| If true, polygon interiors will be determined by the even/odd rule, where a point is inside if it crosses an odd number of edges to reach a point at infinity. Otherwise polygons use the left-inside rule, where interiors are on the left side of the shell's edges when walking the vertices in the given order.  
