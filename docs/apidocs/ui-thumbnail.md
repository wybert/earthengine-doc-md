 
#  ui.Thumbnail 
Stay organized with collections  Save and categorize content based on your preferences. 
A fixed-size thumbnail image generated asynchronously from an ee.Image. Usage| Returns  
---|---  
`ui.Thumbnail( _image_, _params_, _onClick_, _style_)`| ui.Thumbnail  
Argument| Type| Details  
---|---|---  
`image`| Image, optional| The ee.Image from which to generate the thumbnail. Defaults to an empty ee.Image.  
`params`| Object, optional| For an explanation of the possible parameters, see ui.Thumbnail.setParams(). Defaults to an empty object.  
`onClick`| Function, optional| A callback fired when the thumbnail is clicked.  
`style`| Object, optional| An object of allowed CSS styles with their values to be set for this label. Defaults to an empty object.  
## Examples
### Code Editor (JavaScript)
```
// The goal is to create a series of thumbnail images for an elevation dataset
// with different backgrounds. The background layers and image visualization
// are previewed in the Code Editor map before creating the thumbnails.
// Define a black background.
varblackBg=ee.Image.rgb(0,0,0)
.visualize({min:0,max:255});
Map.addLayer(blackBg,{},'Black background');
// Define a water / land background.
varwaterLandBg=ee.Image('NOAA/NGDC/ETOPO1').select('bedrock').gt(0.0)
.visualize({palette:['cadetblue','lightgray']});
Map.addLayer(waterLandBg,{},'Water / land background');
// A map display of a digital elevation model (DEM).
varimage=ee.Image('AU/GA/DEM_1SEC/v10/DEM-S').select('elevation')
.visualize({
min:-10.0,
max:1300.0,
palette:[
'3ae237','b5e22e','d6e21f','fff705','ffd611','ffb613','ff8b13',
'ff6e08','ff500d','ff0000','de0101','c21301','0602ff','235cb1',
'307ef3','269db1','30c8e2','32d3ef','3be285','3ff38f','86e26f'
],
});
Map.addLayer(image,{},'Elevation');
// Set the center of the map.
varlon=133.95;
varlat=-24.69;
Map.setCenter(lon,lat,4);
// Set the basic parameters for the thumbnail.
// Half-width of the thumbnail in degrees in EPSG:3857.
vardelta=22;
// Width and Height of the Thumbail image.
varpixels=256;
varareaOfInterest=ee.Geometry.Rectangle(
[lon-delta,lat-delta,lon+delta,lat+delta],null,false);
varparameters={
dimensions:[pixels,pixels],
region:areaOfInterest,
crs:'EPSG:3857',
format:'png'};
// Create a thumbnail with no background fill.
// Masked pixels will be transparent.
print(ui.Thumbnail({image:image,params:parameters}));
// Use a black background to replace masked image pixels.
varimageWithBlackBg=blackBg.blend(image);
print(ui.Thumbnail({
image:imageWithBlackBg,params:parameters}));
// Use the water / land background to replace masked image pixels.
varimageWithWaterLandBg=waterLandBg.blend(image);
print(ui.Thumbnail({
image:imageWithWaterLandBg,params:parameters}));
```

