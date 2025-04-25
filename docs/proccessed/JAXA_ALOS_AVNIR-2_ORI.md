 
#  ALOS/AVNIR-2 ORI 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![JAXA/ALOS/AVNIR-2/ORI](https://developers.google.com/earth-engine/datasets/images/JAXA/JAXA_ALOS_AVNIR-2_ORI_sample.png) 

Dataset Availability
    2006-04-26T00:00:00Z–2011-04-18T00:00:00Z 

Dataset Provider
     [ JAXA Earth Observation Research Center ](https://www.eorc.jaxa.jp/ALOS/en/dataset/ori_e.htm) 

Earth Engine Snippet
     `    ee.ImageCollection("JAXA/ALOS/AVNIR-2/ORI")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/JAXA/JAXA_ALOS_AVNIR-2_ORI) 

Tags
     [alos](https://developers.google.com/earth-engine/datasets/tags/alos) [jaxa](https://developers.google.com/earth-engine/datasets/tags/jaxa) [orthophoto](https://developers.google.com/earth-engine/datasets/tags/orthophoto) [satellite-imagery](https://developers.google.com/earth-engine/datasets/tags/satellite-imagery) [visible](https://developers.google.com/earth-engine/datasets/tags/visible)
avnir-2
eorc
[Description](https://developers.google.com/earth-engine/datasets/catalog/JAXA_ALOS_AVNIR-2_ORI#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/JAXA_ALOS_AVNIR-2_ORI#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/JAXA_ALOS_AVNIR-2_ORI#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/JAXA_ALOS_AVNIR-2_ORI#terms-of-use) More
This dataset is contains orthorectified imagery from the Advanced Visible and Near Infrared Radiometer type 2 (AVNIR-2) sensor on-board the Advanced Land Observing Satellite (ALOS) "DAICHI".
The AVNIR-2 ORI product was created from AVNIR-2 1B1 data after stereo matching with reference to ALOS's Panchromatic Remote-sensing Instrument for Stereo Mapping (PRISM)-derived DSM AW3D30. The orthorectification process used AW3D30 DSM data when available and SRTM (The Shuttle Radar Topography Mission) DSM data otherwise.
**Pixel Size** 10 meters 
**Bands**
Name | Min | Max | Description  
---|---|---|---  
`B1` |  1*  |  255*  | Blue (0.42 - 0.50 μm)  
`B2` |  1*  |  255*  | Green (0.52 - 0.60 μm)  
`B3` |  1*  |  255*  | Red (0.61 - 0.69 μm)  
`B4` |  1*  |  255*  | Near-Infrared (0.76 - 0.89 μm)  
* estimated min or max value 
**Image Properties**
Name | Type | Description  
---|---|---  
CENTER_ALTITUDE | DOUBLE | Satellite alitutude at scene center (km)  
CENTER_FRAME_NUMBER | DOUBLE | Frame number of scene center (0000 to 7198)  
CENTER_HEADING_ANGLE | DOUBLE | Satellite heading angle including Earth rotation at scene center (radians)  
CENTER_SKEW_ANGLE | DOUBLE | Image skew angle at scene center (milli-radians)  
CENTER_SOLAR_AZIMUTH | DOUBLE | Azimuth angle of the sun at scene center (°)  
CENTER_SOLAR_ZENITH | DOUBLE | Solar elevation (zenith) angle of the sun at scene center (°)  
CENTER_START_TIME | STRING | Scene center time (UTC).  
INCIDENT_ANGLE | STRING | Incident angle "SNN.NNN" (S: Incident direction R/L, NN.NNN degrees)  
ORBIT_DIRECTION | STRING | Orbit direction ("A"/"D": ascending/descending)  
ORBIT_INCLINATION | DOUBLE | Nominal satellite orbit inclination (°)  
ORBIT_CYCLE_PERIOD | DOUBLE | Nominal satellite orbit cycle period (min)  
ORIENTATION_ANGLE | DOUBLE | Angle of the vertical axis of image frame from the map northing axis.  
PROCESSING_DATE | STRING | Processing date (JST)  
PROCESSING_FACILITY | STRING | Processing facility.  
PROCESSING_SOFTWARE_VESRION | STRING | Processing software version.  
PROCESSING_TIME | STRING | Processing time (JST)  
PRODUCT_ID | STRING | Product ID e.g: "ABBBCCDE"
  * A: Observation mode ("O")
  * BBB: Processing level ("ORI")
  * CC: Framing ("RF" Geo-reference, "GT", Geo-coded True-north "GM", Geo-coded Map-north),
  * D: Map projection ("U": UTM, "P": PS)
  * E: Sensor type ("N": nadir 35km, "F": forward 35km "B": backward 35km "W": nadir 70km)
  * A: AVNIR-2

  
PRODUCT_NUMBER | DOUBLE | Product version number  
RSP_ID | STRING | RSP ID e.g: "MPPPFFFFSN"
  * M: Oribit direction ("A": ascending, "D": descending)
  * PPP: RSP path number (0 to 671)
  * FFFF: RSP frame number (0000 to 7199)
  * SN: Scene shift ("-2" to " 2")

  
SATELLITE_NAME | STRING | Satellite name.  
SCENE_ID | STRING | Scene ID e.g. "AABBBCDDDDDEEEE"
  * AA: Satellite code ("AL": ALOS)
  * BBB: Sensor code ("PSM": PRISM, "AV2": AVNIR-2)
  * C: Sensor type ("N": nadir 35km, "F": forward 35km, "B": backward 35km "W": nadir 70km, "A": AVNIR-2)
  * DDDDD: Total orbit number of scene center ("00001" to "99999")
  * EEEE: Frame number of scene center, including scene shift ("0000" to "7199")

  
SENSOR_CODE | STRING | Sensor code ("PSM": PRISM, "AV2": AVNIR-2)  
SENSOR_TYPE | STRING | Sensor type ("N": nadir 35km, "F": forward 35km, "B": backward 35km "W": nadir 70km, "A": AVNIR-2)  
TOTAL_ORBIT_NUMBER | DOUBLE | Total orbit number of scene center.  
**Terms of Use**
The Japan Aerospace Exploration Agency (JAXA) releases the ALOS Orthorectified Image Product (ALOS-ORI) free of charge and open to the public with the following conditions:
  * When you provide or publish any products or services to a third party using this dataset, you are kindly requested to display that the original data is provided by JAXA.
  * When you publish your product(s) using this dataset, you are kindly requested to show the copyright (© JAXA) and the source of the data.
  * JAXA does not guarantee the quality and reliability of this dataset and JAXA assume no responsibility whatsoever for any direct or indirect damage and loss caused by use of this dataset. Also, JAXA will not be responsible for any damages of users due to changing, deleting or terminating the provision of this dataset.


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/JAXA_ALOS_AVNIR-2_ORI#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('JAXA/ALOS/AVNIR-2/ORI')
.filter(ee.Filter.date('2011-01-01','2011-04-01'));
varavnir2OriRgb=dataset.select(['B3','B2','B1']);
varavnir2OriRgbVis={
min:0.0,
max:255.0,
};
Map.setCenter(138.7302,35.3641,12);
Map.addLayer(avnir2OriRgb,avnir2OriRgbVis,'AVNIR-2 ORI RGB');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/JAXA/JAXA_ALOS_AVNIR-2_ORI)
[ ALOS/AVNIR-2 ORI ](https://developers.google.com/earth-engine/datasets/catalog/JAXA_ALOS_AVNIR-2_ORI)
This dataset is contains orthorectified imagery from the Advanced Visible and Near Infrared Radiometer type 2 (AVNIR-2) sensor on-board the Advanced Land Observing Satellite (ALOS) "DAICHI". The AVNIR-2 ORI product was created from AVNIR-2 1B1 data after stereo matching with reference to ALOS's Panchromatic Remote-sensing Instrument for Stereo Mapping (PRISM)-derived …
JAXA/ALOS/AVNIR-2/ORI, alos,jaxa,orthophoto,satellite-imagery,visible 
2006-04-26T00:00:00Z/2011-04-18T00:00:00Z
23.81 127.05 46.04 154.41 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.eorc.jaxa.jp/ALOS/en/dataset/ori_e.htm)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/JAXA_ALOS_AVNIR-2_ORI)


