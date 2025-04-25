 
#  WeatherNext Graph Forecasts 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![projects/gcp-public-data-weathernext/assets/59572747_4_0](https://developers.google.com/earth-engine/datasets/images/gcp-public-data-weathernext/projects_gcp-public-data-weathernext_assets_59572747_4_0_sample.png)
info
This dataset is part of a Publisher Catalog, and not managed by Google Earth Engine. Contact weathernext@google.com for bugs or [view more datasets](https://developers.google.com/earth-engine/datasets/publisher/gcp-public-data-weathernext) from the WeatherNext Catalog. [Learn more about Publisher datasets](https://developers.google.com/earth-engine/datasets/publisher). 
[ ![Catalog Owner Logo](https://developers.google.com/static/earth-engine/datasets/logos/gcp-public-data-weathernext_logo.png) ](https://deepmind.google/discover/blog/graphcast-ai-model-for-faster-and-more-accurate-global-weather-forecasting/) 

Catalog Owner
    WeatherNext 

Dataset Availability
    2020-01-01T00:00:00Z–2025-04-22T06:00:00Z 

Dataset Provider
     [ Google ](https://deepmind.google/discover/blog/graphcast-ai-model-for-faster-and-more-accurate-global-weather-forecasting/) 

Earth Engine Snippet
     `    ee.ImageCollection("projects/gcp-public-data-weathernext/assets/59572747_4_0")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/gcp-public-data-weathernext/projects_gcp-public-data-weathernext_assets_59572747_4_0) 

Tags
     [climate](https://developers.google.com/earth-engine/datasets/tags/climate) [forecast](https://developers.google.com/earth-engine/datasets/tags/forecast) [gcp-public-data-weathernext](https://developers.google.com/earth-engine/datasets/tags/gcp-public-data-weathernext) [precipitation](https://developers.google.com/earth-engine/datasets/tags/precipitation) [publisher-dataset](https://developers.google.com/earth-engine/datasets/tags/publisher-dataset) [temperature](https://developers.google.com/earth-engine/datasets/tags/temperature) [weather](https://developers.google.com/earth-engine/datasets/tags/weather) [weathernext](https://developers.google.com/earth-engine/datasets/tags/weathernext) [wind](https://developers.google.com/earth-engine/datasets/tags/wind)
graphcast
[Description](https://developers.google.com/earth-engine/datasets/catalog/projects_gcp-public-data-weathernext_assets_59572747_4_0#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/projects_gcp-public-data-weathernext_assets_59572747_4_0#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/projects_gcp-public-data-weathernext_assets_59572747_4_0#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/projects_gcp-public-data-weathernext_assets_59572747_4_0#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/projects_gcp-public-data-weathernext_assets_59572747_4_0#citations) More
WeatherNext Graph is an experimental dataset of global medium-range weather forecasts produced by an operational version of Google DeepMind's [graphical neural network weather model](https://www.science.org/stoken/author-tokens/ST-1550/full).
The experimental dataset includes real-time and historic data. Real-time data is any data that relates to a time that is no more than 48 hours in the past ("Real-Time Experimental Data"), while historic data is any data that relates to a time that is more than 48 hours ago ("Historic Experimental Data"). This dataset includes major surface fields including temperature, wind, precipitation, humidity, geopotential, vertical velocity, and pressure. The spatial resolution is 0.25 degrees. Forecast init times have 6 hour resolution (00z, 06z, 12z, 18z). Forecast lead times have 6 hour resolution up to a max lead time of 10 days.
If you are interested in accessing the experimental dataset, please fill out this [WeatherNext Data Request form](https://docs.google.com/forms/d/e/1FAIpQLSeCf1JY8G78UDWzbm0ly9kJxfSjUIJT5WyMR_HiNqCm-IHIBg/viewform).
More information on the model is in "[Learning skillful medium-range global weather forecasting](https://www.science.org/stoken/author-tokens/ST-1550/full)". The model used to produce this experimental dataset is an operational version derived from that research model (formerly known as GraphCast). Please note that the accuracy of this operational model may not directly correspond to the accuracy reported for the research model, and that additional variables may be included in this forecast dataset.
If you have any questions on using this experimental dataset, or would like to use it for purposes not currently permitted under the terms of use set out below, please contact weathernext@google.com.
**Accessing Raw Data (.zarr)**
A bucket containing the raw .zarr files for the historical dataset ("Historic Experimental Data") is available at `gs://weathernext/59572747_4_0/zarr`. To gain access to the bucket, please request access through the same [WeatherNext Data Request form](https://docs.google.com/forms/d/e/1FAIpQLSeCf1JY8G78UDWzbm0ly9kJxfSjUIJT5WyMR_HiNqCm-IHIBg/viewform?usp=preview), and note your interest in receiving access to the raw .zarr files.
**Acknowledgements**
The experimental data was generated by models which communicate with and/or reference the following separate libraries and packages:
  * Data and products of the European Centre for Medium-range Weather Forecasts (ECMWF), as modified by Google.
  * Modified Copernicus Climate Change Service information 2023. Neither the European Commission nor ECMWF is responsible for any use that may be made of the Copernicus information or data it contains.
  * ECMWF HRES datasets 
    * Copyright statement: Copyright "© 2023 European Centre for Medium-Range Weather Forecasts (ECMWF)".
    * Source: [www.ecmwf.int](http://www.ecmwf.int)
    * License Statement: ECMWF open data is published under a Creative Commons Attribution 4.0 International (CC BY 4.0). <https://creativecommons.org/licenses/by/4.0/>
    * Disclaimer: ECMWF does not accept any liability whatsoever for any error or omission in the data, their availability, or for any loss or damage arising from their use.


**Pixel Size** 27750 meters 
**Bands**
Name | Units | Description  
---|---|---  
`total_precipitation_6hr` | m | Total precipitation over a 6-hour period  
`10m_u_component_of_wind` | m/s | 10 meter U wind component  
`10m_v_component_of_wind` | m/s | 10 meter V wind component  
`2m_temperature` | K | 2 meter temperature  
`mean_sea_level_pressure` | Pa | Mean sea level pressure  
`50_geopotential` | m^2/s^2 | Geopotential at 50 hPa  
`100_geopotential` | m^2/s^2 | Geopotential at 100 hPa  
`150_geopotential` | m^2/s^2 | Geopotential at 150 hPa  
`200_geopotential` | m^2/s^2 | Geopotential at 200 hPa  
`250_geopotential` | m^2/s^2 | Geopotential at 250 hPa  
`300_geopotential` | m^2/s^2 | Geopotential at 300 hPa  
`400_geopotential` | m^2/s^2 | Geopotential at 400 hPa  
`500_geopotential` | m^2/s^2 | Geopotential at 500 hPa  
`600_geopotential` | m^2/s^2 | Geopotential at 600 hPa  
`700_geopotential` | m^2/s^2 | Geopotential at 700 hPa  
`850_geopotential` | m^2/s^2 | Geopotential at 850 hPa  
`925_geopotential` | m^2/s^2 | Geopotential at 925 hPa  
`1000_geopotential` | m^2/s^2 | Geopotential at 1000 hPa  
`50_specific_humidity` | kg/kg | Specific humidity at 50 hPa  
`100_specific_humidity` | kg/kg | Specific humidity at 100 hPa  
`150_specific_humidity` | kg/kg | Specific humidity at 150 hPa  
`200_specific_humidity` | kg/kg | Specific humidity at 200 hPa  
`250_specific_humidity` | kg/kg | Specific humidity at 250 hPa  
`300_specific_humidity` | kg/kg | Specific humidity at 300 hPa  
`400_specific_humidity` | kg/kg | Specific humidity at 400 hPa  
`500_specific_humidity` | kg/kg | Specific humidity at 500 hPa  
`600_specific_humidity` | kg/kg | Specific humidity at 600 hPa  
`700_specific_humidity` | kg/kg | Specific humidity at 700 hPa  
`850_specific_humidity` | kg/kg | Specific humidity at 850 hPa  
`925_specific_humidity` | kg/kg | Specific humidity at 925 hPa  
`1000_specific_humidity` | kg/kg | Specific humidity at 1000 hPa  
`50_temperature` | K | Temperature at 50 hPa  
`100_temperature` | K | Temperature at 100 hPa  
`150_temperature` | K | Temperature at 150 hPa  
`200_temperature` | K | Temperature at 200 hPa  
`250_temperature` | K | Temperature at 250 hPa  
`300_temperature` | K | Temperature at 300 hPa  
`400_temperature` | K | Temperature at 400 hPa  
`500_temperature` | K | Temperature at 500 hPa  
`600_temperature` | K | Temperature at 600 hPa  
`700_temperature` | K | Temperature at 700 hPa  
`850_temperature` | K | Temperature at 850 hPa  
`925_temperature` | K | Temperature at 925 hPa  
`1000_temperature` | K | Temperature at 1000 hPa  
`50_u_component_of_wind` | m/s | U wind component at 50 hPa  
`100_u_component_of_wind` | m/s | U wind component at 100 hPa  
`150_u_component_of_wind` | m/s | U wind component at 150 hPa  
`200_u_component_of_wind` | m/s | U wind component at 200 hPa  
`250_u_component_of_wind` | m/s | U wind component at 250 hPa  
`300_u_component_of_wind` | m/s | U wind component at 300 hPa  
`400_u_component_of_wind` | m/s | U wind component at 400 hPa  
`500_u_component_of_wind` | m/s | U wind component at 500 hPa  
`600_u_component_of_wind` | m/s | U wind component at 600 hPa  
`700_u_component_of_wind` | m/s | U wind component at 700 hPa  
`850_u_component_of_wind` | m/s | U wind component at 850 hPa  
`925_u_component_of_wind` | m/s | U wind component at 925 hPa  
`1000_u_component_of_wind` | m/s | U wind component at 1000 hPa  
`50_v_component_of_wind` | m/s | V wind component at 50 hPa  
`100_v_component_of_wind` | m/s | V wind component at 100 hPa  
`150_v_component_of_wind` | m/s | V wind component at 150 hPa  
`200_v_component_of_wind` | m/s | V wind component at 200 hPa  
`250_v_component_of_wind` | m/s | V wind component at 250 hPa  
`300_v_component_of_wind` | m/s | V wind component at 300 hPa  
`400_v_component_of_wind` | m/s | V wind component at 400 hPa  
`500_v_component_of_wind` | m/s | V wind component at 500 hPa  
`600_v_component_of_wind` | m/s | V wind component at 600 hPa  
`700_v_component_of_wind` | m/s | V wind component at 700 hPa  
`850_v_component_of_wind` | m/s | V wind component at 850 hPa  
`925_v_component_of_wind` | m/s | V wind component at 925 hPa  
`1000_v_component_of_wind` | m/s | V wind component at 1000 hPa  
`50_vertical_velocity` | Pa/s | Vertical velocity at 50 hPa  
`100_vertical_velocity` | Pa/s | Vertical velocity at 100 hPa  
`150_vertical_velocity` | Pa/s | Vertical velocity at 150 hPa  
`200_vertical_velocity` | Pa/s | Vertical velocity at 200 hPa  
`250_vertical_velocity` | Pa/s | Vertical velocity at 250 hPa  
`300_vertical_velocity` | Pa/s | Vertical velocity at 300 hPa  
`400_vertical_velocity` | Pa/s | Vertical velocity at 400 hPa  
`500_vertical_velocity` | Pa/s | Vertical velocity at 500 hPa  
`600_vertical_velocity` | Pa/s | Vertical velocity at 600 hPa  
`700_vertical_velocity` | Pa/s | Vertical velocity at 700 hPa  
`850_vertical_velocity` | Pa/s | Vertical velocity at 850 hPa  
`925_vertical_velocity` | Pa/s | Vertical velocity at 925 hPa  
`1000_vertical_velocity` | Pa/s | Vertical velocity at 1000 hPa  
**Image Properties**
Name | Type | Description  
---|---|---  
start_time | STRING | The initialization time of the forecast. This is the same for all forecast hours within a single model run.  
end_time | STRING | The valid time for this specific forecast. Calculated as start_time + forecast_hour.  
forecast_hour | INT | The forecast lead time in hours. Represents the number of hours from the start_time.  
ingestion_time | DOUBLE | The time when this forecast data became available in Earth Engine.  
**Terms of Use**
The Historic Experimental Data is licensed under the Creative Commons Attribution International License, Version 4.0 (CC BY 4.0).
The Real-Time Experimental Data is made available under the following GDM Real-Time Weather Forecasting Experimental Data [Terms of Use](https://storage.googleapis.com/weathernext-public/terms-of-use.pdf).
**Third-party materials**
Use of the third-party materials referred to in the Acknowledgements section may be governed by separate terms and conditions or license provisions. Your use of the third-party materials is subject to any such terms and you should check that you can comply with any applicable restrictions or terms and conditions before use.
Citations:
  * For Real-Time Experimental Data, please see the applicable Terms of Use for citation requirements.
If you disclose findings arising from the Historical Data, you must cite "© 2024 DeepMind Technologies Limited's machine learning models used to create the experimental data made available at <https://developers.google.com/earth-engine/datasets/catalog/projects_gcp-public-data-weathernext_assets_59572747_4_0> under CC BY 4.0 licence terms. This data is intended for experimental modelling only and is not intended, validated, or approved for real world use."


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/projects_gcp-public-data-weathernext_assets_59572747_4_0#code-editor-javascript-sample) More
```
vardataset=
ee.ImageCollection(
'projects/gcp-public-data-weathernext/assets/59572747_4_0')
.filter(ee.Filter.date('2020-10-01T06:00:00Z','2020-10-01T06:01:00Z'))
.filter(ee.Filter.eq('forecast_hour',6));
vartemperature=dataset.select('2m_temperature');
varvisParams={
min:220,
max:350,
palette:[
'darkblue','blue','cyan','green','yellow','orange','red','darkred'
]
};
Map.addLayer(temperature,visParams,'2m Temperature');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/gcp-public-data-weathernext/projects_gcp-public-data-weathernext_assets_59572747_4_0)
[ WeatherNext Graph Forecasts ](https://developers.google.com/earth-engine/datasets/catalog/projects_gcp-public-data-weathernext_assets_59572747_4_0)
WeatherNext Graph is an experimental dataset of global medium-range weather forecasts produced by an operational version of Google DeepMind's graphical neural network weather model. The experimental dataset includes real-time and historic data. Real-time data is any data that relates to a time that is no more than 48 hours in …
projects/gcp-public-data-weathernext/assets/59572747_4_0, climate,forecast,gcp-public-data-weathernext,precipitation,publisher-dataset,temperature,weather,weathernext,wind 
2020-01-01T00:00:00Z/2025-04-22T06:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://deepmind.google/discover/blog/graphcast-ai-model-for-faster-and-more-accurate-global-weather-forecasting/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/projects_gcp-public-data-weathernext_assets_59572747_4_0)


