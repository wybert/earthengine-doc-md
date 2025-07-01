 
#  ee.Array.tan
Stay organized with collections  Save and categorize content based on your preferences. 
On an element-wise basis, computes the tangent of the input in radians. Usage| Returns  
---|---  
`Array.tan()`| Array  
Argument| Type| Details  
---|---|---  
this: `input`| Array| The input array.  
## Examples
### Code Editor (JavaScript)
```
varπ=Math.PI;
print(ee.Array([-π/4]).tan());// [Almost -1]
print(ee.Array([0]).tan());// [0]
print(ee.Array([π/4]).tan());// [Almost 1]
varstart=-π/3;
varend=π/3;
varpoints=ee.Array(ee.List.sequence(start,end,null,50));
varvalues=points.tan();
// Plot tan() defined above.
varchart=ui.Chart.array.values(values,0,points)
.setOptions({
viewWindow:{min:start,max:end},
hAxis:{
title:'x',
viewWindowMode:'maximized',
ticks:[
{v:start,f:'-π / 3'},
{v:0,f:0},
{v:end,f:'π / 3'}]
},
vAxis:{
title:'tan(x)',
ticks:[
{v:-Math.sqrt(3),f:'-√3'},
{v:0},
{v:Math.sqrt(3),f:'√3'}]
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
π = math.pi
display(ee.Array([-π / 4]).tan()) # [Almost -1]
display(ee.Array([0]).tan()) # [0]
display(ee.Array([π / 4]).tan()) # [Almost 1]
start = -π / 3
end = π / 3
points = ee.Array(ee.List.sequence(start, end, None, 50))
values = points.tan()
df = pd.DataFrame({'x': points.getInfo(), 'tan(x)': values.getInfo()})
# Plot tan() defined above.
alt.Chart(df).mark_line().encode(
  x=alt.X('x', axis=alt.Axis(values=[start, 0, end])),
  y=alt.Y('tan(x)', axis=alt.Axis(values=[-math.sqrt(3), 0, math.sqrt(3)]))
)
```

