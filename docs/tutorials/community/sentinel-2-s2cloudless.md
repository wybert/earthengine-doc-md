 
#  Sentinel-2 Cloud Masking with s2cloudless
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Run me first](https://developers.google.com/earth-engine/tutorials/community/sentinel-2-s2cloudless#run_me_first)
  * [Assemble cloud mask components](https://developers.google.com/earth-engine/tutorials/community/sentinel-2-s2cloudless#assemble_cloud_mask_components)
    * [Define collection filter and cloud mask parameters](https://developers.google.com/earth-engine/tutorials/community/sentinel-2-s2cloudless#define_collection_filter_and_cloud_mask_parameters)
    * [Build a Sentinel-2 collection](https://developers.google.com/earth-engine/tutorials/community/sentinel-2-s2cloudless#build_a_sentinel-2_collection)
    * [Define cloud mask component functions](https://developers.google.com/earth-engine/tutorials/community/sentinel-2-s2cloudless#define_cloud_mask_component_functions)
  * [Visualize and evaluate cloud mask components](https://developers.google.com/earth-engine/tutorials/community/sentinel-2-s2cloudless#visualize_and_evaluate_cloud_mask_components)
    * [Define functions to display image and mask component layers.](https://developers.google.com/earth-engine/tutorials/community/sentinel-2-s2cloudless#define_functions_to_display_image_and_mask_component_layers)
    * [Display mask component layers](https://developers.google.com/earth-engine/tutorials/community/sentinel-2-s2cloudless#display_mask_component_layers)
    * [Evaluate mask component layers](https://developers.google.com/earth-engine/tutorials/community/sentinel-2-s2cloudless#evaluate_mask_component_layers)
  * [Apply cloud and cloud shadow mask](https://developers.google.com/earth-engine/tutorials/community/sentinel-2-s2cloudless#apply_cloud_and_cloud_shadow_mask)
    * [Define collection filter and cloud mask parameters](https://developers.google.com/earth-engine/tutorials/community/sentinel-2-s2cloudless#define_collection_filter_and_cloud_mask_parameters_2)
    * [Build a Sentinel-2 collection](https://developers.google.com/earth-engine/tutorials/community/sentinel-2-s2cloudless#build_a_sentinel-2_collection_2)
    * [Define cloud mask application function](https://developers.google.com/earth-engine/tutorials/community/sentinel-2-s2cloudless#define_cloud_mask_application_function)
    * [Process the collection](https://developers.google.com/earth-engine/tutorials/community/sentinel-2-s2cloudless#process_the_collection)
    * [Display the cloud-free composite](https://developers.google.com/earth-engine/tutorials/community/sentinel-2-s2cloudless#display_the_cloud-free_composite)


Author(s): [ jdbcode ](https://github.com/jdbcode "View the profile for jdbcode on GitHub")
Tutorials contributed by the Earth Engine developer community are not part of the official Earth Engine product documentation. 
[ ![Colab logo](https://developers.google.com/static/earth-engine/images/colab_logo_32px.png) Run in Google Colab ](https://colab.research.google.com/github/google/earthengine-community/blob/master/tutorials/sentinel-2-s2cloudless/index.ipynb) |  [ ![GitHub logo](https://developers.google.com/static/earth-engine/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/earthengine-community/blob/master/tutorials/sentinel-2-s2cloudless/index.ipynb)  
---|---  
This tutorial is an introduction to masking clouds and cloud shadows in Sentinel-2 (S2) surface reflectance (SR) data using Earth Engine. Clouds are identified from the S2 cloud probability dataset (s2cloudless) and shadows are defined by cloud projection intersection with low-reflectance near-infrared (NIR) pixels.
For a similar JavaScript API script, see this [Code Editor example](https://code.earthengine.google.com/?scriptPath=Examples%3ACloud%20Masking%2FSentinel2%20Cloud%20And%20Shadow).
### Run me first
Run the following cell to initialize the Earth Engine API. The output will contain instructions on how to grant this notebook access to Earth Engine using your account.
```
importee

# Trigger the authentication flow.
ee.Authenticate()

# Initialize the library.
ee.Initialize(project='my-project')

```

## Assemble cloud mask components
This section builds an S2 SR collection and defines functions to add cloud and cloud shadow component layers to each image in the collection.
### Define collection filter and cloud mask parameters
Define parameters that are used to filter the S2 image collection and determine cloud and cloud shadow identification.
Parameter | Type | Description  
---|---|---  
`AOI` | `ee.Geometry` | Area of interest  
`START_DATE` | string | Image collection start date (inclusive)  
`END_DATE` | string | Image collection end date (exclusive)  
`CLOUD_FILTER` | integer | Maximum image cloud cover percent allowed in image collection  
`CLD_PRB_THRESH` | integer | Cloud probability (%); values greater than are considered cloud  
`NIR_DRK_THRESH` | float | Near-infrared reflectance; values less than are considered potential cloud shadow  
`CLD_PRJ_DIST` | float | Maximum distance (km) to search for cloud shadows from cloud edges  
`BUFFER` | integer | Distance (m) to dilate the edge of cloud-identified objects  
The values currently set for `AOI`, `START_DATE`, `END_DATE`, and `CLOUD_FILTER` are intended to build a collection for a single S2 overpass of a region near Portland, Oregon, USA. When parameterizing and evaluating cloud masks for a new area, it is good practice to identify a single overpass date and limit the regional extent to minimize processing requirements. If you want to work with a different example, use this [Earth Engine App](https://showcase.earthengine.app/view/s2-sr-browser-s2cloudless-nb) to identify an image that includes some clouds, then replace the relevant parameter values below with those provided in the app.
```
AOI = ee.Geometry.Point(-122.269, 45.701)
START_DATE = '2020-06-01'
END_DATE = '2020-06-02'
CLOUD_FILTER = 60
CLD_PRB_THRESH = 50
NIR_DRK_THRESH = 0.15
CLD_PRJ_DIST = 1
BUFFER = 50

```

### Build a Sentinel-2 collection
[Sentinel-2 surface reflectance](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR) and [Sentinel-2 cloud probability](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_CLOUD_PROBABILITY) are two different image collections. Each collection must be filtered similarly (e.g., by date and bounds) and then the two filtered collections must be joined.
Define a function to filter the SR and s2cloudless collections according to area of interest and date parameters, then join them on the `system:index` property. The result is a copy of the SR collection where each image has a new `'s2cloudless'` property whose value is the corresponding s2cloudless image.
```
defget_s2_sr_cld_col(aoi, start_date, end_date):
    # Import and filter S2 SR.
    s2_sr_col = (ee.ImageCollection('COPERNICUS/S2_SR')
        .filterBounds(aoi)
        .filterDate(start_date, end_date)
        .filter(ee.Filter.lte('CLOUDY_PIXEL_PERCENTAGE', CLOUD_FILTER)))

    # Import and filter s2cloudless.
    s2_cloudless_col = (ee.ImageCollection('COPERNICUS/S2_CLOUD_PROBABILITY')
        .filterBounds(aoi)
        .filterDate(start_date, end_date))

    # Join the filtered s2cloudless collection to the SR collection by the 'system:index' property.
    return ee.ImageCollection(ee.Join.saveFirst('s2cloudless').apply(**{
        'primary': s2_sr_col,
        'secondary': s2_cloudless_col,
        'condition': ee.Filter.equals(**{
            'leftField': 'system:index',
            'rightField': 'system:index'
        })
    }))

```

Apply the `get_s2_sr_cld_col` function to build a collection according to the parameters defined above.
```
s2_sr_cld_col_eval = get_s2_sr_cld_col(AOI, START_DATE, END_DATE)

```
```
/tmpfs/src/tf_docs_env/lib/python3.9/site-packages/ee/deprecation.py:209: DeprecationWarning: 

Attention required for COPERNICUS/S2_SR! You are using a deprecated asset.
To make sure your code keeps working, please update it.
Learn more: https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR

  warnings.warn(warning, category=DeprecationWarning)

```

### Define cloud mask component functions
#### Cloud components
Define a function to add the s2cloudless probability layer and derived cloud mask as bands to an S2 SR image input.
```
defadd_cloud_bands(img):
    # Get s2cloudless image, subset the probability band.
    cld_prb = ee.Image(img.get('s2cloudless')).select('probability')

    # Condition s2cloudless by the probability threshold value.
    is_cloud = cld_prb.gt(CLD_PRB_THRESH).rename('clouds')

    # Add the cloud probability layer and cloud mask as image bands.
    return img.addBands(ee.Image([cld_prb, is_cloud]))

```

#### Cloud shadow components
Define a function to add dark pixels, cloud projection, and identified shadows as bands to an S2 SR image input. Note that the image input needs to be the result of the above `add_cloud_bands` function because it relies on knowing which pixels are considered cloudy (`'clouds'` band).
```
defadd_shadow_bands(img):
    # Identify water pixels from the SCL band.
    not_water = img.select('SCL').neq(6)

    # Identify dark NIR pixels that are not water (potential cloud shadow pixels).
    SR_BAND_SCALE = 1e4
    dark_pixels = img.select('B8').lt(NIR_DRK_THRESH*SR_BAND_SCALE).multiply(not_water).rename('dark_pixels')

    # Determine the direction to project cloud shadow from clouds (assumes UTM projection).
    shadow_azimuth = ee.Number(90).subtract(ee.Number(img.get('MEAN_SOLAR_AZIMUTH_ANGLE')));

    # Project shadows from clouds for the distance specified by the CLD_PRJ_DIST input.
    cld_proj = (img.select('clouds').directionalDistanceTransform(shadow_azimuth, CLD_PRJ_DIST*10)
        .reproject(**{'crs': img.select(0).projection(), 'scale': 100})
        .select('distance')
        .mask()
        .rename('cloud_transform'))

    # Identify the intersection of dark pixels with cloud shadow projection.
    shadows = cld_proj.multiply(dark_pixels).rename('shadows')

    # Add dark pixels, cloud projection, and identified shadows as image bands.
    return img.addBands(ee.Image([dark_pixels, cld_proj, shadows]))

```

#### Final cloud-shadow mask
Define a function to assemble all of the cloud and cloud shadow components and produce the final mask.
```
defadd_cld_shdw_mask(img):
    # Add cloud component bands.
    img_cloud = add_cloud_bands(img)

    # Add cloud shadow component bands.
    img_cloud_shadow = add_shadow_bands(img_cloud)

    # Combine cloud and shadow mask, set cloud and shadow as value 1, else 0.
    is_cld_shdw = img_cloud_shadow.select('clouds').add(img_cloud_shadow.select('shadows')).gt(0)

    # Remove small cloud-shadow patches and dilate remaining pixels by BUFFER input.
    # 20 m scale is for speed, and assumes clouds don't require 10 m precision.
    is_cld_shdw = (is_cld_shdw.focalMin(2).focalMax(BUFFER*2/20)
        .reproject(**{'crs': img.select([0]).projection(), 'scale': 20})
        .rename('cloudmask'))

    # Add the final cloud-shadow mask to the image.
    return img_cloud_shadow.addBands(is_cld_shdw)

```

## Visualize and evaluate cloud mask components
This section provides functions for displaying the cloud and cloud shadow components. In most cases, adding all components to images and viewing them is unnecessary. This section is included to illustrate how the cloud/cloud shadow mask is developed and demonstrate how to test and evaluate various parameters, which is helpful when defining masking variables for an unfamiliar region or time of year.
In applications outside of this tutorial, if you prefer to include only the final cloud/cloud shadow mask along with the original image bands, replace:
```
returnimg_cloud_shadow.addBands(is_cld_shdw)

```

with
```
returnimg.addBands(is_cld_shdw)

```

in the above `add_cld_shdw_mask` function.
### Define functions to display image and mask component layers.
Folium will be used to display map layers. Import `folium` and define a method to display Earth Engine image tiles.
```
# Import the folium library.
importfolium

# Define a method for displaying Earth Engine image tiles to a folium map.
defadd_ee_layer(self, ee_image_object, vis_params, name, show=True, opacity=1, min_zoom=0):
    map_id_dict = ee.Image(ee_image_object).getMapId(vis_params)
    folium.raster_layers.TileLayer(
        tiles=map_id_dict['tile_fetcher'].url_format,
        attr='Map Data &copy; <a href="https://earthengine.google.com/">Google Earth Engine</a>',
        name=name,
        show=show,
        opacity=opacity,
        min_zoom=min_zoom,
        overlay=True,
        control=True
        ).add_to(self)

# Add the Earth Engine layer method to folium.
folium.Map.add_ee_layer = add_ee_layer

```

Define a function to display all of the cloud and cloud shadow components to an interactive Folium map. The input is an image collection where each image is the result of the `add_cld_shdw_mask` function defined previously.
```
defdisplay_cloud_layers(col):
    # Mosaic the image collection.
    img = col.mosaic()

    # Subset layers and prepare them for display.
    clouds = img.select('clouds').selfMask()
    shadows = img.select('shadows').selfMask()
    dark_pixels = img.select('dark_pixels').selfMask()
    probability = img.select('probability')
    cloudmask = img.select('cloudmask').selfMask()
    cloud_transform = img.select('cloud_transform')

    # Create a folium map object.
    center = AOI.centroid(10).coordinates().reverse().getInfo()
    m = folium.Map(location=center, zoom_start=12)

    # Add layers to the folium map.
    m.add_ee_layer(img,
                   {'bands': ['B4', 'B3', 'B2'], 'min': 0, 'max': 2500, 'gamma': 1.1},
                   'S2 image', True, 1, 9)
    m.add_ee_layer(probability,
                   {'min': 0, 'max': 100},
                   'probability (cloud)', False, 1, 9)
    m.add_ee_layer(clouds,
                   {'palette': 'e056fd'},
                   'clouds', False, 1, 9)
    m.add_ee_layer(cloud_transform,
                   {'min': 0, 'max': 1, 'palette': ['white', 'black']},
                   'cloud_transform', False, 1, 9)
    m.add_ee_layer(dark_pixels,
                   {'palette': 'orange'},
                   'dark_pixels', False, 1, 9)
    m.add_ee_layer(shadows, {'palette': 'yellow'},
                   'shadows', False, 1, 9)
    m.add_ee_layer(cloudmask, {'palette': 'orange'},
                   'cloudmask', True, 0.5, 9)

    # Add a layer control panel to the map.
    m.add_child(folium.LayerControl())

    # Display the map.
    display(m)

```

### Display mask component layers
Map the `add_cld_shdw_mask` function over the collection to add mask component bands to each image, then display the results.
Give the system some time to render everything, it should take less than a minute.
```
s2_sr_cld_col_eval_disp = s2_sr_cld_col_eval.map(add_cld_shdw_mask)

display_cloud_layers(s2_sr_cld_col_eval_disp)

```

![png](https://developers.google.com/static/earth-engine/tutorials/community/sentinel-2-s2cloudless/index_files/output_gvsULCqgdLHu_0.png)
### Evaluate mask component layers
In the above map, use the layer control panel in the upper right corner to toggle layers on and off; layer names are the same as band names, for easy code referral. Note that the layers have a minimum zoom level of 9 to avoid resource issues that can occur when visualizing layers that depend on the `ee.Image.reproject` function (used during cloud shadow project and mask dilation).
Try changing the above `CLD_PRB_THRESH`, `NIR_DRK_THRESH`, `CLD_PRJ_DIST`, and `BUFFER` input variables and rerunning the previous cell to see how the results change. Find a good set of values for a given overpass and then try the procedure with a new overpass with different cloud conditions (this [S2 SR image browser app](https://showcase.earthengine.app/view/s2-sr-browser-s2cloudless-nb) is handy for quickly identifying images and determining image collection filter criteria). Try to identify a set of parameter values that balances cloud/cloud shadow commission and omission error for a range of cloud types. In the next section, we'll use the values to actually apply the mask to generate a cloud-free composite for 2020.
## Apply cloud and cloud shadow mask
In this section we'll generate a cloud-free composite for the same region as above that represents mean reflectance for July and August, 2020.
### Define collection filter and cloud mask parameters
We'll redefine the parameters to be a little more aggressive, i.e. decrease the cloud probability threshold, increase the cloud projection distance, and increase the buffer. These changes will increase cloud commission error (mask out some clear pixels), but since we will be compositing images from three months, there should be plenty of observations to complete the mosaic.
```
AOI = ee.Geometry.Point(-122.269, 45.701)
START_DATE = '2020-06-01'
END_DATE = '2020-09-01'
CLOUD_FILTER = 60
CLD_PRB_THRESH = 40
NIR_DRK_THRESH = 0.15
CLD_PRJ_DIST = 2
BUFFER = 100

```

### Build a Sentinel-2 collection
Reassemble the S2-cloudless collection since the collection filter parameters have changed.
```
s2_sr_cld_col = get_s2_sr_cld_col(AOI, START_DATE, END_DATE)

```

### Define cloud mask application function
Define a function to apply the cloud mask to each image in the collection.
```
defapply_cld_shdw_mask(img):
    # Subset the cloudmask band and invert it so clouds/shadow are 0, else 1.
    not_cld_shdw = img.select('cloudmask').Not()

    # Subset reflectance bands and update their masks, return the result.
    return img.select('B.*').updateMask(not_cld_shdw)

```

### Process the collection
Add cloud and cloud shadow component bands to each image and then apply the mask to each image. Reduce the collection by median (in your application, you might consider using medoid reduction to build a composite from actual data values, instead of per-band statistics).
```
s2_sr_median = (s2_sr_cld_col.map(add_cld_shdw_mask)
                             .map(apply_cld_shdw_mask)
                             .median())

```

### Display the cloud-free composite
Display the results. Be patient while the map renders, it may take a minute; [`ee.Image.reproject`](https://developers.google.com/earth-engine/guides/projections#reprojecting) is forcing computations to happen at 100 and 20 m scales (i.e. it is not relying on appropriate pyramid level [scales for analysis](https://developers.google.com/earth-engine/guides/scale#scale-of-analysis)). The issues with `ee.Image.reproject` being resource-intensive in this case are mostly confined to interactive map viewing. Batch image [exports](https://developers.google.com/earth-engine/guides/exporting) and table reduction exports where the `scale` parameter is set to typical Sentinel-2 scales (10-60 m) are less affected.
```
# Create a folium map object.
center = AOI.centroid(10).coordinates().reverse().getInfo()
m = folium.Map(location=center, zoom_start=12)

# Add layers to the folium map.
m.add_ee_layer(s2_sr_median,
                {'bands': ['B4', 'B3', 'B2'], 'min': 0, 'max': 2500, 'gamma': 1.1},
                'S2 cloud-free mosaic', True, 1, 9)

# Add a layer control panel to the map.
m.add_child(folium.LayerControl())

# Display the map.
display(m)

```

![png](https://developers.google.com/static/earth-engine/tutorials/community/sentinel-2-s2cloudless/index_files/output_hMObmv_tdLaX_0.png)
Hopefully you now have a good sense for Sentinel-2 cloud masking in the cloud 😉 with Earth Engine. 
