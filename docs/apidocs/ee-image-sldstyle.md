 
#  ee.Image.sldStyle 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Styles a raster input with the provided OGC SLD styling. 
Points of note:
* OGC SLD 1.0 and OGC SE 1.1 are supported.
* The XML document passed in can be complete, or just the SldRasterSymbolizer element and down.
* Exactly one SldRasterSymbolizer is required.
* Bands may be selected by their proper EarthEngine names or using numeric identifiers ("1", "2", ...). Proper EarthEngine names are tried first.
* The Histogram and Normalize contrast stretch mechanisms are supported.
* The type="values", type="intervals" and type="ramp" attributes for ColorMap element in SLD 1.0 (GeoServer extensions) are supported.
* Opacity is only taken into account when it is 0.0 (transparent). Non-zero opacity values are treated as completely opaque.
* The OverlapBehavior definition is currently ignored.
* The ShadedRelief mechanism is not currently supported.
* The ImageOutline mechanism is not currently supported.
* The Geometry element is ignored.
The output image will have histogram_bandname metadata if histogram equalization or normalization is requested.
Usage| Returns  
---|---  
`Image.sldStyle(sldXml)`| Image  
Argument| Type| Details  
---|---|---  
this: `input`| Image| The image to rendering using the SLD.  
`sldXml`| String| The OGC SLD 1.0 or 1.1 document (or fragment).  
Was this helpful?
