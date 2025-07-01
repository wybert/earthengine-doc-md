 
#  Cloud GeoTiff-Backed Earth Engine Assets
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Sample image manifest with one Tileset](https://developers.google.com/earth-engine/Earth_Engine_asset_from_cloud_geotiff#sample_image_manifest_with_one_tileset)
  * [More than one Tileset](https://developers.google.com/earth-engine/Earth_Engine_asset_from_cloud_geotiff#more_than_one_tileset)
  * [Details on COG-backed assets](https://developers.google.com/earth-engine/Earth_Engine_asset_from_cloud_geotiff#details_on_cog-backed_assets)
    * [Location](https://developers.google.com/earth-engine/Earth_Engine_asset_from_cloud_geotiff#location)
    * [Storage class](https://developers.google.com/earth-engine/Earth_Engine_asset_from_cloud_geotiff#storage_class)
    * [Permissions for sharing](https://developers.google.com/earth-engine/Earth_Engine_asset_from_cloud_geotiff#permissions_for_sharing)
    * [Generations](https://developers.google.com/earth-engine/Earth_Engine_asset_from_cloud_geotiff#generations)
    * [Configuration](https://developers.google.com/earth-engine/Earth_Engine_asset_from_cloud_geotiff#configuration)
  * [Creating Cloud GeoTiff-Backed Assets using the REST API](https://developers.google.com/earth-engine/Earth_Engine_asset_from_cloud_geotiff#creating_cloud_geotiff-backed_assets_using_the_rest_api)
  * [Start an authorized session](https://developers.google.com/earth-engine/Earth_Engine_asset_from_cloud_geotiff#start_an_authorized_session)
  * [Request body](https://developers.google.com/earth-engine/Earth_Engine_asset_from_cloud_geotiff#request_body)
  * [Send the request](https://developers.google.com/earth-engine/Earth_Engine_asset_from_cloud_geotiff#send_the_request)


[ ![Colab logo](https://developers.google.com/static/earth-engine/images/colab_logo_32px.png) Run in Google Colab ](https://colab.research.google.com/github/google/earthengine-community/blob/master/guides/linked/generated/Earth_Engine_asset_from_cloud_geotiff.ipynb) |  [ ![GitHub logo](https://developers.google.com/static/earth-engine/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/earthengine-community/blob/master/guides/linked/generated/Earth_Engine_asset_from_cloud_geotiff.ipynb)  
---|---  
Earth Engine supports assets backed by Cloud Optimized GeoTIFFs (COGs). An advantage of COG-backed assets is that the spatial and metadata fields of the image will be indexed at asset creation time, making the image more performant in collections. The performance of COG-backed assets is comparable to that of ingested assets in typical use cases.
Note that a single asset can be backed by multiple COGs (for example, there can be one COG per band). However, using many COG tiles for a single band is not supported.
(Alternatively, Earth Engine can directly load images from COGs in Google Cloud Storage ([learn more](https://developers.google.com/earth-engine/guides/image_overview#images-from-cloud-geotiffs)). However, an image loaded through `ee.Image.loadGeoTIFF` and added to an image collection will require a read of the GeoTiff for filtering operations on the collection.)
To create a COG-backed asset,
  1. Place your COG files into a GCS bucket (see below for allowed regions).
  2. Write an [image upload manifest](https://developers.google.com/earth-engine/guides/image_manifest)
  3. Use the `earthengine` command-line utility to send an upload command:

```
earthengine upload external_image --manifest my_manifest.json
```

## Sample image manifest with one `Tileset`
The simplest `ImageManifest` is one with a single `Tileset`. If no bands are specified, the resulting asset will contain all the bands of the GeoTIFF with the band names encoded in the GeoTIFF (in this case, "vis-red", "vis-green", and "vis-blue").
```
request = {
 'imageManifest': {
  'name': f'projects/{ee_project}/assets/cogdemo1',
  'tilesets': [
   { 'id': '0', 'sources': [ { 'uris': ['gs://ee-docs-demos/COG_demo.tif'] } ] }
  ],
  'properties': {
   'version': '1.1'
  },
  'startTime': '2016-01-01T00:00:00.000000000Z',
  'endTime': '2016-12-31T15:01:23.000000000Z',
 },
}
pprint(request)

```

## More than one `Tileset`
It is possible to specify an `ImageManifest` with more than one `Tileset` where each band of the resulting asset is backed by one of the bands of a `Tileset` using the `tilesetId` and `tilesetBandIndex` fields. This is useful in the case when different bands have different resolutions or data types. Bands can be listed in any order from any available `Tileset`. In the example below:
  * "b4b3b2.tif" has a 10 m scale, while "b5b6b7" has a 20 m scale.
  * The band order of the resulting asset is mixed from the input COGs (e.g. output band 0 is from `Tileset` 0, while output band 1 is from `Tileset` 1).

```
request = {
 'imageManifest': {
  'name': f'projects/{ee_project}/assets/cogdemo2',
  'uriPrefix': 'gs://ee-docs-demos/external_image_demo/',
  'tilesets': [
   { 'id': '0', 'sources': [ { 'uris': ['b4b3b2.tif'] } ] },
   { 'id': '1', 'sources': [ { 'uris': ['b5b6b7.tif'] } ] },
  ],
  'bands': [
   { 'id': 'red', 'tilesetId': '0', 'tilesetBandIndex': 0 },
   { 'id': 'rededge3', 'tilesetId': '1', 'tilesetBandIndex': 2 },
   { 'id': 'rededge2', 'tilesetId': '1', 'tilesetBandIndex': 1 },
   { 'id': 'green', 'tilesetId': '0', 'tilesetBandIndex': 1 },
   { 'id': 'blue', 'tilesetId': '1', 'tilesetBandIndex': 0 },
   { 'id': 'rededge1', 'tilesetId': '0', 'tilesetBandIndex': 2 },
  ],
 },
}
pprint(request)

```

## Details on COG-backed assets
### Location
The Cloud Storage bucket location must be one of:
  * The US multi-region
  * Any US dual-region that includes US-CENTRAL1
  * The region US-CENTRAL1


### Storage class
The [storage class](https://cloud.google.com/storage/docs/storage-classes#classes) of the bucket must be "Standard storage".
### Permissions for sharing
The ACLs of COG-backed Earth Engine assets and the underlying data are managed separately. When sharing COG-backed assets with collaborators for reading, **it is the owner's responsibility to ensure that read access is granted to both the Earth Engine asset and the underlying COG files.**
#### 1. Grant Google Cloud Storage bucket permissions for reading
For collaborators to read COG-backed assets, they must first have read access to the underlying COG files in the Google Cloud Storage bucket. Without these permissions, Earth Engine won't be able to retrieve the data for them. If the data in Google Cloud Storage is not visible to an Earth Engine user, Earth Engine will return an error of the form "Failed to load the GeoTIFF at `gs://my-bucket/my-object#123456`" (where 123456 is the generation of the object).
Specifically, collaborators must have the following permissions:
  * `storage.buckets.get` on the bucket (to retrieve bucket metadata and location, allowing Earth Engine to properly resolve the asset's source).
  * `storage.objects.get` on the bucket (to read the actual COG-backed asset data).


These permissions are provided by the roles **"Storage Legacy Bucket Reader"** and **"Storage Legacy Object Reader"** respectively, [among others](https://cloud.google.com/storage/docs/access-control/iam-roles).
To assign these roles to collaborators:
  1. Go to the bucket permission page: `https://console.cloud.google.com/storage/browser/{MY-BUCKET};tab=permissions`
  2. Click "**GRANT ACCESS** "
  3. Add all principals (e.g., users, groups, service accounts) who should be granted read access.
  4. Assign the following roles: 
     * **"Storage Legacy Bucket Reader"** (provides `storage.buckets.get` and other bucket-level read permissions).
     * **"Storage Legacy Object Reader"** (provides `storage.objects.get`).
     * (Alternatively, you could create a new custom role with just the `storage.buckets.get` and `storage.objects.get` permissions and assign that.)
  5. Save


#### 2. Share the Earth Engine asset for reading
After ensuring your collaborators have the necessary permissions on the underlying GCS bucket and objects, you must also share the Earth Engine asset itself. For more information on setting Earth Engine asset permissions, refer to the [Earth Engine asset management guide](https://developers.google.com/earth-engine/guides/manage_assets#set_asset_permissions).
### Generations
When a COG-backed asset is created, Earth Engine reads the metadata of TIFFs specified in the manifest and creates an asset store entry. Each URI associated with that entry can have a generation. See the [object versioning docs](https://cloud.google.com/storage/docs/object-versioning) for details on generations. If a generation is specified, for example `gs://foo/bar#123`, Earth Engine will store that URI verbatim. If a generation is not specified, Earth Engine will store that URI with the generation of the TIFF at the time `ImportExternalImage` was called.
That means that if any TIFF comprising an external asset in GCS is updated (therefore changing its generation), Earth Engine will return a "Failed to load the GeoTIFF at `gs://my-bucket/my-object#123456`" error because the expected object no longer exists (unless the bucket enables multiple object versions). This policy is designed to keep metadata of the asset in sync with the metadata of the object.
### Configuration
In terms of how a COG should be configured, the TIFF MUST be:
  * Tiled, where the tile dimensions are either:
    * 256x256
    * 512x512
    * 1024x1024
    * 2048x2048
  * Arranged so that all IFDs are at the beginning.


For best performance:
  * Use tile dimensions of 512x512 or higher.
  * Include power of 2 overviews.


Depending on your intended use cases, the ['INTERLEAVE'](https://gdal.org/en/stable/drivers/raster/gtiff.html#creation-options) creation option may affect performance. We recommend using BAND interleave in all circumstances.
See [this page](https://cogeotiff.github.io/rio-cogeo/Advanced/#web-optimized-cog) for more details on an optimized configuration.
The following `gdal_translate` command will convert a raster into a band-interleaved, zstd-compressed, Cloud Optimized GeoTIFF that will perform well in Earth Engine:
```
gdal_translatein.tifout.tif\
-coCOPY_SRC_OVERVIEWS=YES\
-coTILED=YES\
-coBLOCKXSIZE=512\
-coBLOCKYSIZE=512\
-coCOMPRESS=ZSTD\
-coZSTD_LEVEL=22\
-coINTERLEAVE=BAND\
-coNUM_THREADS=ALL_CPUS

```

It may be possible to reduce the output file size further by specifying a [predictor](https://gdal.org/en/stable/drivers/raster/gtiff.html#creation-options) (`-co PREDICTOR=2` for integer data types and `-co PREDICTOR=3` for floating point data types).
For users with GDAL >= 3.11, the [COG driver](https://gdal.org/en/stable/drivers/raster/cog.html) can produce files without having to worry about creating and preserving overviews.
```
gdal_translatein.tifout.tif\
-ofCOG\
-coOVERVIEWS=IGNORE_EXISTING\
-coCOMPRESS=ZSTD\
-coLEVEL=22\
-coPREDICTOR=2\
-coINTERLEAVE=BAND\
-coNUM_THREADS=ALL_CPUS\

```

## Creating Cloud GeoTiff-Backed Assets using the REST API
**_Note:_** _The REST API contains new and advanced features that may not be suitable for all users. If you are new to Earth Engine, we recommend getting started with the[JavaScript guide](https://developers.google.com/earth-engine/guides/getstarted)._
To create a COG-backed asset using the REST API, make a `POST` request to the Earth Engine [`ImportExternalImage` endpoint](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets/create). As shown in the following, this request must be authorized to create an asset in your user folder.
## Start an authorized session
To be able to make an Earth Engine asset in your user folder, you need to be able to authenticate as yourself when you make the request. You can use credentials from the Earth Engine authenticator to start an [`AuthorizedSession`](https://google-auth.readthedocs.io/en/master/reference/google.auth.transport.requests.html#google.auth.transport.requests.AuthorizedSession). You can then use the `AuthorizedSession` to send requests to Earth Engine.
```
importee
importjson
frompprintimport pprint
fromgoogle.auth.transport.requestsimport AuthorizedSession
ee.Authenticate() # or !earthengine authenticate --auth_mode=gcloud
# Specify the cloud project you want associated with Earth Engine requests.
ee_project = 'your-project'
session = AuthorizedSession(
  ee.data.get_persistent_credentials().with_quota_project(ee_project)
)

```

## Request body
The request body is an instance of an [`ImageManifest`](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.image/import#ImageManifest). This is where the path to the COG is specified, along with other useful properties.
See [this guide](https://developers.google.com/earth-engine/guides/image_manifest) for details on how to configure an `ImageManifest`. It is possible to define one or more `Tileset` with each backing one or more bands. For `ImportExternalImage`, at most one `ImageSource` is supported per `Tileset`.
See [this doc](https://developers.google.com/earth-engine/exporting#configuration-parameters) for details on exporting COGs.
## Send the request
Make the POST request to the Earth Engine [`projects.images.importExternal`](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.images/importExternal) endpoint.
```
url = f'https://earthengine.googleapis.com/v1alpha/projects/{ee_project}/image:importExternal'
response = session.post(
 url = url,
 data = json.dumps(request)
)
pprint(json.loads(response.content))

```

Was this helpful?
