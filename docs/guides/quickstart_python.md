 
#  Get started with Earth Engine for Python 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Before you begin](https://developers.google.com/earth-engine/guides/quickstart_python#before_you_begin)
  * [Notebook setup](https://developers.google.com/earth-engine/guides/quickstart_python#notebook_setup)
  * [Add raster data to a map](https://developers.google.com/earth-engine/guides/quickstart_python#add_raster_data_to_a_map)
  * [Add vector data to a map](https://developers.google.com/earth-engine/guides/quickstart_python#add_vector_data_to_a_map)
  * [Extract and chart data](https://developers.google.com/earth-engine/guides/quickstart_python#extract_and_chart_data)
  * [What's next](https://developers.google.com/earth-engine/guides/quickstart_python#whats_next)


[ ![Colab logo](https://developers.google.com/static/earth-engine/images/colab_logo_32px.png) Run in Google Colab ](https://colab.research.google.com/github/google/earthengine-community/blob/master/guides/linked/generated/quickstart_python.ipynb) |  [ ![GitHub logo](https://developers.google.com/static/earth-engine/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/earthengine-community/blob/master/guides/linked/generated/quickstart_python.ipynb)  
---|---  
This quickstart will give you an interactive introduction to visualizing and analyzing geospatial data with the Earth Engine Python interface.
## Before you begin
[Register or create](https://console.cloud.google.com/earth-engine) a Google Cloud Project; you'll be prompted to complete the following steps. If you already have a project registered for Earth Engine access, skip to the next section. 
  * Select the project's purpose: commercial or noncommercial.
  * If the purpose is noncommercial, select a project type.
  * Create a new Google Cloud project or select an existing project.
  * If the purpose is commercial, verify or set up billing for your project.
  * Confirm your project information. 
**Note:** If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can [delete the project](https://cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects), removing all resources owned by the project. 


## Notebook setup
Jupyter notebooks allow you to use Earth Engine and explore results interactively. The quickest way to get started is with a notebook in Google Colab notebook. You can either [**open a new notebook**](https://colab.new/) and copy the following code chunks into individual cells or use the prefilled [**Earth Engine Python Quickstart notebook**](https://colab.sandbox.google.com/github/google/earthengine-community/blob/master/guides/linked/generated/quickstart_python.ipynb). 
  1. Import the Earth Engine and geemap libraries. ```
importee
importgeemap.coreasgeemap
```



  1. Authenticate and initialize the Earth Engine service. Follow the resulting prompts to complete authentication. Be sure to replace PROJECT_ID with the name of the project you set up for this quickstart. ```
ee.Authenticate()
ee.Initialize(project='PROJECT_ID')
```



## Add raster data to a map
  1. Load climate data for a given period and display its metadata. ```
jan_2023_climate = (
  ee.ImageCollection('ECMWF/ERA5_LAND/MONTHLY_AGGR')
  .filterDate('2023-01', '2023-02')
  .first()
)
jan_2023_climate
```



  1. Instantiate a map object and add the temperature band as a layer with specific visualization properties. Display the map. ```
m = geemap.Map(center=[30, 0], zoom=2)
vis_params = {
  'bands': ['temperature_2m'],
  'min': 229,
  'max': 304,
  'palette': 'inferno',
}
m.add_layer(jan_2023_climate, vis_params, 'Temperature (K)')
m
```



## Add vector data to a map
  1. Create a vector data object with points for three cities. ```
cities = ee.FeatureCollection([
  ee.Feature(ee.Geometry.Point(10.75, 59.91), {'city': 'Oslo'}),
  ee.Feature(ee.Geometry.Point(-118.24, 34.05), {'city': 'Los Angeles'}),
  ee.Feature(ee.Geometry.Point(103.83, 1.33), {'city': 'Singapore'}),
])
cities
```



  1. Add the city locations to the map and redisplay it. ```
m.add_layer(cities, name='Cities')
m
```



## Extract and chart data
  1. Import the Altair charting library. ```
%pip install -q --upgrade altair
importaltairasalt
```



  1. Extract the climate data for the three cities as a pandas DataFrame. ```
city_climates = jan_2023_climate.reduceRegions(cities, ee.Reducer.first())
city_climates_dataframe = ee.data.computeFeatures(
  {'expression': city_climates, 'fileFormat': 'PANDAS_DATAFRAME'}
)
city_climates_dataframe
```



  1. Plot the temperature for the cities as a bar chart. ```
alt.Chart(city_climates_dataframe).mark_bar(size=100).encode(
  alt.X('city:N', sort='y', axis=alt.Axis(labelAngle=0), title='City'),
  alt.Y('temperature_2m:Q', title='Temperature (K)'),
  tooltip=[
    alt.Tooltip('city:N', title='City'),
    alt.Tooltip('temperature_2m:Q', title='Temperature (K)'),
  ],
).properties(title='January 2023 temperature for selected cities', width=500)
```



## What's next
  * Learn about analyzing data with Earth Engine's [objects and methods](https://developers.google.com/earth-engine/guides/objects_methods_overview).
  * Learn about Earth Engine's [processing environments](https://developers.google.com/earth-engine/guides/processing_environments).
  * Learn about Earth Engine's [machine learning capabilities](https://developers.google.com/earth-engine/guides/machine-learning).
  * Learn how to [export your computation results to BigQuery](https://developers.google.com/earth-engine/guides/exporting_to_bigquery).


