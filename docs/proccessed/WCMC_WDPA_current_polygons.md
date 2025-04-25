 
#  WDPA: World Database on Protected Areas (polygons) 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![WCMC/WDPA/current/polygons](https://developers.google.com/earth-engine/datasets/images/WCMC/WCMC_WDPA_current_polygons_sample.png) 

Dataset Availability
    2017-07-01T00:00:00Z–2030-01-01T00:00:00Z 

Dataset Provider
     [ UN Environment World Conservation Monitoring Centre (UNEP-WCMC) / Protected Planet ](https://www.protectedplanet.net/) 

Earth Engine Snippet
     FeatureCollection `    ee.FeatureCollection("WCMC/WDPA/current/polygons")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/WCMC/WCMC_WDPA_current_polygons)      FeatureView  `    ui.Map.FeatureViewLayer("WCMC/WDPA/current/polygons_FeatureView")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/WCMC/WCMC_WDPA_current_polygons_FeatureView) 

Tags
     [boundaries](https://developers.google.com/earth-engine/datasets/tags/boundaries) [ecosystems](https://developers.google.com/earth-engine/datasets/tags/ecosystems) [iucn](https://developers.google.com/earth-engine/datasets/tags/iucn) [marine](https://developers.google.com/earth-engine/datasets/tags/marine) [mpa](https://developers.google.com/earth-engine/datasets/tags/mpa) [protected](https://developers.google.com/earth-engine/datasets/tags/protected) [table](https://developers.google.com/earth-engine/datasets/tags/table) [wcmc](https://developers.google.com/earth-engine/datasets/tags/wcmc) [wdpa](https://developers.google.com/earth-engine/datasets/tags/wdpa)
[Description](https://developers.google.com/earth-engine/datasets/catalog/WCMC_WDPA_current_polygons#description)[Table Schema](https://developers.google.com/earth-engine/datasets/catalog/WCMC_WDPA_current_polygons#table-schema)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/WCMC_WDPA_current_polygons#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/WCMC_WDPA_current_polygons#citations) More
The World Database on Protected Areas (WDPA) is the most up-to-date and complete source of information on protected areas, updated monthly with submissions from governments, non-governmental organizations, landowners, and communities. It is managed by the United Nations Environment Programme's World Conservation Monitoring Centre (UNEP-WCMC) with support from IUCN and its World Commission on Protected Areas (WCPA).
**WDPA User Manual.** For details including methodologies,standards, data providers, metadata field definitions and descriptions, refer to the [WDPA User Manual](https://pp-import-production.s3.amazonaws.com/WDPA_Manual_1_5.pdf).
The WDPA has two feature classes with associated spatial and tabular data on more than 200k protected areas. About 91% contain polygon boundaries, with the remaining only as points, representing the center of the protected area as much as possible.
**Asset Naming Conventions.** WCMC updates the WDPA on a monthly basis. The most recent version is always available as WCMC/WDPA/current/polygons and WCMC/WDPA/current/points. Historical versions, starting with July 2017, are available in the format WCMC/WDPA/YYYYMM/polygons and WCMC/WDPA/YYYYMM/points.
Please see the [WDPA User Manual](https://pp-import-production.s3.amazonaws.com/WDPA_Manual_1_5.pdf) for additional details on the field list.
**Table Schema**
Name | Type | Description  
---|---|---  
WDPAID | DOUBLE | Unique identifier for a protected area (PA), assigned by UNEP-WCMC.  
WDPA_PID | STRING | Unique identifier for parcels or zones within a PA, assigned by UNEP-WCMC.  
PA_DEF | STRING | PA definition. Whether this site meets the IUCN and/or CBD definition of a PA: 1=yes, 0=no (currently stored outside WDPA).  
NAME | STRING | Name of the PA as provided by the data provider.  
ORIG_NAME | STRING | Name of the PA in the original language.  
DESIG | STRING | Designation of the PA in the native language.  
DESIG_ENG | STRING | Designation of the PA in English. Allowed values for international-level designations: Ramsar Site, Wetland of International Importance; UNESCO-MAB Biosphere Reserve; or World Heritage Site. Allowed values for regional-level designations: Baltic Sea Protected Area (HELCOM), Specially Protected Area (Cartagena Convention), Marine Protected Area (CCAMLR), Marine Protected Area (OSPAR), Site of Community Importance (Habitats Directive), Special Protection Area (Birds Directive), or Specially Protected Areas of Mediterranean Importance (Barcelona Convention). No fixed values for PAs designated at a national level.  
DESIG_TYPE | STRING | Designation type, one of: national, regional, international, or not applicable  
IUCN_CAT | STRING | IUCN management category, one of: Ia (strict nature reserve), Ib (wilderness area), II (national park), III (natural monument or feature), IV (habitat/species management area), V (protected landscape/seascape), VI (PA with sustainable use of natural resources), not applicable, not assigned, or not reported.  
INT_CRIT | STRING | International criteria, assigned by UNEP-WCMC. For World Heritage and Ramsar sites only.  
MARINE | STRING | This field describes whether a PA falls totally or partially within the marine environment, one of: 0 (100% terrestrial PA), 1 (coastal: marine and terrestrial PA), or 2 (100% marine PA).  
REP_M_AREA | DOUBLE | Marine area in square kilometers provided by the data provider.  
REP_AREA | DOUBLE | The total PA extent, including both marine (if applicable) and terrestrial areas, in square kilometers provided by data provider as specified in the legal text for the site.  
NO_TAKE | STRING | No take means that the taking of living or dead natural resources, inclusive of all methods of fishing, extraction, dumping, dredging and construction, is strictly prohibited in all or part of a marine PA. This is only applicable to PAs where the field marine = 1 or 2. One of: all, part, none, not reported, or not applicable (if MARINE field = 0).  
NO_TK_AREA | DOUBLE | Area of the marine no-take area in square kilometers.  
STATUS | STRING | Status of a PA, one of: proposed, inscribed, adopted, designated, or established.  
STATUS_YR | INT | Year of enactment of status in the STATUS field.  
GOV_TYPE | STRING | Description of the decision-making structure of a PA. One of: federal or national ministry or agency, sub-national ministry or agency, government-delegated management, transboundary governance, collaborative governance, joint governance, individual landowners, non-profit organizations, for-profit organizations, indigenous peoples, local communities, or not reported.  
OWN_TYPE | STRING | Ownership type, one of: state, communal, individual landowners, for-profit organizations, non-profit organizations, joint ownership, multiple ownership, contested, or not Reported.  
MANG_AUTH | STRING | Management authority. Agency, organization, individual or group that manages the PA.  
MANG_PLAN | STRING | Link or reference to the PAs management plan.  
VERIF | STRING | Verification status, assigned by UNEP-WCMC. One of: state verified, expert verified, not reported (for unverified data that was already in the WDPA prior to the inclusion of the ''Verification'' field).  
METADATAID | INT | Metadata ID, assigned by UNEP-WCMC. Link to WDPA source table.  
SUB_LOC | STRING | Sub-national location. [ISO 3166-2 sub-national code](https://en.wikipedia.org/wiki/ISO_3166-2) where the PA is located. If the PA is in more than one state, province, region etc., multiple ISO-3166-2 codes can be listed separated by a comma and space.  
PARENT_ISO | STRING | Parent ISO3 code. [ISO 3166-3 character code](https://en.wikipedia.org/wiki/ISO_3166-3) of country where the PA is located.  
ISO3 | STRING | ISO3 Code. [ISO 3166-3 character code](https://en.wikipedia.org/wiki/ISO_3166-3) of the country or territory where the PA is located.  
GIS_AREA | DOUBLE | Protected area total extent, including both marine (if applicable) and terrestrial areas, in square kilometers calculated by UNEP-WCMC projecting the protected area polygon in the standard Mollweide projection and using GIS software tools.  
GIS_M_AREA | DOUBLE | Protected area marine extent in square kilometers calculated by UNEP-WCMC projecting the protected area polygon in the standard Mollweide projection and using GIS software tools.  
**Terms of Use**
Please visit the [full terms and conditions page](https://www.protectedplanet.net/c/terms-and-conditions) of Protected Planet. Select highlights below:
**No Commercial Use.** Neither (a) the WDPA Materials nor (b) any work derived from or based upon the WDPA Materials ("Derivative Works") may be put to Commercial Use without the prior written permission of UNEP-WCMC. "Commercial Use" means a) any use by, on behalf of, or to inform or assist the activities of, a commercial entity (an entity that operates 'for profit') or b) use by any individual or non-profit entity for the purposes of revenue generation.
**Disclaimer.** The designations of geographical entities in any Data Set do not imply the expression of any view or opinion whatsoever on the part of UNEP or WCMC concerning the legal status of any country, territory, or area, or of its authorities, or concerning the delimitation of its frontiers or boundaries.
**Attribution.** You must ensure that the citation is always clearly reproduced in any publication or analysis involving the WDPA Materials in any derived form or format.
Citations:
  * UNEP-WCMC and IUCN (year), Protected Planet: The World Database on Protected Areas (WDPA) [On-line], [insert month/year of the version used], Cambridge, UK: UNEP-WCMC and IUCN Available at: www.protectedplanet.net.


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/WCMC_WDPA_current_polygons#code-editor-javascript-sample) More
```
vardataset=ee.FeatureCollection('WCMC/WDPA/current/polygons');
varvisParams={
palette:['2ed033','5aff05','67b9ff','5844ff','0a7618','2c05ff'],
min:0.0,
max:1550000.0,
opacity:0.8,
};
varimage=ee.Image().float().paint(dataset,'REP_AREA');
Map.setCenter(41.104,-17.724,6);
Map.addLayer(image,visParams,'WCMC/WDPA/current/polygons');
Map.addLayer(dataset,null,'for Inspector',false);
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/WCMC/WCMC_WDPA_current_polygons)
### Visualize as a FeatureView
A `FeatureView` is a view-only, accelerated representation of a `FeatureCollection`. For more details, visit the [ `FeatureView` documentation. ](https://developers.google.com/earth-engine/guides/featureview_overview)
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/WCMC_WDPA_current_polygons#code-editor-javascript-sample) More
```
varfvLayer=ui.Map.FeatureViewLayer('WCMC/WDPA/current/polygons_FeatureView');
varvisParams={
color:{
property:'REP_AREA',
mode:'linear',
palette:['2ed033','5aff05','67b9ff','5844ff','0a7618','2c05ff'],
min:0.0,
max:1550000.0
},
opacity:0.8
};
fvLayer.setVisParams(visParams);
fvLayer.setName('WCMC/WDPA/current/polygons');
Map.setCenter(41.104,-17.724,6);
Map.add(fvLayer);
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/WCMC/WCMC_WDPA_current_polygons_FeatureView)
[ WDPA: World Database on Protected Areas (polygons) ](https://developers.google.com/earth-engine/datasets/catalog/WCMC_WDPA_current_polygons)
The World Database on Protected Areas (WDPA) is the most up-to-date and complete source of information on protected areas, updated monthly with submissions from governments, non-governmental organizations, landowners, and communities. It is managed by the United Nations Environment Programme's World Conservation Monitoring Centre (UNEP-WCMC) with support from IUCN and its …
WCMC/WDPA/current/polygons, boundaries,ecosystems,iucn,marine,mpa,protected,table,wcmc,wdpa 
2017-07-01T00:00:00Z/2030-01-01T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.protectedplanet.net/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/WCMC_WDPA_current_polygons)


