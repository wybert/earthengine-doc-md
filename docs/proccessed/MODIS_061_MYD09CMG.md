 
#  MYD09CMG.061 Aqua Surface Reflectance Daily L3 Global 0.05 Deg CMG 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![MODIS/061/MYD09CMG](https://developers.google.com/earth-engine/datasets/images/MODIS/MODIS_061_MYD09CMG_sample.png) 

Dataset Availability
    2002-07-04T00:00:00Z–2025-04-19T00:00:00Z 

Dataset Provider
     [ NASA LP DAAC at the USGS EROS Center ](https://doi.org/10.5067/MODIS/MYD09CMG.061) 

Earth Engine Snippet
     `    ee.ImageCollection("MODIS/061/MYD09CMG")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_061_MYD09CMG) 

Cadence
    1 Day 

Tags
     [aqua](https://developers.google.com/earth-engine/datasets/tags/aqua) [brightness-temperature](https://developers.google.com/earth-engine/datasets/tags/brightness-temperature) [ozone](https://developers.google.com/earth-engine/datasets/tags/ozone) [satellite-imagery](https://developers.google.com/earth-engine/datasets/tags/satellite-imagery) [surface-reflectance](https://developers.google.com/earth-engine/datasets/tags/surface-reflectance)
[Description](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD09CMG#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD09CMG#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD09CMG#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD09CMG#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD09CMG#dois) More
The MYD09CMG Version 6.1 product provides an estimate of the surface spectral reflectance of Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) Bands 1 through 7, resampled to 5600 meter pixel resolution and corrected for atmospheric conditions such as gasses, aerosols, and Rayleigh scattering. The MYD09CMG data product provides 25 layers including MODIS bands 1 through 7; Brightness Temperature data from thermal bands 20, 21, 31, and 32; along with Quality Assurance (QA) and observation bands. This product is based on a Climate Modeling Grid (CMG) for use in climate simulation models.
This dataset has a striping issue originating from Band 5’s dead detector 20. The MYD09/Band 5 show the dead detector striping in band 5, but it has been properly flagged in the QA layer. The science team has been notified and the issue will be addressed in the Collection 7. More details can be found on [the known issue page](https://landweb.modaps.eosdis.nasa.gov/displayissue?id=939).
Documentation:
  * [User's Guide](https://lpdaac.usgs.gov/documents/925/MOD09_User_Guide_V61.pdf)
  * [Algorithm Theoretical Basis Document (ATBD)](https://lpdaac.usgs.gov/documents/305/MOD09_ATBD.pdf)
  * [General Documentation](https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MYD09CMG)


**Pixel Size** 5600 meters 
**Bands**
Name | Units | Min | Max | Wavelength | Description  
---|---|---|---|---|---  
`Coarse_Resolution_Surface_Reflectance_Band_1` | Dimensionless |  -0.01  |  1.6  | 620-670nm | Surface reflectance for band 1  
`Coarse_Resolution_Surface_Reflectance_Band_2` | Dimensionless |  -0.01  |  1.6  | 841-876nm | Surface reflectance for band 2  
`Coarse_Resolution_Surface_Reflectance_Band_3` | Dimensionless |  -0.01  |  1.6  | 459-479nm | Surface reflectance for band 3  
`Coarse_Resolution_Surface_Reflectance_Band_4` | Dimensionless |  -0.01  |  1.6  | 545-565nm | Surface reflectance for band 4  
`Coarse_Resolution_Surface_Reflectance_Band_5` | Dimensionless |  -0.01  |  1.6  | 1230-1250nm | Surface reflectance for band 5  
`Coarse_Resolution_Surface_Reflectance_Band_6` | Dimensionless |  -0.01  |  1.6  | 1628-1652nm | Surface reflectance for band 6  
`Coarse_Resolution_Surface_Reflectance_Band_7` | Dimensionless |  -0.01  |  1.6  | 2105-2155nm | Surface reflectance for band 7  
`Coarse_Resolution_Solar_Zenith_Angle` | deg |  0  |  180  | Solar Zenith Angle  
`Coarse_Resolution_View_Zenith_Angle` | deg |  0  |  180  | View Zenith Angle  
`Coarse_Resolution_Relative_Azimuth_Angle` | deg |  -180  |  180  | Relative Azimuth Angle  
`Coarse_Resolution_Ozone` | atm cm |  0.0025  |  0.6375  | Ozone Resolution  
`Coarse_Resolution_Brightness_Temperature_Band_20` | K |  0.01  |  400  | 3.360-3.840µm | Band 20 Brightness Temperature  
`Coarse_Resolution_Brightness_Temperature_Band_21` | K |  0.01  |  400  | 3.929-3.989µm | Band 21 Brightness Temperature  
`Coarse_Resolution_Brightness_Temperature_Band_31` | K |  0.01  |  400  | 10.780-11.280µm | Band 31 Brightness Temperature  
`Coarse_Resolution_Brightness_Temperature_Band_32` | K |  0.01  |  400  | 11.770-12.270µm | Band 32 Brightness Temperature  
`Coarse_Resolution_Granule_Time` |  1  |  2355  | Granule time of day, as HHMM  
`Coarse_Resolution_Band_3_Path_Radiance` | Dimensionless |  -0.01  |  1.6  | Band 3 Radiance  
`Coarse_Resolution_QA` | Quality Assurance  
Bitmask for Coarse_Resolution_QA
  * Bits 0-1: MODLAND QA bits 
    * 0: Corrected product produced at ideal quality - all bands
    * 1: Corrected product produced at less than ideal quality - some or all bands
    * 2: Corrected product not produced due to cloud effects - all bands
    * 3: Corrected product not produced for other reasons - some or all bands, may be fill value (11) [Note that a value of (11) overrides a value of (01)]
  * Bits 2-5: Band 1 data quality, four bit range 
    * 0: Highest quality
    * 7: Noisy detector
    * 8: Dead detector, data interpolated in L1B
    * 9: Solar zenith >= 86 degrees
    * 10: Solar zenith >= 85 and < 86 degrees
    * 11: Missing input
    * 12: Internal constant used in place of climatological data for at least one atmospheric constant
    * 13: Correction out of bounds, pixel constrained to extreme allowable value
    * 14: L1B data faulty
    * 15: Not processed due to deep ocean or clouds
  * Bits 6-9: Band 2 data quality, four bit range 
    * 0: Highest quality
    * 7: Noisy detector
    * 8: Dead detector, data interpolated in L1B
    * 9: Solar zenith >= 86 degrees
    * 10: Solar zenith >= 85 and < 86 degrees
    * 11: Missing input
    * 12: Internal constant used in place of climatological data for at least one atmospheric constant
    * 13: Correction out of bounds, pixel constrained to extreme allowable value
    * 14: L1B data faulty
    * 15: Not processed due to deep ocean or clouds
  * Bits 10-13: Band 3 data quality, four bit range 
    * 0: Highest quality
    * 7: Noisy detector
    * 8: Dead detector, data interpolated in L1B
    * 9: Solar zenith >= 86 degrees
    * 10: Solar zenith >= 85 and < 86 degrees
    * 11: Missing input
    * 12: Internal constant used in place of climatological data for at least one atmospheric constant
    * 13: Correction out of bounds, pixel constrained to extreme allowable value
    * 14: L1B data faulty
    * 15: Not processed due to deep ocean or clouds
  * Bits 14-17: Band 4 data quality, four bit range 
    * 0: Highest quality
    * 7: Noisy detector
    * 8: Dead detector, data interpolated in L1B
    * 9: Solar zenith >= 86 degrees
    * 10: Solar zenith >= 85 and < 86 degrees
    * 11: Missing input
    * 12: Internal constant used in place of climatological data for at least one atmospheric constant
    * 13: Correction out of bounds, pixel constrained to extreme allowable value
    * 14: L1B data faulty
    * 15: Not processed due to deep ocean or clouds
  * Bits 18-21: Band 5 data quality, four bit range 
    * 0: Highest quality
    * 7: Noisy detector
    * 8: Dead detector, data interpolated in L1B
    * 9: Solar zenith >= 86 degrees
    * 10: Solar zenith >= 85 and < 86 degrees
    * 11: Missing input
    * 12: Internal constant used in place of climatological data for at least one atmospheric constant
    * 13: Correction out of bounds, pixel constrained to extreme allowable value
    * 14: L1B data faulty
    * 15: Not processed due to deep ocean or clouds
  * Bits 22-25: Band 6 data quality, four bit range 
    * 0: Highest quality
    * 7: Noisy detector
    * 8: Dead detector, data interpolated in L1B
    * 9: Solar zenith >= 86 degrees
    * 10: Solar zenith >= 85 and < 86 degrees
    * 11: Missing input
    * 12: Internal constant used in place of climatological data for at least one atmospheric constant
    * 13: Correction out of bounds, pixel constrained to extreme allowable value
    * 14: L1B data faulty
    * 15: Not processed due to deep ocean or clouds
  * Bits 26-29: Band 7 data quality, four bit range 
    * 0: Highest quality
    * 7: Noisy detector
    * 8: Dead detector, data interpolated in L1B
    * 9: Solar zenith >= 86 degrees
    * 10: Solar zenith >= 85 and < 86 degrees
    * 11: Missing input
    * 12: Internal constant used in place of climatological data for at least one atmospheric constant
    * 13: Correction out of bounds, pixel constrained to extreme allowable value
    * 14: L1B data faulty
    * 15: Not processed due to deep ocean or clouds
  * Bit 30: Atmospheric correction performed 
    * 0: No
    * 1: Yes
  * Bit 31: Adjacency correction performed 
    * 0: No
    * 1: Yes

  
`Coarse_Resolution_Internal_CM` | Internal Cloud Mask  
Bitmask for Coarse_Resolution_Internal_CM
  * Bit 0: Cloudy 
    * 0: No
    * 1: Yes
  * Bit 1: Clear 
    * 0: No
    * 1: Yes
  * Bit 2: High clouds 
    * 0: No
    * 1: Yes
  * Bit 3: Low clouds 
    * 0: No
    * 1: Yes
  * Bit 4: Snow 
    * 0: No
    * 1: Yes
  * Bit 5: Fire 
    * 0: No
    * 1: Yes
  * Bit 6: Sun glint 
    * 0: No
    * 1: Yes
  * Bit 7: Dust 
    * 0: No
    * 1: Yes
  * Bit 8: Cloud shadow 
    * 0: No
    * 1: Yes
  * Bit 9: Pixel is adjacent to cloud 
    * 0: No
    * 1: Yes
  * Bits 10-11: Cirrus 
    * 0: None
    * 1: Small
    * 2: Average
    * 3: High
  * Bit 12: Pan flag 
    * 0: No salt pan
    * 1: Salt pan
  * Bit 13: Criteria used for aerosol retrieval 
    * 0: Criterion 1
    * 1: Criterion 2
  * Bit 14: AOT (aerosol optical thickness) has climatological values 
    * 0: No
    * 1: Yes
  * Bit 15: Pixel has interpolated TR, PR or SA data 
    * 0: No
    * 1: Yes

  
`Coarse_Resolution_State_QA` | State Quality Assurance  
Bitmask for Coarse_Resolution_State_QA
  * Bits 0-1: Cloud state 
    * 0: Clear
    * 1: Cloudy
    * 2: Mixed
    * 3: Not set, assumed clear
  * Bit 2: Cloud shadow 
    * 0: No
    * 1: Yes
  * Bits 3-5: Land/water flag 
    * 0: Shallow ocean
    * 1: Land
    * 2: Ocean coastlines and lake shorelines
    * 3: Shallow inland water
    * 4: Ephemeral water
    * 5: Deep inland water
    * 6: Continental/moderate ocean
    * 7: Deep ocean
  * Bits 6-7: Aerosol quantity 
    * 0: Climatology
    * 1: Low
    * 2: Average
    * 3: High
  * Bits 8-9: Cirrus detected 
    * 0: None
    * 1: Small
    * 2: Average
    * 3: High
  * Bit 10: Internal cloud algorithm flag 
    * 0: No cloud
    * 1: Cloud
  * Bit 11: Internal fire algorithm flag 
    * 0: No fire
    * 1: Fire
  * Bit 12: MOD35 snow/ice flag 
    * 0: No
    * 1: Yes
  * Bit 13: Pixel is adjacent to cloud 
    * 0: No
    * 1: Yes
  * Bit 14: BRDF correction performed data 
    * 0: No
    * 1: Yes
  * Bit 15: Internal snow mask 
    * 0: No snow
    * 1: Snow

  
`Coarse_Resolution_Number_Mapping` | Number Mapping Cloud/Snow  
Bitmask for Coarse_Resolution_Number_Mapping
  * Bits 0-7: Number of pixel mapping flagged as cloudy 
  * Bits 8-15: Number of pixel mapping flagged as cloud shadow 
  * Bits 16-23: Number of pixel mapping flagged as adjacent to cloud 
  * Bits 24-31: Number of pixel mapping flagged for snow 

  
`number_of_500m_pixels_averaged_b3` |  1  |  200  | Number of 500m pixels used in average  
`number_of_500m_rej_detector` |  1  |  100  | Number of 500m pixels rejected for use  
`number_of_250m_pixels_averaged_b1-2` |  1  |  640  | Number of 250m pixels used in b1-2 average  
`n_pixels_averaged` |  1  |  40  | Number of pixels used in average  
**Terms of Use**
MODIS data and products acquired through the LP DAAC have no restrictions on subsequent use, sale, or redistribution.
Citations:
  * Please visit [LP DAAC 'Citing Our Data' page](https://lpdaac.usgs.gov/citing_our_data) for information on citing LP DAAC datasets.


  * [ https://doi.org/10.5067/MODIS/MYD09CMG.061 ](https://doi.org/10.5067/MODIS/MYD09CMG.061)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD09CMG#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('MODIS/061/MYD09CMG')
.filter(ee.Filter.date('2018-01-01','2018-05-01'));
vartrueColor=
dataset.select([
'Coarse_Resolution_Surface_Reflectance_Band_1',
'Coarse_Resolution_Surface_Reflectance_Band_2',
'Coarse_Resolution_Surface_Reflectance_Band_3'
]);
vartrueColorVis={
min:-0.4,
max:1.0,
};
Map.setCenter(6.746,46.529,6);
Map.addLayer(trueColor,trueColorVis,'True Color');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_061_MYD09CMG)
[ MYD09CMG.061 Aqua Surface Reflectance Daily L3 Global 0.05 Deg CMG ](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD09CMG)
The MYD09CMG Version 6.1 product provides an estimate of the surface spectral reflectance of Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) Bands 1 through 7, resampled to 5600 meter pixel resolution and corrected for atmospheric conditions such as gasses, aerosols, and Rayleigh scattering. The MYD09CMG data product provides 25 layers including …
MODIS/061/MYD09CMG, aqua,brightness-temperature,ozone,satellite-imagery,surface-reflectance 
2002-07-04T00:00:00Z/2025-04-19T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.5067/MODIS/MYD09CMG.061 ](https://doi.org/https://doi.org/10.5067/MODIS/MYD09CMG.061)
  * [ https://doi.org/10.5067/MODIS/MYD09CMG.061 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD09CMG)


