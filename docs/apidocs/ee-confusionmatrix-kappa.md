 
#  ee.ConfusionMatrix.kappa 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-confusionmatrix-kappa#examples)


Computes the Kappa statistic for the confusion matrix. 
Usage| Returns  
---|---  
`ConfusionMatrix.kappa()`| Float  
Argument| Type| Details  
---|---|---  
this: `confusionMatrix`| ConfusionMatrix  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-confusionmatrix-kappa#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-confusionmatrix-kappa#colab-python-sample) More
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
print("Constructed confusion matrix",confusionMatrix);
// Calculate overall accuracy.
print("Overall accuracy",confusionMatrix.accuracy());
// Calculate consumer's accuracy, also known as user's accuracy or
// specificity and the complement of commission error (1 − commission error).
print("Consumer's accuracy",confusionMatrix.consumersAccuracy());
// Calculate producer's accuracy, also known as sensitivity and the
// compliment of omission error (1 − omission error).
print("Producer's accuracy",confusionMatrix.producersAccuracy());
// Calculate kappa statistic.
print('Kappa statistic',confusionMatrix.kappa());
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
frompprintimport pprint
# Construct a confusion matrix from an array (rows are actual values,
# columns are predicted values). We construct a confusion matrix here for
# brevity and clear visualization, in most applications the confusion matrix
# will be generated from ee.Classifier.confusionMatrix.
array = ee.Array([[32, 0, 0, 0, 1, 0],
         [ 0, 5, 0, 0, 1, 0],
         [ 0, 0, 1, 3, 0, 0],
         [ 0, 1, 4, 26, 8, 0],
         [ 0, 0, 0, 7, 15, 0],
         [ 0, 0, 0, 1, 0, 5]])
confusion_matrix = ee.ConfusionMatrix(array)
print("Constructed confusion matrix:")
pprint(confusion_matrix.getInfo())
# Calculate overall accuracy.
print("Overall accuracy:", confusion_matrix.accuracy().getInfo())
# Calculate consumer's accuracy, also known as user's accuracy or
# specificity and the complement of commission error (1 − commission error).
print("Consumer's accuracy:")
pprint(confusion_matrix.consumersAccuracy().getInfo())
# Calculate producer's accuracy, also known as sensitivity and the
# compliment of omission error (1 − omission error).
print("Producer's accuracy:")
pprint(confusion_matrix.producersAccuracy().getInfo())
# Calculate kappa statistic.
print("Kappa statistic:", confusion_matrix.kappa().getInfo())
```

