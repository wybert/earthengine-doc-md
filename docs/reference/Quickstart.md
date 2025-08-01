 
#  Quickstart
Stay organized with collections  Save and categorize content based on your preferences. 
This guide explains how you can quickly get started issuing queries to the Earth Engine REST API from Python using [Google Colab](https://colab.research.google.com). The same concepts apply to accessing the API from other languages and environments.
**_Note:_** _The REST API contains new and advanced features that may not be suitable for all users. If you are new to Earth Engine, please get started with the[JavaScript guide](https://developers.google.com/earth-engine/getstarted)._
[ ![Colab logo](https://developers.google.com/static/earth-engine/images/colab_logo_32px.png) Run in Google Colab ](https://colab.research.google.com/github/google/earthengine-community/blob/master/guides/linked/Earth_Engine_REST_API_Quickstart.ipynb) |  [ ![GitHub logo](https://developers.google.com/static/earth-engine/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/earthengine-community/blob/master/guides/linked/Earth_Engine_REST_API_Quickstart.ipynb)  
---|---  
## Before you begin
Follow [these instructions](https://developers.google.com/earth-engine/earthengine_cloud_project_setup) to:
  * [Configure](https://console.cloud.google.com/earth-engine) Earth Engine access
  * [Create](https://console.cloud.google.com/iam-admin/serviceaccounts) a service account


## Set up your Colab notebook
If you are starting this quickstart from scratch, you can create a new Colab notebook by clicking [**NEW NOTEBOOK**](https://colab.research.google.com/notebook#create=true&language=python3) from the Colab start page and enter the code samples below into a new code cell. Colab already has the [Cloud SDK](https://cloud.google.com/sdk/) installed. This includes the `gcloud` command-line tool that you can use to manage Cloud services. Alternatively, run the demo notebook from the button at the start of this page.
## Authenticate to Google Cloud
The first thing to do is login so that you can make authenticated requests to Google Cloud.
In Colab, you can run:
```
PROJECT = 'my-project'
!gcloud auth login --project {PROJECT}
```

(Or if you're running locally, from a command line, assuming you have the Cloud SDK installed:)
```
PROJECT='my-project'
gcloud auth login --project $PROJECT

```

Accept the option to log in using your Google user account and complete the sign-in process.
### Obtain a private key file for your service account
Before you can use the service account to authenticate, you must download a private key file. To do that in Colab, downloading to the notebook VM:
```
SERVICE_ACCOUNT='foo-name@project-name.iam.gserviceaccount.com'
KEY = 'my-secret-key.json'
!gcloud iam service-accounts keys create {KEY} --iam-account {SERVICE_ACCOUNT}
```

Or alternatively from command line:
```
SERVICE_ACCOUNT='foo-name@project-name.iam.gserviceaccount.com'
KEY='my-secret-key.json'
gcloud iam service-accounts keys create $KEY --iam-account $SERVICE_ACCOUNT

```

## Accessing and Testing your Credentials
You are now ready to send your first query to the Earth Engine API. Use the private key to get credentials. Use the credentials to create an authorized session to make HTTP requests. You can enter this into a new code cell of your Colab notebook. (If you are using command line, you will need to ensure that the necessary libraries are installed).
```
fromgoogle.auth.transport.requestsimport AuthorizedSession
fromgoogle.oauth2import service_account

credentials = service_account.Credentials.from_service_account_file(KEY)
scoped_credentials = credentials.with_scopes(
    ['https://www.googleapis.com/auth/cloud-platform'])

session = AuthorizedSession(scoped_credentials)

url = 'https://earthengine.googleapis.com/v1alpha/projects/earthengine-public/assets/LANDSAT'

response = session.get(url)

frompprintimport pprint
importjson
pprint(json.loads(response.content))
```

If everything is configured correctly, running this will produce output that looks like:
```
{'id': 'LANDSAT',
 'name': 'projects/earthengine-public/assets/LANDSAT',
 'type': 'FOLDER'}

```

## Pick a Dataset
You can search and explore available datasets using the [Earth Engine Code Editor](https://developers.google.com/earth-engine/playground) at [code.earthengine.google.com](https://code.earthengine.google.com/). Let's look for some [Sentinel 2](https://sentinel.esa.int/web/sentinel/missions/sentinel-2) data. (If this is your first time using the Code Editor then you will be prompted to authorize it to access Earth Engine on your behalf when you sign in.) In the Code Editor, search for "sentinel" in search box at the top. Several raster datasets appear:
![](https://developers.google.com/static/earth-engine/images/sentinel-search.png)
Click on "Sentinel-2: MultiSpectral Instrument (MSI), Level-1C":
![](https://developers.google.com/static/earth-engine/images/sentinel-2-description.png)
Dataset description pages like this one include the critical information you need in order to use any dataset in the Earth Engine Public Data Catalog, including a brief description of the dataset, links to the data provider to get additional details, information about any usage restrictions that may apply to the dataset, and the dataset's Earth Engine asset ID.
In this case we see on the right side of the window that this is an image collection asset whose path is `COPERNICUS/S2`.
## Query for Particular Images
This Sentinel-2 dataset includes over two million images covering the world from 2015 through the present. Let's issue a [projects.assets.listImages](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets/listImages) query against the image collection to find some data from April, 2017, with low cloud cover that includes a particular point in Mountain View, California.
```
importurllib

coords = [-122.085, 37.422]

project = 'projects/earthengine-public'
asset_id = 'COPERNICUS/S2'
name = '{}/assets/{}'.format(project, asset_id)
url = 'https://earthengine.googleapis.com/v1alpha/{}:listImages?{}'.format(
  name, urllib.parse.urlencode({
    'startTime': '2017-04-01T00:00:00.000Z',
    'endTime': '2017-05-01T00:00:00.000Z',
    'region': '{"type":"Point", "coordinates":' + str(coords) + '}',
    'filter': 'CLOUDY_PIXEL_PERCENTAGE < 10',
}))

response = session.get(url)
content = response.content

for asset in json.loads(content)['images']:
    id = asset['id']
    cloud_cover = asset['properties']['CLOUDY_PIXEL_PERCENTAGE']
    print('%s : %s' % (id, cloud_cover))
```

This script queries the collection for matching images, decodes the resulting JSON response, and prints the asset ID and cloud cover for each matching image asset. The output should look like:
```
COPERNICUS/S2/20170420T184921_20170420T190203_T10SEG : 4.3166
COPERNICUS/S2/20170430T190351_20170430T190351_T10SEG : 0

```

Evidently there are two images over this point that were taken in this month and have low cloud cover.
## Inspect a Particular Image
It looks like one of the matching has essentially zero cloud cover. Let's take a closer look at that asset, whose ID is `COPERNICUS/S2/20170430T190351_20170430T190351_T10SEG`. Note that all public catalog assets belong to the project `earthengine-public`. Here's a Python snippet that will issue a [projects.assets.get](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets/get) query to fetch the details of that particular asset by ID, print the available data bands, and print more detailed information about the first band:
```
asset_id = 'COPERNICUS/S2/20170430T190351_20170430T190351_T10SEG'
name = '{}/assets/{}'.format(project, asset_id)
url = 'https://earthengine.googleapis.com/v1alpha/{}'.format(name)

response = session.get(url)
content = response.content

asset = json.loads(content)
print('Band Names: %s' % ','.join(band['id'] for band in asset['bands']))
print('First Band: %s' % json.dumps(asset['bands'][0], indent=2, sort_keys=True))
```

The output should look like something like this:
```
Band Names: B1,B2,B3,B4,B5,B6,B7,B8,B8A,B9,B10,B11,B12,QA10,QA20,QA60
First Band: {
  "dataType": {
    "precision": "INTEGER",
    "range": {
      "max": 65535
    }
  },
  "grid": {
    "affineTransform": {
      "scaleX": 60,
      "scaleY": -60,
      "translateX": 499980,
      "translateY": 4200000
    },
    "crsCode": "EPSG:32610",
    "dimensions": {
      "height": 1830,
      "width": 1830
    }
  },
  "id": "B1",
  "pyramidingPolicy": "MEAN"
}

```

The list of data bands corresponds to what we saw earlier in the [dataset description](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2). We can see that this dataset has 16-bit integer data in the [EPSG:32610](https://epsg.io/32610) coordinate system, or UTM Zone 10N. This first band has the ID `B1` and a resolution of 60 meters per pixel. The origin of the image is at position (499980,4200000) in this coordinate system.
The negative value of `affineTransform.scaleY` indicates that the origin is in the north-west corner of the image, as is usually the case: increasing `y` pixel indices correspond to decreasing `y` spatial coordinates (heading south).
## Fetching Pixel Values
Let's issue a [projects.assets.getPixels](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets/getPixels) query to fetch some data from the high resolution bands of this image. The dataset description page says that bands `B2`, `B3`, `B4`, and `B8` have a resolution of 10 meters per pixel. This script fetches the top-left 256x256-pixel tile of data from those four bands. Loading the data in the `numpy` NPY format makes it easy to decode the response into a Python data array.
```
importnumpy
importio

name = '{}/assets/{}'.format(project, asset_id)
url = 'https://earthengine.googleapis.com/v1alpha/{}:getPixels'.format(name)
body = json.dumps({
    'fileFormat': 'NPY',
    'bandIds': ['B2', 'B3', 'B4', 'B8'],
    'grid': {
        'affineTransform': {
            'scaleX': 10,
            'scaleY': -10,
            'translateX': 499980,
            'translateY': 4200000,
        },
        'dimensions': {'width': 256, 'height': 256},
    },
})

pixels_response = session.post(url, body)
pixels_content = pixels_response.content

array = numpy.load(io.BytesIO(pixels_content))
print('Shape: %s' % (array.shape,))
print('Data:')
print(array)
```

The output should look like this:
```
Shape: (256, 256)
Data:
[[( 899, 586, 351, 189) ( 918, 630, 501, 248) (1013, 773, 654, 378) ...,
  (1014, 690, 419, 323) ( 942, 657, 424, 260) ( 987, 691, 431, 315)]
 [( 902, 630, 541, 227) (1059, 866, 719, 429) (1195, 922, 626, 539) ...,
  ( 978, 659, 404, 287) ( 954, 672, 426, 279) ( 990, 678, 397, 304)]
 [(1050, 855, 721, 419) (1257, 977, 635, 569) (1137, 770, 400, 435) ...,
  ( 972, 674, 421, 312) (1001, 688, 431, 311) (1004, 659, 378, 284)]
 ...,
 [( 969, 672, 375, 275) ( 927, 680, 478, 294) (1018, 724, 455, 353) ...,
  ( 924, 659, 375, 232) ( 921, 664, 438, 273) ( 966, 737, 521, 306)]
 [( 920, 645, 391, 248) ( 979, 728, 481, 327) ( 997, 708, 425, 324) ...,
  ( 927, 673, 387, 243) ( 927, 688, 459, 284) ( 962, 732, 509, 331)]
 [( 978, 723, 449, 330) (1005, 712, 446, 314) ( 946, 667, 393, 269) ...,
  ( 949, 692, 413, 271) ( 927, 689, 472, 285) ( 966, 742, 516, 331)]]

```

To select a different set of pixels from this image, simply specify the `affineTransform` accordingly. Remember that the `affineTransform` is specified in the image's spatial coordinate reference system; if you want to adjust the location of the origin in _pixel_ coordinates instead, use this simple formula:
```
request_origin = image_origin + pixel_scale * offset_in_pixels
```

## Generating a Thumbnail Image
We can use a similar mechanism to generate an RGB thumbnail of this image. Instead of requesting data at its native resolution, we will specify a region and image dimensions explicitly. To get a thumbnail of the entire image, we can use the image's footprint geometry as the request region. Finally, by specifying the red, green, and blue image bands and an appropriate range of data values, we can obtain an attractive RGB thumbnail image.
Putting this all together, the Python snippet looks like this (using the Colab `IPython` image display widget):
```
url = 'https://earthengine.googleapis.com/v1alpha/{}:getPixels'.format(name)
body = json.dumps({
    'fileFormat': 'PNG',
    'bandIds': ['B4', 'B3', 'B2'],
    'region': asset['geometry'],
    'grid': {
        'dimensions': {'width': 256, 'height': 256},
    },
    'visualizationOptions': {
        'ranges': [{'min': 0, 'max': 3000}],
    },
})

image_response = session.post(url, body)
image_content = image_response.content

fromIPython.displayimport Image
Image(image_content)
```

Here is the resulting thumbnail image:
![](https://developers.google.com/static/earth-engine/images/sentinel_2_thumbnail.png)
