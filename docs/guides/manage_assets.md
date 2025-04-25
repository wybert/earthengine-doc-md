 
#  Manage assets 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Asset types](https://developers.google.com/earth-engine/guides/manage_assets#asset_types)
  * [Asset organization](https://developers.google.com/earth-engine/guides/manage_assets#asset_organization)
  * [Create assets](https://developers.google.com/earth-engine/guides/manage_assets#create_assets)
  * [List assets](https://developers.google.com/earth-engine/guides/manage_assets#list_assets)
  * [Set asset permissions](https://developers.google.com/earth-engine/guides/manage_assets#set_asset_permissions)
  * [Check asset permissions](https://developers.google.com/earth-engine/guides/manage_assets#check_asset_permissions)
  * [Copy assets](https://developers.google.com/earth-engine/guides/manage_assets#copy_assets)
  * [Move or rename assets](https://developers.google.com/earth-engine/guides/manage_assets#move_or_rename_assets)
  * [Delete assets](https://developers.google.com/earth-engine/guides/manage_assets#delete_assets)
  * [View asset metadata](https://developers.google.com/earth-engine/guides/manage_assets#view_asset_metadata)
  * [Set asset metadata](https://developers.google.com/earth-engine/guides/manage_assets#set_asset_metadata)
  * [Check asset quota](https://developers.google.com/earth-engine/guides/manage_assets#check_asset_quota)


Earth Engine assets are project-owned geospatial data stored within the platform. You can upload your own data and store data produced from your Earth Engine analyses as assets.
## Asset types
Earth Engine offers various asset formats for different data types, along with container elements for organization.
Asset types  
---  
`Image` | A raster, a grid-based representation of geographic information where each cell in the grid holds a value corresponding to a specific location on the Earth's surface.  
`ImageCollection` | A collection of related raster images that constitute a mosaic or a time series. It is functionally similar to a folder, but can be imported into Earth Engine as an `ee.ImageCollection` object which includes a set of methods for filtering and analysis.  
`Table` | A table data structure composed of vector features (rows), each containing a series of properties (columns). It is represented by the `ee.FeatureCollection` object, which includes a set of methods for filtering and analysis.  
`Classifier` | A trained Earth Engine machine learning model. It is represented by the `ee.Classifier` object, which includes a set of methods for application and analysis.  
`FeatureView` | A visualization view of a table for use in Earth Engine Apps.  
`Folder` | A container for assets and additional folders to aid in organization.  
## Asset organization
Earth Engine assets are organized into a hierarchical system of folders and collections. The structure is similar to common file systems.
### Root
Assets are owned by a Cloud project. The project name defines the root of the asset directory. For example, the root of `my-project` is `projects/my-project/assets`. All assets that belong to `my-project` are in the `projects/my-project/assets` folder or a sub-folder (or ImageCollection) within it.
**Note:** Legacy user-owned assets use a different root format: `users/user-name/assets`
### Directory
Earth Engine uses a tree-like directory structure for organizing assets. Each Cloud project has a root directory that can contain individual assets and folders. ImageCollections are a special asset type designed specifically to hold sets of related images, such as time series or mosaics. Unlike folders, ImageCollections can only contain image assets and cannot nest other folders or collections within them.
  * folder_dataprojects/my-project/assets/
    * folder folder-name/
      * photo image-name
      * view_comfy table-name
      * satellite featureview-name
      * bubble_chart classifier-name
      * photo_library imagecollection-name/
        * photo image-name-1
        * photo image-name-2


### Asset ID
Earth Engine uses asset IDs to reference data in both scripts and command-line operations. They define asset locations using forward slashes (/) as separators between directories. For example, `projects/my-project/assets/my-asset` specifies an asset named "my-asset" located in the "my-project" root. Here's an example of using this ID to get information about the asset.
[Python](https://developers.google.com/earth-engine/guides/manage_assets#python)[Code Editor](https://developers.google.com/earth-engine/guides/manage_assets#code-editor)[Command line](https://developers.google.com/earth-engine/guides/manage_assets#command-line) More
```
print(ee.data.getAsset('projects/my-project/assets/my-asset'))

```
```
print(ee.Image('projects/my-project/assets/my-asset'))

```
```
earthengineassetinfoprojects/my-project/assets/my-asset
```

## Create assets
You can create folders and ImageCollections and ingest images and tables from local files or files in a Google Cloud Storage bucket. Supported image formats include GeoTIFF (standard and COG) and TFRecord. Supported table formats include Shapefile and CSV. (Assets can also be created by [exporting an Earth Engine analysis result](https://developers.google.com/earth-engine/guides/exporting) using batch functions `Export.*.toAsset`).
[Python client](https://developers.google.com/earth-engine/guides/manage_assets#python-client)[Code Editor](https://developers.google.com/earth-engine/guides/manage_assets#code-editor)[Command line](https://developers.google.com/earth-engine/guides/manage_assets#command-line) More
### Image
Use the [`ee.data.startIngestion`](https://developers.google.com/earth-engine/apidocs/ee-data-startingestion) function to ingest images from Cloud Storage. See the [image manifest](https://developers.google.com/earth-engine/guides/image_manifest#using-manifests) page for more information on configuring the upload.
```
manifest = {
 'name': 'projects/my-project/assets/asset-name',
 'tilesets': [
  {
   'sources': [
    {
     'uris': [
      'gs://my-bucket/filename.tif'
     ]
    }
   ]
  }
 ]
}
ee.data.startIngestion(None, manifest)

```

### Table
Use the [`ee.data.startTableIngestion`](https://developers.google.com/earth-engine/apidocs/ee-data-starttableingestion) function to ingest tables from Cloud Storage. See the [image manifest](https://developers.google.com/earth-engine/guides/table_manifest#using-manifests) page for more information on configuring the upload.
```
manifest = {
 'name': 'projects/my-project/assets/asset-name',
 'sources': [
  {
   'uris': [
    'gs://my-bucket/filename.csv'
   ]
  }
 ]
}
ee.data.startTableIngestion(None, manifest)

```

### Folder or ImageCollection
Use the [`ee.data.createAsset`](https://developers.google.com/earth-engine/apidocs/ee-data-createasset) function to create empty folders or ImageCollections.
```
ee.data.createAsset(
  {'type': 'FOLDER'}, # or 'IMAGE_COLLECTION'
  'projects/my-project/assets/asset-name'
)

```

Within the Asset Manager, click the NEW button and select the asset type you'd like to upload or create from the drop list. Configure the asset upload or creation in the dialog.
### Image or table
```
earthengineuploadimage--asset_id=projects/my-project/assets/asset-namegs://my-bucket/filename.tif
earthengineuploadtable--asset_id=projects/my-project/assets/asset-namegs://my-bucket/filename.csv
```

### Folder or ImageCollection
Use the [`earthengine create`](https://developers.google.com/earth-engine/guides/command_line#create) command to create empty folders or ImageCollections.
```
earthenginecreatefolderprojects/my-project/assets/folder-name
earthenginecreatecollectionprojects/my-project/assets/collection-name
```

### External image
Cloud-optimized GeoTIFF (COG) files that you upload to a Google Cloud Storage bucket can be registered as external image assets and used directly in Earth Engine. See the [reference docs](https://developers.google.com/earth-engine/guides/command_line#upload-external_image) for more information on COG backed assets and constructing a manifest.
```
earthenginealphauploadexternal_image--manifest/tmp/foo.json
```

## List assets
[Python client](https://developers.google.com/earth-engine/guides/manage_assets#python-client)[Code Editor](https://developers.google.com/earth-engine/guides/manage_assets#code-editor)[Command line](https://developers.google.com/earth-engine/guides/manage_assets#command-line) More
Use the [`ee.data.listAssets`](https://developers.google.com/earth-engine/apidocs/ee-data-listassets) function to list assets in a folder or collection (not recursive). See the reference docs for more information about filtering and pagination.
```
ee.data.listAssets('projects/my-project/assets')

```

Also see [`ee.data.listImages`](https://developers.google.com/earth-engine/apidocs/ee-data-listimages) and [`ee.data.listFeatures`](https://developers.google.com/earth-engine/apidocs/ee-data-listfeatures).
Expand folders in the Asset Manager to view assets.
Use the [`earthengine ls`](https://developers.google.com/earth-engine/guides/command_line#ls) command to list assets in a folder or collection (not recursive). See the reference docs for more information about limiting the number of assets to list and the amount detail to return.
```
earthenginelsprojects/my-project/assets
```

## Set asset permissions
[Python client](https://developers.google.com/earth-engine/guides/manage_assets#python-client)[Code Editor](https://developers.google.com/earth-engine/guides/manage_assets#code-editor)[Command line](https://developers.google.com/earth-engine/guides/manage_assets#command-line) More
Use the [`ee.data.setAssetAcl`](https://developers.google.com/earth-engine/apidocs/ee-data-setassetacl) function to set permissions on an asset.
```
asset_id = 'projects/my-project/assets/asset-name'
acl_update = {
  'owners': [
    'user:big_cheese@example.com',
    'user:el_jefe@example.com'
  ],
  'writers': [
    'user:romeo@example.com',
    'user:juliet@example.com'
  ],
  'readers': [
    'group:some-group@googlegroups.com',
    'domain:example.com',
    'serviceAccount:some-project-id@appspot.gserviceaccount.com'
  ],
  'all_users_can_read': False
}
ee.data.setAssetAcl(asset_id, acl_update)

```

Within the Asset Manager, hold the pointer over an asset and click the share icon. In the dialog, enter an email address or domain to share the asset with, then select a permission level to grant from the drop list. Click the ADD ACCESS button to confirm the change. Check the "Anyone can read" box to grant any entity read permission. You can also provide access to Earth Engine apps from the dialog by selecting the app's name from the drop list (assets owned by the active Code Editor project).
Use the `earthengine acl set` command to set an asset's read access to `public` or `private`.
```
earthengineaclsetpublicprojects/my-project/assets/asset-name
```

Use the `earthengine acl ch` command to set individual permissions for asset read and write.
```
earthengineaclch-uperson@gmail.com:Rprojects/my-project/assets/asset-name
```

See the [command line reference](https://developers.google.com/earth-engine/guides/command_line#acl) page for more details.
## Check asset permissions
[Python client](https://developers.google.com/earth-engine/guides/manage_assets#python-client)[Code Editor](https://developers.google.com/earth-engine/guides/manage_assets#code-editor)[Command line](https://developers.google.com/earth-engine/guides/manage_assets#command-line) More
Use the [`ee.data.getAssetAcl`](https://developers.google.com/earth-engine/apidocs/ee-data-getassetacl) function to fetch the access control list for an asset.
```
ee.data.getAssetAcl('projects/my-project/assets/asset-name')

```

Within the Asset Manager, hold the pointer over an asset and click the share icon. The dialog displays a list of emails and domains along with their respective access levels.
Use the [`earthengine acl get`](https://developers.google.com/earth-engine/guides/command_line#acl) command to fetch the access control list for an asset.
```
earthengineaclgetprojects/my-project/assets/asset-name
```

## Copy assets
[Python client](https://developers.google.com/earth-engine/guides/manage_assets#python-client)[Code Editor](https://developers.google.com/earth-engine/guides/manage_assets#code-editor)[Command line](https://developers.google.com/earth-engine/guides/manage_assets#command-line) More
Use the [`ee.data.copyAsset`](https://developers.google.com/earth-engine/apidocs/ee-data-copyasset) function to copy an asset.
```
ee.data.copyAsset('projects/my-project/assets/asset-name', 'projects/my-project/assets/asset-copy-name')

```

Use the Python client or the command line tool to copy assets.
Use the [`earthengine cp`](https://developers.google.com/earth-engine/guides/command_line#cp) command to copy an asset.
```
earthenginecpprojects/my-project/assets/asset-nameprojects/my-project/assets/asset-copy-name
```

## Move or rename assets
[Python client](https://developers.google.com/earth-engine/guides/manage_assets#python-client)[Code Editor](https://developers.google.com/earth-engine/guides/manage_assets#code-editor)[Command line](https://developers.google.com/earth-engine/guides/manage_assets#command-line) More
Use the [`ee.data.renameAsset`](https://developers.google.com/earth-engine/apidocs/ee-data-renameasset) function to move or rename an asset.
```
ee.data.renameAsset('projects/my-project/assets/asset-name', 'projects/my-project/assets/new-asset-name')

```

#### Move
Within the Asset Manager, drag an asset into a new folder.
#### Rename
Within the Asset Manager, hold the pointer over an asset and click the edit icon and type a new name in the editable input field.
Use the [`earthengine mv`](https://developers.google.com/earth-engine/guides/command_line#mv) command to move or rename an asset.
```
earthenginemvprojects/my-project/assets/asset-nameprojects/my-project/assets/new-asset-name
```

## Delete assets
[Python client](https://developers.google.com/earth-engine/guides/manage_assets#python-client)[Code Editor](https://developers.google.com/earth-engine/guides/manage_assets#code-editor)[Command line](https://developers.google.com/earth-engine/guides/manage_assets#command-line) More
Use the [`ee.data.deleteAsset`](https://developers.google.com/earth-engine/apidocs/ee-data-deleteasset) function to delete an asset.
```
ee.data.deleteAsset('projects/my-project/assets/asset-name')

```

Click an asset to open the asset dialog page, then click the DELETE button.
Use the [`earthengine rm`](https://developers.google.com/earth-engine/guides/command_line#rm) command to delete an asset. See the function reference for recursive and dry run options.
```
earthenginermprojects/my-project/assets/asset-name
```

## View asset metadata
[Python client](https://developers.google.com/earth-engine/guides/manage_assets#python-client)[Code Editor](https://developers.google.com/earth-engine/guides/manage_assets#code-editor)[Command line](https://developers.google.com/earth-engine/guides/manage_assets#command-line) More
Use the [`ee.data.getAsset`](https://developers.google.com/earth-engine/apidocs/ee-data-getasset) function to get asset metadata.
```
ee.data.getAsset('projects/my-project/assets/asset-name')

```

Click an asset to open the asset dialog page. View the asset information.
Use the [`earthengine asset info`](https://developers.google.com/earth-engine/guides/command_line#asset) command to get asset metadata.
```
earthengineassetinfoprojects/my-project/assets/asset-name
```

## Set asset metadata
The following asset metadata can be set:
  * `start_time`
  * `end_time`
  * `properties`


[Python client](https://developers.google.com/earth-engine/guides/manage_assets#python-client)[Code Editor](https://developers.google.com/earth-engine/guides/manage_assets#code-editor)[Command line](https://developers.google.com/earth-engine/guides/manage_assets#command-line) More
Use the [`ee.data.updateAsset`](https://developers.google.com/earth-engine/apidocs/ee-data-updateasset) function to update asset metadata.
```
asset_id = 'projects/my-project/assets/asset-name'
new_metadata = {
 'properties': {
  'name': 'value'
 },
 'start_time': '2024-10-02T15:01:24Z',
 'end_time': '2024-10-02T15:01:25Z',
}
update_these = ['start_time', 'end_time', 'properties']
ee.data.updateAsset(asset_id, new_metadata, update_these)

```

Click an asset to open the asset dialog page, then activate the edit toggle in the upper right. You can edit the description, properties, and start and end date. Deactivate the edit toggle to save the changes.
Use the [`earthengine asset set`](https://developers.google.com/earth-engine/guides/command_line#asset) command to update asset metadata. See the reference docs for more information.
```
earthengine asset set \
 --time_start 2024-10-02T15:01:24 \
 --time_end 2024-10-02T15:01:25 \
 --property 'name=value' \
 projects/my-project/assets/asset-name

```

## Check asset quota
Quota is applied at the project level. Learn more about asset quota in the [usage and quota limits](https://developers.google.com/earth-engine/guides/usage#adjustable_quota_limits) page.
[Python client](https://developers.google.com/earth-engine/guides/manage_assets#python-client)[Code Editor](https://developers.google.com/earth-engine/guides/manage_assets#code-editor)[Command line](https://developers.google.com/earth-engine/guides/manage_assets#command-line) More
Use the [`ee.data.getAssetRootQuota`](https://developers.google.com/earth-engine/apidocs/ee-data-getassetrootquota) function to get the storage quota usage for an asset root.
```
ee.data.getAssetRootQuota('projects/my-project/assets')

```

Within the Asset Manager, hold the pointer over a project root and click the data_usage icon. An information dialog will appear.
Use the Python client or the Code Editor to check asset quota.
