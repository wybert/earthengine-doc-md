 
#  ee.Array.log
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-log#examples)


On an element-wise basis, computes the natural logarithm of the input. 
Usage| Returns  
---|---  
`Array.log()`| Array  
Argument| Type| Details  
---|---|---  
this: `input`| Array| The input array.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-log#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-log#colab-python-sample) More
```
print(ee.Array([Math.pow(Math.E,-1),1,Math.E]).log());// [-1,0,1]
varstart=0.1;
varend=6;
varpoints=ee.Array(ee.List.sequence(start,end,null,50));
varvalues=points.log();
// Plot log() defined above.
varchart=ui.Chart.array.values(values,0,points)
.setOptions({
viewWindow:{min:start,max:end},
hAxis:{
title:'x',
viewWindowMode:'maximized',
ticks:[
{v:0},
{v:3},
{v:end}]
},
vAxis:{
title:'log(x)',
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
importmath
importaltairasalt
importpandasaspd
display(ee.Array([pow(math.e, -1), 1, math.e]).log()) # [-1,0,1]
start = 0.1
end = 6
points = ee.Array(ee.List.sequence(start, end, None, 50))
values = points.log()
df = pd.DataFrame({'x': points.getInfo(), 'log(x)': values.getInfo()})
# Plot log() defined above.
alt.Chart(df).mark_line().encode(
  x=alt.X('x', axis=alt.Axis(values=[0, 3, end])),
  y=alt.Y('log(x)', axis=alt.Axis(values=[-3, 0, 3]))
)
```

Was this helpful?
