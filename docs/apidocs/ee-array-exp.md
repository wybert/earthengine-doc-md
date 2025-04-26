 
#  ee.Array.exp 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-exp#examples)


On an element-wise basis, computes the Euler's number e raised to the power of the input. 
Usage| Returns  
---|---  
`Array.exp()`| Array  
Argument| Type| Details  
---|---|---  
this: `input`| Array| The input array.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-exp#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-exp#colab-python-sample) More
```
varempty=ee.Array([],ee.PixelType.int8());
print(empty.exp());// []
// [Math.pow(Math.E, -1), 1, Math.E, 7.389]
print(ee.Array([-1,0,1,2]).exp());
varstart=-5;
varend=2;
varpoints=ee.Array(ee.List.sequence(start,end,null,50));
varvalues=points.exp();
// Plot exp() defined above.
varchart=ui.Chart.array.values(values,0,points)
.setOptions({
viewWindow:{min:start,max:end},
hAxis:{
title:'x',
viewWindowMode:'maximized',
},
vAxis:{
title:'exp(x)',
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
empty = ee.Array([], ee.PixelType.int8())
display(empty.exp()) # []
# [pow(math.e, -1), 1, math.e, 7.389]
display(ee.Array([-1, 0, 1, 2]).exp())
start = -5
end = 2
points = ee.Array(ee.List.sequence(start, end, None, 50))
values = points.exp()
df = pd.DataFrame({'x': points.getInfo(), 'exp(x)': values.getInfo()})
# Plot exp() defined above.
alt.Chart(df).mark_line().encode(
  x=alt.X('x'),
  y=alt.Y('exp(x)')
)
```

Was this helpful?
