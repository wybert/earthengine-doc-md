 
#  Access control 
Stay organized with collections  Save and categorize content based on your preferences. 
You can share the assets or compute quota of your [Earth Engine enabled project](https://developers.google.com/earth-engine/guides/access) with other Earth Engine users at the project level. Earth Engine assets or compute can be shared with another user or group of users. If you want to share with a group of users, [Create a new Google Group](https://groups.google.com/forum/#!creategroup) and note its email (available from the About link on the group page). This page describes how to provide access to resources, for either an individual or group and the [Roles and Permissions](https://developers.google.com/earth-engine/guides/access_control#roles_and_permissions) required for different activities.
## Set Earth Engine service usage
To use the Earth Engine API on a Cloud project, the API must be [enabled on the project](https://developers.google.com/earth-engine/guides/access), and the user must have at least the permissions in the _Earth Engine Resource Viewer_ role (learn more about [predefined Earth Engine IAM Roles](https://developers.google.com/earth-engine/guides/access_control#predefined_earth_engine_iam_roles)). Additionally, the user must have at least `serviceusage.services.use` permission on the project. That permission can be provided through the project _Owner_ or _Editor_ roles, or through the specific [_Service Usage Consumer_ role](https://cloud.google.com/service-usage/docs/access-control#roles). An error will be thrown if the user does not have required Earth Engine permissions and Service Usage permissions on the selected project.
## Set asset permissions
### Set asset-level permissions
There are [several options](https://developers.google.com/earth-engine/guides/manage_assets#set_asset_permissions) to update permissions at the asset level.
  * Use the Assets Manager in the Code Editor.
  * Use the Earth Engine command line.
  * Use a client library, for example, `ee.data.setAssetAcl()`.
  * Or call the [REST API](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets) directly.


### Set project-level asset permissions
Sharing at the project level sets permissions on all assets in your Earth Engine enabled Cloud project at once.
You can share assets at the project level by assigning the appropriate [Identity and Access Management (IAM)](https://cloud.google.com/iam/docs/overview) role on your project's IAM admin page. There are [Predefined Earth Engine IAM Roles](https://developers.google.com/earth-engine/guides/access_control#predefined_earth_engine_iam_roles) for sharing Earth Engine assets and resources. See [Understanding Roles](https://cloud.google.com/iam/docs/understanding-roles) for a more general overview of IAM roles.
When another user attempts to access one of your assets, permissions are first checked at the asset level. If permissions have not been set at the asset level or the check fails (i.e., no access), permissions will be checked at the project level.
## Set project level permissions
To set permissions at the project level, assign a project IAM role to a user or group of users:
  1. Open the IAM page in the Google Cloud console [ Open the IAM Page](https://console.cloud.google.com/iam-admin) Or hold the pointer over your project name on the **Assets** tab of the Code Editor and click the  share icon.
  2. Click **select a project** and choose your project (you should already be there if you opened the IAM page from the Code Editor).
  3. Click **ADD** at the top and add the individual or group email as the new member, or click the edit icon next to the existing member in the project.
  4. In the **Role** drop down search for the _Earth Engine Resource_ role you want to grant. See [Predefined Earth Engine IAM Roles](https://developers.google.com/earth-engine/guides/access_control#predefined_earth_engine_iam_roles) for details.
  5. Click the **SAVE** button.

**Note:** the special user identifiers [`allUsers`](https://cloud.google.com/iam/docs/overview#all-users) and [`allAuthenticatedUsers`](https://cloud.google.com/iam/docs/overview#all-authenticated-users) are [not supported project principal types](https://cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy).
## VPC Service Controls
Earth Engine supports [VPC Service Controls](https://cloud.google.com/security/vpc-service-controls), a Google Cloud security feature which helps users secure their resources and mitigate data exfiltration risk. Adding resources to a VPC service perimeter allow for more control over data read and write operations.
Learn more about [VPC-SC features and configuration](https://cloud.google.com/security/vpc-service-controls#documentation).
### Limitations
Enabling VPC Service Controls for your resources comes with a few limitations, for which we provided example workarounds:
Limitation | Example alternative  
---|---  
[Code Editor](https://code.earthengine.google.com/) is not supported and VPC Service Controls won't allow using it with resources and clients inside a service perimeter.  |  Use [ Earth Engine Python API](https://developers.google.com/earth-engine/tutorials/community/intro-to-python-api) together with [ the `geemap` library](https://developers.google.com/earth-engine/guides/image_visualization#colab-python).   
[ Legacy assets](https://developers.google.com/earth-engine/cloud/assets#legacy-assets_1) are not protected by VPC Service Controls.  |  Use assets [ stored in Cloud projects](https://developers.google.com/earth-engine/cloud/assets).   
[ Export to Google Drive](https://developers.google.com/earth-engine/guides/exporting) is not supported by VPC Service Controls.  | 
  * Use [ other available export destinations](https://developers.google.com/earth-engine/guides/exporting) like [Google Cloud Storage](https://cloud.google.com/storage) and [BigQuery](https://developers.google.com/earth-engine/guides/exporting_to_bigquery). 
  * Save your resources in Earth Engine by exporting [ raster](https://developers.google.com/earth-engine/guides/exporting_images#to_asset) or [ tabular](https://developers.google.com/earth-engine/guides/exporting_tables#to_asset) data to assets.

  
[ Earth Engine Apps](https://developers.google.com/earth-engine/guides/apps) are not supported for resources and clients inside a service perimeter. |  No workaround available.   
Using Earth Engine with resources inside a secured VPC service perimeter is only available for Professional and Premium pricing plans. Trying to use Earth Engine API with a VPC-SC secured project associated with a Basic pricing plan will result in an error. To learn more about Earth Engine pricing visit [official documentation](https://cloud.google.com/earth-engine/pricing).
More information about VPC Service Controls and its limitations can be found in [Supported products and limitations](https://cloud.google.com/vpc-service-controls/docs/supported-products).
## Roles and permissions
The following sections describe the permissions and roles required to perform activities and access Earth Engine resources. See the Google Cloud documentation to learn more about Cloud project [permissions](https://cloud.google.com/iam/docs/permissions-reference) and [roles](https://cloud.google.com/iam/docs/understanding-roles).
### Predefined Earth Engine IAM Roles
Earth Engine provides predefined roles which allow varying degrees of control over Earth Engine resources within a project. These roles are:
Role | Title | Description  
---|---|---  
`roles/earthengine.viewer` | Earth Engine Resource Viewer | Provides permission to view and list Assets and tasks.  
`roles/earthengine.writer` | Earth Engine Resource Writer | Provides permission to read, create, modify and delete assets, import images and tables, read and update tasks, perform interactive computations, and create long running export tasks.  
`roles/earthengine.admin` | Earth Engine Admin | Provides permission for all Earth Engine resources including changing access controls for Earth Engine assets.  
`roles/earthengine.appsPublisher` | Earth Engine Apps Publisher | Provides permission to create a service account for use with an Earth Engine app. Also grants permission to edit and delete Project-owned apps under the Cloud Project.  
Note that you may set a [primitive](https://cloud.google.com/iam/docs/understanding-roles#primitive_roles) or [custom](https://cloud.google.com/iam/docs/understanding-custom-roles) role if the predefined Earth Engine roles don't meet your needs. You can see the bundle of permissions associated with each role from the [IAM Roles page](https://console.cloud.google.com/iam-admin/roles) by filtering to a specific role and clicking on the role.
### Full access to the Earth Engine API
To give users full access to the Earth Engine service, either through the REST API directly, through the Code Editor or through a client library, users will need permission to perform operations like:
  * Executing Earth Engine expressions
  * Running batch computations (exports)
  * Getting interactive results (online maps, thumbnails, charts, etc.)
  * Creating/deleting Earth Engine assets
  * [Using OAuth Authentication via a Client Library](https://developers.google.com/earth-engine/guides/auth#authentication_with_earth_engine_client_library_helpers) to connect to Earth Engine

Permissions needed | 
  * `clientauthconfig.clients.listWithSecrets`
  * `earthengine.assets.get`
  * `earthengine.assets.getIamPolicy`
  * `earthengine.assets.list`
  * `earthengine.computations.create`
  * `earthengine.operations.get`
  * `earthengine.operations.list`
  * `monitoring.timeSeries.list`
  * `resourcemanager.projects.get`
  * `resourcemanager.projects.list`
  * `serviceusage.operations.get`
  * `serviceusage.operations.list`
  * `serviceusage.quotas.get`
  * `serviceusage.services.get`
  * `serviceusage.services.list`
  * `serviceusage.services.use`

  
---|---  
Suggested roles | 
  * _Service Usage Consumer_ (`roles/serviceusage.serviceUsageConsumer`) AND one of:
    * _Earth Engine Resource Viewer_ (`roles/earthengine.viewer`) OR
    * _Earth Engine Resource Writer_ (`roles/earthengine.writer`) OR
    * _Earth Engine Resource Admin_ (`roles/earthengine.admin`)
  * _OAuth Config Editor_ (`roles/oauthconfig.editor`) is additionally required for users who access Earth Engine through a notebook environment and use the Notebook Authenticator. See [ Colab or JupyterLab notebook authentication](https://developers.google.com/earth-engine/guides/python_install#expandable-1) for more details.

  
Notes |  Google Cloud requires the _Service Usage Consumer_ role to use the project as the active project when calling APIs, and `ee.Initialize(project=X)` will fail without this permission on project X. Additionally you can then select this project in the Cloud Console to [display](https://developers.google.com/earth-engine/cloud/api_monitoring) your use of resources.   
### Asset sharing only
Grant the user one of the [Predefined Earth Engine IAM Roles](https://developers.google.com/earth-engine/guides/access_control#predefined_earth_engine_iam_roles) with minimal permissions to perform the needed activity. Note that users won't be able to consume project resources without necessary `serviceusage` permissions.
### Project management
#### List and display available projects
This happens when using the Code Editor to browse available projects.
Permissions needed | 
  * `resourcemanager.projects.get`
  * `resourcemanager.folders.list`
  * `resourcemanager.folders.get`
  * `resourcemanager.organizations.get` (uncommon)

  
---|---  
Suggested roles | 
  * _Viewer_ (`roles/viewer`) OR _Earth Engine Resource Viewer_ (`roles/earthengine.viewer`) on relevant projects OR _Browser_ (`roles/browser`, recommended for advanced organization cases) 
  * _Folder Viewer_ (`roles/resourcemanager.folderViewer`) on relevant folders 

  
#### Select a project for use in the Code Editor
Permissions needed | 
  * `resourcemanager.projects.get`
  * `serviceusage.services.get`


###### If project has not previously been set up
On first selecting a project through the Code Editor, the project is initialized for use with Earth Engine. If this hasn't been done before, you will need these roles for setup to succeed.
  * `resourcemanager.projects.update` AND
  * `serviceusage.services.enable`

  
---|---  
Suggested roles | 
  * _Viewer_ (`roles/viewer`) OR 
  * _Earth Engine Resource Viewer_ (`roles/earthengine.viewer`) AND _Service Usage Consumer_ (`roles/serviceusage.serviceUsageConsumer`) 


###### Additional roles (if project has not previously been set up)
  * _Editor_ (`roles/editor`) OR
  * _Project Mover_ (`roles/resourcemanager.projectMover`) AND _Project IAM Admin_ (`roles/resourcemanager.projectIamAdmin`) AND _Service Usage Admin_ (`roles/serviceusage.serviceUsageAdmin`) 

  
#### Create project through the Code Editor
Permissions needed | 
  * `resourcemanager.projects.get`
  * `resourcemanager.projects.create`
  * `resourcemanager.projects.update`
  * `serviceusage.services.get`
  * `serviceusage.services.enable`

  
---|---  
Suggested roles | 
  * _Editor_ (`roles/editor`) OR
  * _Project Mover_ (`roles/resourcemanager.projectMover`) AND _Project Creator_ (`roles/resourcemanager.projectCreator`) AND _Service Usage Admin_ (`roles/serviceusage.serviceUsageAdmin`) 

  
Notes  |  Your organization may not grant you the _Editor_ role, so the finer-grained roles may be needed. _Project Mover_ is needed to cover the `projects.update` permission.   
#### Commercial Project Registration
The following permissions pertain to [registering projects for paid use](https://console.cloud.google.com/earth-engine).
Permissions needed  
---  
Billing account | If the billing account already has an Earth Engine plan, then **no billing account permissions are needed**. Otherwise: 
  * `billing.accounts.get` (for creating a new Limited plan)
  * `billing.subscriptions.create` (for creating a new Basic or Professional plan)

  
Cloud project | 
  * `earthengine.computations.create`
  * `earthengine.config.update`
  * `serviceusage.services.get`
  * `serviceusage.services.enable`

  
Suggested roles  
Billing account | If the billing account already has an Earth Engine plan, then **no billing account permissions are needed**. Otherwise: 
  * _Billing Account User_ (`roles/billing.user`), for creating a new Limited plan 
  * _Billing Account Administrator_ (`roles/billing.admin`), for creating a new Basic or Professional plan 

  
Cloud project | 
  * _Earth Engine Resource Writer_ (`roles/earthengine.writer`) 
  * _Service Usage Admin_ (`roles/serviceusage.serviceUsageAdmin`) 

  
### Commercial Earth Engine plan management
The following permissions pertain to managing [Earth Engine pricing plans](https://cloud.google.com/earth-engine/pricing#monthly_subscriptions).
Permissions needed on the billing account  | 
  * `billing.subscriptions.create` (to change an Earth Engine plan)
  * `billing.subscriptions.list` (to view the current Earth Engine plan)

  
---|---  
Suggested roles on the billing account  | 
  * _Billing Account Viewer_ (`roles/billing.viewer`), to view the current Earth Engine plan
  * _Billing Account Administrator_ (`roles/billing.admin`), to change an Earth Engine plan

  
### Batch task management
The following permissions pertain to configuring [per-project limits on batch task concurrency](https://developers.google.com/earth-engine/guides/usage#concurrent_batch_tasks). This feature is only available for commercial users of Earth Engine.
#### Viewing project-level batch task limits
Permissions needed on the Cloud account  |  `earthengine.config.get`  
---|---  
#### Setting project-level batch task limits
Permissions needed on the Cloud account  |  `earthengine.config.update` Note: This permission also encompasses viewing the plan-level limits that are configured on the billing account.   
---|---  
Permissions needed on the billing account  |  `billing.subscriptions.list`  
### Apps management
#### Display app info
Permissions needed  | 
  * `iam.serviceAccounts.get`
  * `iam.serviceAccounts.getIamPolicy`, if app is restricted (less common)

  
---|---  
Suggested roles  |  _Viewer_ (`roles/viewer`) OR _Earth Engine Apps Publisher_ (`roles/earthengine.appsPublisher`)   
#### Publish/Update app
Permissions needed | 
  * `iam.serviceAccounts.get`
  * `iam.serviceAccounts.create`
  * `iam.serviceAccounts.enable`
  * `iam.serviceAccounts.getIamPolicy`
  * `iam.serviceAccounts.setIamPolicy`
  * `iam.serviceAccounts.disable`, if app is moved from one project to another (uncommon)

  
---|---  
Suggested roles |  _Earth Engine Apps Publisher_ (`roles/earthengine.appsPublisher`) OR _Service Account Admin_ (`roles/iam.serviceAccountAdmin`)   
Notes | 
  * In addition, Earth Engine App service accounts identify themselves to the Earth Engine servers by presenting an OAuth access token. Therefore, certain identities are added during app creation as _Service Account Token Creator_ (`roles/iam.serviceAccountTokenCreator`) on the service accounts.
  * In the case of a public Earth Engine App, the identity granted that role is `earth-engine-public-apps@appspot.gserviceaccount.com` and in the case of restricted apps the identity is the Access Restriction Google Group configured by the app creator.

  
#### Delete and app
Permissions needed | `iam.serviceAccounts.disable`  
---|---  
Suggested roles |  _Earth Engine Apps Publisher_ (`roles/earthengine.appsPublisher`) OR _Service Account Admin_ (`roles/iam.serviceAccountAdmin`)   
