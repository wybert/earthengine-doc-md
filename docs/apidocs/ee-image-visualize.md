 
#  ee.Image.visualize
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Produces an RGB or grayscale visualization of an image. Each of the gain, bias, min, max and gamma arguments can take either a single value, which will be applied to all bands, or a list of values the same length as bands.
Usage | Returns  
---|---  
`Image.visualize(_bands_, _gain_, _bias_, _min_, _max_, _gamma_, _opacity_, _palette_, _forceRgbOutput_)`|  Image  
Argument | Type | Details  
---|---|---  
this: `image` | Image | The image to visualize.  
`bands` | Object, default: null | A list of the bands to visualize. If empty, the first 3 are used.  
`gain` | Object, default: null | The visualization gain(s) to use.  
`bias` | Object, default: null | The visualization bias(es) to use.  
`min` | Object, default: null | The value(s) to map to RGB8 value 0.  
`max` | Object, default: null | The value(s) to map to RGB8 value 255.  
`gamma` | Object, default: null | The gamma correction factor(s) to use.  
`opacity` | Number, default: null | The opacity scaling factor to use.  
`palette` | Object, default: null | The color palette to use. List of CSS color identifiers or hexadecimal color strings (e.g., ['red', '00FF00', 'blueviolet']).  
`forceRgbOutput` | Boolean, default: false | Whether to produce RGB output even for single-band inputs.  
Was this helpful?
