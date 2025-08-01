 
#  ee.Array.erfInv
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-erfinv#examples)


On an element-wise basis, computes the inverse error function of the input.
Usage | Returns  
---|---  
`Array.erfInv()` | Array  
Argument | Type | Details  
---|---|---  
this: `input` | Array | The input array.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-erfinv#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-erfinv#colab-python-sample) More
```
print(ee.Array([-0.99]).erfInv());// [-1.82]
print(ee.Array([0]).erfInv());// [0]
print(ee.Array([0.99]).erfInv());// [1.82]

varstart=-0.99;
varend=0.99;
varpoints=ee.Array(ee.List.sequence(start,end,null,50));
varvalues=points.erfInv();

// Plot erfInv() defined above.
varchart=ui.Chart.array.values(values,0,points)
.setOptions({
viewWindow:{min:start,max:end},
hAxis:{
title:'x',
viewWindowMode:'maximized',
ticks:[
{v:-1},
{v:0},
{v:1}]
},
vAxis:{
title:'erfInv(x)',
ticks:[
{v:-2},
{v:0},
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

display(ee.Array([-0.99]).erfInv())  # [-1.82]
display(ee.Array([0]).erfInv())  # [0]
display(ee.Array([0.99]).erfInv())  # [1.82]

start = -0.99
end = 0.99
points = ee.Array(ee.List.sequence(start, end, None, 50))
values = points.erfInv()

df = pd.DataFrame({'x': points.getInfo(), 'erfInv(x)': values.getInfo()})

# Plot erfInv() defined above.
alt.Chart(df).mark_line().encode(
    x=alt.X('x', axis=alt.Axis(values=[-1, 0, 1])),
    y=alt.Y('erfInv(x)', axis=alt.Axis(values=[-2, 0, 2]))
)
```

Was this helpful?
