 
#  ee.Array.erfc
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-erfc#examples)


On an element-wise basis, computes the complementary error function of the input.
Usage | Returns  
---|---  
`Array.erfc()` | Array  
Argument | Type | Details  
---|---|---  
this: `input` | Array | The input array.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-erfc#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-erfc#colab-python-sample) More
```
print(ee.Array([-6]).erfc());// [2]
print(ee.Array([0]).erfc());// [1]
print(ee.Array([28]).erfc());// [0]

varstart=-3;
varend=3;
varpoints=ee.Array(ee.List.sequence(start,end,null,50));
varvalues=points.erfc();

// Plot erfc() defined above.
varchart=ui.Chart.array.values(values,0,points)
.setOptions({
viewWindow:{min:start,max:end},
hAxis:{
title:'x',
viewWindowMode:'maximized',
ticks:[
{v:start},
{v:0},
{v:end}]
},
vAxis:{
title:'erfc(x)',
ticks:[
{v:0},
{v:1},
{v:2}]
},
lineWidth:1,
pointSize:0,
});
print(chart);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
importaltairasalt
importpandasaspd

display(ee.Array([-6]).erfc())  # [2]
display(ee.Array([0]).erfc())  # [1]
display(ee.Array([28]).erfc())  # [0]

start = -3
end = 3
points = ee.Array(ee.List.sequence(start, end, None, 50))
values = points.erfc()

df = pd.DataFrame({'x': points.getInfo(), 'erfc(x)': values.getInfo()})

# Plot erfc() defined above.
alt.Chart(df).mark_line().encode(
    x=alt.X('x', axis=alt.Axis(values=[start, 0, end])),
    y=alt.Y('erfc(x)', axis=alt.Axis(values=[0, 1, 2]))
)
```

