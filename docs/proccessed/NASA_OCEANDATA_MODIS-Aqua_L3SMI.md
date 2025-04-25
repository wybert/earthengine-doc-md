 
#  Ocean Color SMI: Standard Mapped Image MODIS Aqua Data 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![NASA/OCEANDATA/MODIS-Aqua/L3SMI](https://developers.google.com/earth-engine/datasets/images/NASA/NASA_OCEANDATA_MODIS-Aqua_L3SMI_sample.png) 

Dataset Availability
    2002-07-03T23:40:05Z–2022-02-28T00:20:00Z 

Dataset Provider
     [ NASA OB.DAAC at NASA Goddard Space Flight Center ](https://oceancolor.gsfc.nasa.gov/) 

Earth Engine Snippet
     `    ee.ImageCollection("NASA/OCEANDATA/MODIS-Aqua/L3SMI")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NASA/NASA_OCEANDATA_MODIS-Aqua_L3SMI) 

Cadence
    1 Day 

Tags
     [biology](https://developers.google.com/earth-engine/datasets/tags/biology) [chlorophyll](https://developers.google.com/earth-engine/datasets/tags/chlorophyll) [modis](https://developers.google.com/earth-engine/datasets/tags/modis) [nasa](https://developers.google.com/earth-engine/datasets/tags/nasa) [ocean](https://developers.google.com/earth-engine/datasets/tags/ocean) [oceandata](https://developers.google.com/earth-engine/datasets/tags/oceandata) [oceans](https://developers.google.com/earth-engine/datasets/tags/oceans) [reflectance](https://developers.google.com/earth-engine/datasets/tags/reflectance) [sst](https://developers.google.com/earth-engine/datasets/tags/sst) [temperature](https://developers.google.com/earth-engine/datasets/tags/temperature) [weather](https://developers.google.com/earth-engine/datasets/tags/weather)
[Description](https://developers.google.com/earth-engine/datasets/catalog/NASA_OCEANDATA_MODIS-Aqua_L3SMI#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/NASA_OCEANDATA_MODIS-Aqua_L3SMI#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/NASA_OCEANDATA_MODIS-Aqua_L3SMI#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/NASA_OCEANDATA_MODIS-Aqua_L3SMI#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/NASA_OCEANDATA_MODIS-Aqua_L3SMI#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/NASA_OCEANDATA_MODIS-Aqua_L3SMI#dois) More
This level 3 product includes ocean color and satellite ocean biology data produced or collected under [EOSDIS](https://earthdata.nasa.gov/about).
This dataset may be used for studying the biology and hydrology of coastal zones, changes in the diversity and geographical distribution of coastal marine habitats, biogeochemical fluxes and their influence in Earth's oceans and climate over time, and finally the impact of climate and environmental variability and change on ocean ecosystems and the biodiversity they support.
Scale factor and offset are already applied.
Documentation:
  * [Ocean Color Forum](https://oceancolor.gsfc.nasa.gov/forum/oceancolor/forum_show.pl)
  * [Chlorophyll Forum](https://oceancolor.gsfc.nasa.gov/forum/oceancolor/forum_show.pl)
  * [Algorithm Theoretical Basis Document (Chlorophyll)](https://oceancolor.gsfc.nasa.gov/resources/atbd/chlor_a)
  * [Algorithm Theoretical Basis Document (Fluorescence Line Height)](https://oceancolor.gsfc.nasa.gov/resources/atbd/nflh)
  * [Algorithm Theoretical Basis Document (Particulate Organic Carbon)](https://oceancolor.gsfc.nasa.gov/resources/atbd/poc)
  * [Algorithm Theoretical Basis Document (Remote-Sensing Reflectance)](https://oceancolor.gsfc.nasa.gov/resources/atbd/rrs)
  * [Processing History](https://oceancolor.gsfc.nasa.gov/reprocessing)


Newer datasets have scaled POC values while older ones don't. This scaling gets rid of negative values but older datasets still retain them hence the -2147.48 estimated minimum value. For more information, visit the [Ocean Color Forum](https://oceancolor.gsfc.nasa.gov/forum/oceancolor/forum_show.pl).
[MODIS-Aqua OceanData](https://oceancolor.gsfc.nasa.gov/about/missions/aqua/)
**Pixel Size** 4616 meters 
**Bands**
Name | Units | Min | Max | Wavelength | Description  
---|---|---|---|---|---  
`chlor_a` | mg/m^3 |  0*  |  99.99*  | Chlorophyll a concentration  
`nflh` | mW cm-2 μm-1 sr-1 |  -0.5*  |  5.03*  | Normalized fluorescence line height  
`poc` | mg/m^3 |  -2147.48*  |  12953.4*  | Particulate organic carbon  
`Rrs_412` | sr-1 |  0*  |  0.11*  | 412nm | Remote sensing reflectance at band 412nm  
`Rrs_443` | sr-1 |  0*  |  0.08*  | 443nm | Remote sensing reflectance at band 443nm  
`Rrs_469` | sr-1 |  0*  |  0.08*  | 469nm | Remote sensing reflectance at band 469nm  
`Rrs_488` | sr-1 |  0*  |  0.08*  | 488nm | Remote sensing reflectance at band 488nm  
`Rrs_531` | sr-1 |  0*  |  0.07*  | 531nm | Remote sensing reflectance at band 531nm  
`Rrs_547` | sr-1 |  0*  |  0.07*  | 547nm | Remote sensing reflectance at band 547nm  
`Rrs_555` | sr-1 |  0*  |  0.07*  | 555nm | Remote sensing reflectance at band 555nm  
`Rrs_645` | sr-1 |  0*  |  0.05*  | 645nm | Remote sensing reflectance at band 645nm  
`Rrs_667` | sr-1 |  0*  |  0.04*  | 667nm | Remote sensing reflectance at band 667nm  
`Rrs_678` | sr-1 |  0*  |  0.04*  | 678nm | Remote sensing reflectance at band 678nm  
`sst` | °C |  -2*  |  40*  | Sea surface temperature  
* estimated min or max value 
**Image Properties**
Name | Type | Description  
---|---|---  
Rrs_412_lastModified | STRING | Last date this product was modified  
Rrs_412_software_name | STRING | 'smigen' or 'l3mapgen'; name of the software used to create this product  
Rrs_412_software_version | STRING | Version of the software used to create this product  
Rrs_443_lastModified | STRING | Last date this product was modified  
Rrs_443_software_name | STRING | 'smigen' or 'l3mapgen'; name of the software used to create this product  
Rrs_443_software_version | STRING | Version of the software used to create this product  
Rrs_555_lastModified | STRING | Last date this product was modified  
Rrs_555_software_name | STRING | 'smigen' or 'l3mapgen'; name of the software used to create this product  
Rrs_555_software_version | STRING | Version of the software used to create this product  
chlor_a_lastModified | STRING | Last date this product was modified  
chlor_a_software_name | STRING | 'smigen' or 'l3mapgen'; name of the software used to create this product  
chlor_a_software_version | STRING | Version of the software used to create this product  
poc_lastModified | STRING | Last date this product was modified  
poc_software_name | STRING | 'smigen' or 'l3mapgen'; name of the software used to create this product  
poc_software_version | STRING | Version of the software used to create this product  
Rrs_469_lastModified | STRING | Last date this product was modified  
Rrs_469_software_name | STRING | 'smigen' or 'l3mapgen'; name of the software used to create this product  
Rrs_469_software_version | STRING | Version of the software used to create this product  
Rrs_488_lastModified | STRING | Last date this product was modified  
Rrs_488_software_name | STRING | 'smigen' or 'l3mapgen'; name of the software used to create this product  
Rrs_488_software_version | STRING | Version of the software used to create this product  
Rrs_531_lastModified | STRING | Last date this product was modified  
Rrs_531_software_name | STRING | 'smigen' or 'l3mapgen'; name of the software used to create this product  
Rrs_531_software_version | STRING | Version of the software used to create this product  
Rrs_547_lastModified | STRING | Last date this product was modified  
Rrs_547_software_name | STRING | 'smigen' or 'l3mapgen'; name of the software used to create this product  
Rrs_547_software_version | STRING | Version of the software used to create this product  
Rrs_645_lastModified | STRING | Last date this product was modified  
Rrs_645_software_name | STRING | 'smigen' or 'l3mapgen'; name of the software used to create this product  
Rrs_645_software_version | STRING | Version of the software used to create this product  
Rrs_667_lastModified | STRING | Last date this product was modified  
Rrs_667_software_name | STRING | 'smigen' or 'l3mapgen'; name of the software used to create this product  
Rrs_667_software_version | STRING | Version of the software used to create this product  
Rrs_678_lastModified | STRING | Last date this product was modified  
Rrs_678_software_name | STRING | 'smigen' or 'l3mapgen'; name of the software used to create this product  
Rrs_678_software_version | STRING | Version of the software used to create this product  
nflh_lastModified | STRING | Last date this product was modified  
nflh_software_name | STRING | 'smigen' or 'l3mapgen'; name of the software used to create this product  
nflh_software_version | STRING | Version of the software used to create this product  
sst_lastModified | STRING | Last date this product was modified  
sst_software_name | STRING | 'smigen' or 'l3mapgen'; name of the software used to create this product  
sst_software_version | STRING | Version of the software used to create this product  
**Terms of Use**
This dataset is in the public domain and is available without restriction on use and distribution. See [NASA's Earth Science Data & Information Policy](https://www.earthdata.nasa.gov/engage/open-data-services-and-software/data-and-information-policy) for additional information.
Citations:
  * NASA Goddard Space Flight Center, Ocean Ecology Laboratory, Ocean Biology Processing Group. Moderate-resolution Imaging Spectroradiometer (MODIS) Aqua Ocean Color Data, NASA OB.DAAC, Greenbelt, MD, USA.
    * DOI: 10.5067/AQUA/MODIS/L3M/CHL/2018 [unrecoverable]
  * NASA Ocean Biology Processing Group. (2017). _MODIS-Aqua Level 3 Mapped Fluorescent Line Height Data Version R2018.0_ [Data set]. NASA Ocean Biology DAAC.
    * DOI: 10.5067/AQUA/MODIS/L3M/FLH/2018 [unrecoverable]
  * NASA Ocean Biology Processing Group. (2017). _MODIS-Aqua Level 3 Mapped Particulate Organic Carbon Data Version R2018.0_ [Data set]. NASA Ocean Biology DAAC.
    * DOI: 10.5067/AQUA/MODIS/L3M/POC/2018 [unrecoverable]
  * NASA Ocean Biology Processing Group. (2017). _MODIS-Aqua Level 3 Mapped Remote-Sensing Reflectance Data Version R2018.0_ [Data set]. NASA Ocean Biology DAAC.
    * DOI: 10.5067/AQUA/MODIS/L3M/RRS/2018 [unrecoverable]
  * NASA/JPL. (2020). _GHRSST Level 2P Global Sea Surface Skin Temperature from the Moderate Resolution Imaging Spectroradiometer (MODIS) on the NASA Aqua satellite (GDS2)_ [Data set]. NASA Physical Oceanography DAAC.


  * [ https://doi.org/10.5067/GHMDA-2PJ19 ](https://doi.org/10.5067/GHMDA-2PJ19)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/NASA_OCEANDATA_MODIS-Aqua_L3SMI#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('NASA/OCEANDATA/MODIS-Aqua/L3SMI')
.filterDate('2016-01-01','2016-01-31');
varremoteSensingReflectance=
dataset.select(['Rrs_645','Rrs_555','Rrs_443']);
varremoteSensingReflectanceVis={
min:0.0,
max:0.011,
};
Map.setCenter(-52.12,-46.13,4);
Map.addLayer(
remoteSensingReflectance,remoteSensingReflectanceVis,
'Remote Sensing Reflectance');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NASA/NASA_OCEANDATA_MODIS-Aqua_L3SMI)
[ Ocean Color SMI: Standard Mapped Image MODIS Aqua Data ](https://developers.google.com/earth-engine/datasets/catalog/NASA_OCEANDATA_MODIS-Aqua_L3SMI)
This level 3 product includes ocean color and satellite ocean biology data produced or collected under EOSDIS. This dataset may be used for studying the biology and hydrology of coastal zones, changes in the diversity and geographical distribution of coastal marine habitats, biogeochemical fluxes and their influence in Earth's oceans …
NASA/OCEANDATA/MODIS-Aqua/L3SMI, biology,chlorophyll,modis,nasa,ocean,oceandata,oceans,reflectance,sst,temperature,weather 
2002-07-03T23:40:05Z/2022-02-28T00:20:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.5067/GHMDA-2PJ19 ](https://doi.org/https://oceancolor.gsfc.nasa.gov/)
  * [ https://doi.org/10.5067/GHMDA-2PJ19 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/NASA_OCEANDATA_MODIS-Aqua_L3SMI)


