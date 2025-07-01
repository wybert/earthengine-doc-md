 
#  ee.Array.cat
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-cat#examples)


Concatenates multiple arrays into a single array along the given axis. Each array must have the same dimensionality and the same length on all axes except the concatenation axis. 
Usage| Returns  
---|---  
`ee.Array.cat(arrays,  _axis_)`| Array  
Argument| Type| Details  
---|---|---  
`arrays`| List| Arrays to concatenate.  
`axis`| Integer, default: 0| Axis to concatenate along.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-cat#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-cat#colab-python-sample) More
```
// Requires an explicit PixelType if no data.
varempty=ee.Array([],ee.PixelType.int8());// Empty []
varone=ee.Array([1]);
vartwo=ee.Array([2]);
print(ee.Array.cat([empty]));// []
print(ee.Array.cat([empty,empty]));// []
print(ee.Array.cat([empty,one]));// [1]
print(ee.Array.cat([one,empty]));// [1]
print(ee.Array.cat([one,two]));// [1, 2]
print(ee.Array.cat([one,two],0));// [1, 2]
print(ee.Array.cat([one,two],1));// [[1,2]]
vara=ee.Array([0,1,2]);
varb=ee.Array([3,4,5]);
print(ee.Array.cat([a,b]));// [0,1,2,3,4,5]
print(ee.Array.cat([a,b],0));// [0,1,2,3,4,5]
print(ee.Array.cat([a,b],1));// [[0,3],[1,4],[2,5]]
varc=ee.Array([[0],[1],[2]]);
vard=ee.Array([[3],[4],[5]]);
print(ee.Array.cat([c,d]));// [[0],[1],[2],[3],[4],[5]]
print(ee.Array.cat([c,d],0));// [[0],[1],[2],[3],[4],[5]]
print(ee.Array.cat([c,d],1));// [[0,3],[1,4],[2,5]]
print(ee.Array.cat([c,d],2));// [[[0,3]],[[1,4]],[[2,5]]]
vare=ee.Array([[[0,1],[2,3]],[[4,5],[6,7]]]);
varf=ee.Array([[[10,11],[12,13]],[[14,15],[16,17]]]);
// [[[0,1],[2,3]]
// [[4,5],[6,7]]
// [[10,11],[12,13]]
// [[14,15],[16,17]]
print(ee.Array.cat([e,f],0));
// [[[0,1],[2,3],[10,11],[12,13]]
// [[4,5],[6,7],[14,15],[16,17]]]
print(ee.Array.cat([e,f],1));
// [[[0,1,10,11],[2,3,12,13]]
// [[4,5,14,15],[6,7,16,17]]]
print(ee.Array.cat([e,f],2));
// [[[[0,10],[1,11]],[[2,12],[3,13]]]
// [[[4,14],[5,15]],[[6,16],[7,17]]]]
print(ee.Array.cat([e,f],3));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Requires an explicit PixelType if no data.
empty = ee.Array([], ee.PixelType.int8()) # []
one = ee.Array([1])
two = ee.Array([2])
display(ee.Array.cat([empty])) # []
display(ee.Array.cat([empty, empty])) # []
display(ee.Array.cat([empty, one])) # [1]
display(ee.Array.cat([one, empty])) # [1]
display(ee.Array.cat([one, two])) # [1, 2]
display(ee.Array.cat([one, two], 0)) # [1, 2]
display(ee.Array.cat([one, two], 1)) # [[1, 2]]
a = ee.Array([0, 1, 2])
b = ee.Array([3, 4, 5])
display(ee.Array.cat([a, b])) # [0, 1, 2, 3, 4, 5]
display(ee.Array.cat([a, b], 0)) # [0, 1, 2, 3, 4, 5]
display(ee.Array.cat([a, b], 1)) # [[0, 3], [1, 4], [2, 5]]
c = ee.Array([[0], [1], [2]])
d = ee.Array([[3], [4], [5]])
display(ee.Array.cat([c, d])) # [[0], [1], [2], [3], [4], [5]]
display(ee.Array.cat([c, d], 0)) # [[0], [1], [2], [3], [4], [5]]
display(ee.Array.cat([c, d], 1)) # [[0, 3], [1, 4], [2, 5]]
display(ee.Array.cat([c, d], 2)) # [[[0, 3]], [[1, 4]], [[2, 5]]]
e = ee.Array([[[0, 1], [2, 3]], [[4, 5], [6, 7]]])
f = ee.Array([[[10, 11], [12, 13]], [[14, 15], [16, 17]]])
# [[[0, 1], [2, 3]]
# [[4, 5], [6, 7]]
# [[10, 11], [12, 13]]
# [[14, 15], [16, 17]]
display(ee.Array.cat([e, f], 0))
# [[[0, 1], [2, 3], [10, 11], [12, 13]]
# [[4, 5], [6, 7], [14, 15], [16, 17]]]
display(ee.Array.cat([e, f], 1))
# [[[0, 1, 10, 11], [2, 3, 12, 13]]
# [[4, 5, 14, 15], [6, 7, 16, 17]]]
display(ee.Array.cat([e, f], 2))
# [[[[0, 10], [1, 11]], [[2, 12], [3, 13]]]
# [[[4, 14], [5, 15]], [[6, 16], [7, 17]]]]
display(ee.Array.cat([e, f], 3))
```

