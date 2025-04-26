 
#  Registering Images 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Image displacement](https://developers.google.com/earth-engine/guides/register#image_displacement)
  * [Warping an image](https://developers.google.com/earth-engine/guides/register#warping_an_image)


The Earth Engine image registration algorithm is designed to be a final, post-ortho, fine-grained step in aligning images. It is assumed that the images to be registered have already gone through initial alignment stages, so they are already within a few degrees of rotation of one another, and differ by only small translations. The registration uses a "rubber-sheet" technique, allowing local image warping to correct for orthorectification errors and other artifacts from earlier processing. The underlying alignment technique is image correlation, so the bands for the input and reference images must be visually similar in order for the algorithm to compute an accurate alignment.
## Image displacement
There are two steps to registering an image: Determining the displacement image using `displacement()`, and then applying it with `displace()`. The required inputs are the pair of images to register, and a maximum displacement parameter (`maxOffset`).
The `displacement()` algorithm takes a reference image, a maximum displacement parameter (`maxOffset`), and two optional parameters that modify the algorithm behaviour. The output is a displacement image with bands `dx` and `dy` which give the X and Y components (in meters) of the displacement vector at each pixel.
All bands of the calling and reference images are used for matching during registration, so the number of bands must be exactly equal. The input bands must be visually similar for registration to succeed. If that is not the case, it may be possible to pre-process them (e.g. smoothing, edge detection) to make them appear more similar. The registration computations are performed using a multiscale, coarse-to-fine process, with (multiscale) working projections that depend on three of the projections supplied to the algorithm:
  1. the default projection of the calling image (_P c_)
  2. the default projection of the reference image (_P r_)
  3. the output projection (_P o_)


The highest resolution working projection (_P w_ will be in the CRS of _P r_, at a scale determined by the coarsest resolution of these 3 projections, to minimize computation. The results from _P r_ are then resampled to be in the projection specified by the input 'projection' parameter.
The output is a displacement image with the following bands: 

`dx`
    For a given reference image pixel location, this band contains the distance in the X direction that must be travelled to arrive at the matching location in the calling image. Units are in geodesic meters. 

`dy`
    For a given reference image pixel location, this band contains the distance in the Y direction that must be travelled to arrive at the matching location in the calling image. Units are in geodesic meters. 

`confidence`
    This is a per-pixel estimate of displacement confidence (where 0 is low confidence and 1 is high confidence) based on the correlation scores in regions where valid matches were found. In regions where no matches were found, confidence is estimated from nearby correlations using a Gaussian kernel to provide higher weight to nearby correlations.
The following example computes the magnitude and angle of displacement between two high-resolution [Terra Bella](https://terrabella.google.com/) images:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/register#code-editor-javascript-sample) More
```
// Load the two images to be registered.
varimage1=ee.Image('SKYSAT/GEN-A/PUBLIC/ORTHO/MULTISPECTRAL/s01_20150502T082736Z');
varimage2=ee.Image('SKYSAT/GEN-A/PUBLIC/ORTHO/MULTISPECTRAL/s01_20150305T081019Z');
// Use bicubic resampling during registration.
varimage1Orig=image1.resample('bicubic');
varimage2Orig=image2.resample('bicubic');
// Choose to register using only the 'R' band.
varimage1RedBand=image1Orig.select('R');
varimage2RedBand=image2Orig.select('R');
// Determine the displacement by matching only the 'R' bands.
vardisplacement=image2RedBand.displacement({
referenceImage:image1RedBand,
maxOffset:50.0,
patchWidth:100.0
});
// Compute image offset and direction.
varoffset=displacement.select('dx').hypot(displacement.select('dy'));
varangle=displacement.select('dx').atan2(displacement.select('dy'));
// Display offset distance and angle.
Map.addLayer(offset,{min:0,max:20},'offset');
Map.addLayer(angle,{min:-Math.PI,max:Math.PI},'angle');
Map.setCenter(37.44,0.58,15);
```

## Warping an image
There are two ways to warp an image to match another image: `displace()` or `register()`. The `displace()` algorithm takes a displacement image having `dx` and `dy` bands as the first two bands, and warps the image accordingly. The output image will be the result of warping the bands of the input image by the offsets present in the displacement image. Using the displacements computed in the previous example:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/register#code-editor-javascript-sample) More
```
// Use the computed displacement to register all original bands.
varregistered=image2Orig.displace(displacement);
// Show the results of co-registering the images.
varvisParams={bands:['R','G','B'],max:4000};
Map.addLayer(image1Orig,visParams,'Reference');
Map.addLayer(image2Orig,visParams,'Before Registration');
Map.addLayer(registered,visParams,'After Registration');
```

If you don't need the displacement bands, Earth Engine provides the `register()` method, which is a shortcut for calling `displacement()` followed by `displace()`. For example:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/register#code-editor-javascript-sample) More
```
varalsoRegistered=image2Orig.register({
referenceImage:image1Orig,
maxOffset:50.0,
patchWidth:100.0
});
Map.addLayer(alsoRegistered,visParams,'Also Registered');
```

In this example, the results of `register()` differ from the results of `displace()`. This is because a different set of bands was used in the two approaches: `register()` always uses all bands of the input images, while the `displacement()` example used only the red band before feeding the result to `displace()`. Note that when multiple bands are used, if band variances are very different this could over-weight the high-variance bands, since the bands are jointly normalized when their spatial correlation scores are combined. This illustrates the importance of selecting band(s) that are visually the most similar when registering. As in the previous example, use `displacement()` and `displace()` for control over which bands are used to compute displacement.
