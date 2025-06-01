 
#  ee.FeatureCollection.filterBounds 
Stay organized with collections  Save and categorize content based on your preferences. 
Shortcut to filter a collection by intersection with geometry. Items in the collection with a footprint that fails to intersect the given geometry will be excluded. 
This is equivalent to this.filter(ee.Filter.bounds(...)).
**Caution:** providing a large or complex collection as the `geometry` argument can result in poor performance. Collating the geometry of collections does not scale well; use the smallest collection (or geometry) that is required to achieve the desired outcome.
Returns the filtered collection.
Usage| Returns  
---|---  
`FeatureCollection.filterBounds(geometry)`| Collection  
Argument| Type| Details  
---|---|---  
this: `collection`| Collection| The Collection instance.  
`geometry`| ComputedObject|FeatureCollection|Geometry| The geometry, feature or collection to intersect with.  
## Examples
### Code Editor (JavaScript)
```
// FeatureCollection of global power plants.
varpowerPlants=ee.FeatureCollection('WRI/GPPD/power_plants');
// FeatureCollection of counties in Oregon, USA.
varoregonCounties=ee.FeatureCollection('TIGER/2018/States')
.filter('STATEFP == "41"');
// Filter global power plants to those that intersect Oregon counties.
varoregonPowerPlants=powerPlants.filterBounds(oregonCounties.geometry());
// Display Oregon power plants on the map.
Map.setCenter(-120.492,44.109,6);
Map.addLayer(oregonPowerPlants);
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# FeatureCollection of global power plants.
power_plants = ee.FeatureCollection('WRI/GPPD/power_plants')
# FeatureCollection of counties in Oregon, USA.
oregon_counties = ee.FeatureCollection('TIGER/2018/States').filter(
  'STATEFP == "41"'
)
# Filter global power plants to those that intersect Oregon counties.
oregon_power_plants = power_plants.filterBounds(oregon_counties.geometry())
# Display Oregon power plants on the map.
m = geemap.Map()
m.set_center(-120.492, 44.109, 6)
m.add_layer(oregon_power_plants)
m
```

