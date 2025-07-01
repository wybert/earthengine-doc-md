 
#  Command Line Tool
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Service account credentials](https://developers.google.com/earth-engine/guides/command_line#service_account_credentials)
  * [Usage in Colab](https://developers.google.com/earth-engine/guides/command_line#usage_in_colab)
    * [Authentication](https://developers.google.com/earth-engine/guides/command_line#authentication)
    * [Command execution](https://developers.google.com/earth-engine/guides/command_line#command_execution)
    * [Set a Cloud project](https://developers.google.com/earth-engine/guides/command_line#set_a_cloud_project)
  * [Command Reference](https://developers.google.com/earth-engine/guides/command_line#command_reference)
    * [authenticate](https://developers.google.com/earth-engine/guides/command_line#authenticate)
    * [acl](https://developers.google.com/earth-engine/guides/command_line#acl)
    * [asset](https://developers.google.com/earth-engine/guides/command_line#asset)
    * [cp](https://developers.google.com/earth-engine/guides/command_line#cp)
    * [create](https://developers.google.com/earth-engine/guides/command_line#create)
    * [ls](https://developers.google.com/earth-engine/guides/command_line#ls)
    * [model](https://developers.google.com/earth-engine/guides/command_line#model)
    * [mv](https://developers.google.com/earth-engine/guides/command_line#mv)
    * [project_config](https://developers.google.com/earth-engine/guides/command_line#project_config)
    * [rm](https://developers.google.com/earth-engine/guides/command_line#rm)
    * [set_project](https://developers.google.com/earth-engine/guides/command_line#set_project)
    * [task](https://developers.google.com/earth-engine/guides/command_line#task)
    * [upload](https://developers.google.com/earth-engine/guides/command_line#upload)


The `earthengine` tool is a utility program that lets you manage Earth Engine assets and tasks from the command line. It is installed automatically when you [install the Python API](https://developers.google.com/earth-engine/guides/python_install). To check whether the tool is installed and functioning correctly, type the following on a command line:
```
  earthengine

```

If the tool is properly installed, it prints out a short summary of available commands. To get help on a specific command, use:
```
  earthengine command -h

```

When you first install the Python API you need to sign in using the `authenticate` command described below. The following sections describe the available commands in more detail.
## Service account credentials
To use the CLI with a service account's credentials, use the `service_account_file` flag to point to a JSON file containing the service account's key.
```
  earthengine --service_account_file=service_account_creds.json

```

## Usage in Colab
The Earth Engine Command Line Tool is preinstalled and ready for use in [Google Colab](https://colab.google/).
### Authentication
Authenticate for each new Colab session or if the virtual machine expires from inactivity (credentials are not saved across sessions).
Import the Python client library and call `ee.Authenticate()` to trigger the authentication flow. Follow the prompts to complete authentication. The default `auth_mode` in Colab is `colab`, see the [Authentication guide](https://developers.google.com/earth-engine/guides/auth#python_and_command_line) for other options.
```
importee
ee.Authenticate()

```

### Command execution
To run command line utilities, like the Earth Engine CLI, you need to prepend command calls with an exclamation point.
```
!earthengine -h

```

### Set a Cloud project
Use the `--project` option to set a Cloud project for each individual `earthengine` command.
```
!earthengine --project my-project <command>

```

Alternatively, set a default project to be used by all `earthengine` calls using the [`set_project`](https://developers.google.com/earth-engine/guides/command_line#set_project) command. The project will be added to a credentials file (~/.config/earthengine/credentials) and used for subsequent commands, unless overridden by the `--project` option. Set a default project for each new Colab session or if the virtual machine expires from inactivity (credentials are not saved across sessions).
```
!earthengine set_project my-project

```

## Command Reference
### authenticate
Authenticates the command line tool and Python client library to Earth Engine. Example:
```
  earthengine authenticate

```

Earth Engine uses the [OAuth 2.0 protocol](http://oauth.net/2/) for authenticating clients. The earthengine authenticate command will prompt you through the authentication process using your web browser.
You will need to [install gcloud](https://cloud.google.com/sdk/docs/install) if using the default gcloud authentication mode. See other authentication modes available through the `auth_mode` parameter in the [authentication guide](https://developers.google.com/earth-engine/guides/auth).
### acl
Prints or updates the access control list (ACL) of an Earth Engine asset. The ACL controls who can read or write to an asset. Examples:
```
  earthengine acl get projects/my-project/assets/asset_id
  earthengine acl set public projects/my-project/assets/asset_id
  earthengine acl ch -u username@gmail.com:R projects/my-project/assets/asset_id

```

The `get` sub-command prints a JSON description of the ACL. The `set` sub-command sets an ACL provided in a file with the same JSON format. You can copy an ACL from one asset to others by saving the output from `get` and providing it to `set`.
The set sub-command also accepts two special ACL names:
  * `private`: Removes permissions from everyone except the owner.
  * `public`: Grants read permission to all users.


The `ch` sub-command lets you make individual changes to an ACL. To grant read permission specify `-u username@gmail.com:R`, to grant write permission specify `-u username@gmail.com:W`, and to remove a user's permissions specify `-d username@gmail.com`. The special user identifier `AllUsers` may be used to grant or revoke read permission to or from all users. (Note that revoking `AllUsers` permissions does _not_ revoke any additional permissions you may have also granted to individual users.)
### asset
Prints or updates metadata associated with the an Earth Engine asset. Examples:
```
  earthengine asset info projects/my-project/assets/asset_id
  earthengine asset set -p name=value projects/my-project/assets/asset_id

```

The `info` sub-command prints detailed information about the asset, including its metadata, in JSON form. The `set` sub-command sets individual metadata properties on an asset.
The values of metadata properties that you set may be either numbers or strings. When setting property names using the `--property` or `-p` flag, separate the property name and value with an equals sign. The data type is detected automatically, or you may specify it explicitly by prefixing the property name with `(string)`, `(number)`, or `(date)`. For example, this sets a string-valued property with the value `"42"`:
```
  earthengine asset set -p '(string)name=42' projects/my-project/assets/asset_id

```

(The quotes in this example prevent the shell from interpreting the parentheses. They may or may not be necessary, depending on your shell and platform.)
To delete a property, set it to `null` without a type:
```
  earthengine asset set -p name=null projects/my-project/assets/asset_id

```

Date properties are just numbers that represent a number of milliseconds since the Unix epoch (_i.e._ midnight on January 1st, 1970) and may be specified directly as a number or in one of the following formats:
```
  YYYY-MM-DD
  YYYY-MM-DDThh:mm:ss
  YYYY-MM-DDThh:mm:ss.f

```

The time zone is assumed to be UTC. You may set the special start and end time properties using the `--time_start` and `--time_end` flags:
```
  earthengine asset set --time_start 1978-10-15T12:34:56 projects/my-project/assets/asset_id

```

### cp
Copies an asset. Example:
```
  earthengine cp projects/my-project/assets/asset_id projects/my-project/assets/new_asset_id

```

### create
Creates new folders and image collections. Example:
```
  earthengine create folder projects/my-project/assets/folder_id
  earthengine create collection projects/my-project/assets/collection_id

```

Use the `folder` sub-command to create folders and the `collection` to create image collections. You can specify the `-p` option to recursively create parent folders as required. Newly-created folders and images have private ACLs by default.
### ls
Lists the contents of one or more folders or collections. Example:
```
  earthengine ls users/username

```

The `-l` option requests a long format with more information about each asset (currently just its type). You may specify `--max_items number` (or `-m` for short) to limit the number of items from each folder or collection you list:
```
  earthengine ls -m 10 projects/my-project/assets/my_large_collection

```

Running the `ls` command with no arguments will list the top-level folders that you own.
### model
Tool with which to manipulate TensorFlow saved models.
#### `model prepare`
Prepare a saved model for serving in Earth Engine. Specifically, this transforms your `SavedModel` into a form suitable for processing requests from Earth Engine. ([Learn more about `SavedModel`](https://www.tensorflow.org/guide/saved_model#save_and_restore_models).)
```
  earthengine model prepare my_source_dir my_dest_dir '{"Conv2D:0":"my_input_band"}' '{"Sigmoid:0":"my_output_band"}'

```

Learn more about AI Platform models [here](https://developers.google.com/earth-engine/guides/tensorflow#eemodel). See a complete example [here](https://developers.google.com/earth-engine/guides/tf_examples#deploying-to-ai-platform).
### mv
Moves or renames an asset. Example:
```
  earthengine mv projects/my-project/assets/asset_id projects/my-project/assets/new_asset_id

```

### project_config
**Preview:** setting the project configuration is a Preview feature, so invocations must include the `alpha` keyword.
Sets project configuration values. Before using this command, be sure to set a project using [`set_project`](https://developers.google.com/earth-engine/guides/command_line#set_project).
#### get
To view a project configuration, use the `get` sub-command:
```
  earthengine alpha project_config get

```

If you have [permission to view the project's batch task settings](https://developers.google.com/earth-engine/cloud/roles_permissions#batch-task-management), the output contains:
  * `maxConcurrentExports`: a number indicating the maximum number of batch tasks that can run in parallel across all users for the given project. By default, this is set to the maximum allowed by the associated billing account's [subscription plan](https://cloud.google.com/earth-engine/pricing).


Additionally, if you have [permission to view the plan configuration](https://developers.google.com/earth-engine/cloud/roles_permissions#batch-task-management), the output contains:
  * `planMaxConcurrentExports`, a number indicating the maximum number of batch tasks that can run in parallel across all users and projects that use the billing account.


#### set
To update the project's configuration, use the `set` sub-command. The following settings can be configured:
  * `max_concurrent_exports`, to control the project's maximum [batch task parallelism](https://developers.google.com/earth-engine/guides/usage#concurrent_batch_tasks)
    * requires the correct [permissions](https://developers.google.com/earth-engine/cloud/roles_permissions)


For example, to configure a project to only ever allow 10 tasks to run in parallel for the given project:
```
  earthengine alpha project_config set --max_concurrent_exports=10

```

The output displays the updated project configuration, identical to what [`get`](https://developers.google.com/earth-engine/guides/command_line#project_config-get) returns.
For more information about batch task parallelism, see the [Earth Engine quotas](https://developers.google.com/earth-engine/guides/usage#concurrent_batch_tasks) page.
### rm
Deletes one or more assets. Example:
```
  earthengine rm projects/my-project/assets/asset_id
  earthengine rm -r projects/my-project/assets/folder_id

```

You can use the `-r` flag to delete the contents of a folder or collection recursively. For safety when deleting multiple assets, you can use the `--dry_run` flag to verify exactly what will be deleted without actually deleting anything.
### set_project
Sets the Google Cloud project through which computation requests are routed.
```
  earthengine set_project foo-project

```

This command is needed prior to running commands that require Cloud functionality, for example [`model`](https://developers.google.com/earth-engine/guides/command_line#model).
### task
Prints information about or manages long-running tasks. Examples:
```
  earthengine task list
  earthengine task list -l
  earthengine task info TASK_ID
  earthengine task cancel TASK_ID

```

The `list` sub-command lists basic information about the tasks that you submitted recently. The `-l` option requests a long format with more information about each task. The `info` sub-command prints detailed information about individual tasks. The `cancel` sub-command cancels one or more running tasks.
### upload
Uploads images or tables from Google Cloud Storage to Earth Engine, or creates assets backed by external images.
#### image
To upload an image asset using default settings:
```
  earthengine upload image --asset_id=projects/my-project/assets/asset_id gs://bucket/image.tif

```

If you specify multiple input image files they will be interpreted as tiles of a single image asset. You can learn more about the options for uploading images to Earth Engine in [Uploading image assets: Advanced options](https://developers.google.com/earth-engine/guides/image_upload#advanced-options).
You can specify the pyramid reduction policy using the `--pyramiding_policy` flag, which can be set to one of `mean` (the default), `sample`, `mode`, `min`, or `max`. This will control how Earth Engine generates the pyramid of lower-resolution versions of your image:
```
  earthengine upload image --asset_id=projects/my-project/assets/asset_id --pyramiding_policy=sample gs://bucket/image.tif

```

You can use the `--last_band_alpha` to indicate that the mask for the image should be taken from an alpha channel in the last band:
```
  earthengine upload image --asset_id=projects/my-project/assets/asset_id --last_band_alpha gs://bucket/image.tif

```

You can specify a no-data value using the `--nodata_value` flag. This will mask any pixels in the image with that value:
```
  earthengine upload image --asset_id=users/myuser/asset --nodata_value=255 gs://bucket/image.tif

```

You may also specify metadata properties to set on the asset using the same flags that are accepted by the `asset set` command [described above](https://developers.google.com/earth-engine/guides/command_line#asset). The options are also described in the [Image Manifest](https://developers.google.com/earth-engine/guides/image_manifest) guide.
#### table
To upload a Shapefile, CSV, or TFRecord from Google Cloud Storage to an Earth Engine table asset, you can use any of:
```
  earthengine upload table --asset_id=projects/my-project/assets/myUploadedShapefile gs://bucket/foo.shp
  earthengine upload table --asset_id=projects/my-project/assets/myUploadedCSV gs://bucket/foo.csv
  earthengine upload table --asset_id=projects/my-project/assets/myUploadedTFRecord gs://bucket/foo.tfrecord

```
**Note:** when uploading Shapefiles, you only need to specify the path to the `.shp` file. The related `.dbf`, `.shx`, and `.prj` files must be present in the same location. Alternatively, you can specify a `.zip` file that contains the necessary files.
There are many options pertaining to the way in which CSV and TFRecord files are interpreted. You can see a complete list of table upload options by visiting the [Table Manifest](https://developers.google.com/earth-engine/guides/table_manifest) guide or with:
```
  earthengine upload table -h

```

#### external_image
**Preview:** Creating an asset backed by an external image is a Preview feature, so invocations must include the `alpha` keyword.
To create an asset backed by an external image, run the `upload_image` command with a manifest:
```
earthengine alpha upload external_image --manifest /tmp/foo.json

```

An example manifest is:
```
{
"name":"projects/{project}/assets/cogdemo1",
"tilesets":[
{"id":"0","sources":[{"uris":["gs://ee-docs-demos/COG_demo.tif"]}]}
],
"properties":{
"source":"https://code.earthengine.google.com/d541cf8b268b2f9d8f834c255698201d"
},
"startTime":"2016-01-01T00:00:00.000000000Z",
"endTime":"2016-12-31T15:01:23.000000000Z"
}

```

See the [Cloud GeoTIFF](https://developers.google.com/earth-engine/Earth_Engine_asset_from_cloud_geotiff) guide and the [Image Manifest](https://developers.google.com/earth-engine/guides/image_manifest) guide for more details on constructing the manifest.
Was this helpful?
