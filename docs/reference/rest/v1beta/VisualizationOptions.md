 
#  VisualizationOptions
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Describes how to produce an 8-bit RGB visualization of the requested data.
JSON representation  
---  
```
{
  "ranges": [
    {
      object (DoubleRange[](https://developers.google.com/earth-engine/reference/rest/v1beta/DoubleRange))
    }
  ],
  "paletteColors": [
    string
  ],
  "gamma": number,
  "opacity": number
}
```
  
Fields  
---  
`ranges[]` |  `object (`DoubleRange[](https://developers.google.com/earth-engine/reference/rest/v1beta/DoubleRange)`)` If present, specifies the range of data values to visualize. This range of values will be mapped to 0-255 (black to white) in the resulting image, and values outside this range will be clamped. May specify as one range for each band being visualized or else a single range to be applied to all bands.  
`paletteColors[]` |  `string` If present, specifies sequence of CSS-style RGB color identifiers to apply as a color palette. Only allowed when visualizing a single data band.  
`gamma` |  `number` If present, specifies an overall gamma correction factor to apply to the image.  
`opacity` |  `number` If present, specifies an overall opacity factor to apply to the image, in the range 0.0 to 1.0.  
