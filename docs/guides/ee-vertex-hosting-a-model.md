 
#  Hosted Custom Model for Earth Engine 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Model Input](https://developers.google.com/earth-engine/guides/ee-vertex-hosting-a-model#model_input)
  * [Model Artifact](https://developers.google.com/earth-engine/guides/ee-vertex-hosting-a-model#model_artifact)
    * [TensorFlow](https://developers.google.com/earth-engine/guides/ee-vertex-hosting-a-model#tensorflow)
    * [PyTorch](https://developers.google.com/earth-engine/guides/ee-vertex-hosting-a-model#pytorch)
  * [Model Deployment to Vertex AI](https://developers.google.com/earth-engine/guides/ee-vertex-hosting-a-model#model_deployment_to_vertex_ai)
  * [Model Endpoint Management](https://developers.google.com/earth-engine/guides/ee-vertex-hosting-a-model#model_endpoint_management)


Performing inference with a custom trained model using a machine learning framework such as TensorFlow or PyTorch requires saving and uploading the model to Vertex AI, creating a prediction endpoint and deploying the model to serve traffic at the created endpoint.
## Model Input
Before you save and upload your model to Vertex AI you should ensure that the model accepts data in a payload format that Earth Engine supports. For more details see our [payload formats](https://developers.google.com/earth-engine/guides/ee-vertex-payload-formats.md) page for more details.
## Model Artifact
The next step is to save your model to a format that is hostable in Vertex AI.
### TensorFlow
TensorFlow based models can be saved in several different formats, but Vertex AI requires the SavedModel format. Keras based models must be exported as SavedModels with [`tf.keras.Model.export()`](https://www.tensorflow.org/guide/keras/serialization_and_saving#simple_exporting_with_export). Other TensorFlow models require using the more primitive [`tf.saved_model.save()`](https://www.tensorflow.org/api_docs/python/tf/saved_model/save). See the documentation on the [SavedModel format](https://www.tensorflow.org/guide/saved_model) for more details.
### PyTorch
PyTorch models have a slightly different way to prepare the model artifacts for prediction serving. If creating a custom trained model, the model must first be saved. For performance reasons it is recommended to convert your PyTorch model to TorchScript and saved the model file with:
```
model_scripted = torch.jit.script(model) # Export to TorchScript
model_scripted.save('model.pt') # Save

```

Once the model file is saved it needs to be archived so it can be deployed to Vertex AI. When using a prebuilt container the model [must be named "model"](https://cloud.google.com/vertex-ai/docs/training/exporting-model-artifacts#pytorch). To archive the model torch-model-archiver needs to be run including any custom handler and additional files your model requires. An example of that is here:
```
torch-model-archiver-f\
--model-namemodel\
--version1.0\
--serialized-file$model_file\
--handler$hander_file\
--extra-files$index_to_name_file\
--export-path$model_path

```

## Model Deployment to Vertex AI
Once your model files are saved the next step is to upload your model to Vertex AI. If your model artifact is not already in Google Cloud Storage copy your model archive there first with a command like `gsutil cp $model_path gs://${your-bucket}/models/model`.
Once copied you can either use the [Vertex AI's Model Registry](https://console.cloud.google.com/vertex-ai/models) to upload your model or use gcloud command line and run something like:
```
gcloudaimodelsupload\
--artifact-uri=gs://{your-bucket}/models/model\
--display-name=${display-name}\
--container-image-uri=${model-container}\
--container-grpc-ports=8500

```

TIP: For optimal performance enable gRPC predictions with the `container-grpc-ports` flag. See more information about gRPC predictions at our [payload formats documentation](https://developers.google.com/earth-engine/guides/ee-vertex-payload-formats). This flag can only be specified using the gcloud commandline tool.
## Model Endpoint Management
Once a model is uploaded to Vertex AI, create an endpoint and deploy the model through the Online Prediction page by [creating a new endpoint](https://console.cloud.google.com/vertex-ai/online-prediction/endpoints) or by using the gcloud command line with the commands `endpoints create` and `endpoints deploy-model`. For example:
Creating an model:
```
gcloudaiendpointscreate\
--display-name=${endpoint-name}

```

Deploying a model
```
gcloudaiendpointsdeploy-model{endpoint-id}\
--model=${model-id}\
--traffic-split=0=100\
--display-name=${model-display-name}\
--min-replica-count=${min-replica-count}\
--max-replica-count=${max-replica-count}

```

Once your model is deployed you are ready to connect to your model in Earth Engine to perform inferences.
