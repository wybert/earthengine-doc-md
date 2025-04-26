 
#  ee.Array.mod 
Stay organized with collections  Save and categorize content based on your preferences. 
On an element-wise basis, calculates the remainder of the first value divided by the second. Usage| Returns  
---|---  
`Array.mod(right)`| Array  
Argument| Type| Details  
---|---|---  
this: `left`| Array| The left-hand value.  
`right`| Array| The right-hand value.  
## Examples
### Code Editor (JavaScript)
```
varempty=ee.Array([],ee.PixelType.int8());
print(empty.mod(empty));// []
print(ee.Array([0,0]).mod(ee.Array([-1,2])));// [0,0]
print(ee.Array([0,1,2,3,4]).mod(ee.Array([1,1,1,1,1])));// [0,0,0,0,0]
print(ee.Array([0,1,2,3,4]).mod(ee.Array([2,2,2,2,2])));// [0,1,0,1,0]
print(ee.Array([0,1,7,8,9]).mod(ee.Array([8,8,8,8,8])));// [0,1,7,0,1]
print(ee.Array([-1,-7,-8,-9]).mod(ee.Array([8,8,8,8])));// [-1,-7,0,-1]
print(ee.Array([8,8,8,8]).mod(ee.Array([-1,-7,-8,-9])));// [0,1,0,8]
print(ee.Array([2.5]).mod(ee.Array([1.2])));// [0.10000000000000009]
// Generate a square wave graph using mod.
varstart=-10;
varend=10;
varnumElements=1000;
varstepSize=2;
varpoints=ee.Array(ee.List.sequence(start,end,null,numElements));
varmodValues=ee.Array([stepSize]).repeat(0,numElements);
varvalues=points.mod(modValues).floor();
// Plot mod().floor() defined above.
// Generate a square wave that is different for negative and positive values.
varchart=ui.Chart.array.values(values,0,points)
.setOptions({
viewWindow:{min:start,max:end},
hAxis:{
title:'x',
viewWindowMode:'maximized'
},
vAxis:{
title:'mod().floor()',
ticks:[{v:-3},{v:-2},{v:-1},{v:0},{v:1},{v:2}]
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
empty = ee.Array([], ee.PixelType.int8())
display(empty.mod(empty)) # []
display(ee.Array([0, 0]).mod(ee.Array([-1, 2]))) # [0,0]
# [0,0,0,0,0]
display(ee.Array([0, 1, 2, 3, 4]).mod(ee.Array([1, 1, 1, 1, 1])))
# [0,1,0,1,0]
display(ee.Array([0, 1, 2, 3, 4]).mod(ee.Array([2, 2, 2, 2, 2])))
# [0,1,7,0,1]
display(ee.Array([0, 1, 7, 8, 9]).mod(ee.Array([8, 8, 8, 8, 8])))
# [-1,-7,0,-1]
display(ee.Array([-1, -7, -8, -9]).mod(ee.Array([8, 8, 8, 8])))
# [0,1,0,8]
display(ee.Array([8, 8, 8, 8]).mod(ee.Array([-1, -7, -8, -9])))
display(ee.Array([2.5]).mod(ee.Array([1.2]))) # [0.10000000000000009]
# Generate a square wave graph using mod.
start = -10
end = 10
num_elements = 1000
step_size = 2
points = ee.Array(ee.List.sequence(start, end, None, num_elements))
mod_values = ee.Array([step_size]).repeat(0, num_elements)
values = points.mod(mod_values).floor()
df = pd.DataFrame({'x': points.getInfo(), 'mod()': values.getInfo()})
# Plot mod().floor() defined above.
# Generate a square wave that is different for negative and positive values.
alt.Chart(df).mark_line().encode(
  x=alt.X('x'),
  y=alt.Y('mod()', axis=alt.Axis(values=[-3, -2, -1, 0, 1, 2]))
)
```

