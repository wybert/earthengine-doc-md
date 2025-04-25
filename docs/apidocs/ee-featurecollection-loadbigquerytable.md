 
#  ee.FeatureCollection.loadBigQueryTable 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-loadbigquerytable#examples)


Reads data from a BigQuery table and presents the results as a FeatureCollection. 
Usage| Returns  
---|---  
`ee.FeatureCollection.loadBigQueryTable(table,  _geometryColumn_)`| FeatureCollection  
Argument| Type| Details  
---|---|---  
`table`| String| Path to BigQuery table in a `project.dataset.table` format.  
`geometryColumn`| String, default: null| The name of the column to use as the main feature geometry. If not specified, all features will have null geometry.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-loadbigquerytable#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-loadbigquerytable#colab-python-sample) More
```
// Load stations from the New York Subway System.
varfeatures=ee.FeatureCollection.loadBigQueryTable({
table:'bigquery-public-data.new_york_subway.stations',
geometryColumn:'station_geom',
});
// Display all relevant features on the map.
Map.setCenter(-73.90,40.73,11);
Map.addLayer(features,
{'color':'black'},
'Stations from New York Subway System');
// Print all stations in the "Astoria" line.
varline=features.filter(ee.Filter.eq('line','Astoria'));
print(line);
Map.addLayer(line,
{'color':'yellow'},
'Astoria line');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Load stations from the New York Subway System.
features = ee.FeatureCollection.loadBigQueryTable(
  table="bigquery-public-data.new_york_subway.stations",
  geometryColumn="station_geom")
# Display all relevant features on the map.
m = geemap.Map()
m.set_center(-73.90, 40.73, 11)
m.add_layer(
  features, {'color': 'black'}, 'Stations from New York Subway System')
# Print all stations in the "Astoria" line.
line = features.filter(ee.Filter.eq('line', 'Astoria'))
display(line)
m.add_layer(line, {'color': 'yellow'}, 'Astoria line')
m
```

Was this helpful?
