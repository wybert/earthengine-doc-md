 
#  ee.FeatureCollection.randomColumn
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-randomcolumn#examples)


Adds a column of deterministic pseudorandom numbers to a collection. The outputs are double-precision floating point numbers. When using the 'uniform' distribution (default), outputs are in the range of [0, 1). Using the 'normal' distribution, outputs have μ=0, σ=1, but have no explicit limits. 
Usage| Returns  
---|---  
`FeatureCollection.randomColumn( _columnName_, _seed_, _distribution_, _rowKeys_)`| FeatureCollection  
Argument| Type| Details  
---|---|---  
this: `collection`| FeatureCollection| The input collection to which to add a random column.  
`columnName`| String, default: "random"| The name of the column to add.  
`seed`| Long, default: 0| A seed used when generating the random numbers.  
`distribution`| String, default: "uniform"| The distribution type of random numbers to produce; one of 'uniform' or 'normal'.  
`rowKeys`| List, optional| A list of properties that should uniquely and repeatably identify an element of the collection, used to generate the random number. Defaults to [system:index].  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-randomcolumn#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-randomcolumn#colab-python-sample) More
```
// FeatureCollection of power plants in Belgium.
varfc=ee.FeatureCollection('WRI/GPPD/power_plants')
.filter('country_lg == "Belgium"');
print('N features in collection',fc.size());
// Add a uniform distribution random value column to the FeatureCollection.
fc=fc.randomColumn();
// Randomly split the collection into two sets, 30% and 70% of the total.
varrandomSample30=fc.filter('random < 0.3');
print('N features in 30% sample',randomSample30.size());
varrandomSample70=fc.filter('random >= 0.3');
print('N features in 70% sample',randomSample70.size());
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
print('N features in collection:', fc.size().getInfo())
# Add a uniform distribution random value column to the FeatureCollection.
fc = fc.randomColumn()
# Randomly split the collection into two sets, 30% and 70% of the total.
random_sample_30 = fc.filter('random < 0.3')
print('N features in 30% sample:', random_sample_30.size().getInfo())
random_sample_70 = fc.filter('random >= 0.3')
print('N features in 70% sample:', random_sample_70.size().getInfo())
```

