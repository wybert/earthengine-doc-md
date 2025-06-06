 
#  ERA5-Land Daily Aggregated - ECMWF Climate Reanalysis 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![ECMWF/ERA5_LAND/DAILY_AGGR](https://developers.google.com/earth-engine/datasets/images/ECMWF/ECMWF_ERA5_LAND_DAILY_AGGR_sample.png) 

Dataset Availability
    1950-01-02T00:00:00Z–2025-04-15T00:00:00Z 

Dataset Provider
     [ Daily Aggregates: Google and Copernicus Climate Data Store ](https://cds.climate.copernicus.eu/cdsapp) 

Earth Engine Snippet
     `    ee.ImageCollection("ECMWF/ERA5_LAND/DAILY_AGGR")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/ECMWF/ECMWF_ERA5_LAND_DAILY_AGGR) 

Cadence
    1 Month 

Tags
     [cds](https://developers.google.com/earth-engine/datasets/tags/cds) [climate](https://developers.google.com/earth-engine/datasets/tags/climate) [copernicus](https://developers.google.com/earth-engine/datasets/tags/copernicus) [ecmwf](https://developers.google.com/earth-engine/datasets/tags/ecmwf) [era5-land](https://developers.google.com/earth-engine/datasets/tags/era5-land) [evaporation](https://developers.google.com/earth-engine/datasets/tags/evaporation) [heat](https://developers.google.com/earth-engine/datasets/tags/heat) [lakes](https://developers.google.com/earth-engine/datasets/tags/lakes) [precipitation](https://developers.google.com/earth-engine/datasets/tags/precipitation) [pressure](https://developers.google.com/earth-engine/datasets/tags/pressure) [radiation](https://developers.google.com/earth-engine/datasets/tags/radiation) [reanalysis](https://developers.google.com/earth-engine/datasets/tags/reanalysis) [runoff](https://developers.google.com/earth-engine/datasets/tags/runoff) [snow](https://developers.google.com/earth-engine/datasets/tags/snow) [soil-water](https://developers.google.com/earth-engine/datasets/tags/soil-water) [temperature](https://developers.google.com/earth-engine/datasets/tags/temperature) [vegetation](https://developers.google.com/earth-engine/datasets/tags/vegetation) [wind](https://developers.google.com/earth-engine/datasets/tags/wind)
[Description](https://developers.google.com/earth-engine/datasets/catalog/ECMWF_ERA5_LAND_DAILY_AGGR#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/ECMWF_ERA5_LAND_DAILY_AGGR#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/ECMWF_ERA5_LAND_DAILY_AGGR#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/ECMWF_ERA5_LAND_DAILY_AGGR#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/ECMWF_ERA5_LAND_DAILY_AGGR#citations) More
ERA5-Land is a reanalysis dataset providing a consistent view of the evolution of land variables over several decades at an enhanced resolution compared to ERA5. ERA5-Land has been produced by replaying the land component of the ECMWF ERA5 climate reanalysis. Reanalysis combines model data with observations from across the world into a globally complete and consistent dataset using the laws of physics. Reanalysis produces data that goes several decades back in time, providing an accurate description of the climate of the past. This dataset includes all 50 variables as available on CDS.
ERA5-Land data is available from 1950 to three months from real-time.
Please consult [the ERA5-Land "Known Issues" section](https://confluence.ecmwf.int/display/CKB/ERA5-Land%3A+data+documentation). In particular, note that three components of the total evapotranspiration have values swapped as follows:
  * variable "Evaporation from bare soil" (mars parameter code 228101 (evabs)) has the values corresponding to the "Evaporation from vegetation transpiration" (mars parameter 228103 (evavt)),
  * variable "Evaporation from open water surfaces excluding oceans (mars parameter code 228102 (evaow)) has the values corresponding to the "Evaporation from bare soil" (mars parameter code 228101 (evabs)),
  * variable "Evaporation from vegetation transpiration" (mars parameter code 228103 (evavt)) has the values corresponding to the "Evaporation from open water surfaces excluding oceans" (mars parameter code 228102 (evaow)).


The asset is a daily aggregate of ECMWF ERA5 Land hourly assets which includes both flow and non-flow bands. Flow bands are formed by collecting the first hour's data of the following day which holds aggregated sum of previous day and while the non-flow bands are created by averaging all hourly data of the day. The flow bands are labeled with the "_sum" identifier, which approach is different from the daily data produced by Copernicus Climate Data Store, where flow bands are averaged too.
Daily aggregates have been pre-calculated to facilitate many applications requiring easy and fast access to the data.
Precipitation and other flow (accumulated) bands might occasionally have negative values, which doesn't make physical sense. At other times their values might be excessively high.
This problem is due to how the GRIB format saves data: it simplifies or "packs" the data into smaller, less precise numbers, which can introduce errors. These errors get worse when the data varies a lot.
Because of this, when we look at the data for a whole day to compute daily totals, sometimes the highest amount of rainfall recorded at one time can seem larger than the total rainfall measured for the entire day.
To learn more, Please see: ["Why are there sometimes small negative precipitation accumulations"](https://confluence.ecmwf.int/display/UDOC/Why+are+there+sometimes+small+negative+precipitation+accumulations+-+ecCodes+GRIB+FAQ)
**Pixel Size** 11132 meters 
**Bands**
Name | Units | Description  
---|---|---  
`dewpoint_temperature_2m` | K | Temperature to which the air, at 2 meters above the surface of the Earth, would have to be cooled for saturation to occur. It is a measure of the humidity of the air. Combined with temperature and pressure, it can be used to calculate the relative humidity. 2m dew point temperature is calculated by interpolating between the lowest model level and the Earth's surface, taking account of the atmospheric conditions.  
`temperature_2m` | K | Temperature of air at 2m above the surface of land, sea or in-land waters. 2m temperature is calculated by interpolating between the lowest model level and the Earth's surface, taking account of the atmospheric conditions.  
`skin_temperature` | K | Temperature of the surface of the Earth. The skin temperature is the theoretical temperature that is required to satisfy the surface energy balance. It represents the temperature of the uppermost surface layer, which has no heat capacity and so can respond instantaneously to changes in surface fluxes. Skin temperature is calculated differently over land and sea.  
`soil_temperature_level_1` | K | Temperature of the soil in layer 1 (0 - 7 cm) of the ECMWF Integrated Forecasting System. The surface is at 0 cm. Soil temperature is set at the middle of each layer, and heat transfer is calculated at the interfaces between them. It is assumed that there is no heat transfer out of the bottom of the lowest layer.  
`soil_temperature_level_2` | K | Temperature of the soil in layer 2 (7-28 cm) of the ECMWF Integrated Forecasting System.  
`soil_temperature_level_3` | K | Temperature of the soil in layer 3 (28-100 cm) of the ECMWF Integrated Forecasting System.  
`soil_temperature_level_4` | K | Temperature of the soil in layer 4 (100-289 cm) of the ECMWF Integrated Forecasting System.  
`lake_bottom_temperature` | K | Temperature of water at the bottom of inland water bodies (lakes, reservoirs, rivers) and coastal waters. ECMWF implemented a lake model in May 2015 to represent the water temperature and lake ice of all the world's major inland water bodies in the Integrated Forecasting System. The model keeps lake depth and surface area (or fractional cover) constant in time.  
`lake_ice_depth` | m | The thickness of ice on inland water bodies (lakes, reservoirs and rivers) and coastal waters. The ECMWF Integrated Forecasting System (IFS) represents the formation and melting of ice on inland water bodies (lakes, reservoirs and rivers) and coastal water. A single ice layer is represented. This parameter is the thickness of that ice layer.  
`lake_ice_temperature` | K | The temperature of the uppermost surface of ice on inland water bodies (lakes, reservoirs, rivers) and coastal waters. The ECMWF Integrated Forecasting System represents the formation and melting of ice on lakes. A single ice layer is represented.  
`lake_mix_layer_depth` | m | The thickness of the upper most layer of an inland water body (lake, reservoirs, and rivers) or coastal waters that is well mixed and has a near constant temperature with depth (uniform distribution of temperature). The ECMWF Integrated Forecasting System represents inland water bodies with two layers in the vertical, the mixed layer above and the thermocline below. Thermoclines upper boundary is located at the mixed layer bottom, and the lower boundary at the lake bottom. Mixing within the mixed layer can occur when the density of the surface (and near-surface) water is greater than that of the water below. Mixing can also occur through the action of wind on the surface of the lake.  
`lake_mix_layer_temperature` | K | The temperature of the upper most layer of inland water bodies (lakes, reservoirs and rivers) or coastal waters) that is well mixed. The ECMWF Integrated Forecasting System represents inland water bodies with two layers in the vertical, the mixed layer above and the thermocline below. Thermoclines upper boundary is located at the mixed layer bottom, and the lower boundary at the lake bottom. Mixing within the mixed layer can occur when the density of the surface (and near-surface) water is greater than that of the water below. Mixing can also occur through the action of wind on the surface of the lake.  
`lake_shape_factor` | This parameter describes the way that temperature changes with depth in the thermocline layer of inland water bodies (lakes, reservoirs and rivers) and coastal waters. It is used to calculate the lake bottom temperature and other lake-related parameters. The ECMWF Integrated Forecasting System represents inland and coastal water bodies with two layers in the vertical, the mixed layer above and the thermocline below where temperature changes with depth.  
`lake_total_layer_temperature` | K | The mean temperature of total water column in inland water bodies (lakes, reservoirs and rivers) and coastal waters. The ECMWF Integrated Forecasting System represents inland water bodies with two layers in the vertical, the mixed layer above and the thermocline below where temperature changes with depth. This parameter is the mean over the two layers.  
`snow_albedo` | It is defined as the fraction of solar (shortwave) radiation reflected by the snow, across the solar spectrum, for both direct and diffuse radiation. It is a measure of the reflectivity of the snow covered grid cells. Values vary between 0 and 1. Typically, snow and ice have high reflectivity with albedo values of 0.8 and above.  
`snow_cover` | It represents the fraction (0-1) of the cell / grid-box occupied by snow (similar to the cloud cover fields of ERA5).  
`snow_density` | kg/m^3 | Mass of snow per cubic meter in the snow layer. The ECMWF Integrated Forecast System (IFS) model represents snow as a single additional layer over the uppermost soil level. The snow may cover all or part of the grid box.  
`snow_depth` | m | Instantaneous grib-box average of the snow thickness on the ground (excluding snow on canopy).  
`snow_depth_water_equivalent` | m of water equivalent | Depth of snow from the snow-covered area of a grid box. Its units are meters of water equivalent, so it is the depth the water would have if the snow melted and was spread evenly over the whole grid box. The ECMWF Integrated Forecast System represents snow as a single additional layer over the uppermost soil level. The snow may cover all or part of the grid box.  
`snowfall_sum` | m of water equivalent | Accumulated total snow that has fallen to the Earth's surface. It consists of snow due to the large-scale atmospheric flow (horizontal scales greater than around a few hundred meters) and convection where smaller scale areas (around 5km to a few hundred kilometers) of warm air rise. If snow has melted during the period over which this variable was accumulated, then it will be higher than the snow depth. This variable is the total amount of water accumulated from the beginning of the forecast time to the end of the forecast step. The units given measure the depth the water would have if the snow melted and was spread evenly over the grid box. Care should be taken when comparing model variables with observations, because observations are often local to a particular point in space and time, rather than representing averages over a model grid box and model time step.  
`snowmelt_sum` | m of water equivalent | Melting of snow averaged over the grid box (to find melt over snow, divide by snow fraction). This variable is accumulated from the beginning of the forecast time to the end of the forecast step.  
`temperature_of_snow_layer` | K | This variable gives the temperature of the snow layer from the ground to the snow-air interface. The ECMWF Integrated Forecast System (IFS) model represents snow as a single additional layer over the uppermost soil level. The snow may cover all or part of the grid box.  
`skin_reservoir_content` | m of water equivalent | Amount of water in the vegetation canopy and/or in a thin layer on the soil. It represents the amount of rain intercepted by foliage, and water from dew. The maximum amount of 'skin reservoir content' a grid box can hold depends on the type of vegetation, and may be zero. Water leaves the 'skin reservoir' by evaporation.  
`volumetric_soil_water_layer_1` | Volume fraction | Volume of water in soil layer 1 (0 - 7 cm) of the ECMWF Integrated Forecasting System. The surface is at 0 cm. The volumetric soil water is associated with the soil texture (or classification), soil depth, and the underlying groundwater level.  
`volumetric_soil_water_layer_2` | Volume fraction | Volume of water in soil layer 2 (7 -28 cm) of the ECMWF Integrated Forecasting System.  
`volumetric_soil_water_layer_3` | Volume fraction | Volume of water in soil layer 3 (28-100 cm) of the ECMWF Integrated Forecasting System.  
`volumetric_soil_water_layer_4` | Volume fraction | Volume of water in soil layer 4 (100-289 cm) of the ECMWF Integrated Forecasting System.  
`forecast_albedo` | Is a measure of the reflectivity of the Earth's surface. It is the fraction of solar (shortwave) radiation reflected by Earth's surface, across the solar spectrum, for both direct and diffuse radiation. Values are between 0 and 1. Typically, snow and ice have high reflectivity with albedo values of 0.8 and above, land has intermediate values between about 0.1 and 0.4 and the ocean has low values of 0.1 or less. Radiation from the Sun (solar, or shortwave, radiation) is partly reflected back to space by clouds and particles in the atmosphere (aerosols) and some of it is absorbed. The rest is incident on the Earth's surface, where some of it is reflected. The portion that is reflected by the Earth's surface depends on the albedo. In the ECMWF Integrated Forecasting System (IFS), a climatological background albedo (observed values averaged over a period of several years) is used, modified by the model over water, ice and snow. Albedo is often shown as a percentage (%).  
`surface_latent_heat_flux_sum` | J/m^2 | Exchange of latent heat with the surface through turbulent diffusion. This variables is accumulated from the beginning of the forecast time to the end of the forecast step. By model convention, downward fluxes are positive.  
`surface_net_solar_radiation_sum` | J/m^2 | Amount of solar radiation (also known as shortwave radiation) reaching the surface of the Earth (both direct and diffuse) minus the amount reflected by the Earth's surface (which is governed by the albedo). Radiation from the Sun (solar, or shortwave, radiation) is partly reflected back to space by clouds and particles in the atmosphere (aerosols) and some of it is absorbed. The rest is incident on the Earth's surface, where some of it is reflected. The difference between downward and reflected solar radiation is the surface net solar radiation. This variable is accumulated from the beginning of the forecast time to the end of the forecast step. The units are joules per square meter (J m-2). To convert to watts per square meter (W m-2), the accumulated values should be divided by the accumulation period expressed in seconds. The ECMWF convention for vertical fluxes is positive downwards.  
`surface_net_thermal_radiation_sum` | J/m^2 | Net thermal radiation at the surface. Accumulated field from the beginning of the forecast time to the end of the forecast step. By model convention downward fluxes are positive.  
`surface_sensible_heat_flux_sum` | J/m^2 | Transfer of heat between the Earth's surface and the atmosphere through the effects of turbulent air motion (but excluding any heat transfer resulting from condensation or evaporation). The magnitude of the sensible heat flux is governed by the difference in temperature between the surface and the overlying atmosphere, wind speed and the surface roughness. For example, cold air overlying a warm surface would produce a sensible heat flux from the land (or ocean) into the atmosphere. This is a single level variable and it is accumulated from the beginning of the forecast time to the end of the forecast step. The units are joules per square meter (J m-2). To convert to watts per square meter (W m-2), the accumulated values should be divided by the accumulation period expressed in seconds. The ECMWF convention for vertical fluxes is positive downwards.  
`surface_solar_radiation_downwards_sum` | J/m^2 | Amount of solar radiation (also known as shortwave radiation) reaching the surface of the Earth. This variable comprises both direct and diffuse solar radiation. Radiation from the Sun (solar, or shortwave, radiation) is partly reflected back to space by clouds and particles in the atmosphere (aerosols) and some of it is absorbed. The rest is incident on the Earth's surface (represented by this variable). To a reasonably good approximation, this variable is the model equivalent of what would be measured by a pyranometer (an instrument used for measuring solar radiation) at the surface. However, care should be taken when comparing model variables with observations, because observations are often local to a particular point in space and time, rather than representing averages over a model grid box and model time step. This variable is accumulated from the beginning of the forecast time to the end of the forecast step. The units are joules per square meter (J m-2). To convert to watts per square meter (W m-2), the accumulated values should be divided by the accumulation period expressed in seconds. The ECMWF convention for vertical fluxes is positive downwards.  
`surface_thermal_radiation_downwards_sum` | J/m^2 | Amount of thermal (also known as longwave or terrestrial) radiation emitted by the atmosphere and clouds that reaches the Earth's surface. The surface of the Earth emits thermal radiation, some of which is absorbed by the atmosphere and clouds. The atmosphere and clouds likewise emit thermal radiation in all directions, some of which reaches the surface (represented by this variable). This variable is accumulated from the beginning of the forecast time to the end of the forecast step. The units are joules per square meter (J m-2). To convert to watts per square meter (W m-2), the accumulated values should be divided by the accumulation period expressed in seconds. The ECMWF convention for vertical fluxes is positive downwards.  
`evaporation_from_bare_soil_sum` | m of water equivalent | The amount of evaporation from bare soil at the top of the land surface. This variable is accumulated from the beginning of the forecast time to the end of the forecast step. **Note:** Due to a known issue with ECMWF data, this band has values corresponding to the evaporation_from_vegetation_transpiration band. Users are encouraged to perform their own validation before using this band.  
`evaporation_from_open_water_surfaces_excluding_oceans_sum` | m of water equivalent | Amount of evaporation from surface water storage like lakes and inundated areas but excluding oceans. This variable is accumulated from the beginning of the forecast time to the end of the forecast step. **Note:** Due to a known issue with ECMWF data, this band has values corresponding to the evaporation_from_bare_soil band. Users are encouraged to perform their own validation before using this band.  
`evaporation_from_the_top_of_canopy_sum` | m of water equivalent | The amount of evaporation from the canopy interception reservoir at the top of the canopy. This variable is accumulated from the beginning of the forecast time to the end of the forecast step.  
`evaporation_from_vegetation_transpiration_sum` | m of water equivalent | Amount of evaporation from vegetation transpiration. This has the same meaning as root extraction i.e. the amount of water extracted from the different soil layers. This variable is accumulated from the beginning of the forecast time to the end of the forecast step. **Note:** Due to a known issue with ECMWF data, this band has values corresponding to the evaporation_from_open_water_surfaces_excluding_oceans band. Users are encouraged to perform their own validation before using this band.  
`potential_evaporation_sum` | m | Potential evaporation (pev) in the current ECMWF model is computed, by making a second call to the surface energy balance routine with the vegetation variables set to "crops/mixed farming" and assuming no stress from soil moisture. In other words, evaporation is computed for agricultural land as if it is well watered and assuming that the atmosphere is not affected by this artificial surface condition. The latter may not always be realistic. Although pev is meant to provide an estimate of irrigation requirements, the method can give unrealistic results in arid conditions due to too strong evaporation forced by dry air. This variable is accumulated from the beginning of the forecast time to the end of the forecast step.  
`runoff_sum` | m | Some water from rainfall, melting snow, or deep in the soil, stays stored in the soil. Otherwise, the water drains away, either over the surface (surface runoff), or under the ground (sub-surface runoff) and the sum of these two is simply called 'runoff'. This variable is the total amount of water accumulated from the beginning of the forecast time to the end of the forecast step. The units of runoff are depth in meters. This is the depth the water would have if it were spread evenly over the grid box. Care should be taken when comparing model variables with observations, because observations are often local to a particular point rather than averaged over a grid square area. Observations are also often taken in different units, such as mm/day, rather than the accumulated meters produced here. Runoff is a measure of the availability of water in the soil, and can, for example, be used as an indicator of drought or flood. More information about how runoff is calculated is given in the IFS Physical Processes documentation.  
`snow_evaporation_sum` | m of water equivalent | Evaporation from snow averaged over the grid box (to find flux over snow, divide by snow fraction). This variable is accumulated from the beginning of the forecast time to the end of the forecast step.  
`sub_surface_runoff_sum` | m | Some water from rainfall, melting snow, or deep in the soil, stays stored in the soil. Otherwise, the water drains away, either over the surface (surface runoff), or under the ground(sub-surface runoff) and the sum of these two is simply called 'runoff'. This variable is accumulated from the beginning of the forecast time to the end of the forecast step. The units of runoff are depth in meters. This is the depth the water would have if it were spread evenly over the grid box. Care should be taken when comparing model variables with observations, because observations are often local to a particular point rather than averaged over a grid square area. Observations are also often taken in different units, such as mm/day, rather than the accumulated meters produced here. Runoff is a measure of the availability of water in the soil, and can, for example, be used as an indicator of drought or flood. More information about how runoff is calculated is given in the IFS Physical Processes documentation.  
`surface_runoff_sum` | m | Some water from rainfall, melting snow, or deep in the soil, stays stored in the soil. Otherwise, the water drains away, either over the surface (surface runoff), or under the ground (sub-surface runoff) and the sum of these two is simply called 'runoff'. This variable is the total amount of water accumulated from the beginning of the forecast time to the end of the forecast step. The units of runoff are depth in meters. This is the depth the water would have if it were spread evenly over the grid box. Care should be taken when comparing model variables with observations, because observations are often local to a particular point rather than averaged over a grid square area. Observations are also often taken in different units, such as mm/day, rather than the accumulated meters produced here. Runoff is a measure of the availability of water in the soil, and can, for example, be used as an indicator of drought or flood. More information about how runoff is calculated is given in the IFS Physical Processes documentation.  
`total_evaporation_sum` | m of water equivalent | Accumulated amount of water that has evaporated from the Earth's surface, including a simplified representation of transpiration (from vegetation), into vapor in the air above. This variable is accumulated from the beginning of the forecast to the end of the forecast step. The ECMWF Integrated Forecasting System convention is that downward fluxes are positive. Therefore, negative values indicate evaporation and positive values indicate condensation.  
`u_component_of_wind_10m` | m/s | Eastward component of the 10m wind. It is the horizontal speed of air moving towards the east, at a height of ten meters above the surface of the Earth, in meters per second. Care should be taken when comparing this variable with observations, because wind observations vary on small space and time scales and are affected by the local terrain, vegetation and buildings that are represented only on average in the ECMWF Integrated Forecasting System. This variable can be combined with the V component of 10m wind to give the speed and direction of the horizontal 10m wind.  
`v_component_of_wind_10m` | m/s | Northward component of the 10m wind. It is the horizontal speed of air moving towards the north, at a height of ten meters above the surface of the Earth, in meters per second. Care should be taken when comparing this variable with observations, because wind observations vary on small space and time scales and are affected by the local terrain, vegetation and buildings that are represented only on average in the ECMWF Integrated Forecasting System. This variable can be combined with the U component of 10m wind to give the speed and direction of the horizontal 10m wind.  
`surface_pressure` | Pa | Pressure (force per unit area) of the atmosphere on the surface of land, sea and in-land water. It is a measure of the weight of all the air in a column vertically above the area of the Earth's surface represented at a fixed point. Surface pressure is often used in combination with temperature to calculate air density. The strong variation of pressure with altitude makes it difficult to see the low and high pressure systems over mountainous areas, so mean sea level pressure, rather than surface pressure, is normally used for this purpose. The units of this variable are Pascals (Pa). Surface pressure is often measured in hPa and sometimes is presented in the old units of millibars, mb (1 hPa = 1 mb = 100 Pa).  
`total_precipitation_sum` | m | Accumulated liquid and frozen water, including rain and snow, that falls to the Earth's surface. It is the sum of large-scale precipitation (that precipitation which is generated by large-scale weather patterns, such as troughs and cold fronts) and convective precipitation (generated by convection which occurs when air at lower levels in the atmosphere is warmer and less dense than the air above, so it rises). Precipitation variables do not include fog, dew or the precipitation that evaporates in the atmosphere before it lands at the surface of the Earth. This variable is accumulated from the beginning of the forecast time to the end of the forecast step. The units of precipitation are depth in meters. It is the depth the water would have if it were spread evenly over the grid box. Care should be taken when comparing model variables with observations, because observations are often local to a particular point in space and time, rather than representing averages over a model grid box and model time step.  
`leaf_area_index_high_vegetation` | Area fraction | One-half of the total green leaf area per unit horizontal ground surface area for high vegetation type.  
`leaf_area_index_low_vegetation` | Area fraction | One-half of the total green leaf area per unit horizontal ground surface area for low vegetation type.  
`dewpoint_temperature_2m_min` | K | daily minimum dewpoint_temperature_2m value  
`dewpoint_temperature_2m_max` | K | daily maximum dewpoint_temperature_2m value  
`temperature_2m_min` | K | daily minimum temperature_2m value  
`temperature_2m_max` | K | daily maximum temperature_2m value  
`skin_temperature_min` | K | daily minimum skin_temperature value  
`skin_temperature_max` | K | daily maximum skin_temperature value  
`soil_temperature_level_1_min` | K | daily minimum soil_temperature_level_1 value  
`soil_temperature_level_1_max` | K | daily maximum soil_temperature_level_1 value  
`soil_temperature_level_2_min` | K | daily minimum soil_temperature_level_2 value  
`soil_temperature_level_2_max` | K | daily maximum soil_temperature_level_2 value  
`soil_temperature_level_3_min` | K | daily minimum soil_temperature_level_3 value  
`soil_temperature_level_3_max` | K | daily maximum soil_temperature_level_3 value  
`soil_temperature_level_4_min` | K | daily minimum soil_temperature_level_4 value  
`soil_temperature_level_4_max` | K | daily maximum soil_temperature_level_4 value  
`lake_bottom_temperature_min` | K | daily minimum lake_bottom_temperature value  
`lake_bottom_temperature_max` | K | daily maximum lake_bottom_temperature value  
`lake_ice_depth_min` | m | daily minimum lake_ice_depth value  
`lake_ice_depth_max` | m | daily maximum lake_ice_depth value  
`lake_ice_temperature_min` | K | daily minimum lake_ice_temperature value  
`lake_ice_temperature_max` | K | daily maximum lake_ice_temperature value  
`lake_mix_layer_depth_min` | m | daily minimum lake_mix_layer_depth value  
`lake_mix_layer_depth_max` | m | daily maximum lake_mix_layer_depth value  
`lake_mix_layer_temperature_min` | K | daily minimum lake_mix_layer_temperature value  
`lake_mix_layer_temperature_max` | K | daily maximum lake_mix_layer_temperature value  
`lake_shape_factor_min` | daily minimum lake_shape_factor value  
`lake_shape_factor_max` | daily maximum lake_shape_factor value  
`lake_total_layer_temperature_min` | K | daily minimum lake_total_layer_temperature value  
`lake_total_layer_temperature_max` | K | daily maximum lake_total_layer_temperature value  
`snow_albedo_min` | daily minimum snow_albedo value  
`snow_albedo_max` | daily maximum snow_albedo value  
`snow_cover_min` | daily minimum snow_cover value  
`snow_cover_max` | daily maximum snow_cover value  
`snow_density_min` | kg/m^3 | daily minimum snow_density value  
`snow_density_max` | kg/m^3 | daily maximum snow_density value  
`snow_depth_min` | m | daily minimum snow_depth value  
`snow_depth_max` | m | daily maximum snow_depth value  
`snow_depth_water_equivalent_min` | m of water equivalent | daily minimum snow_depth_water_equivalent value  
`snow_depth_water_equivalent_max` | m of water equivalent | daily maximum snow_depth_water_equivalent value  
`snowfall_min` | m of water equivalent | daily minimum snowfall value  
`snowfall_max` | m of water equivalent | daily maximum snowfall value  
`snowmelt_min` | m of water equivalent | daily minimum snowmelt value  
`snowmelt_max` | m of water equivalent | daily maximum snowmelt value  
`temperature_of_snow_layer_min` | K | daily minimum temperature_of_snow_layer value  
`temperature_of_snow_layer_max` | K | daily maximum temperature_of_snow_layer value  
`skin_reservoir_content_min` | m of water equivalent | daily minimum skin_reservoir_content value  
`skin_reservoir_content_max` | m of water equivalent | daily maximum skin_reservoir_content value  
`volumetric_soil_water_layer_1_min` | Volume fraction | daily minimum volumetric_soil_water_layer_1 value  
`volumetric_soil_water_layer_1_max` | Volume fraction | daily maximum volumetric_soil_water_layer_1 value  
`volumetric_soil_water_layer_2_min` | Volume fraction | daily minimum volumetric_soil_water_layer_2 value  
`volumetric_soil_water_layer_2_max` | Volume fraction | daily maximum volumetric_soil_water_layer_2 value  
`volumetric_soil_water_layer_3_min` | Volume fraction | daily minimum volumetric_soil_water_layer_3 value  
`volumetric_soil_water_layer_3_max` | Volume fraction | daily maximum volumetric_soil_water_layer_3 value  
`volumetric_soil_water_layer_4_min` | Volume fraction | daily minimum volumetric_soil_water_layer_4 value  
`volumetric_soil_water_layer_4_max` | Volume fraction | daily maximum volumetric_soil_water_layer_4 value  
`forecast_albedo_min` | daily minimum forecast_albedo value  
`forecast_albedo_max` | daily maximum forecast_albedo value  
`surface_latent_heat_flux_min` | J/m^2 | daily minimum surface_latent_heat_flux value  
`surface_latent_heat_flux_max` | J/m^2 | daily maximum surface_latent_heat_flux value  
`surface_net_solar_radiation_min` | J/m^2 | daily minimum surface_net_solar_radiation value  
`surface_net_solar_radiation_max` | J/m^2 | daily maximum surface_net_solar_radiation value  
`surface_net_thermal_radiation_min` | J/m^2 | daily minimum surface_net_thermal_radiation value  
`surface_net_thermal_radiation_max` | J/m^2 | daily maximum surface_net_thermal_radiation value  
`surface_sensible_heat_flux_min` | J/m^2 | daily minimum surface_sensible_heat_flux value  
`surface_sensible_heat_flux_max` | J/m^2 | daily maximum surface_sensible_heat_flux value  
`surface_solar_radiation_downwards_min` | J/m^2 | daily minimum surface_solar_radiation_downwards value  
`surface_solar_radiation_downwards_max` | J/m^2 | daily maximum surface_solar_radiation_downwards value  
`surface_thermal_radiation_downwards_min` | J/m^2 | daily minimum surface_thermal_radiation_downwards value  
`surface_thermal_radiation_downwards_max` | J/m^2 | daily maximum surface_thermal_radiation_downwards value  
`evaporation_from_bare_soil_min` | m of water equivalent | daily minimum evaporation_from_bare_soil value  
`evaporation_from_bare_soil_max` | m of water equivalent | daily maximum evaporation_from_bare_soil value  
`evaporation_from_open_water_surfaces_excluding_oceans_min` | m of water equivalent | daily minimum evaporation_from_open_water_surfaces_excluding_oceans value  
`evaporation_from_open_water_surfaces_excluding_oceans_max` | m of water equivalent | daily maximum evaporation_from_open_water_surfaces_excluding_oceans value  
`evaporation_from_the_top_of_canopy_min` | m of water equivalent | daily minimum evaporation_from_the_top_of_canopy value  
`evaporation_from_the_top_of_canopy_max` | m of water equivalent | daily maximum evaporation_from_the_top_of_canopy value  
`evaporation_from_vegetation_transpiration_min` | m of water equivalent | daily minimum evaporation_from_vegetation_transpiration value  
`evaporation_from_vegetation_transpiration_max` | m of water equivalent | daily maximum evaporation_from_vegetation_transpiration value  
`potential_evaporation_min` | m | daily minimum potential_evaporation value  
`potential_evaporation_max` | m | daily maximum potential_evaporation value  
`runoff_min` | m | daily minimum runoff value  
`runoff_max` | m | daily maximum runoff value  
`snow_evaporation_min` | m of water equivalent | daily minimum snow_evaporation value  
`snow_evaporation_max` | m of water equivalent | daily maximum snow_evaporation value  
`sub_surface_runoff_min` | m | daily minimum sub_surface_runoff value  
`sub_surface_runoff_max` | m | daily maximum sub_surface_runoff value  
`surface_runoff_min` | m | daily minimum surface_runoff value  
`surface_runoff_max` | m | daily maximum surface_runoff value  
`total_evaporation_min` | m of water equivalent | daily minimum total_evaporation value  
`total_evaporation_max` | m of water equivalent | daily maximum total_evaporation value  
`u_component_of_wind_10m_min` | m/s | daily minimum u_component_of_wind_10m value  
`u_component_of_wind_10m_max` | m/s | daily maximum u_component_of_wind_10m value  
`v_component_of_wind_10m_min` | m/s | daily minimum v_component_of_wind_10m value  
`v_component_of_wind_10m_max` | m/s | daily maximum v_component_of_wind_10m value  
`surface_pressure_min` | Pa | daily minimum surface_pressure value  
`surface_pressure_max` | Pa | daily maximum surface_pressure value  
`total_precipitation_min` | m | daily minimum total_precipitation value  
`total_precipitation_max` | m | daily maximum total_precipitation value  
`leaf_area_index_high_vegetation_min` | Area fraction | daily minimum leaf_area_index_high_vegetation value  
`leaf_area_index_high_vegetation_max` | Area fraction | daily maximum leaf_area_index_high_vegetation value  
`leaf_area_index_low_vegetation_min` | Area fraction | daily minimum leaf_area_index_low_vegetation value  
`leaf_area_index_low_vegetation_max` | Area fraction | daily maximum leaf_area_index_low_vegetation value  
**Image Properties**
Name | Type | Description  
---|---|---  
day | INT | Calendar day  
month | INT | Calendar month  
year | INT | Calendar year  
**Terms of Use**
Please acknowledge the use of ERA5-Land as stated in the [Copernicus C3S/CAMS License agreement](https://apps.ecmwf.int/datasets/licences/copernicus/):
  * 5.1.1 Where the Licensee communicates or distributes Copernicus Products to the public, the Licensee shall inform the recipients of the source by using the following or any similar notice: 'Generated using Copernicus Climate Change Service Information [Year]'.
  * 5.1.2 Where the Licensee makes or contributes to a publication or distribution containing adapted or modified Copernicus Products, the Licensee shall provide the following or any similar notice: 'Contains modified Copernicus Climate Change Service Information [Year]';


Any such publication or distribution covered by clauses 5.1.1 and 5.1.2 shall state that neither the European Commission nor ECMWF is responsible for any use that may be made of the Copernicus Information or Data it contains.
Citations:
  * Muñoz Sabater, J., (2019): ERA5-Land monthly averaged data from 1981 to present. Copernicus Climate Change Service (C3S) Climate Data Store (CDS). (<date of access>), [doi:10.24381/cds.68d2bb30](https://doi.org/10.24381/cds.68d2bb30)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/ECMWF_ERA5_LAND_DAILY_AGGR#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('ECMWF/ERA5_LAND/DAILY_AGGR').first();
varvisualization={
bands:['temperature_2m'],
min:250,
max:320,
palette:[
'000080','0000d9','4000ff','8000ff','0080ff','00ffff',
'00ff80','80ff00','daff00','ffff00','fff500','ffda00',
'ffb000','ffa400','ff4f00','ff2500','ff0a00','ff00ff',
]
};
Map.setCenter(70,45,3);
Map.addLayer(
dataset,visualization,'Air temperature (K) at 2m height',true,0.8);
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/ECMWF/ECMWF_ERA5_LAND_DAILY_AGGR)
[ ERA5-Land Daily Aggregated - ECMWF Climate Reanalysis ](https://developers.google.com/earth-engine/datasets/catalog/ECMWF_ERA5_LAND_DAILY_AGGR)
ERA5-Land is a reanalysis dataset providing a consistent view of the evolution of land variables over several decades at an enhanced resolution compared to ERA5. ERA5-Land has been produced by replaying the land component of the ECMWF ERA5 climate reanalysis. Reanalysis combines model data with observations from across the world …
ECMWF/ERA5_LAND/DAILY_AGGR, cds,climate,copernicus,ecmwf,era5-land,evaporation,heat,lakes,precipitation,pressure,radiation,reanalysis,runoff,snow,soil-water,temperature,vegetation,wind 
1950-01-02T00:00:00Z/2025-04-15T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://cds.climate.copernicus.eu/cdsapp)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/ECMWF_ERA5_LAND_DAILY_AGGR)


