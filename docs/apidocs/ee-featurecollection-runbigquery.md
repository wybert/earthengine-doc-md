 
#  ee.FeatureCollection.runBigQuery
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Release Notes 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-runbigquery#examples)


Runs a BigQuery query, fetches the results and presents the them as a FeatureCollection.
Usage | Returns  
---|---  
`ee.FeatureCollection.runBigQuery(query, _geometryColumn_, _maxBytesBilled_)`|  FeatureCollection  
Argument | Type | Details  
---|---|---  
`query` | String | GoogleSQL query to perform on the BigQuery resources.  
`geometryColumn` | String, default: null | The name of the column to use as the main feature geometry. If not specified, the first geometry column will be used.  
`maxBytesBilled` | Long, default: 100000000000 | Maximum number of bytes billed while processing the query. Any BigQuery job that exceeds this limit will fail and won't be billed.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-runbigquery#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-runbigquery#colab-python-sample) More
```
// Get places from Overture Maps Dataset in BigQuery public data.
Map.setCenter(-3.69,40.41,12)
varmapGeometry=ee.Geometry(Map.getBounds(true)).toGeoJSONString();
varsql=
"SELECT geometry, names.primary as name, categories.primary as category "
+" FROM bigquery-public-data.overture_maps.place "
+" WHERE ST_INTERSECTS(geometry, ST_GEOGFROMGEOJSON('"+mapGeometry+"'))";

varfeatures=ee.FeatureCollection.runBigQuery({
query:sql,
geometryColumn:'geometry'
});

// Display all relevant features on the map.
Map.addLayer(features,
{'color':'black'},
'Places from Overture Maps Dataset');


// Create a histogram of the categories and print it.
varpropertyOfInterest='category';
varhistogram=features.filter(ee.Filter.notNull([propertyOfInterest]))
.aggregate_histogram(propertyOfInterest);
print(histogram);

// Create a frequency chart for the histogram.
varcategories=histogram.keys().map(function(k){
returnee.Feature(null,{
key:k,
value:histogram.get(k)
});
});
varsortedCategories=ee.FeatureCollection(categories).sort('value',false);
print(ui.Chart.feature.byFeature(sortedCategories).setChartType('Table'));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
importjson
importpandasaspd

# Get places from Overture Maps Dataset in BigQuery public data.
location = ee.Geometry.Point(-3.69, 40.41)
map_geometry = json.dumps(location.buffer(5e3).getInfo())

sql = f"""SELECT geometry, names.primary as name, categories.primary as category
FROM bigquery-public-data.overture_maps.place
WHERE ST_INTERSECTS(geometry, ST_GEOGFROMGEOJSON('{map_geometry}'))"""

features = ee.FeatureCollection.runBigQuery(
    query=sql, geometryColumn="geometry"
)

# Display all relevant features on the map.
m = geemap.Map()
m.center_object(location, 13)
m.add_layer(features, {'color': 'black'}, 'Places from Overture Maps Dataset')
display(m)

# Create a histogram of the place categories.
property_of_interest = 'category'
histogram = (
    features.filter(
        ee.Filter.notNull([property_of_interest])
    ).aggregate_histogram(property_of_interest)
).getInfo()

# Display the histogram as a pandas DataFrame.
df = pd.DataFrame(list(histogram.items()), columns=['category', 'frequency'])
df = df.sort_values(by=['frequency'], ascending=False, ignore_index=True)
display(df)
```

