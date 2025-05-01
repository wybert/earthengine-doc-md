 
#  Earth Engine access 
Stay organized with collections  Save and categorize content based on your preferences. 
Earth Engine runs on Google Cloud and requires Cloud projects for access and API management. All Earth Engine calls (whether from the Code Editor, client libraries, Apps, or REST API) are routed through a Cloud project, enabling access control, resource management, and usage monitoring in the Cloud Console.
## Get access to Earth Engine
To use Earth Engine you'll need access to a Cloud project that:
  * has the Earth Engine API enabled,
  * is registered for [commercial](https://earthengine.google.com/commercial) or [noncommercial](https://earthengine.google.com/noncommercial) use, and
  * grants you (or the user) the [correct roles and permissions](https://developers.google.com/earth-engine/guides/access_control).


### Create a project
Visit the [ registration page](https://console.cloud.google.com/earth-engine) to create and register a new Cloud project or register an existing project. 
Projects created during the registration process can be managed in the [ Google Cloud Console](https://console.cloud.google.com/cloud-resource-manager). You can activate or deactivate the Earth Engine API from the [ Earth Engine API page on the Cloud Console](https://console.cloud.google.com/apis/library/earthengine.googleapis.com). 
**Note:** In some cases, your organization's IT policy may prevent you from creating Google Cloud projects. In that case, we recommend reaching out to your admins to grant you the correct permissions (or to create a project for you). 
_Manual steps (automated by the registration page)_
The [ registration page](https://console.cloud.google.com/earth-engine) automates these steps and is recommended. 
#### Create a Cloud project
If you haven't already, create a [ Google Cloud Project](https://cloud.google.com/resource-manager/docs/creating-managing-projects). You can do so from the [projects page](https://console.cloud.google.com/project) of the Cloud Console or click the following button: 
[ Create a Cloud project](https://console.cloud.google.com/projectcreate)
#### Enable the Earth Engine API
To enable the Earth Engine API for your project, click the following button to go to the Earth Engine API page: 
[ Enable the Earth Engine API](https://console.cloud.google.com/apis/library/earthengine.googleapis.com)
On the Earth Engine API page, ensure that you have selected your project, and click the ENABLE button. 
#### Register the project for commercial or noncommerial use
Edit the following URL for your project, visit the page, and complete the registration flow. 
```
https://code.earthengine.google.com/register?project=my-project
```

#### Create an assets folder (optional)
You can create an Earth Engine assets folder associated with a Cloud project to which you have access using the [ `earthengine create folder`](https://developers.google.com/earth-engine/guides/command_line#create) command using a path as described [here](https://developers.google.com/earth-engine/cloud/assets#personal-assets). For example: 
```
earthengine create folder projects/my-project/assets/
```

You can also create an asset folder for a project in the Code Editor by [adding the project](https://developers.google.com/earth-engine/cloud/assets#add-a-project) in the Assets panel. 
You don't need to create this folder unless you plan to store assets in the project. 
### Use an existing project
Check with your organization's IT staff about existing Cloud projects configured for Earth Engine. Ensure that the Google Account you'll use to access Earth Engine services is granted the [correct roles and permissions](https://developers.google.com/earth-engine/guides/access_control) on the project.
## Specify a project
The following sections describe how to specify a project for the various interfaces to Earth Engine's services.
### Client libraries (Python, JavaScript)
The `ee.Initialize()` function is used to specify a project for Earth Engine requests originating from the [Python](https://developers.google.com/earth-engine/guides/python_install) and [JavaScript](https://developers.google.com/earth-engine/guides/npm_install) client libraries. There are several ways to configure project specification, see the [authentication and initialization](https://developers.google.com/earth-engine/guides/auth#python_and_command_line) page for more details.
### Code Editor
Click the profile icon in the top right corner of the [Code Editor](https://developers.google.com/earth-engine/playground) and select "Change Cloud Project" from the menu. Choose a project from the selection dialog.
### Earth Engine Apps
When [publishing an Earth Engine App](https://developers.google.com/earth-engine/guides/apps#publishing-your-app), you'll be prompted to select a project to route requests through. Follow instructions in the publishing dialog.
### Command-line tool
To associate Earth Engine calls from the [command-line tool](https://developers.google.com/earth-engine/guides/command_line) with a Cloud project, use the `--project` parameter in your call to `earthengine` or use [`set_project`](https://developers.google.com/earth-engine/guides/command_line#set_project) to set a default project.
### REST API
To associate calls to the REST API with a Cloud project, issue authenticated HTTP calls where authentication is handled by `oauth2`. In a local environment, you can use the [`gcloud`](https://cloud.google.com/sdk/gcloud/reference/auth/application-default/login) command. You can also use a service account associated with a Cloud Project. See the [REST API Quickstart](https://developers.google.com/earth-engine/reference/Quickstart#authenticate-to-google-cloud) for an example of using `google.oath.service_account.Credentials.from_service_account_file()` to authenticate with a service account.
## Configure project access
The following sections describe how to configure Earth Engine-enabled projects for use by other individuals and service accounts.
### Service accounts
**Key Term:** **[Service account](https://cloud.google.com/iam/docs/overview#service-account)** , an account typically used by an application or compute workload, such as a [Compute Engine](https://cloud.google.com/products/compute) instance, rather than a person.
Service accounts automatically have access once their parent project is registered and has the Earth Engine API enabled. They also need the correct [permissions](https://developers.google.com/earth-engine/guides/access_control) within the project. Any number of service accounts on a project can be configured to use Earth Engine. Visit the [service accounts](https://developers.google.com/earth-engine/guides/service_account) page to learn more about using service accounts with Earth Engine.
### Google Accounts
**Key Term:** **[Google Account](https://cloud.google.com/iam/docs/overview#google-account)** , an account belonging to an individual user, such as a Gmail account (example@gmail.com) or Google Workspace account.
Cloud projects use Cloud IAM to manage roles and permissions. In order for other humans to access Earth Engine via your project, you'll need to use the [Cloud Console](https://console.cloud.google.com/iam-admin/iam) to grant them the [correct roles and permissions](https://developers.google.com/earth-engine/guides/access_control).
### OAuth 2.0 Client ID
**Key Term:** [OAuth 2.0 Client ID](https://datatracker.ietf.org/doc/html/rfc6749#section-2.2): A unique application identifier used by Google to authenticate and authorize access to user resources during the OAuth 2.0 authorization process.
You may need to create an OAuth 2.0 Client ID from a project, for example to create an app that passes user credentials to Earth Engine. You can manage credentials for your Cloud project by going to the [Cloud Console](https://console.cloud.google.com) menu (menu) and selecting **APIs & Services** > [**Credentials**](https://console.cloud.google.com/apis/credentials). (Choose the project if prompted).
To create a new Client ID for the project, click [+ CREATE CREDENTIALS](https://console.cloud.google.com/apis/credentials/oauthclient) > **OAuth client ID** > **Web application**.
In the configuration of the web application:
  * Specify authorized JavaScript origins, for example:

```
http://localhost:8080
https://foo-ee-project.appspot.com

```

  * Specify authorized redirect URIs, for example:

```
http://localhost:8080/oauth2callback
https://foo-ee-project.appspot.com/oauth2callback

```

[Learn more about authenticating users with OAuth](https://developers.google.com/identity/protocols/OAuth2UserAgent).
### Common scenarios
#### I'm teaching an educational class...
Great! If you register a noncommercial project, no billing configuration is required. Then, you can add your students to the project.
#### I'm part of an operational team/commercial organization...
Great! You're able to register a project for commercial use, and add your collaborators to it. Please also pay attention to the seat limit in the Earth Engine subscription that you select.
## Earth Engine data deletion
### Account-level deletion
[Account-level deletion](https://support.google.com/accounts/answer/32046) will remove **all** Earth Engine data from your account.
If your account is part of a Google Workspace organization, your administrator controls your account data. When an [administrator deletes a Google Account](https://support.google.com/a/answer/33314), **all** associated Earth Engine data are wiped out within approximately 30 days.
It's not possible for the Earth Engine team to recover data once they're deleted.
### Cloud projects
When a [Cloud project is deleted](https://cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects), it triggers the deletion of Earth Engine data associated with that project (including, for example, any assets stored in the project root, any project-level EE Apps, Monitoring data, etc.). This process _may_ be reversible for up to 30 days, but it's never possible to recover those data after 30 days.
### Assets
The simplest method for deleting your assets is to use the "Assets" tab in the Code Editor to view and manually delete your Earth Engine assets.
For programmatic asset deletion of an asset with ID `projects/{project-id}/assets/{asset-id}` (e.g., `projects/my-project/assets/my-asset`):
### Python client
```
ee.data.deleteAsset('projects/my-project/assets/my-asset')

```

### JavaScript client
Note that the Code Editor's security sandbox prevents this call from working in that environment.
```
ee.data.deleteAsset('projects/my-project/assets/my-asset')

```

### Command-line tool
Use the `rm` command:
```
earthenginermprojects/my-project/assets/my-asset
```

**Note:** for legacy user-owned assets, the path structure is `users/{user-id}/{asset-id}`.
### Code Editor scripts
To delete your [Earth Engine Code Editor scripts](https://developers.google.com/earth-engine/guides/playground#script_manager_scripts_tab):
### Code Editor
From the ["Scripts" tab in the Code Editor](https://developers.google.com/earth-engine/guides/playground#script_manager_scripts_tab), select a script or repository and delete it. Once a repository has been marked as deleted, it becomes unrecoverable within 30 days.
### Using Git
Advanced users can use Git to manage their scripts. See <https://earthengine.googlesource.com/> to list the repositories that you can view.
### Earth Engine Apps
To delete your Earth Engine Apps, use the ["Apps" button in the Code Editor to manage your Apps](https://developers.google.com/earth-engine/guides/apps#publishing-your-app).
### "Get Link" references
Use the [Manage Links page](https://code.earthengine.google.com/links?page_size=1000&days=all) to view and delete your "Get Link" links from the Code Editor. This page can be found by navigating to the ["Manage Links" option in the drop-down menu](https://developers.google.com/earth-engine/guides/playground#get_link) next to the "Get Link" button.
## Terminating commercial access
If you are a direct customer of Earth Engine and want to stop using Earth Engine in a paid context, there are several changes needed to stop incurring charges:
  * **Stop subscription charges**
    * To terminate the Earth Engine subscription on your billing account, you need to use the "Manage Plans" page (accessible from the user settings drop-down menu in the top right of the Code Editor when using a registered Cloud project linked to that billing account).
    * You can also access the "Manage Plans" page directly for a billing account:
```
https://code.earthengine.google.com/manage/plans?billing=YOUR_BILLING_ACCT_ID

```

    * Choosing the "Limited" plan stops your billing account from incurring any further Earth Engine platform subscription fees after your current billing cycle.
  * **Stop compute charges**
    * To prevent new charges related to compute (EECU-time), disable the Earth Engine API on your Cloud project(s). Note that this doesn't terminate in-progress requests or [delete stored objects](https://developers.google.com/earth-engine/guides/access#earth_engine_data_deletion), so you may still incur Earth Engine charges even with the API disabled.
    * See the [API Console Help](https://support.google.com/googleapi/answer/6158841) for information about disabling APIs.
  * **Stop storage charges**
    * Stored Earth Engine assets continue to drive costs even if the API is disabled. [Deleting your assets](https://developers.google.com/earth-engine/guides/access#assets) stops you from incurring further EE storage fees.


