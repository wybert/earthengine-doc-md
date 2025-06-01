 
#  ee.Array.cosh 
Stay organized with collections  Save and categorize content based on your preferences. 
On an element-wise basis, computes the hyperbolic cosine of the input. Usage| Returns  
---|---  
`Array.cosh()`| Array  
Argument| Type| Details  
---|---|---  
this: `input`| Array| The input array.  
## Examples
### Code Editor (JavaScript)
```
print(ee.Array([-4]).cosh());// [~27.31]
print(ee.Array([0]).cosh());// [1]
print(ee.Array([4]).cosh());// [~27.31]
varstart=-4;
varend=4;
varpoints=ee.Array(ee.List.sequence(start,end,null,50));
varvalues=points.cosh();
// Plot cosh() defined above.
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
importaltairasalt
importpandasaspd
display(ee.Array([-4]).cosh()) # [~27.31]
display(ee.Array([0]).cosh()) # [1]
display(ee.Array([4]).cosh()) # [~27.31]
start = -4
end = 4
points = ee.Array(ee.List.sequence(start, end, None, 50))
values = points.cosh()
df = pd.DataFrame({'x': points.getInfo(), 'cosh(x)': values.getInfo()})
# Plot cosh() defined above.
alt.Chart(df).mark_line().encode(
  x=alt.X('x', axis=alt.Axis(values=[start, 0, end])),
  y=alt.Y('cosh(x)')
)
```

