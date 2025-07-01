 
#  ee.Array
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array#examples)


Returns an array with the given coordinates. 
Usage| Returns  
---|---  
`ee.Array(values,  _pixelType_)`| Array  
Argument| Type| Details  
---|---|---  
`values`| Object| An existing array to cast, or a number/list of numbers/nested list of numbers of any depth to create an array from. For nested lists, all inner arrays at the same depth must have the same length and numbers may only be present at the deepest level.  
`pixelType`| PixelType, default: null| The type of each number in the values argument. If the pixel type is not provided, it will be inferred from the numbers in 'values'. If there aren't any numbers in 'values', this type must be provided.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array#colab-python-sample) More
```
// Requires an explicit PixelType if no data.
print(ee.Array([],ee.PixelType.int8()));// Empty []
print(ee.Array([[]],ee.PixelType.uint8()));// Empty [[]]
print(ee.Array([[],[]],ee.PixelType.float()));// Empty [[], []]
// 1-D Arrays
print(ee.Array([0]));// [0]
print(ee.Array([0,1]));// [0, 1]
// 2-D Arrays
print(ee.Array([[1]]));// [[1]]
print(ee.Array([[0,1],[2,3]]));// [[0,1],[2,3]]
// Arrays from ee.Number.
print(ee.Array([ee.Number(123).toUint8()]));// [123]
// Lists are useful ways to construct larger Arrays.
print(ee.Array(ee.List.sequence(0,10,2)));// // [0,2,4,6,8,10]
// Arrays can be used to make Arrays.
vararray1D=ee.Array([1,2,3]);
// This is a cast.
print(ee.Array(array1D));// [1,2,3]
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Requires an explicit PixelType if no data.
print(ee.Array([], ee.PixelType.int8()).getInfo()) # Empty []
print(ee.Array([[]], ee.PixelType.uint8()).getInfo()) # Empty [[]]
print(ee.Array([[], []], ee.PixelType.float()).getInfo()) # Empty [[], []]
# 1-D Arrays
print(ee.Array([0]).getInfo()) # [0]
print(ee.Array([0, 1]).getInfo()) # [0, 1]
# 2-D Arrays
print(ee.Array([[1]]).getInfo()) # [[1]]
print(ee.Array([[0, 1], [2, 3]]).getInfo()) # [[0,1],[2,3]]
# Arrays from ee.Number.
print(ee.Array([ee.Number(123).toUint8()]).getInfo()) # [123]
# Lists are useful ways to construct larger Arrays.
print(ee.Array(ee.List.sequence(0, 10, 2)).getInfo()) # [0, 2, 4, 6, 8, 10]
# Arrays can be used to make Arrays.
array_one = ee.Array([1, 2, 3])
# This is a cast.
print(ee.Array(array_one).getInfo()) # [1, 2, 3]
```

