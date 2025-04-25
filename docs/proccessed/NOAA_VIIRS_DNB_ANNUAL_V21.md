 
#  VIIRS Nighttime Day/Night Annual Band Composites V2.1 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![NOAA/VIIRS/DNB/ANNUAL_V21](https://developers.google.com/earth-engine/datasets/images/NOAA/NOAA_VIIRS_DNB_ANNUAL_V21_sample.png) 

Dataset Availability
    2012-04-01T00:00:00Z–2021-01-01T00:00:00Z 

Dataset Provider
     [ Earth Observation Group, Payne Institute for Public Policy, Colorado School of Mines ](https://eogdata.mines.edu/products/vnl/#annual_v2) 

Earth Engine Snippet
     `    ee.ImageCollection("NOAA/VIIRS/DNB/ANNUAL_V21")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NOAA/NOAA_VIIRS_DNB_ANNUAL_V21) 

Cadence
    1 Year 

Tags
     [annual](https://developers.google.com/earth-engine/datasets/tags/annual) [dnb](https://developers.google.com/earth-engine/datasets/tags/dnb) [eog](https://developers.google.com/earth-engine/datasets/tags/eog) [lights](https://developers.google.com/earth-engine/datasets/tags/lights) [nighttime](https://developers.google.com/earth-engine/datasets/tags/nighttime) [noaa](https://developers.google.com/earth-engine/datasets/tags/noaa) [population](https://developers.google.com/earth-engine/datasets/tags/population) [viirs](https://developers.google.com/earth-engine/datasets/tags/viirs) [visible](https://developers.google.com/earth-engine/datasets/tags/visible)
[Description](https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_DNB_ANNUAL_V21#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_DNB_ANNUAL_V21#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_DNB_ANNUAL_V21#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_DNB_ANNUAL_V21#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_DNB_ANNUAL_V21#dois) More
Annual global VIIRS nighttime lights dataset is a time series produced from monthly cloud-free average radiance grids spanning 2013 to 2021. Data for 2022 are available in the [NOAA/VIIRS/DNB/ANNUAL_V22](https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_DNB_ANNUAL_V22) dataset.
An initial filtering step removed sunlit, moonlit and cloudy pixels, leading to rough composites that contains lights, fires, aurora and background. The rough annual composites are made on monthly increments and then combined to form rough annual composites.
The subsequent steps uses the twelve-month median radiance to discard high and low radiance outliers, filtering out most fires and isolating the background. Background areas are zeroed out using the data range (DR) calculated from 3x3 grid cells. The DR threshold for background is indexed to cloud-cover levels, with higher DR thresholds in areas having low numbers of cloud-free coverages.
**Note:** 2012 data are not yet included because of differences in processing. (A) 201204-201212, and (B) 201204-201303. Only set (B) has masked median and average bands which doesn't follow the pattern there in other year datasets.
**Pixel Size** 463.83 meters 
**Bands**
Name | Units | Description  
---|---|---  
`average` | nanoWatts/sr/cm^2 | Average DNB radiance values.  
`average_masked` | nanoWatts/sr/cm^2 | Average Masked DNB radiance values  
`cf_cvg` | Cloud-free coverages; the total number of observations that went into each pixel. This band can be used to identify areas with low numbers of observations where the quality is reduced.  
`cvg` | Total number of observations free of sunlight and moonlight.  
`maximum` | nanoWatts/sr/cm^2 | Maximum DNB radiance values.  
`median` | nanoWatts/sr/cm^2 | Median DNB radiance values  
`median_masked` | nanoWatts/sr/cm^2 | Median masked DNB radiance values.  
`minimum` | nanoWatts/sr/cm^2 | Minimum DNB radiance values  
**Terms of Use**
Colorado School of Mines data, information, and products, regardless of the method of delivery, are not subject to copyright and carry no restrictions on their subsequent use by the public. Once obtained, they may be put to any lawful use. The forgoing data is in the public domain and is being provided without restriction on use and distribution.
Citations:
  * Elvidge, C.D, Zhizhin, M., Ghosh T., Hsu FC, Taneja J. Annual time series of global VIIRS nighttime lights derived from monthly averages:2012 to 2019. Remote Sensing 2021, 13(5), p.922, doi:10.3390/rs13050922 [doi:10.3390/rs13050922](https://doi.org/10.3390/rs13050922)


  * [ https://doi.org/10.3390/rs13050922 ](https://doi.org/10.3390/rs13050922)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_DNB_ANNUAL_V21#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('NOAA/VIIRS/DNB/ANNUAL_V21')
.filter(ee.Filter.date('2020-01-01','2021-01-01'));
varnighttime=dataset.select('maximum');
varnighttimeVis={min:0.0,max:60.0};
Map.setCenter(-77.1056,38.8904,8);
Map.addLayer(nighttime,nighttimeVis,'Nighttime');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NOAA/NOAA_VIIRS_DNB_ANNUAL_V21)
[ VIIRS Nighttime Day/Night Annual Band Composites V2.1 ](https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_DNB_ANNUAL_V21)
Annual global VIIRS nighttime lights dataset is a time series produced from monthly cloud-free average radiance grids spanning 2013 to 2021. Data for 2022 are available in the NOAA/VIIRS/DNB/ANNUAL_V22 dataset. An initial filtering step removed sunlit, moonlit and cloudy pixels, leading to rough composites that contains lights, fires, aurora and …
NOAA/VIIRS/DNB/ANNUAL_V21, annual,dnb,eog,lights,nighttime,noaa,population,viirs,visible 
2012-04-01T00:00:00Z/2021-01-01T00:00:00Z
-65 -180 75 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.3390/rs13050922 ](https://doi.org/https://eogdata.mines.edu/products/vnl/#annual_v2)
  * [ https://doi.org/10.3390/rs13050922 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_DNB_ANNUAL_V21)


