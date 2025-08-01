 
#  ee.ConfusionMatrix.array
Stay organized with collections  Save and categorize content based on your preferences. 
Returns a confusion matrix as an Array. Usage | Returns  
---|---  
`ConfusionMatrix.array()` | Array  
Argument | Type | Details  
---|---|---  
this: `confusionMatrix` | ConfusionMatrix |   
## Examples
### Code Editor (JavaScript)
```
// Construct a confusion matrix from an array (rows are actual values,
// columns are predicted values). We construct a confusion matrix here for
// brevity and clear visualization, in most applications the confusion matrix
// will be generated from ee.Classifier.confusionMatrix.
vararray=ee.Array([[32,0,0,0,1,0],
[0,5,0,0,1,0],
[0,0,1,3,0,0],
[0,1,4,26,8,0],
[0,0,0,7,15,0],
[0,0,0,1,0,5]]);
varconfusionMatrix=ee.ConfusionMatrix(array);
print("ee.ConfusionMatrix",confusionMatrix);

print("ee.ConfusionMatrix as ee.Array",confusionMatrix.array());
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

# Construct a confusion matrix from an array (rows are actual values,
# columns are predicted values). We construct a confusion matrix here for
# brevity and clear visualization, in most applications the confusion matrix
# will be generated from ee.Classifier.confusionMatrix.
array = ee.Array([[32, 0, 0,  0,  1, 0],
                  [ 0, 5, 0,  0,  1, 0],
                  [ 0, 0, 1,  3,  0, 0],
                  [ 0, 1, 4, 26,  8, 0],
                  [ 0, 0, 0,  7, 15, 0],
                  [ 0, 0, 0,  1,  0, 5]])
confusion_matrix = ee.ConfusionMatrix(array)
print("ee.ConfusionMatrix:")
pprint(confusion_matrix.getInfo())

print("ee.ConfusionMatrix as ee.Array:")
pprint(confusion_matrix.array().getInfo())
```

