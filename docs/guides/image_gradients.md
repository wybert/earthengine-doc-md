 
#  Gradients 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
You can compute the gradient of each band of an image with `image.gradient()`. For example, the following code computes the gradient magnitude and direction of the Landsat 8 panchromatic band:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/image_gradients#code-editor-javascript-sample) More
```
// Load a Landsat 8 image and select the panchromatic band.
varimage=ee.Image('LANDSAT/LC08/C02/T1/LC08_044034_20140318').select('B8');
// Compute the image gradient in the X and Y directions.
varxyGrad=image.gradient();
// Compute the magnitude of the gradient.
vargradient=xyGrad.select('x').pow(2)
.add(xyGrad.select('y').pow(2)).sqrt();
// Compute the direction of the gradient.
vardirection=xyGrad.select('y').atan2(xyGrad.select('x'));
// Display the results.
Map.setCenter(-122.054,37.7295,10);
Map.addLayer(direction,{min:-2,max:2,format:'png'},'direction');
Map.addLayer(gradient,{min:-7,max:7,format:'png'},'gradient');
```

Note that `gradient()` outputs two bands: the gradient in the X-direction and the gradient in the Y-direction. As shown in the example, the two directions can be combined to get gradient magnitude and direction. The magnitude should look something like Figure 1.
![gradient_sf](https://developers.google.com/static/earth-engine/images/Images_gradients_sf.png) Figure 1. Panchromatic gradient magnitude for the Landsat 8 imagery over the San Francisco Bay area, California, USA. 
