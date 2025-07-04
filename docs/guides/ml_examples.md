 
#  Vertex AI example workflows
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Costs](https://developers.google.com/earth-engine/guides/ml_examples#costs)
  * [AutoML](https://developers.google.com/earth-engine/guides/ml_examples#automl)
    * [Low-code Crop Classification](https://developers.google.com/earth-engine/guides/ml_examples#low-code-crop-classification)
  * [PyTorch](https://developers.google.com/earth-engine/guides/ml_examples#pytorch)
    * [Landcover Classification with a CNN](https://developers.google.com/earth-engine/guides/ml_examples#landcover-classification-with-a-cnn)
  * [Tensorflow](https://developers.google.com/earth-engine/guides/ml_examples#tensorflow)
    * [Multi-class prediction with a DNN from scratch](https://developers.google.com/earth-engine/guides/ml_examples#multi-class-prediction-with-a-dnn-from-scratch)
    * [Multi-class prediction with a DNN hosted on Vertex AI](https://developers.google.com/earth-engine/guides/ml_examples#multi-class-prediction-with-a-dnn-hosted-on-vertex-ai)
    * [Semantic segmentation with an FCNN trained and hosted on Vertex AI](https://developers.google.com/earth-engine/guides/ml_examples#semantic-segmentation-with-an-fcnn-trained-and-hosted-on-vertex-ai)
    * [Host a Pre-trained Tree-crown Segmentation Model](https://developers.google.com/earth-engine/guides/ml_examples#host-a-pre-trained-tree-crown-segmentation-model)
    * [Yggdrasil Decision Forests (YDF)](https://developers.google.com/earth-engine/guides/ml_examples#yggdrasil-decision-forests-ydf)
  * [Deprecated](https://developers.google.com/earth-engine/guides/ml_examples#deprecated)
    * [TensorFlow Decision Forests](https://developers.google.com/earth-engine/guides/ml_examples#tensorflow-decision-forests)
    * [Regression with an FCNN](https://developers.google.com/earth-engine/guides/ml_examples#regression-with-an-fcnn)
    * [Training on AI Platform](https://developers.google.com/earth-engine/guides/ml_examples#training-on-ai-platform)


The examples on this page demonstrate uses of Vertex AI with Earth Engine. See [the hosted models page](https://developers.google.com/earth-engine/guides/tensorflow-vertex) for details. These examples use the [Earth Engine Python API](https://developers.google.com/earth-engine/guides/python_install) running in [Colab Notebooks](https://colab.research.google.com/). 
## Costs
**Warning!** These guides use billable components of Google Cloud including: 
  * Vertex AI ([pricing](https://cloud.google.com/vertex-ai/pricing))
  * Cloud Storage ([pricing](https://cloud.google.com/storage/pricing))
  * Earth Engine ([pricing (commercial)](https://earthengine.google.com/commercial))


You can use the [Pricing Calculator](https://cloud.google.com/products/calculator) to generate a cost estimate based on your projected usage.
## AutoML
### Low-code Crop Classification
AutoML enables creating and training a model with minimal technical effort. This example demonstrates training and deploying an AutoML Tabular model using the Vertex AI Python SDK and then connecting to it from Earth Engine to classify crop types from National Agriculture Imagery Program (NAIP) aerial imagery. 
[ ![Colab logo](https://developers.google.com/static/earth-engine/images/colab_logo_32px.png) Run in Google Colab ](https://colab.research.google.com/github/google/earthengine-community/blob/master/guides/linked/Earth_Engine_AutoML_Vertex_AI.ipynb) |  [ ![GitHub logo](https://developers.google.com/static/earth-engine/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/earthengine-community/blob/master/guides/linked/Earth_Engine_AutoML_Vertex_AI.ipynb)  
---|---  
## PyTorch
### Landcover Classification with a CNN
This example demonstrates a simple CNN which takes several spectral vectors as inputs (i.e. one pixel at a time) and outputs a single class label per-pixel. The Colab notebook demonstrates creating the CNN, training it with data from Earth Engine, deploying the model to Vertex AI, and getting predictions from the model in Earth Engine. 
[ ![Colab logo](https://developers.google.com/static/earth-engine/images/colab_logo_32px.png) Run in Google Colab ](https://colab.research.google.com/github/google/earthengine-community/blob/master/guides/linked/Earth_Engine_PyTorch_Vertex_AI.ipynb) |  [ ![GitHub logo](https://developers.google.com/static/earth-engine/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/earthengine-community/blob/master/guides/linked/Earth_Engine_PyTorch_Vertex_AI.ipynb)  
---|---  
## Tensorflow
### Multi-class prediction with a DNN from scratch
A "deep" neural network (DNN) is an artificial neural network (ANN) with one or more hidden layers. This example demonstrates a simple DNN with a single hidden layer. The DNN takes spectral vectors as inputs (i.e. one pixel at a time) and outputs a single class label and class probabilities per pixel. The Colab notebook demonstrates creating the DNN, training it with data from Earth Engine, making predictions on exported imagery and importing the predictions to Earth Engine. 
[ ![Colab logo](https://developers.google.com/static/earth-engine/images/colab_logo_32px.png) Run in Google Colab ](https://colab.research.google.com/github/google/earthengine-community/blob/master/guides/linked/Earth_Engine_TensorFlow_DNN_from_scratch.ipynb) |  [ ![GitHub logo](https://developers.google.com/static/earth-engine/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/earthengine-community/blob/master/guides/linked/Earth_Engine_TensorFlow_DNN_from_scratch.ipynb)  
---|---  
### Multi-class prediction with a DNN hosted on Vertex AI
You can get predictions from a model hosted on [Vertex AI](https://cloud.google.com/vertex-ai) directly in Earth Engine (e.g. in the [Code Editor](https://developers.google.com/earth-engine/guides/playground)). This guide demonstrates how to train, save and prepare a TensorFlow model for hosting, deploy the model to a Vertex AI endpoint and get and get a map of interactive model predictions from Earth Engine. 
[ ![Colab logo](https://developers.google.com/static/earth-engine/images/colab_logo_32px.png) Run in Google Colab ](https://colab.research.google.com/github/google/earthengine-community/blob/master/guides/linked/Earth_Engine_TensorFlow_Vertex_AI.ipynb) |  [ ![GitHub logo](https://developers.google.com/static/earth-engine/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/earthengine-community/blob/master/guides/linked/Earth_Engine_TensorFlow_Vertex_AI.ipynb)  
---|---  
### Semantic segmentation with an FCNN trained and hosted on Vertex AI
This guide demonstrates semantic segmentation for land cover mapping. Details on the inputs or training data are in this [2022 Geo for Good session](https://earthoutreachonair.withgoogle.com/events/geoforgood22?talk=day1-trackthree-talk2). Powered by data from Earth Engine, this guide shows how to train a model on Vertex AI using a custom machine, prepare the model for hosting, deploy the model to an endpoint and get and get a map of interactive model predictions from Earth Engine. 
[ ![Colab logo](https://developers.google.com/static/earth-engine/images/colab_logo_32px.png) Run in Google Colab ](https://colab.research.google.com/github/google/earthengine-community/blob/master/guides/linked/Earth_Engine_Vertex_AI_training_demo.ipynb) |  [ ![GitHub logo](https://developers.google.com/static/earth-engine/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/earthengine-community/blob/master/guides/linked/Earth_Engine_Vertex_AI_training_demo.ipynb)  
---|---  
### Host a Pre-trained Tree-crown Segmentation Model
You can host pretrained models to get interactive predictions in Earth Engine. For example, [Li et al. (2023)](https://doi.org/10.1093/pnasnexus/pgad076) published several tree-crown segmentation models implemented in TensorFlow. If the inputs and outputs are shaped accordingly, these models can be hosted directly and used to get predictions in Earth Engine wherever there's input imagery. This guide demonstrates how to download a pre-trained model, prepare it for hosting on Vertex AI, and get predictions on imagery in the Earth Engine public catalog. 
[ ![Colab logo](https://developers.google.com/static/earth-engine/images/colab_logo_32px.png) Run in Google Colab ](https://colab.research.google.com/github/google/earthengine-community/blob/master/guides/linked/Earth_Engine_TensorFlow_tree_counting_model.ipynb) |  [ ![GitHub logo](https://developers.google.com/static/earth-engine/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/earthengine-community/blob/master/guides/linked/Earth_Engine_TensorFlow_tree_counting_model.ipynb)  
---|---  
### Yggdrasil Decision Forests (YDF)
[Yggdrasil Decision Forests (YDF)](https://ydf.readthedocs.io/en/latest/) is an implementation of popular tree-based machine learning models compatible with TensorFlow. These models can be trained, saved and hosted on Vertex AI, as with neural networks. This notebook demonstrates how to install YDF, train a simple model, host the model on Vertex AI and get interactive predictions in Earth Engine. 
[ ![Colab logo](https://developers.google.com/static/earth-engine/images/colab_logo_32px.png) Run in Google Colab ](https://colab.research.google.com/github/google/earthengine-community/blob/master/guides/linked/Yggdrasil_decision_forests_earthengine_vertex_ai.ipynb) |  [ ![GitHub logo](https://developers.google.com/static/earth-engine/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/earthengine-community/blob/master/guides/linked/Yggdrasil_decision_forests_earthengine_vertex_ai.ipynb)  
---|---  
## Deprecated
**Deprecated!** This guide uses datasets that may be removed from the Earth Engine catalog and/or methods that may be removed in future versions of the used APIs. 
### TensorFlow Decision Forests
[TensorFlow Decision Forests (TF-DF)](https://www.tensorflow.org/decision_forests) is an implementation of popular tree-based machine learning models in TensorFlow. These models can be trained, saved and hosted on Vertex AI, as with TensorFlow neural networks. This notebook demonstrates how to install TF-DF, train a random forest, host the model on Vertex AI and get interactive predictions in Earth Engine. 
[ ![Colab logo](https://developers.google.com/static/earth-engine/images/colab_logo_32px.png) Run in Google Colab ](https://colab.research.google.com/github/google/earthengine-community/blob/master/guides/linked/Earth_Engine_TensorFlow_Decision_Forests.ipynb) |  [ ![GitHub logo](https://developers.google.com/static/earth-engine/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/earthengine-community/blob/master/guides/linked/Earth_Engine_TensorFlow_Decision_Forests.ipynb)  
---|---  
### Regression with an FCNN
**Deprecated!** This guide uses datasets that may be removed from the Earth Engine catalog and/or methods that may be removed in future versions of the Earth Engine API.
A "convolutional" neural network (CNN) contains one or more convolutional layers, in which inputs are neighborhoods of pixels, resulting in a network that is not fully-connected, but is suited to identifying spatial patterns. A fully convolutional neural network (FCNN) does not contain a fully-connected layer as output. This means that it does not learn a global output (i.e. a single output per image), but rather localized outputs (i.e. per-pixel).
This Colab notebook demonstrates the use of the [UNET model](https://arxiv.org/abs/1505.04597), an FCNN developed for medical image segmentation, for predicting a continuous [0,1] output in each pixel from 256x256 neighborhoods of pixels. Specifically, this example shows how to export patches of data to train the network and how to overtile image patches for inference, to eliminate tile boundary artifacts. 
[ ![Colab logo](https://developers.google.com/static/earth-engine/images/colab_logo_32px.png) Run in Google Colab ](https://colab.research.google.com/github/google/earthengine-community/blob/master/guides/linked/UNET_regression_demo.ipynb) |  [ ![GitHub logo](https://developers.google.com/static/earth-engine/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/earthengine-community/blob/master/guides/linked/UNET_regression_demo.ipynb)  
---|---  
### Training on AI Platform
**Deprecated!** This guide uses datasets that may be removed from the Earth Engine catalog and/or methods that may be removed in future versions of the Earth Engine API.
For relatively large models (like the FCNN example), the longevity of the free virtual machine on which Colab notebooks run may not be sufficient for a long-running training job. Specifically, if the expected prediction error is not minimized on the evaluation dataset, then more training iterations may be prudent. For performing large training jobs in the Cloud, this Colab notebook demonstrates how to [package your training code](https://cloud.google.com/ml-engine/docs/packaging-trainer), [start a training job](https://cloud.google.com/ml-engine/docs/training-jobs), prepare a [`SavedModel`](https://cloud.google.com/ml-engine/docs/tensorflow/exporting-for-prediction) with the `earthengine model prepare` command, and get predictions in Earth Engine interactively with `ee.Model.fromAiPlatformPredictor`. 
[ ![Colab logo](https://developers.google.com/static/earth-engine/images/colab_logo_32px.png) Run in Google Colab ](https://colab.research.google.com/github/google/earthengine-community/blob/master/guides/linked/AI_platform_demo.ipynb) |  [ ![GitHub logo](https://developers.google.com/static/earth-engine/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/earthengine-community/blob/master/guides/linked/AI_platform_demo.ipynb)  
---|---  
Was this helpful?
