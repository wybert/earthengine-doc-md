 
#  ee.Image.interpolate 
Stay organized with collections  Save and categorize content based on your preferences. 
Interpolates each point in the first band of the input image into the piecewise-linear function specified by the x and y arrays. The x values must be strictly increasing. If an input point is less than the first or greater than the last x value, then the output is specified by the "behavior" argument: "extrapolate" specifies the output value is extrapolated from the two nearest points, "clamp" specifies the output value is taken from the nearest point, "input" specifies the output value is copied from the input, and "mask" specifies the output value is masked. Usage| Returns  
---|---  
`Image.interpolate(x, y,  _behavior_)`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The image to which the interpolation is applied.  
`x`| List| The x axis (input) values in the piecewise function.  
`y`| List| The y axis (output) values in the piecewise function.  
`behavior`| String, default: "extrapolate"| The behavior for points that are outside of the range of the supplied function. Options are: 'extrapolate', 'clamp', 'mask', or 'input'.  
