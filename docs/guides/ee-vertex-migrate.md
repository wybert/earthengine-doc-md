 
#  Cloud AI Platform Migration Guide 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Manual Migration](https://developers.google.com/earth-engine/guides/ee-vertex-migrate#manual_migration)


Cloud AI Platform is deprecated and access will be discontinued January 31 2025. The easiest way to migrate is to following Vertex AI's [migration page in the Cloud Console](https://cloud.console.google.com/vertex-ai/migrate).
Otherwise you can manually migrate with the following steps.
## Manual Migration
  1. Re-upload your Cloud AI Platform model to Vertex AI. Be careful to ensure that the uploaded model is using the same ML library when choosing the container image to use otherwise the model may not successfully deploy at a later step.
  2. Create a new Vertex AI endpoint for your hosted model.
  3. Deploy your uploaded model to the new Vertex AI endpoint.
  4. Update any references from `ee.Model.fromAiPlatformPredictor` to `ee.Model.fromVertexAi` in all of your code using Earth Engine and in the `endpoint` field use the new endpoint name that you created in step 2.

**Tip:** When re-deploying your model to Vertex AI consider using a [gRPC prediction format](https://developers.google.com/earth-engine/guides/ee-vertex-payload-formats#grpc_prediction_payloads).
