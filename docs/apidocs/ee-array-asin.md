 
#  ee.Array.asin 
Stay organized with collections  Save and categorize content based on your preferences. 
On an element-wise basis, computes the arcsine in radians of the input. Usage| Returns  
---|---  
`Array.asin()`| Array  
Argument| Type| Details  
---|---|---  
this: `input`| Array| The input array.  
## Examples
### Code Editor (JavaScript)
```
print(ee.Array([-1]).asin());// [-π/2]
print(ee.Array([0]).asin());// [0]
print(ee.Array([1]).asin());// [π/2]
varstart=-1;
varend=1;
varpoints=ee.Array(ee.List.sequence(start,end,null,50));
varvalues=points.asin();
// Plot asin() defined above.
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
title:'asin(x)',
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

### Colab (Python)
```
importmath
importaltairasalt
importpandasaspd
display(ee.Array([-1]).asin()) # [-π/2]
display(ee.Array([0]).asin()) # [0]
display(ee.Array([1]).asin()) # [π/2]
start = -1
end = 1
points = ee.Array(ee.List.sequence(start, end, None, 50))
values = points.asin()
df = pd.DataFrame({'x': points.getInfo(), 'asin(x)': values.getInfo()})
# Plot asin() defined above.
alt.Chart(df).mark_line().encode(
  x=alt.X('x', axis=alt.Axis(values=[start, 0, end])),
  y=alt.Y('asin(x)', axis=alt.Axis(values=[-math.pi / 2, 0, math.pi / 2]))
)
```

