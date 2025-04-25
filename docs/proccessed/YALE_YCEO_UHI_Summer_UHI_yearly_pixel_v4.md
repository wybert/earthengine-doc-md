 
#  YCEO Surface Urban Heat Islands: Pixel-Level Composites of Yearly Summertime Daytime and Nighttime Intensity 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![YALE/YCEO/UHI/Summer_UHI_yearly_pixel/v4](https://developers.google.com/earth-engine/datasets/images/YALE/YALE_YCEO_UHI_Summer_UHI_yearly_pixel_v4_sample.png) 

Dataset Availability
    2003-01-01T00:00:00Z–2018-12-31T00:00:00Z 

Dataset Provider
     [ Yale Center for Earth Observation (YCEO) ](https://yceo.yale.edu/research/global-surface-uhi-explorer) 

Earth Engine Snippet
     `    ee.ImageCollection("YALE/YCEO/UHI/Summer_UHI_yearly_pixel/v4")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/YALE/YALE_YCEO_UHI_Summer_UHI_yearly_pixel_v4) 

Tags
     [climate](https://developers.google.com/earth-engine/datasets/tags/climate) [uhi](https://developers.google.com/earth-engine/datasets/tags/uhi) [urban](https://developers.google.com/earth-engine/datasets/tags/urban) [yale](https://developers.google.com/earth-engine/datasets/tags/yale)
[Description](https://developers.google.com/earth-engine/datasets/catalog/YALE_YCEO_UHI_Summer_UHI_yearly_pixel_v4#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/YALE_YCEO_UHI_Summer_UHI_yearly_pixel_v4#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/YALE_YCEO_UHI_Summer_UHI_yearly_pixel_v4#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/YALE_YCEO_UHI_Summer_UHI_yearly_pixel_v4#citations) More
This dataset contains annual, summertime, and wintertime surface urban heat island (SUHI) intensities for day and night for over 10,000 urban clusters throughout the world. The dataset was created using the MODIS 8-day TERRA and AQUA land surface temperature (LST) products, the Landscan urban extent database, the Global Multi-resolution Terrain Elevation Data 2010, and the European Space Agency (ESA) Climate Change Initiative (CCI) land cover data using the Simplified Urban-Extent Algorithm. The product is available both at the pixel level (at 300 m resolution after downscaling) and as urban cluster means from 2003 to 2018. The monthly composites are only available as urban cluster means.
A summary of older versions, including changes from the dataset created and analyzed in the originally published manuscript can be found on the [Yale Center for Earth Observation website](https://yceo.yale.edu/research/global-surface-uhi-explorer). The dataset can also be explored using the [Global Surface UHI Explorer web application](https://yceo.users.earthengine.app/view/uhimap).
The dataset is split into the following six components:
  1. **UHI_all_averaged:** Image containing cluster-mean composite daytime and nighttime SUHI intensity for annual, summer, and winter.
  2. **UHI_monthly_averaged:** Image containing cluster-mean monthly composites of daytime and nighttime SUHI intensity.
  3. **UHI_yearly_averaged:** Image collection of cluster-mean yearly composites of daytime and nighttime SUHI intensity from 2003. to 2018.
  4. **UHI_yearly_pixel:** Image collection of spatially disaggregated (nominal scale of 300 m) annual daytime and nighttime SUHI intensity from 2003 to 2018.
  5. **Summer_UHI_yearly_pixel:** Image collection of spatially disaggregated (nominal scale of 300 m) summertime daytime and nighttime SUHI intensity from 2003 to 2018.
  6. **Winter_UHI_yearly_pixel:** Image collection of spatially disaggregated (nominal scale of 300 m) wintertime daytime and nighttime SUHI intensity from 2003 to 2018.


This asset is the fifth component.
**Pixel Size** 300 meters 
**Bands**
Name | Units | Description  
---|---|---  
`Daytime` | °C | Daytime UHI  
`Nighttime` | °C | Nighttime UHI  
**Terms of Use**
[CC-BY-4.0](https://spdx.org/licenses/CC-BY-4.0.html)
Citations:
  * Chakraborty, T., & Lee, X. (2019). A simplified urban-extent algorithm to characterize surface urban heat islands on a global scale and examine vegetation control on their spatiotemporal variability. International Journal of Applied Earth Observation and Geoinformation, 74, 269-280. [doi:10.1016/j.jag.2018.09.015](https://doi.org/10.1016/j.jag.2018.09.015)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/YALE_YCEO_UHI_Summer_UHI_yearly_pixel_v4#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('YALE/YCEO/UHI/Summer_UHI_yearly_pixel/v4');
varvisualization={
bands:['Daytime'],
min:-1.5,
max:7.5,
palette:[
'313695','74add1','fed976','feb24c','fd8d3c','fc4e2a','e31a1c',
'b10026']
};
Map.setCenter(-74.7,40.6,7);
Map.addLayer(dataset,visualization,'Daytime UHI');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/YALE/YALE_YCEO_UHI_Summer_UHI_yearly_pixel_v4)
[ YCEO Surface Urban Heat Islands: Pixel-Level Composites of Yearly Summertime Daytime and Nighttime Intensity ](https://developers.google.com/earth-engine/datasets/catalog/YALE_YCEO_UHI_Summer_UHI_yearly_pixel_v4)
This dataset contains annual, summertime, and wintertime surface urban heat island (SUHI) intensities for day and night for over 10,000 urban clusters throughout the world. The dataset was created using the MODIS 8-day TERRA and AQUA land surface temperature (LST) products, the Landscan urban extent database, the Global Multi-resolution Terrain …
YALE/YCEO/UHI/Summer_UHI_yearly_pixel/v4, climate,uhi,urban,yale 
2003-01-01T00:00:00Z/2018-12-31T00:00:00Z
-49.98 -180 69.7 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://yceo.yale.edu/research/global-surface-uhi-explorer)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/YALE_YCEO_UHI_Summer_UHI_yearly_pixel_v4)


