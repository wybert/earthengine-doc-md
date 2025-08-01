 
#  ee.Array.acos
Stay organized with collections  Save and categorize content based on your preferences. 
On an element-wise basis, computes the arccosine in radians of the input. Usage | Returns  
---|---  
`Array.acos()` | Array  
Argument | Type | Details  
---|---|---  
this: `input` | Array | The input array.  
## Examples
### Code Editor (JavaScript)
```
print(ee.Array([-1]).acos());// [π]
print(ee.Array([0]).acos());// [π/2]
print(ee.Array([1]).acos());// [0]

varstart=-1;
varend=1;
varpoints=ee.Array(ee.List.sequence(start,end,null,50));
varvalues=points.acos();

// Plot acos() defined above.
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
title:'acos(x)',
ticks:[
{v:0,f:0},
{v:Math.PI/2,f:'π/2'},
{v:Math.PI,f:'π'}]
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

display(ee.Array([-1]).acos())  # [π]
display(ee.Array([0]).acos())  # [π/2]
display(ee.Array([1]).acos())  # [0]

start = -1
end = 1
points = ee.Array(ee.List.sequence(start, end, None, 50))
values = points.acos()

df = pd.DataFrame({'x': points.getInfo(), 'acos(x)': values.getInfo()})

# Plot acos() defined above.
alt.Chart(df).mark_line().encode(
    x=alt.X('x', axis=alt.Axis(values=[start, 0, end])),
    y=alt.Y('acos(x)', axis=alt.Axis(values=[0, math.pi / 2, math.pi]))
)
```

