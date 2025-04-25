 
#  ee.Array.erfcInv 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-erfcinv#examples)


On an element-wise basis, computes the inverse complementary error function of the input. 
Usage| Returns  
---|---  
`Array.erfcInv()`| Array  
Argument| Type| Details  
---|---|---  
this: `input`| Array| The input array.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-erfcinv#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-erfcinv#colab-python-sample) More
```
print(ee.Array([0.1]).erfcInv());// [1.163]
print(ee.Array([1]).erfcInv());// [0]
print(ee.Array([1.9]).erfcInv());// [-1.163]
varstart=0.001;
varend=1.999;
varpoints=ee.Array(ee.List.sequence(start,end,null,50));
varvalues=points.erfcInv();
// Plot erfcInv() defined above.
varchart=ui.Chart.array.values(values,0,points)
.setOptions({
viewWindow:{min:start,max:end},
hAxis:{
title:'x',
viewWindowMode:'maximized',
ticks:[
{v:0},
{v:1},
{v:2}]
},
vAxis:{
title:'erfcInv(x)',
ticks:[
{v:-3},
{v:0},
{v:3}]
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
display(ee.Array([0.1]).erfcInv()) # [1.163]
display(ee.Array([1]).erfcInv()) # [0]
display(ee.Array([1.9]).erfcInv()) # [-1.163]
start = 0.001
end = 1.999
points = ee.Array(ee.List.sequence(start, end, None, 50))
values = points.erfcInv()
df = pd.DataFrame({'x': points.getInfo(), 'erfcInv(x)': values.getInfo()})
# Plot erfcInv() defined above.
alt.Chart(df).mark_line().encode(
  x=alt.X('x', axis=alt.Axis(values=[0, 1, 2])),
  y=alt.Y('erfcInv(x)', axis=alt.Axis(values=[-3, 0, 3]))
)
```

