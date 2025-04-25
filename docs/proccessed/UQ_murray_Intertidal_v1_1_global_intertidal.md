 
#  Murray Global Intertidal Change Classification 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![UQ/murray/Intertidal/v1_1/global_intertidal](https://developers.google.com/earth-engine/datasets/images/UQ/UQ_murray_Intertidal_v1_1_global_intertidal_sample.png) 

Dataset Availability
    1984-01-01T00:00:00Z–2017-01-01T00:00:00Z 

Dataset Provider
     [ Murray/UQ/Google/USGS/NASA ](https://intertidal.app) 

Earth Engine Snippet
     `    ee.ImageCollection("UQ/murray/Intertidal/v1_1/global_intertidal")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/UQ/UQ_murray_Intertidal_v1_1_global_intertidal) 

Cadence
    3 Years 

Tags
     [coastal](https://developers.google.com/earth-engine/datasets/tags/coastal) [google](https://developers.google.com/earth-engine/datasets/tags/google) [intertidal](https://developers.google.com/earth-engine/datasets/tags/intertidal) [landsat-derived](https://developers.google.com/earth-engine/datasets/tags/landsat-derived) [murray](https://developers.google.com/earth-engine/datasets/tags/murray) [surface-ground-water](https://developers.google.com/earth-engine/datasets/tags/surface-ground-water) [tidal-flats](https://developers.google.com/earth-engine/datasets/tags/tidal-flats) [uq](https://developers.google.com/earth-engine/datasets/tags/uq)
[Description](https://developers.google.com/earth-engine/datasets/catalog/UQ_murray_Intertidal_v1_1_global_intertidal#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/UQ_murray_Intertidal_v1_1_global_intertidal#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/UQ_murray_Intertidal_v1_1_global_intertidal#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/UQ_murray_Intertidal_v1_1_global_intertidal#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/UQ_murray_Intertidal_v1_1_global_intertidal#dois) More
The Murray Global Intertidal Change Dataset contains global maps of tidal flat ecosystems produced via a supervised classification of 707,528 Landsat Archive images. Each pixel was classified into tidal flat, permanent water or other with reference to a globally distributed set of training data.
The classification was implemented along the entire global coastline between 60° North and 60° South from 1 January 1984 to 31 December 2016. The image collection consists consists of a time-series of 11 global maps of tidal flats at 30m pixel resolution for set time-periods (1984-1986; 1987-1989; 1990-1992; 1993-1995; 1996-1998; 1999-2001; 2002-2004; 2005-2007; 2008-2010; 2011-2013; 2014-2016)
This product depicts tidal flat ecosystems around the global coastline.
Pixels classified as tidal flat in the analysis represent several types of tidal flat ecosystems, including unconsolidated fine-grain sediments (tidal mudflats), unconsolidated coarse-grain sediments (tidal sand flats), and consolidated sediments, organic material or rocks (wide tidal rock-platforms), while excluding spectral signatures indicating the presence of vegetation dominated intertidal ecosystems such as mangroves and vegetated marshes. The analysis aimed to identify pixels that are subject to regular tidal inundation, and therefore may also include other intertidal systems where intertidal dynamics are observable.
**Pixel Size** 30 meters 
**Bands**
Name | Units | Description  
---|---|---  
`classification` | occurrence | Intertertidal area classification for the interval.  
Bitmask for classification
  * Bit 0: Intertidal area classification. 
    * 0: Classified non-intertidal area
    * 1: Classified intertidal area

  
**Terms of Use**
This work is licensed under a Creative Commons Attribution 4.0 International License.
Any use of the intertidal data must include proper acknowledgement, including citing the associated journal article.
Citations:
  * Murray, N.J., Phinn, S.R., DeWitt, M., Ferrari, R., Johnston, R., Lyons, M.B., Clinton, N., Thau, D. & Fuller, R.A. (2019) The global distribution and trajectory of tidal flats. Nature, 565, 222-225. [doi:10.1038/s41586-018-0805-8](https://doi.org/10.1038/s41586-018-0805-8),
  * Murray, N. J., Phinn, S. P., Fuller, R. A., DeWitt, M., Ferrari, R., Johnston, R., Clinton, N., & Lyons, M. B. (2022). High-resolution global maps of tidal flat ecosystems from 1984 to 2019. Scientific Data, 9(1). [doi:10.1038/s41597-022-01635-5](https://doi.org/10.1038/s41597-022-01635-5),


  * [ https://doi.org/10.1038/s41586-018-0805-8 ](https://doi.org/10.1038/s41586-018-0805-8)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/UQ_murray_Intertidal_v1_1_global_intertidal#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('UQ/murray/Intertidal/v1_1/global_intertidal');
varvisualization={
bands:['classification'],
min:0,
max:1,
palette:['0000ff']
};
Map.setCenter(126.6339,37.4394,10);
Map.addLayer(dataset,visualization,'Intertidal areas');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/UQ/UQ_murray_Intertidal_v1_1_global_intertidal)
[ Murray Global Intertidal Change Classification ](https://developers.google.com/earth-engine/datasets/catalog/UQ_murray_Intertidal_v1_1_global_intertidal)
The Murray Global Intertidal Change Dataset contains global maps of tidal flat ecosystems produced via a supervised classification of 707,528 Landsat Archive images. Each pixel was classified into tidal flat, permanent water or other with reference to a globally distributed set of training data. The classification was implemented along the …
UQ/murray/Intertidal/v1_1/global_intertidal, coastal,google,intertidal,landsat-derived,murray,surface-ground-water,tidal-flats,uq 
1984-01-01T00:00:00Z/2017-01-01T00:00:00Z
-60 -180 60 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.1038/s41586-018-0805-8 ](https://doi.org/https://intertidal.app)
  * [ https://doi.org/10.1038/s41586-018-0805-8 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/UQ_murray_Intertidal_v1_1_global_intertidal)


