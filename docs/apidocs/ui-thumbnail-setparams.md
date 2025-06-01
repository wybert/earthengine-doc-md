 
#  ui.Thumbnail.setParams 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Sets the parameters used to generate the thumbnail. 
Returns this thumbnail.
Usage| Returns  
---|---  
`Thumbnail.setParams(params)`| ui.Thumbnail  
Argument| Type| Details  
---|---|---  
this: `ui.thumbnail`| ui.Thumbnail| The ui.Thumbnail instance.  
`params`| Object| The parameters used in generating the thumbnail.  | ` dimensions ` (a number or pair of numbers in format WIDTHxHEIGHT) Maximum dimensions of the thumbnail to render, in pixels. If only one number is passed, it is used as the maximum, and the other dimension is computed by proportional scaling.  
---  
` region ` (E,S,W,N or GeoJSON) Geospatial region of the image to render. By default, the whole image.  
` format ` (string) Either 'png' or 'jpg'.  
` bands ` (comma-separated strings) Comma-delimited list of band names to be mapped to RGB.  
` min ` (comma-separated numbers) Value (or one per band) to map onto 00.  
` max ` (comma-separated numbers) Value (or one per band) to map onto FF.  
` gain ` (comma-separated numbers) Gain (or one per band) to map onto 00-FF.  
` bias ` (comma-separated numbers) Offset (or one per band) to map onto 00-FF.  
` gamma ` (comma-separated numbers) Gamma correction factor (or one per band)  
` palette ` (comma-separated strings) List of CSS-style color strings (single-band previews only).  
` opacity ` (number) a number between 0 and 1 for opacity.  
` version ` (number) Version number of image (or latest).  
