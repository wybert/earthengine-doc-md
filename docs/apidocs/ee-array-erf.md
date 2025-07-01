 
#  ee.Array.erf
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-erf#examples)


On an element-wise basis, computes the error function of the input. 
Usage| Returns  
---|---  
`Array.erf()`| Array  
Argument| Type| Details  
---|---|---  
this: `input`| Array| The input array.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-erf#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-erf#colab-python-sample) More
```
print(ee.Array([-6]).erf());// [-1]
print(ee.Array([0]).erf());// [0]
print(ee.Array([6]).erf());// [1]
varstart=-3;
varend=3;
varpoints=ee.Array(ee.List.sequence(start,end,null,50));
varvalues=points.erf();
// Plot erf() defined above.
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
title:'erf(x)',
ticks:[
{v:-1},
{v:0},
{v:1}]
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
display(ee.Array([-6]).erf()) # [-1]
display(ee.Array([0]).erf()) # [0]
display(ee.Array([6]).erf()) # [1]
start = -3
end = 3
points = ee.Array(ee.List.sequence(start, end, None, 50))
values = points.erf()
df = pd.DataFrame({'x': points.getInfo(), 'erf(x)': values.getInfo()})
# Plot erf() defined above.
alt.Chart(df).mark_line().encode(
  x=alt.X('x', axis=alt.Axis(values=[start, 0, end])),
  y=alt.Y('erf(x)', axis=alt.Axis(values=[-1, 0, 1]))
)
```

Was this helpful?
