 
#  ee.ConfusionMatrix
Stay organized with collections  Save and categorize content based on your preferences. 
Creates a confusion matrix. Axis 0 (the rows) of the matrix correspond to the actual values, and Axis 1 (the columns) to the predicted values. Usage| Returns  
---|---  
`ee.ConfusionMatrix(array,  _order_)`| ConfusionMatrix  
Argument| Type| Details  
---|---|---  
`array`| Object| A square, 2D array of integers, representing the confusion matrix. Note that unlike the ee.Array constructor, this argument cannot take a list.  
`order`| List, default: null| The row and column size and order, for non-contiguous or non-zero based matrices.  
## Examples
### Code Editor (JavaScript)
```
// A confusion matrix. Rows correspond to actual values, columns to
// predicted values.
vararray=ee.Array([[32,0,0,0,1,0],
[0,5,0,0,1,0],
[0,0,1,3,0,0],
[0,1,4,26,8,0],
[0,0,0,7,15,0],
[0,0,0,1,0,5]]);
print('Constructed confusion matrix',
ee.ConfusionMatrix(array));
// The "order" parameter refers to row and column class labels. When
// unspecified, the class labels are assumed to be a 0-based sequence
// incrementing by 1 with a length equal to row/column size.
print('Default row/column labels (unspecified "order" parameter)',
ee.ConfusionMatrix({array:array,order:null}).order());
// Set the "order" parameter when custom class label integers are required. The
// list of integer value labels should correspond to the matrix axes left to
// right / top to bottom.
varorder=[11,22,42,52,71,81];
print('Specified row/column labels (specified "order" parameter)',
ee.ConfusionMatrix({array:array,order:order}).order());
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
frompprintimport pprint
# A confusion matrix. Rows correspond to actual values, columns to
# predicted values.
array = ee.Array([[32, 0, 0, 0, 1, 0],
         [ 0, 5, 0, 0, 1, 0],
         [ 0, 0, 1, 3, 0, 0],
         [ 0, 1, 4, 26, 8, 0],
         [ 0, 0, 0, 7, 15, 0],
         [ 0, 0, 0, 1, 0, 5]])
print('Constructed confusion matrix:')
pprint(ee.ConfusionMatrix(array).getInfo())
# The "order" parameter refers to row and column class labels. When
# unspecified, the class labels are assumed to be a 0-based sequence
# incrementing by 1 with a length equal to row/column size.
print('Default row/column labels (unspecified "order" parameter):',
   ee.ConfusionMatrix(array, None).order().getInfo())
# Set the "order" parameter when custom class label integers are required. The
# list of integer value labels should correspond to the matrix axes left to
# right / top to bottom.
order = [11, 22, 42, 52, 71, 81]
print('Specified row/column labels (specified "order" parameter):',
   ee.ConfusionMatrix(array, order).order().getInfo())
```

