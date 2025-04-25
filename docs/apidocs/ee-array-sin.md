 
#  ee.Array.sin 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-sin#examples)


On an element-wise basis, computes the sine of the input in radians. 
Usage| Returns  
---|---  
`Array.sin()`| Array  
Argument| Type| Details  
---|---|---  
this: `input`| Array| The input array.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-sin#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-sin#colab-python-sample) More
```
varπ=Math.PI;
print(ee.Array([-π]).sin());// [Almost zero]
print(ee.Array([-π/2.0]).sin());// [-1]
print(ee.Array([0]).sin());// [0]
print(ee.Array([π/2.0]).sin());// [1]
print(ee.Array([π]).sin());// [Almost zero]
varstart=-π;
varend=π;
varpoints=ee.Array(ee.List.sequence(start,end,null,50));
varvalues=points.sin();
// Plot sin() defined above.
varchart=ui.Chart.array.values(values,0,points)
.setOptions({
viewWindow:{min:start,max:end},
hAxis:{
title:'x',
viewWindowMode:'maximized',
ticks:[
{v:start,f:'-π'},
{v:0,f:0},
{v:end,f:'-π'}]
},
vAxis:{
title:'sin(x)',
ticks:[
{v:-1,f:-1},
{v:0,f:0},
{v:1,f:1}]
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
π = math.pi
display(ee.Array([-π]).sin()) # [Almost zero]
display(ee.Array([-π / 2.0]).sin()) # [-1]
display(ee.Array([0]).sin()) # [0]
display(ee.Array([π / 2.0]).sin()) # [1]
display(ee.Array([π]).sin()) # [Almost zero]
start = -π
end = π
points = ee.Array(ee.List.sequence(start, end, None, 50))
values = points.sin()
df = pd.DataFrame({'x': points.getInfo(), 'sin(x)': values.getInfo()})
# Plot sin() defined above.
alt.Chart(df).mark_line().encode(
  x=alt.X('x', axis=alt.Axis(values=[start, 0, end])),
  y=alt.Y('sin(x)', axis=alt.Axis(values=[-1, 0, 1]))
)
```

Was this helpful?
