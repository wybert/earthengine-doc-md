 
#  ee.ConfusionMatrix.order
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-confusionmatrix-order#examples)


Returns the name and order of the rows and columns of the matrix.
Usage | Returns  
---|---  
`ConfusionMatrix.order()` | List  
Argument | Type | Details  
---|---|---  
this: `confusionMatrix` | ConfusionMatrix |   
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-confusionmatrix-order#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-confusionmatrix-order#colab-python-sample) More
```
// Construct an error/confusion matrix from an array (rows are actual values,
// columns are predicted values). We construct an error matrix here for brevity
// and matrix visualization, in most applications the confusion matrix will be
// generated from ee.Classifier.confusionMatrix.
vararray=ee.Array([[32,0,0,0,1,0],
[0,5,0,0,1,0],
[0,0,1,3,0,0],
[0,1,4,26,8,0],
[0,0,0,7,15,0],
[0,0,0,1,0,5]]);

varcmDefaultOrder=ee.ConfusionMatrix(array);
print('Default name and order of the rows and columns',
cmDefaultOrder.order());

varorder=[11,22,42,52,71,81];
varcmSpecifiedOrder=ee.ConfusionMatrix({array:array,order:order});
print('Specified name and order of the rows and columns',
cmSpecifiedOrder.order());
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Construct an error/confusion matrix from an array (rows are actual values,
# columns are predicted values). We construct an error matrix here for brevity
# and matrix visualization, in most applications the confusion matrix will be
# generated from ee.Classifier.confusionMatrix.
array = ee.Array([[32, 0, 0,  0,  1, 0],
                  [ 0, 5, 0,  0,  1, 0],
                  [ 0, 0, 1,  3,  0, 0],
                  [ 0, 1, 4, 26,  8, 0],
                  [ 0, 0, 0,  7, 15, 0],
                  [ 0, 0, 0,  1,  0, 5]])

cm_default_order = ee.ConfusionMatrix(array)
print('Default name and order of the rows and columns:',
      cm_default_order.order().getInfo())

order = [11, 22, 42, 52, 71, 81]
cm_specified_order = ee.ConfusionMatrix(array, order)
print('Specified name and order of the rows and columns:',
      cm_specified_order.order().getInfo())
```

Was this helpful?
