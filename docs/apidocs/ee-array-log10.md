 
#  ee.Array.log10 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-log10#examples)


On an element-wise basis, computes the base-10 logarithm of the input. 
Usage| Returns  
---|---  
`Array.log10()`| Array  
Argument| Type| Details  
---|---|---  
this: `input`| Array| The input array.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-log10#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-log10#colab-python-sample) More
```
print(ee.Array([0.1,1,10,100]).log10());// [-1,0,1,2]
varstart=0.1;
varend=100;
varpoints=ee.Array(ee.List.sequence(start,end,null,50));
varvalues=points.log10();
// Plot log10() defined above.
varchart=ui.Chart.array.values(values,0,points)
.setOptions({
viewWindow:{min:start,max:end},
hAxis:{
title:'x',
viewWindowMode:'maximized',
},
vAxis:{
title:'log10(x)',
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
display(ee.Array([0.1, 1, 10, 100]).log10()) # [-1,0,1,2]
start = 0.1
end = 100
points = ee.Array(ee.List.sequence(start, end, None, 50))
values = points.log10()
df = pd.DataFrame({'x': points.getInfo(), 'log10(x)': values.getInfo()})
# Plot log10() defined above.
alt.Chart(df).mark_line().encode(
  x=alt.X('x'),
  y=alt.Y('log10(x)')
)
```

Was this helpful?
