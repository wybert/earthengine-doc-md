 
#  GEDI L2B Vector Canopy Cover Vertical Profile Metrics (Version 2) 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![LARSE/GEDI/GEDI02_B_002](https://developers.google.com/earth-engine/datasets/images/LARSE/LARSE_GEDI_GEDI02_B_002_sample.png) 

Dataset Availability
    2019-03-25T00:00:00Z–2023-01-01T00:00:00Z 

Dataset Provider
     [ USFS Laboratory for Applications of Remote Sensing in Ecology (LARSE) ](https://www.fs.usda.gov/) [ NASA GEDI mission, accessed through the USGS LP DAAC ](https://lpdaac.usgs.gov/products/gedi02_av002/) 

Tags
     [elevation](https://developers.google.com/earth-engine/datasets/tags/elevation) [forest-biomass](https://developers.google.com/earth-engine/datasets/tags/forest-biomass) [gedi](https://developers.google.com/earth-engine/datasets/tags/gedi) [larse](https://developers.google.com/earth-engine/datasets/tags/larse) [nasa](https://developers.google.com/earth-engine/datasets/tags/nasa) [tree-cover](https://developers.google.com/earth-engine/datasets/tags/tree-cover) [usgs](https://developers.google.com/earth-engine/datasets/tags/usgs)
[Description](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI02_B_002#description)[Table Schema](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI02_B_002#table-schema)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI02_B_002#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI02_B_002#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI02_B_002#dois) More
GEDI Level 2B Canopy Cover and Vertical Profile Metrics product (GEDI02_B) extracts biophysical metrics from each GEDI waveform. These metrics are based on the directional gap probability profile derived from the L1B waveform.
The vertical step between foliage profile measurements (known as dZ in GEDI documentation) is always 5 meters. The original GEDI02_B product is a table of points with a spatial resolution (average footprint) of 25 meters.
Please see [User Guide](https://lpdaac.usgs.gov/documents/986/GEDI02_UserGuide_V2.pdf) for more information.
The Global Ecosystem Dynamics Investigation [GEDI](https://gedi.umd.edu/) mission aims to characterize ecosystem structure and dynamics to enable radically improved quantification and understanding of the Earth's carbon cycle and biodiversity. The GEDI instrument, attached to the International Space Station (ISS), collects data globally between 51.6° N and 51.6° S latitudes at the highest resolution and densest sampling of the 3-dimensional structure of the Earth. The GEDI instrument consists of three lasers producing a total of eight beam ground transects, which instantaneously sample eight ~25 m footprints spaced approximately every 60 m along-track.
Product | Description  
---|---  
L2A Vector | [LARSE/GEDI/GEDI02_A_002](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI02_A_002)  
L2A Monthly raster | [LARSE/GEDI/GEDI02_A_002_MONTHLY](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI02_A_002_MONTHLY)  
L2A table index | [LARSE/GEDI/GEDI02_A_002_INDEX](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI02_A_002_INDEX)  
L2B Vector | [LARSE/GEDI/GEDI02_B_002](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI02_B_002)  
L2B Monthly raster | [LARSE/GEDI/GEDI02_B_002_MONTHLY](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI02_B_002_MONTHLY)  
L2B table index | [LARSE/GEDI/GEDI02_B_002_INDEX](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI02_B_002_INDEX)  
L4A Biomass Vector | [LARSE/GEDI/GEDI04_A_002](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI04_A_002)  
L4A Monthly raster | [LARSE/GEDI/GEDI04_A_002_MONTHLY](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI04_A_002_MONTHLY)  
L4A table index | [LARSE/GEDI/GEDI04_A_002_INDEX](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI04_A_002_INDEX)  
L4B Biomass | [LARSE/GEDI/GEDI04_B_002](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI04_B_002)  
**Table Schema**
Name | Type | Description  
---|---|---  
algorithmrun_flag | INT | The L2B algorithm is run if this flag is set to 1 indicating data have sufficient waveform fidelity for L2B to run.  
beam | INT | Beam number  
cover | INT | Total canopy cover  
degrade_flag | INT | Flag indicating degraded state of pointing and/or positioning information.
  * 3X - ADF CHU solution unavailable (ST-2)
  * 4X - Platform attitude
  * 5X - Poor solution (filter covariance large)
  * 6X - Data outage (platform attitude gap also)
  * 7X - ST 1+2 unavailable (similar boresight FOV)
  * 8X - ST 1+2+3 unavailable
  * 9X - ST 1+2+3 and ISS unavailable
  * X1 - Maneuver
  * X2 - GPS data gap
  * X3 - ST blinding
  * X4 - Other
  * X5 - GPS receiver clock drift
  * X6 - Maneuver & GPS receiver clock drift
  * X7 - GPS data gap & GPS receiver clock drift
  * X8 - ST blinding & GPS receiver clock drift
  * X9 - Other & GPS receiver clock drift

  
delta_time | DOUBLE | Transmit time of the shot, measured in seconds from the master_time_epoch since 2018-01-01  
fhd_normal | INT | Foliage Height Diversity  
l2b_quality_flag | INT | L2B quality flag  
local_beam_azimuth | INT | Azimuth of the unit pointing vector for the laser in the local ENU frame measured from North and positive towards East.  
local_beam_elevation | INT | Elevation of the unit pointing vector for the laser in the local ENU frame measured from East-North plane and positive towards Up.  
pai | INT | Total Plant Area Index  
pgap_theta | INT | Total Gap Probability (theta)  
selected_l2a_algorithm | INT | Selected L2A algorithm setting  
selected_rg_algorithm | INT | Selected R (ground) algorithm  
sensitivity | INT | Maxmimum canopy cover that can be penetrated. Valid range is [0, 1]. Values outside of this range may be present but must be ignored. They represent noise and non-land surface waveforms.  
solar_azimuth | INT | The azimuth of the sun position vector from the laser bounce point position in the local ENU frame measured from North and is positive towards East.  
solar_elevation | INT | The elevation of the sun position vector from the laser bounce point position in the local ENU frame measured from the East-North plane and is positive Up.  
shot_number | STRING | Shot number, a unique identifier. This field has the format of OOOOOBBRRGNNNNNNNN, where:
  * OOOOO: Orbit number
  * BB: Beam number
  * RR: Reserved for future use
  * G: Sub-orbit granule number
  * NNNNNNNN: Shot index

  
shot_number_within_beam | INT | Shot number within beam  
cover_z0 | INT | Cumulative canopy cover vertical profile at 0%  
cover_z1 | INT | Cumulative canopy cover vertical profile at 1%  
cover_z2 | INT | Cumulative canopy cover vertical profile at 2%  
cover_z3 | INT | Cumulative canopy cover vertical profile at 3%  
cover_z4 | INT | Cumulative canopy cover vertical profile at 4%  
cover_z5 | INT | Cumulative canopy cover vertical profile at 5%  
cover_z6 | INT | Cumulative canopy cover vertical profile at 6%  
cover_z7 | INT | Cumulative canopy cover vertical profile at 7%  
cover_z8 | INT | Cumulative canopy cover vertical profile at 8%  
cover_z9 | INT | Cumulative canopy cover vertical profile at 9%  
cover_z10 | INT | Cumulative canopy cover vertical profile at 10%  
cover_z11 | INT | Cumulative canopy cover vertical profile at 11%  
cover_z12 | INT | Cumulative canopy cover vertical profile at 12%  
cover_z13 | INT | Cumulative canopy cover vertical profile at 13%  
cover_z14 | INT | Cumulative canopy cover vertical profile at 14%  
cover_z15 | INT | Cumulative canopy cover vertical profile at 15%  
cover_z16 | INT | Cumulative canopy cover vertical profile at 16%  
cover_z17 | INT | Cumulative canopy cover vertical profile at 17%  
cover_z18 | INT | Cumulative canopy cover vertical profile at 18%  
cover_z19 | INT | Cumulative canopy cover vertical profile at 19%  
cover_z20 | INT | Cumulative canopy cover vertical profile at 20%  
cover_z21 | INT | Cumulative canopy cover vertical profile at 21%  
cover_z22 | INT | Cumulative canopy cover vertical profile at 22%  
cover_z23 | INT | Cumulative canopy cover vertical profile at 23%  
cover_z24 | INT | Cumulative canopy cover vertical profile at 24%  
cover_z25 | INT | Cumulative canopy cover vertical profile at 25%  
cover_z26 | INT | Cumulative canopy cover vertical profile at 26%  
cover_z27 | INT | Cumulative canopy cover vertical profile at 27%  
cover_z28 | INT | Cumulative canopy cover vertical profile at 28%  
cover_z29 | INT | Cumulative canopy cover vertical profile at 29%  
cover_z30 | INT | Cumulative canopy cover vertical profile at 30%  
pai_z0 | INT | Plant Area Index profile in 0 m²/m²  
pai_z1 | INT | Plant Area Index profile in 1 m²/m²  
pai_z2 | INT | Plant Area Index profile in 2 m²/m²  
pai_z3 | INT | Plant Area Index profile in 3 m²/m²  
pai_z4 | INT | Plant Area Index profile in 4 m²/m²  
pai_z5 | INT | Plant Area Index profile in 5 m²/m²  
pai_z6 | INT | Plant Area Index profile in 6 m²/m²  
pai_z7 | INT | Plant Area Index profile in 7 m²/m²  
pai_z8 | INT | Plant Area Index profile in 8 m²/m²  
pai_z9 | INT | Plant Area Index profile in 9 m²/m²  
pai_z10 | INT | Plant Area Index profile in 10 m²/m²  
pai_z11 | INT | Plant Area Index profile in 11 m²/m²  
pai_z12 | INT | Plant Area Index profile in 12 m²/m²  
pai_z13 | INT | Plant Area Index profile in 13 m²/m²  
pai_z14 | INT | Plant Area Index profile in 14 m²/m²  
pai_z15 | INT | Plant Area Index profile in 15 m²/m²  
pai_z16 | INT | Plant Area Index profile in 16 m²/m²  
pai_z17 | INT | Plant Area Index profile in 17 m²/m²  
pai_z18 | INT | Plant Area Index profile in 18 m²/m²  
pai_z19 | INT | Plant Area Index profile in 19 m²/m²  
pai_z20 | INT | Plant Area Index profile in 20 m²/m²  
pai_z21 | INT | Plant Area Index profile in 21 m²/m²  
pai_z22 | INT | Plant Area Index profile in 22 m²/m²  
pai_z23 | INT | Plant Area Index profile in 23 m²/m²  
pai_z24 | INT | Plant Area Index profile in 24 m²/m²  
pai_z25 | INT | Plant Area Index profile in 25 m²/m²  
pai_z26 | INT | Plant Area Index profile in 26 m²/m²  
pai_z27 | INT | Plant Area Index profile in 27 m²/m²  
pai_z28 | INT | Plant Area Index profile in 28 m²/m²  
pai_z29 | INT | Plant Area Index profile in 29 m²/m²  
pai_z30 | INT | Plant Area Index profile in 30 m²/m²  
pavd_z0 | INT | Plant Area Volume Density profile in 0 m²/m³  
pavd_z1 | INT | Plant Area Volume Density profile in 1 m²/m³  
pavd_z2 | INT | Plant Area Volume Density profile in 2 m²/m³  
pavd_z3 | INT | Plant Area Volume Density profile in 3 m²/m³  
pavd_z4 | INT | Plant Area Volume Density profile in 4 m²/m³  
pavd_z5 | INT | Plant Area Volume Density profile in 5 m²/m³  
pavd_z6 | INT | Plant Area Volume Density profile in 6 m²/m³  
pavd_z7 | INT | Plant Area Volume Density profile in 7 m²/m³  
pavd_z8 | INT | Plant Area Volume Density profile in 8 m²/m³  
pavd_z9 | INT | Plant Area Volume Density profile in 9 m²/m³  
pavd_z10 | INT | Plant Area Volume Density profile in 10 m²/m³  
pavd_z11 | INT | Plant Area Volume Density profile in 11 m²/m³  
pavd_z12 | INT | Plant Area Volume Density profile in 12 m²/m³  
pavd_z13 | INT | Plant Area Volume Density profile in 13 m²/m³  
pavd_z14 | INT | Plant Area Volume Density profile in 14 m²/m³  
pavd_z15 | INT | Plant Area Volume Density profile in 15 m²/m³  
pavd_z16 | INT | Plant Area Volume Density profile in 16 m²/m³  
pavd_z17 | INT | Plant Area Volume Density profile in 17 m²/m³  
pavd_z18 | INT | Plant Area Volume Density profile in 18 m²/m³  
pavd_z19 | INT | Plant Area Volume Density profile in 19 m²/m³  
pavd_z20 | INT | Plant Area Volume Density profile in 20 m²/m³  
pavd_z21 | INT | Plant Area Volume Density profile in 21 m²/m³  
pavd_z22 | INT | Plant Area Volume Density profile in 22 m²/m³  
pavd_z23 | INT | Plant Area Volume Density profile in 23 m²/m³  
pavd_z24 | INT | Plant Area Volume Density profile in 24 m²/m³  
pavd_z25 | INT | Plant Area Volume Density profile in 25 m²/m³  
pavd_z26 | INT | Plant Area Volume Density profile in 26 m²/m³  
pavd_z27 | INT | Plant Area Volume Density profile in 27 m²/m³  
pavd_z28 | INT | Plant Area Volume Density profile in 28 m²/m³  
pavd_z29 | INT | Plant Area Volume Density profile in 29 m²/m³  
pavd_z30 | INT | Plant Area Volume Density profile in 30 m²/m³  
**Terms of Use**
This dataset is in the public domain and is available without restriction on use and distribution. See [NASA's Earth Science Data & Information Policy](https://www.earthdata.nasa.gov/engage/open-data-services-and-software/data-and-information-policy) for additional information.
Citations:
  * GEDI L2B Canopy Cover and Vertical Profile Metrics Data Global Footprint Level - GEDI02_B Dubayah, R., H. Tang, J. Armston, S. Luthcke, M. Hofton, J. Blair. GEDI L2B Canopy Cover and Vertical Profile Metrics Data Global Footprint Level V002. 2021, distributed by NASA EOSDIS Land Processes DAAC. Accessed YYYY-MM-DD.


  * [ https://doi.org/10.5067/GEDI/GEDI02_B.002 ](https://doi.org/10.5067/GEDI/GEDI02_B.002)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI02_B_002#code-editor-javascript-sample) More
```
vardataset=ee.FeatureCollection(
'LARSE/GEDI/GEDI02_B_002/GEDI02_B_2021043114136_O12295_03_T07619_02_003_01_V002');
Map.setCenter(12.60033,51.01051,14);
Map.addLayer(dataset);
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/LARSE/LARSE_GEDI_GEDI02_B_002)
[ GEDI L2B Vector Canopy Cover Vertical Profile Metrics (Version 2) ](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI02_B_002)
GEDI Level 2B Canopy Cover and Vertical Profile Metrics product (GEDI02_B) extracts biophysical metrics from each GEDI waveform. These metrics are based on the directional gap probability profile derived from the L1B waveform. The vertical step between foliage profile measurements (known as dZ in GEDI documentation) is always 5 meters. …
LARSE/GEDI/GEDI02_B_002, elevation,forest-biomass,gedi,larse,nasa,tree-cover,usgs 
2019-03-25T00:00:00Z/2023-01-01T00:00:00Z
-51.6 -180 51.6 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.5067/GEDI/GEDI02_B.002 ](https://doi.org/https://www.fs.usda.gov/)
  * [ https://doi.org/10.5067/GEDI/GEDI02_B.002 ](https://doi.org/https://lpdaac.usgs.gov/products/gedi02_av002/)
  * [ https://doi.org/10.5067/GEDI/GEDI02_B.002 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI02_B_002)


