 
#  Hosted Model Payload Formats Supported on Earth Engine 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Supported Model Inputs](https://developers.google.com/earth-engine/guides/ee-vertex-payload-formats#supported_model_inputs)
    * [gRPC Prediction Payloads](https://developers.google.com/earth-engine/guides/ee-vertex-payload-formats#grpc_prediction_payloads)
    * [HTTP API Payloads](https://developers.google.com/earth-engine/guides/ee-vertex-payload-formats#http_api_payloads)


Your custom trained model must be configured such that Earth Engine can send well-formed, interpretable inference requests to the model as it is hosted on Vertex AI.
## Supported Model Inputs
Earth Engine constructs requests on your behalf when performing inference. Specify the payload format that EE will send requests with using the `payloadFormat` parameter when you instantiate the model connector with `ee.Model.fromVertexAi`.
### gRPC Prediction Payloads
All hosted TensorFlow models can send predictions over the gRPC protocol. This is the preferred way to connect hosted models with Earth Engine as it will result in lower prediction latency and higher reliability.
**Note:** This is an experimental feature. Models that are deployed to Vertex AI with this enabled must have a gRPC prediction handler implemented and the gRPC prediction port must be specified when uploading your custom model.
#### GRPC_TF_TENSORS
Use the `GRPC_TF_TENSORS` payload format to use gRPC with TensorFlow models. All properties and or bands will be encoded in a single [`PredictRequest`](https://github.com/tensorflow/serving/blob/d89b27235f94b245ae1822b5125f6c67e0b587db/tensorflow_serving/apis/predict.proto#L13). This `PredictRequest` will be converted to a dictionary of tensors for your model to use.
#### GRPC_SERIALIZED_TF_TENSORS
Use the `GRPC_SERIALIZED_TF_TENSORS` format if you want to migrate a Cloud AI Platform model that was previously already integrated with Earth Engine without having to modify the model. You will need to re-upload and re-deploy if `container_grpc_ports` is not set on your model in Vertex AI.
#### GRPC_SERIALIZED_TF_EXAMPLES
Use the `GRPC_SERAILZED_TF_EXAMPLES` for models that support tf.Example protocol buffers. Earth Engine will send a single tensor named "input" that contains the utf-8 encoded proto ByteString of an Example proto.
### HTTP API Payloads
Vertex AI supports connecting to HTTP inference endpoints. Earth Engine supports several of the common HTTP payload formats. By default all Vertex AI custom models support the HTTP inference API.
#### SERIALIZED_TF_TENSORS
This is the default `payloadFormat` when connecting to a hosted model in Vertex AI. This payload format is the most efficient of the HTTP payload formats when using TensorFlow models.
Earth Engine will construct the inputs in the following way: for every band and property required for your inference request will be a single key-value pair in the `instances` object sent to your hosted model.
Each key will be the band or property name and each value will be a [Base64](https://cloud.google.com/vertex-ai/docs/general/base64) encoded TensorProto ByteString as a `string_val`.
#### RAW_JSON
For other model frameworks the most flexible format we can send is a JSON dictionary of named inputs and values. This payload format works well with PyTorch and AutoML models by default.
However do note that all numerical values will be converted into JSON strings. For example, to represent the number we encode 12.345 this as the string "12.345". Large inference payloads are not well supported with this payload format.
#### ND_ARRAYS
This is similar to `RAW_JSON` payload format but will omit the keys and only pass in a list of numbers in the same format of calling [`to_list()`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tolist.html) on a NumPy ndarray. This payload format works well with PyTorch natively.
