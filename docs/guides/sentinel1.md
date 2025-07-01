 
#  Sentinel-1 Algorithms
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Metadata and Filtering](https://developers.google.com/earth-engine/guides/sentinel1#metadata-and-filtering)
  * [Sentinel-1 Preprocessing](https://developers.google.com/earth-engine/guides/sentinel1#sentinel-1-preprocessing)
  * [Dataset Notes](https://developers.google.com/earth-engine/guides/sentinel1#dataset-notes)


[Sentinel-1](https://earth.esa.int/web/sentinel/missions/sentinel-1) is a space mission funded by the European Union and carried out by the European Space Agency (ESA) within the Copernicus Programme. Sentinel-1 collects C-band synthetic aperture radar (SAR) imagery at a variety of polarizations and resolutions. Since radar data requires several specialized algorithms to obtain calibrated, orthorectified imagery, this document describes pre-processing of Sentinel-1 data in Earth Engine.
Sentinel-1 data is collected with several different instrument configurations, resolutions, band combinations during both ascending and descending orbits. Because of this heterogeneity, it's usually necessary to filter the data down to a homogeneous subset before starting processing. This process is outlined below in the [Metadata and Filtering](https://developers.google.com/earth-engine/guides/sentinel1#metadata-and-filtering) section.
## Metadata and Filtering
To create a homogeneous subset of Sentinel-1 data, it will usually be necessary to filter the collection using metadata properties. The common metadata fields used for filtering include these properties:
  1. `transmitterReceiverPolarisation`: ['VV'], ['HH'], ['VV', 'VH'], or ['HH', 'HV']
  2. `instrumentMode`: 'IW' (Interferometric Wide Swath), 'EW' (Extra Wide Swath) or 'SM' (Strip Map). See [this reference](https://sentinel.esa.int/web/sentinel/user-guides/sentinel-1-sar/acquisition-modes) for details.
  3. `orbitProperties_pass`: 'ASCENDING' or 'DESCENDING'
  4. `resolution_meters`: 10, 25 or 40
  5. `resolution`: 'M' (medium) or 'H' (high). See [this reference](https://sentinel.esa.int/web/sentinel/user-guides/sentinel-1-sar/resolutions/level-1-ground-range-detected) for details.


The following code filters the Sentinel-1 collection by `transmitterReceiverPolarisation`, `instrumentMode`, and `orbitProperties_pass` properties, then calculates composites for several observation combinations that are displayed in the map to demonstrate how these characteristics affect the data.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/sentinel1#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/sentinel1#colab-python-sample) More
```
// Load the Sentinel-1 ImageCollection, filter to Jun-Sep 2020 observations.
varsentinel1=ee.ImageCollection('COPERNICUS/S1_GRD')
.filterDate('2020-06-01','2020-10-01');
// Filter the Sentinel-1 collection by metadata properties.
varvvVhIw=sentinel1
// Filter to get images with VV and VH dual polarization.
.filter(ee.Filter.listContains('transmitterReceiverPolarisation','VV'))
.filter(ee.Filter.listContains('transmitterReceiverPolarisation','VH'))
// Filter to get images collected in interferometric wide swath mode.
.filter(ee.Filter.eq('instrumentMode','IW'));
// Separate ascending and descending orbit images into distinct collections.
varvvVhIwAsc=vvVhIw.filter(
ee.Filter.eq('orbitProperties_pass','ASCENDING'));
varvvVhIwDesc=vvVhIw.filter(
ee.Filter.eq('orbitProperties_pass','DESCENDING'));
// Calculate temporal means for various observations to use for visualization.
// Mean VH ascending.
varvhIwAscMean=vvVhIwAsc.select('VH').mean();
// Mean VH descending.
varvhIwDescMean=vvVhIwDesc.select('VH').mean();
// Mean VV for combined ascending and descending image collections.
varvvIwAscDescMean=vvVhIwAsc.merge(vvVhIwDesc).select('VV').mean();
// Mean VH for combined ascending and descending image collections.
varvhIwAscDescMean=vvVhIwAsc.merge(vvVhIwDesc).select('VH').mean();
// Display the temporal means for various observations, compare them.
Map.addLayer(vvIwAscDescMean,{min:-12,max:-4},'vvIwAscDescMean');
Map.addLayer(vhIwAscDescMean,{min:-18,max:-10},'vhIwAscDescMean');
Map.addLayer(vhIwAscMean,{min:-18,max:-10},'vhIwAscMean');
Map.addLayer(vhIwDescMean,{min:-18,max:-10},'vhIwDescMean');
Map.setCenter(-73.8719,4.512,9);// Bogota, Colombia
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Load the Sentinel-1 ImageCollection, filter to Jun-Sep 2020 observations.
sentinel_1 = ee.ImageCollection('COPERNICUS/S1_GRD').filterDate(
  '2020-06-01', '2020-10-01'
)
# Filter the Sentinel-1 collection by metadata properties.
vv_vh_iw = (
  sentinel_1.filter(
    # Filter to get images with VV and VH dual polarization.
    ee.Filter.listContains('transmitterReceiverPolarisation', 'VV')
  )
  .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VH'))
  .filter(
    # Filter to get images collected in interferometric wide swath mode.
    ee.Filter.eq('instrumentMode', 'IW')
  )
)
# Separate ascending and descending orbit images into distinct collections.
vv_vh_iw_asc = vv_vh_iw.filter(
  ee.Filter.eq('orbitProperties_pass', 'ASCENDING')
)
vv_vh_iw_desc = vv_vh_iw.filter(
  ee.Filter.eq('orbitProperties_pass', 'DESCENDING')
)
# Calculate temporal means for various observations to use for visualization.
# Mean VH ascending.
vh_iw_asc_mean = vv_vh_iw_asc.select('VH').mean()
# Mean VH descending.
vh_iw_desc_mean = vv_vh_iw_desc.select('VH').mean()
# Mean VV for combined ascending and descending image collections.
vv_iw_asc_desc_mean = vv_vh_iw_asc.merge(vv_vh_iw_desc).select('VV').mean()
# Mean VH for combined ascending and descending image collections.
vh_iw_asc_desc_mean = vv_vh_iw_asc.merge(vv_vh_iw_desc).select('VH').mean()
# Display the temporal means for various observations, compare them.
m = geemap.Map()
m.add_layer(vv_iw_asc_desc_mean, {'min': -12, 'max': -4}, 'vv_iw_asc_desc_mean')
m.add_layer(
  vh_iw_asc_desc_mean, {'min': -18, 'max': -10}, 'vh_iw_asc_desc_mean'
)
m.add_layer(vh_iw_asc_mean, {'min': -18, 'max': -10}, 'vh_iw_asc_mean')
m.add_layer(vh_iw_desc_mean, {'min': -18, 'max': -10}, 'vh_iw_desc_mean')
m.set_center(-73.8719, 4.512, 9) # Bogota, Colombia
m
```

## Sentinel-1 Preprocessing
Imagery in the Earth Engine `'COPERNICUS/S1_GRD'` Sentinel-1 `ImageCollection` is consists of Level-1 Ground Range Detected (GRD) scenes processed to backscatter coefficient (σ°) in decibels (dB). The backscatter coefficient represents target backscattering area (radar cross-section) per unit ground area. Because it can vary by several orders of magnitude, it is converted to dB as 10*log10σ°. It measures whether the radiated terrain scatters the incident microwave radiation preferentially away from the SAR sensor dB < 0) or towards the SAR sensor dB > 0). This scattering behavior depends on the physical characteristics of the terrain, primarily the geometry of the terrain elements and their electromagnetic characteristics.
Earth Engine uses the following preprocessing steps (as implemented by the [Sentinel-1 Toolbox](https://sentinel.esa.int/web/sentinel/toolboxes/sentinel-1)) to derive the backscatter coefficient in each pixel:
  1. **Apply orbit file**
     * Updates orbit metadata with a restituted [orbit file](https://sentinel.esa.int/web/sentinel/technical-guides/sentinel-1-sar/pod/products-requirements) (or a precise orbit file if the restituted one is not available).
  2. **GRD border noise removal**
     * Removes low intensity noise and invalid data on scene edges. (As of January 12, 2018)
  3. **Thermal noise removal**
     * Removes additive noise in sub-swaths to help reduce discontinuities between sub-swaths for scenes in multi-swath acquisition modes. (This operation cannot be applied to images produced before July 2015)
  4. **Application of radiometric calibration values**
     * Computes backscatter intensity using sensor calibration parameters in the GRD metadata.
  5. **Terrain correction** (orthorectification) 
     * Converts data from ground range geometry, which does not take terrain into account, to σ° using the [SRTM 30 meter DEM](https://developers.google.com/earth-engine/datasets/catalog/USGS_SRTMGL1_003) or the [ASTER DEM](https://asterweb.jpl.nasa.gov/gdem.asp) for high latitudes (greater than 60° or less than -60°).


## Dataset Notes
  * Radiometric Terrain Flattening is not being applied due to artifacts on mountain slopes.
  * The unitless backscatter coefficient is converted to dB as described above.
  * Sentinel-1 SLC data cannot currently be ingested, as Earth Engine does not support images with complex values due to inability to average them during pyramiding without losing phase information.
  * GRD SM assets are not ingested because the `computeNoiseScalingFactor()` function in the [border noise removal operation in the S1 toolbox](https://github.com/senbox-org/s1tbx/blob/master/s1tbx-op-calibration/src/main/java/org/esa/s1tbx/calibration/gpf/RemoveGRDBorderNoiseOp.java) does not support the SM mode.


Was this helpful?
