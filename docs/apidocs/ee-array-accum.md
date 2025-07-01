 
#  ee.Array.accum
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-accum#examples)


Accumulates elements of an array along the given axis, by setting each element of the result to the reduction of elements along that axis up to and including the current position. May be used to make a cumulative sum, a monotonically increasing sequence, etc. 
Usage| Returns  
---|---  
`Array.accum(axis,  _reducer_)`| Array  
Argument| Type| Details  
---|---|---  
this: `array`| Array| Array to accumulate.  
`axis`| Integer| Axis along which to perform the accumulation.  
`reducer`| Reducer, default: null| Reducer to accumulate values. Default is SUM, to produce the cumulative sum of each vector along the given axis.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-accum#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-accum#colab-python-sample) More
```
print(ee.Array([-1]).accum(0));// [-1]
print(ee.Array([-2,1]).accum(0));// [-2, -1]
print(ee.Array([-2,1,9]).accum(0));// [-2, -1, 8]
// accum over 2D arrays with different axes.
print(ee.Array([[1,3],[5,7]]).accum(0));// [[1,3],[6,10]]
print(ee.Array([[1,3],[5,7]]).accum(1));// [[1,4],[5,12]]
// sum is the default reducer.
print(ee.Array([2,-2,3,1]).accum(0));// [2,0,3,4]
print(ee.Array([2,-2,3,1]).accum(0,ee.Reducer.sum()));// [2,0,3,4]
// Some example reducers.
print(ee.Array([2,-2,3,1]).accum(0,ee.Reducer.max()));// [2,2,3,3]
print(ee.Array([2,-2,3,1]).accum(0,ee.Reducer.mean()));// [2,0,1,1]
print(ee.Array([2,-2,3,1]).accum(0,ee.Reducer.min()));// [2,-2,-2,-2]
print(ee.Array([2,-2,3]).accum(0,ee.Reducer.product()));// [2,-4,-12]
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
display(ee.Array([-1]).accum(0)) # [-1]
display(ee.Array([-2, 1]).accum(0)) # [-2, -1]
display(ee.Array([-2, 1, 9]).accum(0)) # [-2, -1, 8]
# accum over 2D arrays with different axes.
display(ee.Array([[1, 3], [5, 7]]).accum(0)) # [[1, 3],[6, 10]]
display(ee.Array([[1, 3], [5, 7]]).accum(1)) # [[1, 4],[5, 12]]
# sum is the default reducer.
display(ee.Array([2, -2, 3, 1]).accum(0)) # [2, 0, 3, 4]
# [2, 0, 3, 4]
display(ee.Array([2, -2, 3, 1]).accum(0, ee.Reducer.sum()))

# Some example reducers.
# [2, 2, 3, 3]
display(ee.Array([2, -2, 3, 1]).accum(0, ee.Reducer.max()))

# [2, 0, 1, 1]
display(ee.Array([2, -2, 3, 1]).accum(0, ee.Reducer.mean()))
# [2, -2, -2, -2]
display(ee.Array([2, -2, 3, 1]).accum(0, ee.Reducer.min()))
# [2, -4, -12]
display(ee.Array([2, -2, 3]).accum(0, ee.Reducer.product()))
```

Was this helpful?
