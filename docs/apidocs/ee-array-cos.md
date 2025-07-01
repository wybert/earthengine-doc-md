 
#  ee.Array.cos
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-cos#examples)


On an element-wise basis, computes the cosine of the input in radians. 
Usage| Returns  
---|---  
`Array.cos()`| Array  
Argument| Type| Details  
---|---|---  
this: `input`| Array| The input array.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-cos#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-cos#colab-python-sample) More
```
varπ=Math.PI;
print(ee.Array([-π]).cos());// [-1]
print(ee.Array([-π/2.0]).cos());// [Almost zero]
print(ee.Array([0]).cos());// [1]
print(ee.Array([π/2.0]).cos());// [Almost zero]
print(ee.Array([π]).cos());// [-1]
varstart=-π;
varend=π;
varpoints=ee.Array(ee.List.sequence(start,end,null,50));
varvalues=points.cos();
// Plot cos() defined above.
varchart=ui.Chart.array.values(values,0,points)
.setOptions({
viewWindow:{min:start,max:end},
hAxis:{
title:'x',
viewWindowMode:'maximized',
ticks:[
{v:start,f:'-π'},
{v:0,f:0},
{v:end,f:'π'}]
},
vAxis:{
title:'cos(x)',
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
display(ee.Array([-π]).cos()) # [-1]
display(ee.Array([-π / 2.0]).cos()) # [Almost zero]
display(ee.Array([0]).cos()) # [1]
display(ee.Array([π / 2.0]).cos()) # [Almost zero]
display(ee.Array([π]).cos()) # [-1]
start = -π
end = π
points = ee.Array(ee.List.sequence(start, end, None, 50))
values = points.cos()
df = pd.DataFrame({'x': points.getInfo(), 'cos(x)': values.getInfo()})
# Plot cos() defined above.
alt.Chart(df).mark_line().encode(
  x=alt.X('x', axis=alt.Axis(values=[start, 0, end])),
  y=alt.Y('cos(x)', axis=alt.Axis(values=[-1, 0, 1]))
)
```

Was this helpful?
