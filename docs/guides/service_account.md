 
#  Service Accounts 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Create a service account](https://developers.google.com/earth-engine/guides/service_account#create-a-service-account)
  * [Create a private key for the service account](https://developers.google.com/earth-engine/guides/service_account#create-a-private-key-for-the-service-account)
    * [Keep your key file safe](https://developers.google.com/earth-engine/guides/service_account#keep-your-key-file-safe)
  * [Register the service account to use Earth Engine](https://developers.google.com/earth-engine/guides/service_account#register-the-service-account-to-use-earth-engine)
  * [Use a service account with a private key](https://developers.google.com/earth-engine/guides/service_account#use-a-service-account-with-a-private-key)
    * [What do I do if I get an invalid_grant error?](https://developers.google.com/earth-engine/guides/service_account#what-do-i-do-if-i-get-an-invalid_grant-error)
  * [Use a default service account](https://developers.google.com/earth-engine/guides/service_account#use-a-default-service-account)
  * [Set up REST API access](https://developers.google.com/earth-engine/guides/service_account#set-up-rest-api-access)


**Note:** You do not need a service account to use the Earth Engine Python API. See [these instructions](https://developers.google.com/earth-engine/guides/python_install) for setting up the Earth Engine Python client library. 
A [service account](https://cloud.google.com/iam/docs/service-accounts) is an account associated with an application rather than an end user. You may need to use a service account to authenticate to Earth Engine if you are developing an app or using the REST API. [Learn more about authenticating with service accounts.](https://developers.google.com/identity/protocols/oauth2/service-account)
## Create a service account
First, [create a Google Cloud project](https://developers.google.com/earth-engine/earthengine_cloud_project_setup#create-a-cloud-project) if you have not already done so. 
You can manage the service accounts for your Cloud project by going to the Cloud Console menu (menu) and selecting **IAM & Admin** > [**Service accounts**](https://console.cloud.google.com/iam-admin/serviceaccounts/). (Choose the project if prompted.)
To create a new service account, click the [+ CREATE SERVICE ACCOUNT](https://console.cloud.google.com/iam-admin/serviceaccounts/create) link. 
If you created an App Engine project, you may already have a default service account (**App Engine default service account**) for that project. If you are setting up an App Engine project, for the service account **Role** , choose **Project** > **Editor**. 
## Create a private key for the service account
Once you have a service account, click the menu for that account (more_vert), then **Create key** > **JSON**. Download the JSON key file. 
### Keep your key file safe
The key file is a special file that allows programs to access Google APIs on behalf of your service account. Ensure it is not possible for anyone to gain unauthorized access to it, since they would be able to access Google APIs on your behalf. Never store your private key in a public place, like a shared folder or a source repository. If you misplace your private key, you can easily revoke access to a service account and create a new one using the Cloud Console. See [this guide](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#deleting_service_account_keys) for details.
## Register the service account to use Earth Engine
All service accounts are created within a Cloud project, which may be the same project used for your App Engine app or Cloud VM. Ensure that the [Cloud project is registered](https://console.cloud.google.com/earth-engine) to access Earth Engine, and that the [Earth Engine API is enabled](https://console.cloud.google.com/apis/library/earthengine.googleapis.com) on the project. All service accounts in the project with the [correct permissions](https://developers.google.com/earth-engine/cloud/roles_permissions) will have access to Earth Engine, and there's no need to register them separately.
Note that individual service account registration is no longer possible; the Cloud project itself must be registered.
## Use a service account with a private key
To authenticate to Earth Engine using a service account:
  1. Create and download a JSON private key file (`.private-key.json`) for the service account.
  2. Test the following Python code from wherever you put the `.private-key.json` file: ```
importee
service_account = 'my-service-account@...gserviceaccount.com'
credentials = ee.ServiceAccountCredentials(service_account, '.private-key.json')
ee.Initialize(credentials)
```



If you are able to initialize without an error, your service account is ready to use. 
### What do I do if I get an invalid_grant error?
OAuth2 can be very sensitive to clock skew. If you're certain you've set everything up correctly and your Google contact has verified that the service account has been approved, check to see if your computer's clock is synchronized to network time.
For Ubuntu systems, the call to sync your computer's clock is:
```
ntpdate ntp.ubuntu.com

```

For systems using OS X, open **System Preferences** > **Date & Time** > **Date & Time** (again) and select **Set date and time automatically**.
## Use a default service account
If you are using [a default service account](https://cloud.google.com/compute/docs/access/service-accounts#default_service_account), you first need to [ modify the access scopes of the VM for the Compute Engine Service Account to "Allow full access to all Cloud APIs"](https://cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#changeserviceaccountandscopes). (If you are using default service accounts in Dataflow or App Engine, this step is not necessary.) 
To authenticate to Earth Engine using a default service account, use the following code:
```
fromgoogle.authimport compute_engine
importee
credentials = compute_engine.Credentials(scopes=['https://www.googleapis.com/auth/earthengine'])
ee.Initialize(credentials)
```

## Set up REST API access
If the service account is to make computations using the REST API, you need to give it [project-level permission](https://developers.google.com/earth-engine/guides/access_control#set_project_level_permissions), specifically the [Earth Engine Resource Viewer role](https://developers.google.com/earth-engine/guides/access_control#predefined_earth_engine_iam_roles). Depending on your project configuration, you may also need to give the service account the [Service Usage Consumer role](https://developers.google.com/earth-engine/guides/access_control#set_earth_engine_service_usage). See [Access Control](https://developers.google.com/earth-engine/guides/access_control) page for more information about project permissions required to use Earth Engine.
