 
#  Machine Learning in Earth Engine
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Machine Learning APIs](https://developers.google.com/earth-engine/guides/machine-learning#machine-learning-apis)
  * [Training and Prediction outside Earth Engine](https://developers.google.com/earth-engine/guides/machine-learning#training-and-prediction-outside-earth-engine)
    * [Exporting Data from Earth Engine for Training](https://developers.google.com/earth-engine/guides/machine-learning#exporting-data-from-earth-engine-for-training)
    * [Getting Predictions from a Model outside Earth Engine](https://developers.google.com/earth-engine/guides/machine-learning#getting-predictions-from-a-model-outside-earth-engine)
    * [Other Reasons to train models outside Earth Engine](https://developers.google.com/earth-engine/guides/machine-learning#other-reasons-to-train-models-outside-earth-engine)


**Note:** This overview assumes familiarity with basic Machine Learning (ML) concepts like training, prediction and models. The introduction to Machine Learning video on this page provides an introduction to these concepts. Alternatively, please take a look at Google's [ Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course). 
## Machine Learning APIs
Machine Learning (ML) is a powerful technique for analyzing Earth Observation data. Earth Engine has built-in capabilities to allow users to build and use ML models for common scenarios with easy-to-use APIs. 
A common ML task is to classify the pixels in satellite imagery into two or more categories. The approach is useful for Land Use Land Cover mapping and other popular applications. 
  * **Supervised Classification:** One ML technique for classifying land is to use ground truth examples to teach a model to differentiate between classes. Earth Engine's built-in [supervised classifiers](https://developers.google.com/earth-engine/guides/classification) support this process. 
  * **Unsupervised Classification:** In unsupervised classification, no ground truth examples are provided to the training algorithm. Instead, the algorithm divides the available data into clusters based on inherent differences. Earth Engine's [unsupervised classifiers](https://developers.google.com/earth-engine/guides/clustering) are particularly useful when no ground truth data exists, when you do not know the final number of classes or when you want to do quick experimentation. 
  * **Regression:** Whereas a classification model attempts to bucket each input into a discrete class, a regression model attempts to predict a continuous variable for each input. For example, a regression model could predict water quality, percent forest cover, percent cloud cover or crop yield. For more information, please refer to the [Linear Regression section of ee.Reducers](https://developers.google.com/earth-engine/guides/reducers_regression). 


## Training and Prediction outside Earth Engine
Deep learning and neural networks are machine-learning techniques that can work well for complex data like satellite imagery. Neither deep learning nor neural networks are supported in Earth Engine's Machine Learning APIs. Instead, to take advantage of them, you will need to use a framework like TensorFlow or PyTorch and train your model outside of Earth Engine. 
You may also want to train outside of Earth Engine if you are already familiar with a framework like scikit-learn for classical machine learning or XGBoost for gradient boosted decision trees. 
Finally, you may want to train a model outside Earth Engine if your data set is very large and exceeds the limits documented below. 
**Note:** Training and prediction outside of Earth Engine require working with products that may require payment for both commercial and non-commercial use. Additionally, they require knowledge of Google Cloud Platform. 
### Exporting Data from Earth Engine for Training
  * The [TFRecord data format](https://developers.google.com/earth-engine/guides/tfrecord) is optimized for training in TensorFlow. The [ machine learning examples page includes several TensorFlow workflows](https://developers.google.com/earth-engine/guides/ml_examples) that demonstrate how to train a model using TFRecords. 
  * Alternatively, for an example of how to download data using Apache Beam, hosted in Google Cloud Dataflow, then train in Vertex AI using TensorFlow, please visit the [Land Cover Classification tutorial](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/people-and-planet-ai/land-cover-classification) and follow along with a [colab notebook.](https://colab.research.google.com/github/GoogleCloudPlatform/python-docs-samples/blob/main/people-and-planet-ai/land-cover-classification/README.ipynb)


### Getting Predictions from a Model outside Earth Engine
If you train a model outside Earth Engine, you have a few options for getting predictions from that model. 
  * Earth Engine's `ee.Model` package allows for predictions using data in Earth Engine and a trained model hosted on Google's Vertex AI. You can host your custom trained model in Vertex AI and perform inference directly in Earth Engine using [`ee.Model.fromVertexAi`](https://developers.google.com/earth-engine/apidocs/ee-model-fromvertexai). See [Connecting to models hosted on Vertex AI](https://developers.google.com/earth-engine/guides/ee-vertex#connecting-to-models-hosted-on-vertex-ai) for more information. 
  * Alternatively, the [Land Cover Classification tutorial](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/people-and-planet-ai/land-cover-classification) demonstrates how you can do predictions using a cloud service like Cloud Functions. 


### Other Reasons to train models outside Earth Engine
In addition to familiarity and preference, you may want to train a model outside Earth Engine if you want to use model architectures (e.g. convolutional neural networks) that are not supported by Earth Engine's Machine Learning APIs, if you want to use more features of Vertex AI or if you encounter scaling limits with Earth Engine's Machine Learning APIs. 
#### Training Set Limits
Training using `ee.Classifier` or `ee.Clusterer` is generally effective with datasets up to 100 MB. As a very rough guideline, assuming 32-bit (i.e. float) precision, this can accommodate training datasets that satisfy (where _n_ is the number of examples and _b_ is the number of bands): 
_nb ≤ (100 * 2 20) / 4_
As one example, if you train using 100 bands, the number of examples used for training should be less than 200,000. 
#### Inference Limits
Since Earth Engine processes 256x256 image tiles, inference requests on imagery must have fewer than 400 bands (again, assuming 32-bit precision of the imagery). 
You can retrain a classifier more than once to keep the dataset for each training run within limits. 
```
vartrainings=ee.List.sequence(0,3).map(function(cover){
returnimage.addBands(landcover.eq(cover).stratifiedSample(…)
})

varclassifier=ee.Classifier.smileCart()
.train(trainings.get(0),"cover")
.train(trainings.get(1),"cover")
.train(trainings.get(2),"cover")
.train(trainings.get(3),"cover")

```

#### Limits on Model Size
Additionally, the model itself must be less than 100 MB. Many of our classifiers can be configured to limit their complexity and hence, size. For example: 
```
varclassifier=ee.Classifier.smileRandomForest({
numberOfTrees:10,
minLeafPopulation:10,
maxNodes:10000
})

```

