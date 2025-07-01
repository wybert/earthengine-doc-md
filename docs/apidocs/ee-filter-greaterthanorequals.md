 
#  ee.Filter.greaterThanOrEquals
Stay organized with collections  Save and categorize content based on your preferences. 
Creates a unary or binary filter that passes unless the left operand is less than the right operand. Usage| Returns  
---|---  
`ee.Filter.greaterThanOrEquals( _leftField_, _rightValue_, _rightField_, _leftValue_)`| Filter  
Argument| Type| Details  
---|---|---  
`leftField`| String, default: null| A selector for the left operand. Should not be specified if leftValue is specified.  
`rightValue`| Object, default: null| The value of the right operand. Should not be specified if rightField is specified.  
`rightField`| String, default: null| A selector for the right operand. Should not be specified if rightValue is specified.  
`leftValue`| Object, default: null| The value of the left operand. Should not be specified if leftField is specified.  
## Examples
### Code Editor (JavaScript)
```
// Field site vegetation characteristics from projects in western USA.
varfc=ee.FeatureCollection('BLM/AIM/v1/TerrADat/TerrestrialAIM')
.filter('ProjectName == "Colorado NWDO Kremmling FO 2016"');
// Display field plots on the map.
Map.setCenter(-107.792,39.871,7);
Map.addLayer(fc);
// Compare the per-feature values of two properties and filter the collection
// based on the results of various relational expressions. The two properties
// to compare are invasive and non-invasive annual forb cover at each plot.
varleftProperty='InvAnnForbCover_AH';
varrightProperty='NonInvAnnForbCover_AH';
print('Plots where invasive forb cover is…');
print('…EQUAL to non-invasive cover',
fc.filter(ee.Filter.equals(
{leftField:leftProperty,rightField:rightProperty})));
print('…NOT EQUAL to non-invasive cover',
fc.filter(ee.Filter.notEquals(
{leftField:leftProperty,rightField:rightProperty})));
print('…LESS THAN non-invasive cover',
fc.filter(ee.Filter.lessThan(
{leftField:leftProperty,rightField:rightProperty})));
print('…LESS THAN OR EQUAL to non-invasive cover',
fc.filter(ee.Filter.lessThanOrEquals(
{leftField:leftProperty,rightField:rightProperty})));
print('…GREATER THAN non-invasive cover',
fc.filter(ee.Filter.greaterThan(
{leftField:leftProperty,rightField:rightProperty})));
print('…GREATER THAN OR EQUAL to non-invasive cover',
fc.filter(ee.Filter.greaterThanOrEquals(
{leftField:leftProperty,rightField:rightProperty})));
print('…is not greater than 10 percent different than non-invasive cover',
fc.filter(ee.Filter.maxDifference(
{difference:10,leftField:leftProperty,rightField:rightProperty})));
// Instead of comparing values of two feature properties using the leftField
// and rightField parameters, you can compare a property value (leftProperty)
// against a constant value (rightValue).
print('Plots where invasive forb cover is greater than 20%',
fc.filter(ee.Filter.greaterThan(
{leftField:leftProperty,rightValue:20})));
// You can also swap the operands to assign the constant to the left side of
// the relational expression (leftValue) and the feature property on the right
// (rightField). Here, we get the complement of the previous example.
print('Plots where 20% is greater than invasive forb cover.',
fc.filter(ee.Filter.greaterThan(
{leftValue:20,rightField:leftProperty})));
// Binary filters are useful in joins. For example, group all same-site plots
// together using a saveAll join.
vargroupingProp='SiteID';
varsitesFc=fc.distinct(groupingProp);
varjoinFilter=ee.Filter.equals(
{leftField:groupingProp,rightField:groupingProp});
vargroupedPlots=ee.Join.saveAll('site_plots').apply(sitesFc,fc,joinFilter);
print('List of plots in first site',groupedPlots.first().get('site_plots'));
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Field site vegetation characteristics from projects in western USA.
fc = ee.FeatureCollection('BLM/AIM/v1/TerrADat/TerrestrialAIM').filter(
  'ProjectName == "Colorado NWDO Kremmling FO 2016"'
)
# Display field plots on the map.
m = geemap.Map()
m.set_center(-107.792, 39.871, 7)
m.add_layer(fc)
display(m)
# Compare the per-feature values of two properties and filter the collection
# based on the results of various relational expressions. The two properties
# to compare are invasive and non-invasive annual forb cover at each plot.
left_property = 'InvAnnForbCover_AH'
right_property = 'NonInvAnnForbCover_AH'
display('Plots where invasive forb cover is…')
display(
  '…EQUAL to non-invasive cover',
  fc.filter(
    ee.Filter.equals(leftField=left_property, rightField=right_property)
  ),
)
display(
  '…NOT EQUAL to non-invasive cover',
  fc.filter(
    ee.Filter.notEquals(leftField=left_property, rightField=right_property)
  ),
)
display(
  '…LESS THAN non-invasive cover',
  fc.filter(
    ee.Filter.lessThan(leftField=left_property, rightField=right_property)
  ),
)
display(
  '…LESS THAN OR EQUAL to non-invasive cover',
  fc.filter(
    ee.Filter.lessThanOrEquals(
      leftField=left_property, rightField=right_property
    )
  ),
)
display(
  '…GREATER THAN non-invasive cover',
  fc.filter(
    ee.Filter.greaterThan(
      leftField=left_property, rightField=right_property
    )
  ),
)
display(
  '…GREATER THAN OR EQUAL to non-invasive cover',
  fc.filter(
    ee.Filter.greaterThanOrEquals(
      leftField=left_property, rightField=right_property
    )
  ),
)
display(
  '…is not greater than 10 percent different than non-invasive cover',
  fc.filter(
    ee.Filter.maxDifference(
      difference=10, leftField=left_property, rightField=right_property
    )
  ),
)
# Instead of comparing values of two feature properties using the leftField
# and rightField parameters, you can compare a property value (left_property)
# against a constant value (rightValue).
display(
  'Plots where invasive forb cover is greater than 20%',
  fc.filter(ee.Filter.greaterThan(leftField=left_property, rightValue=20)),
)
# You can also swap the operands to assign the constant to the left side of
# the relational expression (leftValue) and the feature property on the right
# (rightField). Here, we get the complement of the previous example.
display(
  'Plots where 20% is greater than invasive forb cover.',
  fc.filter(ee.Filter.greaterThan(leftValue=20, rightField=left_property)),
)
# Binary filters are useful in joins. For example, group all same-site plots
# together using a saveAll join.
grouping_prop = 'SiteID'
sites_fc = fc.distinct(grouping_prop)
join_filter = ee.Filter.equals(
  leftField=grouping_prop, rightField=grouping_prop
)
grouped_plots = ee.Join.saveAll('site_plots').apply(sites_fc, fc, join_filter)
display('List of plots in first site', grouped_plots.first().get('site_plots'))
```

