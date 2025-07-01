 
#  Table computations with the Earth Engine REST API
Stay organized with collections  Save and categorize content based on your preferences. 
[ ![Colab logo](https://developers.google.com/static/earth-engine/images/colab_logo_32px.png) Run in Google Colab ](https://colab.research.google.com/github/google/earthengine-community/blob/master/guides/linked/Earth_Engine_REST_API_compute_table.ipynb) |  [ ![GitHub logo](https://developers.google.com/static/earth-engine/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/earthengine-community/blob/master/guides/linked/Earth_Engine_REST_API_compute_table.ipynb)  
---|---  
**_Note:_** _The REST API contains new and advanced features that may not be suitable for all users. If you are new to Earth Engine, please get started with the[JavaScript guide](https://developers.google.com/earth-engine/guides/getstarted)._
The [Earth Engine REST API quickstart](https://developers.google.com/earth-engine/reference/Quickstart) shows how to access blocks of pixels from an Earth Engine asset. The [compute pixels example](https://developers.google.com/earth-engine/Earth_Engine_REST_API_compute_image) demonstrates how to apply a computation to the pixels before obtaining the result. This example demonstrates getting the mean of pixels in each image of an `ImageCollection` in each feature of a `FeatureCollection`. Specifically, this is a `POST` request to the [`computeFeatures`](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.table/computeFeatures) endpoint.
## Before you begin
Follow [these instructions](https://developers.google.com/earth-engine/earthengine_cloud_project_setup#apply-to-use-earth-engine) to:
  1. Apply for Earth Engine
  2. Create a Google Cloud project
  3. Enable the Earth Engine API on the project
  4. Create a service account
  5. Give the service account project level permission to perform Earth Engine computations


**Note** : To complete this tutorial, you will need a service account that is registered for Earth Engine access. See [these instructions](https://developers.google.com/earth-engine/guides/service_account#register-the-service-account-to-use-earth-engine) to register a service account before proceeding.
## Authenticate to Google Cloud
The first thing to do is login so that you can make authenticated requests to Google Cloud. You will set the project at the same time. Follow the instructions in the output to complete the sign in.
```
#INSERTYOURPROJECTHERE
PROJECT='your-project'
!gcloud auth login --project {PROJECT}

```

## Obtain a private key file for your service account
You should already have a service account registered to use Earth Engine. If you don't, follow [these instructions](https://developers.google.com/earth-engine/service_account#create-a-service-account) to get one. Copy the email address of your service account into the following cell. (The service account must already be registered to use Earth Engine). In the following cell, the `gsutil` command line is used to generate a key file for the service account. The key file will be created on the notebook VM.
```
#INSERTYOURSERVICEACCOUNTHERE
SERVICE_ACCOUNT='your-service-account@your-project.iam.gserviceaccount.com'
KEY='key.json'
!gcloud iam service-accounts keys create {KEY} --iam-account {SERVICE_ACCOUNT}

```

## Start an `AuthorizedSession` and test your credentials
Test the private key by using it to get credentials. Use the credentials to create an authorized session to make HTTP requests. Make a `GET` request through the session to check that the credentials work.
```
fromgoogle.auth.transport.requestsimport AuthorizedSession
fromgoogle.oauth2import service_account
credentials = service_account.Credentials.from_service_account_file(KEY)
scoped_credentials = credentials.with_scopes(
  ['https://www.googleapis.com/auth/cloud-platform'])
session = AuthorizedSession(scoped_credentials)
url = 'https://earthengine.googleapis.com/v1beta/projects/earthengine-public/assets/LANDSAT'
response = session.get(url)
frompprintimport pprint
importjson
pprint(json.loads(response.content))

```

## Serialize a computation
Before you can send a request to compute something, the computation needs to be put into the Earth Engine expression graph format. The following demonstrates how to obtain the expression graph.
### Authenticate to Earth Engine
Get Earth Engine scoped credentials from the service account. Use them to initialize Earth Engine.
```
importee
# Get some new credentials since the other ones are cloud scope.
ee_creds = ee.ServiceAccountCredentials(SERVICE_ACCOUNT, KEY)
ee.Initialize(ee_creds)

```

### Define a computation
Prototype a simple computation with the client API. Note that the result of the computation is a `FeatureCollection`. To check that the computation can succeed without errors, get a value from the first `Feature` (the mean NDVI in the polygon).
```
#Acollectionofpolygons.
states=ee.FeatureCollection('TIGER/2018/States')
maine=states.filter(ee.Filter.eq('NAME','Maine'))
#Imagery:NDVIvegetationindexfromMODIS.
band='NDVI'
images=ee.ImageCollection('MODIS/006/MOD13Q1').select(band)
image=images.first()
computation=image.reduceRegions(
collection=maine,
reducer=ee.Reducer.mean().setOutputs([band]),
scale=image.projection().nominalScale()
)
#Printthevaluetotest.
print(computation.first().get(band).getInfo())

```

### Serialize the expression graph
This will create an object that represents the Earth Engine expression graph (specifically, an [`Expression`](https://developers.google.com/earth-engine/reference/rest/v1beta/Expression)). In general, you should build these with one of the client APIs.
```
# Serialize the computation.
serialized = ee.serializer.encode(computation)

```

## Send the request
Make a `POST` request to the [`computeFeatures`](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.table/computeFeatures) endpoint. Note that the request contains the [`Expression`](https://developers.google.com/earth-engine/reference/rest/v1beta/Expression), which is the serialized computation.
```
importjson
url = 'https://earthengine.googleapis.com/v1beta/projects/{}/table:computeFeatures'
response = session.post(
 url = url.format(PROJECT),
 data = json.dumps({'expression': serialized})
)
importjson
pprint(json.loads(response.content))

```

The response contains the resultant `FeatureCollection` as GeoJSON, which can be consumed by other apps or processes.
