 
#  Predictions from Hosted Models 
Stay organized with collections  Save and categorize content based on your preferences. 
Earth Engine provides `ee.Model` as a connector to models hosted on [Vertex AI](https://cloud.google.com/vertex-ai/docs/start/introduction-unified-platform). Earth Engine will send image or table data as online prediction requests to a trained model deployed on a Vertex AI endpoint. The model outputs are then available as Earth Engine images or tables.
## TensorFlow Models
[TensorFlow](https://www.tensorflow.org/) is an open source machine learning (ML) platform that supports advanced ML methods such as deep learning. The Earth Engine API provides methods for importing and or exporting imagery, training and testing data in TFRecord format. See the [ML examples page](https://developers.google.com/earth-engine/guides/ml_examples) for demonstrations that use TensorFlow with data from Earth Engine. See the [TFRecord page](https://developers.google.com/earth-engine/guides/tfrecord) for details about how Earth Engine writes data to TFRecord files.
## `ee.Model`
The `ee.Model` package handles interaction with hosted machine learning models.
### Hosted Models on Vertex AI
A new `ee.Model` instance can be created with [ee.Model.fromVertexAi](https://developers.google.com/earth-engine/apidocs/ee-model-fromvertexai). This is an `ee.Model` object that packages Earth Engine data into tensors, forwards them as predict requests to [Vertex AI](https://cloud.google.com/vertex-ai) then reassembles the responses into Earth Engine.
Earth Engine supports TensorFlow (e.g. a [SavedModel](https://www.tensorflow.org/guide/saved_model#save_and_restore_models) format), PyTorch, and AutoML models. To prepare a model for hosting, [save it](https://cloud.google.com/vertex-ai/docs/training/exporting-model-artifacts), [import it to Vertex AI](https://cloud.google.com/vertex-ai/docs/model-registry/import-model), then [deploy the model to an endpoint](https://cloud.google.com/vertex-ai/docs/predictions/get-predictions#deploy_a_model_to_an_endpoint).
### Input Formats
To interact with Earth Engine, a hosted model's inputs and outputs need to be compatible with a supported interchange format. The default is the TensorProto interchange format, specifically serialized TensorProtos in base64 ([reference](https://cloud.google.com/vertex-ai/docs/general/base64)). This can be done programmatically, as shown on the [ML examples page](https://developers.google.com/earth-engine/guides/ml_examples), after training and before saving, or by loading, adding the input and output transformation, and re-saving. Other supported payload formats include JSON with `RAW_JSON` and multi-dimensional arrays with `ND_ARRAYS`. See our [payload format documentation](https://developers.google.com/earth-engine/guides/ee-vertex-payload-formats) for more details.
### Endpoint IAM Permissions
To use a model with `ee.Model.fromVertexAi()`, you must have sufficient permissions to use the model. Specifically, you (or anyone who uses the model) needs at least the [Vertex AI user role](https://cloud.google.com/vertex-ai/docs/general/access-control#aiplatform.user) for the Cloud Project where the model is hosted. You control permissions for your Cloud Project using [Identify and Access Management (IAM)](https://cloud.google.com/iam) controls.
### Regions
When deploying your model to an endpoint, you will need to specify which region to deploy to. The `us-central1` region is recommended since it will likely perform best due to proximity to Earth Engine servers, but almost any region will work. See the [Vertex AI location docs](https://cloud.google.com/vertex-ai/docs/general/locations) for details about Vertex AI regions and what features each one supports.
If you are migrating from AI Platform, note that Vertex AI does not have a global endpoint, and `ee.Model.fromVertexAi()` does not have a `region` parameter.
### Costs
**Warning:** These guides use billable components of Google Cloud.
For detailed information on costs, see each product's associated pricing page.
  * Vertex AI ([pricing](https://cloud.google.com/vertex-ai/pricing)
  * Cloud Storage ([pricing](https://cloud.google.com/storage/pricing))
  * Earth Engine ([pricing (commercial)](https://earthengine.google.com/commercial))


You can use the [Pricing Calculator](https://cloud.google.com/products/calculator) to generate a cost estimate based on your projected usage.
### Further Reading
For more details on how to use a hosted model with Earth Engine see our [Image Prediction page](https://developers.google.com/earth-engine/guides/ee-vertex-image-predictions) for image prediction, or our [Properties Prediction page](https://developers.google.com/earth-engine/guides/ee-vertex-property-predictions)
