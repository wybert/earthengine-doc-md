 
#  ee.Array.tanh
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-tanh#examples)


On an element-wise basis, computes the hyperbolic tangent of the input.
Usage | Returns  
---|---  
`Array.tanh()` | Array  
Argument | Type | Details  
---|---|---  
this: `input` | Array | The input array.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-tanh#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-tanh#colab-python-sample) More
```
print(ee.Array([-5]).tanh());// [~ -1]
print(ee.Array([0]).tanh());// [0]
print(ee.Array([5]).tanh());// [~ 1]

varstart=-5;
varend=5;
varpoints=ee.Array(ee.List.sequence(start,end,null,50));
varvalues=points.tanh();

// Plot tanh() defined above.
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
```
importaltairasalt
importpandasaspd

display(ee.Array([-5]).tanh())  # [~ -1]
display(ee.Array([0]).tanh())  # [0]
display(ee.Array([5]).tanh())  # [~ 1]

start = -5
end = 5
points = ee.Array(ee.List.sequence(start, end, None, 50))
values = points.tanh()

df = pd.DataFrame({'x': points.getInfo(), 'tanh(x)': values.getInfo()})

# Plot tanh() defined above.
alt.Chart(df).mark_line().encode(
    x=alt.X('x'),
    y=alt.Y('tanh(x)', axis=alt.Axis(values=[start, 0, end]))
)
```

Was this helpful?
