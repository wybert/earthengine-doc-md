 
#  ee.FeatureCollection.iterate 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-iterate#examples)


Applies a user-supplied function to each element of a collection. The user-supplied function is given two arguments: the current element, and the value returned by the previous call to iterate() or the first argument, for the first iteration. The result is the value returned by the final call to the user-supplied function. 
Returns the result of the Collection.iterate() call.
Usage| Returns  
---|---  
`FeatureCollection.iterate(algorithm,  _first_)`| ComputedObject  
Argument| Type| Details  
---|---|---  
this: `collection`| Collection| The Collection instance.  
`algorithm`| Function| The function to apply to each element. Must take two arguments: an element of the collection and the value from the previous iteration.  
`first`| Object, optional| The initial state.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-iterate#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-iterate#colab-python-sample) More
```
/**
 * CAUTION: ee.FeatureCollection.iterate can be less efficient than alternative
 * solutions implemented using ee.FeatureCollection.map or by converting feature
 * properties to an ee.Array object and using ee.Array.slice and
 * ee.Array.arrayAccum methods. Avoid ee.FeatureCollection.iterate if possible.
 */
// Monthly precipitation accumulation for 2020.
varclimate=ee.ImageCollection('IDAHO_EPSCOR/TERRACLIMATE')
.filterDate('2020-01-01','2021-01-01')
.select('pr');
// Region of interest: north central New Mexico, USA.
varroi=ee.Geometry.BBox(-107.19,35.27,-104.56,36.83);
// A FeatureCollection of mean monthly precipitation accumulation for the
// region of interest.
varmeanPrecipTs=climate.map(function(image){
varmeanPrecip=image.reduceRegion(
{reducer:ee.Reducer.mean(),geometry:roi,scale:5000});
returnee.Feature(roi,meanPrecip)
.set('system:time_start',image.get('system:time_start'));
});
// A cumulative sum function to apply to each feature in the
// precipitation FeatureCollection. The first input is the current feature and
// the second is a list of features that accumulates at each step of the
// iteration. The function fetches the last feature in the feature list, gets
// the cumulative precipitation sum value from it, and adds it to the current
// feature's precipitation value. The new cumulative precipitation sum is set
// as a property of the current feature, which is appended to the feature list
// that is passed onto the next step of the iteration.
varcumsum=function(currentFeature,featureList){
featureList=ee.List(featureList);
varpreviousSum=ee.Feature(featureList.get(-1)).getNumber('pr_cumsum');
varcurrentVal=ee.Feature(currentFeature).getNumber('pr');
varcurrentSum=previousSum.add(currentVal);
returnfeatureList.add(currentFeature.set('pr_cumsum',currentSum));
};
// Use "iterate" to cumulatively sum monthly precipitation over the year with
// the above defined "cumsum" function. Note that the feature list used in the
// "cumsum" function is initialized as the "first" variable. It includes a
// temporary feature with the "pr_cumsum" property set to 0; this feature is
// filtered out of the final FeatureCollection.
varfirst=ee.List([ee.Feature(null,{pr_cumsum:0,first:true})]);
varprecipCumSum=
ee.FeatureCollection(ee.List(meanPrecipTs.iterate(cumsum,first)))
.filter(ee.Filter.notNull(['pr']));
// Inspect the outputs.
print('Note cumulative precipitation ("pr_cumsum") property',
precipCumSum);
print(ui.Chart.feature.byFeature(
precipCumSum,'system:time_start',['pr','pr_cumsum']));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
importaltairasalt
# CAUTION: ee.FeatureCollection.iterate can be less efficient than alternative
# solutions implemented using ee.FeatureCollection.map or by converting feature
# properties to an ee.Array object and using ee.Array.slice and
# ee.Array.arrayAccum methods. Avoid ee.FeatureCollection.iterate if possible.
# Monthly precipitation accumulation for 2020.
climate = (
  ee.ImageCollection('IDAHO_EPSCOR/TERRACLIMATE')
  .filterDate('2020-01-01', '2021-01-01')
  .select('pr')
)
# Region of interest: north central New Mexico, USA.
roi = ee.Geometry.BBox(-107.19, 35.27, -104.56, 36.83)

# A FeatureCollection of mean monthly precipitation accumulation for the
# region of interest.
defmean_precip_ts_fun(image):
 mean_precip = image.reduceRegion(
   reducer=ee.Reducer.mean(), geometry=roi, scale=5000
 )
 return ee.Feature(roi, mean_precip).set(
   'system:time_start', image.get('system:time_start')
 )

mean_precip_ts = climate.map(mean_precip_ts_fun)

# A cumulative sum function to apply to each feature in the
# precipitation FeatureCollection. The first input is the current feature and
# the second is a list of features that accumulates at each step of the
# iteration. The function fetches the last feature in the feature list, gets
# the cumulative precipitation sum value from it, and adds it to the current
# feature's precipitation value. The new cumulative precipitation sum is set
# as a property of the current feature, which is appended to the feature list
# that is passed onto the next step of the iteration.
defcumsum(current_feature, feature_list):
 feature_list = ee.List(feature_list)
 previous_sum = ee.Feature(feature_list.get(-1)).getNumber('pr_cumsum')
 current_val = ee.Feature(current_feature).getNumber('pr')
 current_sum = previous_sum.add(current_val)
 return feature_list.add(current_feature.set('pr_cumsum', current_sum))

# Use "iterate" to cumulatively sum monthly precipitation over the year with
# the above defined "cumsum" function. Note that the feature list used in the
# "cumsum" function is initialized as the "first" variable. It includes a
# temporary feature with the "pr_cumsum" property set to 0 this feature is
# filtered out of the final FeatureCollection.
first = ee.List([ee.Feature(None, {'pr_cumsum': 0, 'first': True})])
precip_cum_sum = ee.FeatureCollection(
  ee.List(mean_precip_ts.iterate(cumsum, first))
).filter(ee.Filter.notNull(['pr']))
precip_cum_sum = precip_cum_sum.map(
  lambda feature: feature.set(
    'date',
    ee.Date(feature.getNumber('system:time_start')).format('YYYY-MM-dd'),
  )
)
# Inspect the outputs.
display('Note cumulative precipitation ("pr_cumsum") property', precip_cum_sum)
df = geemap.ee_to_df(precip_cum_sum, ['date', 'pr', 'pr_cumsum'])
display(df)
chart = (
  alt.Chart(df)
  .mark_line()
  .encode(x='date:T', y='pr:Q', color=alt.value('blue'))
)
chart += (
  alt.Chart(df)
  .mark_line()
  .encode(x='date:T', y='pr_cumsum:Q', color=alt.value('red'))
)
chart
```

Was this helpful?
