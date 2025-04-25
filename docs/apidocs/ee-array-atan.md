 
#  ee.Array.atan 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-atan#examples)


On an element-wise basis, computes the arctangent in radians of the input. 
Usage| Returns  
---|---  
`Array.atan()`| Array  
Argument| Type| Details  
---|---|---  
this: `input`| Array| The input array.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-atan#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-atan#colab-python-sample) More
```
print(ee.Array([-5]).atan());// [-1.3734]
print(ee.Array([0]).atan());// [0]
print(ee.Array([5]).atan());// [1.3734]
varstart=-5;
varend=5;
varpoints=ee.Array(ee.List.sequence(start,end,null,50));
varvalues=points.atan();
// Plot atan() defined above.
varchart=ui.Chart.array.values(values,0,points)
.setOptions({
viewWindow:{min:start,max:end},
hAxis:{
title:'x',
viewWindowMode:'maximized',
ticks:[
{v:start,f:start},
{v:0,f:0},
{v:end,f:end}]
},
vAxis:{
title:'atan(x)',
ticks:[
{v:-Math.PI/2,f:'-π/2'},
{v:0,f:0},
{v:Math.PI/2,f:'π/2'}]
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
importmath
importaltairasalt
importpandasaspd
display(ee.Array([-5]).atan()) # [-1.3734]
display(ee.Array([0]).atan()) # [0]
display(ee.Array([5]).atan()) # [1.3734]
start = -5
end = 5
points = ee.Array(ee.List.sequence(start, end, None, 50))
values = points.atan()
df = pd.DataFrame({'x': points.getInfo(), 'atan(x)': values.getInfo()})
# Plot atan() defined above.
alt.Chart(df).mark_line().encode(
  x=alt.X('x', axis=alt.Axis(values=[start, 0, end])),
  y=alt.Y('atan(x)', axis=alt.Axis(values=[-math.pi / 2, 0, math.pi / 2]))
)
```

