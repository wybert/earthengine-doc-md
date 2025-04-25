 
#  Glossary 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Anisotropic](https://developers.google.com/earth-engine/glossary#anisotropic)
  * [crs](https://developers.google.com/earth-engine/glossary#crs)
  * [crs_transform](https://developers.google.com/earth-engine/glossary#crs_transform)
  * [DEM](https://developers.google.com/earth-engine/glossary#dem)
  * [DN](https://developers.google.com/earth-engine/glossary#dn)
  * [DOY](https://developers.google.com/earth-engine/glossary#doy)
  * [FIRMS](https://developers.google.com/earth-engine/glossary#firms)
  * [google:registration_count](https://developers.google.com/earth-engine/glossary#google:registration_count)
  * [google:registration_offset_*](https://developers.google.com/earth-engine/glossary#google:registration_offset_)
  * [Isotropic](https://developers.google.com/earth-engine/glossary#isotropic)
  * [MODIS](https://developers.google.com/earth-engine/glossary#modis)
  * [NIR](https://developers.google.com/earth-engine/glossary#nir)
  * [NDVI](https://developers.google.com/earth-engine/glossary#ndvi)
  * [NDWI](https://developers.google.com/earth-engine/glossary#ndwi)
  * [SAD](https://developers.google.com/earth-engine/glossary#sad)
  * [SD](https://developers.google.com/earth-engine/glossary#sd)
  * [system:time_start](https://developers.google.com/earth-engine/glossary#system:time_start)
  * [system:time_end](https://developers.google.com/earth-engine/glossary#system:time_end)
  * [USGS](https://developers.google.com/earth-engine/glossary#usgs)
  * [WRI](https://developers.google.com/earth-engine/glossary#wri)




### Anisotropic

    Directionally dependent 


### `crs`

    Coordinate Reference System. A coordinate system, as defined by a relevant authority such as [EPSG](http://epsg.io/) or [SR-ORG](http://spatialreference.org/), specified as a string with the authority and the code separated by a colon, for example `'EPSG:4326'`. 


### `crs_transform`

    A post transform for a `crs`, defined as a list of affine transformation parameters in row-major order [xScale, xShearing, xTranslation, yShearing, yScale, yTranslation]. See [this reference](https://docs.oracle.com/javase/8/docs/api/java/awt/geom/AffineTransform.html) for more information. 


### DEM

    Digital Elevation Model 


### DN

    Digital Number 


### DOY

    Day Of Year 


### FIRMS

    [Fire Information for Resource Management System](https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms) 


### google:registration_count

    An image metadata property for the number of points found to be positionally consistent with a reference image known to be accurately registered. Numbers greater than 1000 indicate a good match. 


### google:registration_offset_*

    The measured offset, in meters, between the image and a reference image known to be accurately registered. 


### Isotropic

    Independent of direction 


### MODIS

    [MODerate resolution Imaging Spectro-radiometer](http://modis.gsfc.nasa.gov/) 


### NIR

    Near Infra-Red 


### NDVI

    Normalized Difference Vegetation Index. (NIR - red) / (NIR + red) 


### NDWI

    Normalized Difference Water Index. (green - NIR) / (green + NIR) 


### SAD

    [Sistema de Alerta de Desmatamento](http://imazon.org.br/imprensa/sistema-de-alerta-de-desmatamento-sad-operacional-na-plataforma-google-earth-engine/) 


### SD

    Standard Deviation 


### `system:time_start`

    The Earth Engine time stamp in milliseconds since the UNIX epoch. See [this link](https://en.wikipedia.org/wiki/Unix_time) for more information. The time stamp is set to the nominal image acquisition time for single scenes. It is set to the nominal composite start period for temporal composites. 


### `system:time_end`

    See system:time_start. The ending time stamp is set to the nominal image acquisition time for single scenes. It is set to midnight on the day after the nominal composite end period for MODIS temporal composites. 


### USGS

    [United States Geological Survey](http://www.usgs.gov/) 


### WRI

    [World Resources Institute](http://www.wri.org/)
