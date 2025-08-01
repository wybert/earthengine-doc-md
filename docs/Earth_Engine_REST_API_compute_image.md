 
#  Image computations with the Earth Engine REST API
Stay organized with collections  Save and categorize content based on your preferences. 
[ ![Colab logo](https://developers.google.com/static/earth-engine/images/colab_logo_32px.png) Run in Google Colab ](https://colab.research.google.com/github/google/earthengine-community/blob/master/guides/linked/Earth_Engine_REST_API_compute_image.ipynb) |  [ ![GitHub logo](https://developers.google.com/static/earth-engine/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/earthengine-community/blob/master/guides/linked/Earth_Engine_REST_API_compute_image.ipynb)  
---|---  
**_Note:_** _The REST API contains new and advanced features that may not be suitable for all users. If you are new to Earth Engine, please get started with the[JavaScript guide](https://developers.google.com/earth-engine/guides/getstarted)._
The [Earth Engine REST API quickstart](https://developers.google.com/earth-engine/reference/Quickstart) shows how to access blocks of pixels from an Earth Engine asset. Suppose you want to apply a computation to the pixels before obtaining the result. This guide shows how to prototype a computation with one of the client libraries, serialize the computation graph and use the REST API to obtain the computed result. Making compute requests through the REST API corresponds to a `POST` request to one of the compute endpoints, for example [`computePixels`](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.image/computePixels), [`computeFeatures`](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.table/computeFeatures), or the generic [`value.compute`](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.value/compute). Specifically, this example demonstrates getting a median composite of Sentinel-2 imagery in a small region.
## Before you begin
Follow [these instructions](https://developers.google.com/earth-engine/cloud/earthengine_cloud_project_setup) to:
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
You should already have a service account registered to use Earth Engine. If you don't, follow [these instructions](https://developers.google.com/earth-engine/guides/service_account#create-a-service-account) to get one. Copy the email address of your service account into the following cell. (The service account must already be registered to use Earth Engine). In the following cell, the `gsutil` command line is used to generate a key file for the service account. The key file will be created on the notebook VM.
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
Prototype a simple computation with the client API. Note that the result of the computation is an `Image`.
```
coords=[
-121.58626826832939,
38.059141484827485,
]
region=ee.Geometry.Point(coords)

collection=ee.ImageCollection('COPERNICUS/S2')
collection=collection.filterBounds(region)
collection=collection.filterDate('2020-04-01','2020-09-01')
image=collection.median()

```

### Serialize the expression graph
This will create an object that represents the Earth Engine expression graph (specifically, an [`Expression`](https://developers.google.com/earth-engine/reference/rest/v1beta/Expression)). In general, you should build these with one of the client APIs.
```
serialized = ee.serializer.encode(image)

```

Create the desired projection (WGS84) at the desired scale (10 meters for Sentinel-2). This is just to discover the desired scale in degrees, the units of the projection. These scales will be used to specify the affine transform in the request.
```
# Make a projection to discover the scale in degrees.
proj = ee.Projection('EPSG:4326').atScale(10).getInfo()

# Get scales out of the transform.
scale_x = proj['transform'][0]
scale_y = -proj['transform'][4]

```

## Send the request
Make a `POST` request to the [`computePixels`](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.image/computePixels) endpoint. Note that the request contains the [`Expression`](https://developers.google.com/earth-engine/reference/rest/v1beta/Expression), which is the serialized computation. It also contains a [`PixelGrid`](https://developers.google.com/earth-engine/reference/rest/v1beta/PixelGrid). The `PixelGrid` contains `dimensions` for the desired output and an `AffineTransform` in the units of the requested coordinate system. Here the coordinate system is geographic, so the transform is specified with scale in degrees and geographic coordinates of the upper left corner of the requested image patch.
```
importjson

url = 'https://earthengine.googleapis.com/v1beta/projects/{}/image:computePixels'
url = url.format(PROJECT)

response = session.post(
  url=url,
  data=json.dumps({
    'expression': serialized,
    'fileFormat': 'PNG',
    'bandIds': ['B4','B3','B2'],
    'grid': {
      'dimensions': {
        'width': 640,
        'height': 640
      },
      'affineTransform': {
        'scaleX': scale_x,
        'shearX': 0,
        'translateX': coords[0],
        'shearY': 0,
        'scaleY': scale_y,
        'translateY': coords[1]
      },
      'crsCode': 'EPSG:4326',
    },
    'visualizationOptions': {'ranges': [{'min': 0, 'max': 3000}]},
  })
)

image_content = response.content

```

If you are running this in a notebook, you can display the results using the `IPython` image display widget.
```
# Import the Image function from the IPython.display module.
fromIPython.displayimport Image
Image(image_content)

```

