 
#  ee.FeatureCollection.reduceColumns 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-reducecolumns#examples)


Apply a reducer to each element of a collection, using the given selectors to determine the inputs. 
Returns a dictionary of results, keyed with the output names.
Usage| Returns  
---|---  
`FeatureCollection.reduceColumns(reducer, selectors,  _weightSelectors_)`| Dictionary  
Argument| Type| Details  
---|---|---  
this: `collection`| FeatureCollection| The collection to aggregate over.  
`reducer`| Reducer| The reducer to apply.  
`selectors`| List| A selector for each input of the reducer.  
`weightSelectors`| List, default: null| A selector for each weighted input of the reducer.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-reducecolumns#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-reducecolumns#colab-python-sample) More
```
// FeatureCollection of power plants in Belgium.
varfc=ee.FeatureCollection('WRI/GPPD/power_plants')
.filter('country_lg == "Belgium"');
// Calculate mean of a single FeatureCollection property.
varpropMean=fc.reduceColumns({
reducer:ee.Reducer.mean(),
selectors:['gwh_estimt']
});
print('Mean of a single property',propMean);
// Calculate mean of multiple FeatureCollection properties.
varpropsMean=fc.reduceColumns({
reducer:ee.Reducer.mean().repeat(2),
selectors:['gwh_estimt','capacitymw']
});
print('Mean of multiple properties',propsMean);
// Calculate weighted mean of a single FeatureCollection property. Add a fuel
// source weight property to the FeatureCollection.
varfuelWeights=ee.Dictionary({
Wind:0.9,
Gas:0.2,
Oil:0.2,
Coal:0.1,
Hydro:0.7,
Biomass:0.5,
Nuclear:0.3
});
fc=fc.map(function(feature){
returnfeature.set('weight',fuelWeights.getNumber(feature.get('fuel1')));
});
varweightedMean=fc.reduceColumns({
reducer:ee.Reducer.mean(),
selectors:['gwh_estimt'],
weightSelectors:['weight']
});
print('Weighted mean of a single property',weightedMean);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# FeatureCollection of power plants in Belgium.
fc = ee.FeatureCollection('WRI/GPPD/power_plants').filter(
  'country_lg == "Belgium"')
# Calculate mean of a single FeatureCollection property.
prop_mean = fc.reduceColumns(**{
  'reducer': ee.Reducer.mean(),
  'selectors': ['gwh_estimt']
  })
print('Mean of a single property:', prop_mean.getInfo())
# Calculate mean of multiple FeatureCollection properties.
props_mean = fc.reduceColumns(**{
  'reducer': ee.Reducer.mean().repeat(2),
  'selectors': ['gwh_estimt', 'capacitymw']
  })
print('Mean of multiple properties:', props_mean.getInfo())

# Calculate weighted mean of a single FeatureCollection property. Add a fuel
# source weight property to the FeatureCollection.
defget_fuel(feature):
 return feature.set('weight', fuel_weights.getNumber(feature.get('fuel1')))
fuel_weights = ee.Dictionary({
  'Wind': 0.9,
  'Gas': 0.2,
  'Oil': 0.2,
  'Coal': 0.1,
  'Hydro': 0.7,
  'Biomass': 0.5,
  'Nuclear': 0.3
  })
fc = fc.map(get_fuel)
weighted_mean = fc.reduceColumns(**{
  'reducer': ee.Reducer.mean(),
  'selectors': ['gwh_estimt'],
  'weightSelectors': ['weight']
  })
print('Weighted mean of a single property:', weighted_mean.getInfo())
```

Was this helpful?
