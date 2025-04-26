 
#  Authentication and Initialization 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Earth Engine Code Editor and JavaScript](https://developers.google.com/earth-engine/guides/auth#earth_engine_code_editor_and_javascript)
  * [Python and Command Line](https://developers.google.com/earth-engine/guides/auth#python_and_command_line)
    * [Authentication details](https://developers.google.com/earth-engine/guides/auth#authentication_details)
    * [Quick reference guide and table](https://developers.google.com/earth-engine/guides/auth#quick_reference_guide_and_table)
    * [Credentials for Service Accounts and Compute Engine](https://developers.google.com/earth-engine/guides/auth#credentials_for_service_accounts_and_compute_engine)
    * [Details on modes](https://developers.google.com/earth-engine/guides/auth#details_on_modes)
  * [Troubleshooting](https://developers.google.com/earth-engine/guides/auth#troubleshooting)
    * [What if I cannot create a Cloud Project?](https://developers.google.com/earth-engine/guides/auth#what_if_i_cannot_create_a_cloud_project)
    * [Error: "Earth Engine API has not been used in project XXX before or it is disabled"](https://developers.google.com/earth-engine/guides/auth#error_earth_engine_api_has_not_been_used_in_project_xxx_before_or_it_is_disabled)
    * [Error: "Project has an incompatible OAuth2 Client configuration"](https://developers.google.com/earth-engine/guides/auth#error_project_has_an_incompatible_oauth2_client_configuration)
    * [Error: "gcloud failed. Please check for any errors above and install gcloud if needed."](https://developers.google.com/earth-engine/guides/auth#error_gcloud_failed_please_check_for_any_errors_above_and_install_gcloud_if_needed)
    * [What if I do not have access to a local machine to install gcloud?](https://developers.google.com/earth-engine/guides/auth#what_if_i_do_not_have_access_to_a_local_machine_to_install_gcloud)
    * [Error 400: redirect_uri_mismatch](https://developers.google.com/earth-engine/guides/auth#error_400_redirect_uri_mismatch)
    * [Error: "Your application is authenticating by using local Application Default Credentials. The earthengine.googleapis.com API requires a quota project, which is not set by default."](https://developers.google.com/earth-engine/guides/auth#error_your_application_is_authenticating_by_using_local_application_default_credentials_the_earthenginegoogleapiscom_api_requires_a_quota_project_which_is_not_set_by_default)
  * [Technical notes](https://developers.google.com/earth-engine/guides/auth#technical_notes)


Before you can make requests to Earth Engine through a [client library](https://developers.google.com/earth-engine/client_server), you must authenticate and use the resultant credentials to initialize the Earth Engine client.
## Earth Engine Code Editor and JavaScript
Authentication and initialization are handled automatically in the Code Editor. You may choose to route requests through a Cloud Project from your login at the upper right of [the Code Editor](https://code.earthengine.google.com/).
If you are using the JavaScript API (outside of the Code Editor), use one of the authentication helpers in `ee.data` (for example, [`ee.data.authenticateViaPopup()`](https://developers.google.com/earth-engine/apidocs/ee-data-authenticateviapopup)) followed by [`ee.initialize()`](https://developers.google.com/earth-engine/apidocs/ee-initialize) as shown in [this example](https://developers.google.com/earth-engine/custom-apps/client-js).
## Python and Command Line
Prior to using the Earth Engine Python client library, you need to authenticate (verify your identity) and use the resultant credentials to initialize the Python client. The authentication flows use [Cloud Projects](https://developers.google.com/earth-engine/cloud/earthengine_cloud_project_setup) to authenticate, and they're used for unpaid (free, noncommercial) use as well as paid use. To authenticate and initialize, run
```
  ee.Authenticate()
  ee.Initialize(project='my-project')

```

This will first select the best authentication mode for your environment, and prompt you to confirm access for your scripts. If credentials already exist, they are automatically reused - run `ee.Authenticate(force=True)` to create new credentials.
The initialization step verifies that valid credentials exist, either created from `ee.Authenticate()` or pre-existing as Google default credentials. It then initializes the Python client library with methods that the backend server supports. **You will need to provide a project** that you own, or have [permissions](https://developers.google.com/earth-engine/cloud/roles_permissions) to use. See [Cloud project setup](https://developers.google.com/earth-engine/cloud/earthengine_cloud_project_setup#get-access-to-earth-engine) to register the project and enable the Earth Engine API. This project will be used for running all Earth Engine operations.
On the command line, the equivalent call is `earthengine authenticate`. If credentials are expired or invalid, you may need to run `earthengine authenticate --force`. Command line invocations will initialize on each call, and you may use the `--project` argument to set the project.
You can also configure a project for all future calls by running `earthengine set_project {my-project}`. The command line and `ee.Initialize()` will use this whenever a project is not specified directly. If using authentication through `gcloud` (see below), then the project set by `gcloud auth application-default set-quota-project {my-project}` will be used as a final case.
### Authentication details
The aim of the Earth Engine authentication flows is to get a security "token" from your signed-in account which can be stored to give your scripts permission to access your data. For reasons of security, Google's authentication system will only pass such tokens to systems that can be made secure - see technical notes below.
Because of the sensitivity to the kind of systems involved, there are different ways to proceed depending on your particular situation. Most options are controlled by the `auth_mode` parameter: either as `ee.Authenticate(auth_mode=...)`, or `earthengine authenticate --auth_mode=...` on the command line.
Note that if Google credentials already exist in your environment you may not need to call `ee.Authenticate()` at all. Google Cloud VMs, App Engine, and other environments provide usable "ambient credentials," and `gcloud auth application-default login` will also create them.
However, `ee.Authenticate()` is recommended at the start of all scripts to maximize compatibility. With no `auth_mode` parameter, it is designed to work in most situations, but follow the details below if the default mode does not work. The default mode is selected as follows:
  * `colab` if running in a Google Colab notebook
  * `notebook` if running in other non-Colab Jupyter notebooks
  * `localhost` if a web browser is detected and no gcloud binary is installed
  * `gcloud`, otherwise. For this mode you will need to [install gcloud](https://cloud.google.com/sdk/docs/install).


### Quick reference guide and table
This decision guide outlines the possible options if the default mode selected by `ee.Authenticate()` does not work. For example, if you are running in other notebook environments you may have to specify `notebook` explicitly.
  * **Local environment**. 
    * **"Local"** means that you are running code in a Python shell or Python notebook on the machine in front of you - or more precisely, on the same machine that your web browser is running on. This includes remote-desktop situations where both Python and browser are on the same (remote) machine.
    * Using `auth_mode=localhost` is easiest, and will be selected by default if gcloud is not installed, but your script will only work in local environments.
    * Both `auth_mode=gcloud` and `auth_mode=notebook` are also available.
  * **Remote environment**. 
    * **"Remote"** means your browser is on one (local) machine but your code is running elsewhere, such as on a remote workstation or a web-based notebook.
    * If in Colab, use `auth_mode=colab`; or use `gcloud` if you need to set `scopes` to call other APIs.
    * If you can install gcloud on both the remote machine and your local machine, use `auth_mode=gcloud`.
    * If you can use an authentication project (see below), use `auth_mode=notebook`.
    * Otherwise, if you cannot use a project or install gcloud or use Colab or use a browser on the same machine:
    * Speak to an administrator (again) about creating projects. For example: 
      * Ask the administrator to configure a project for you (as Owner or Editor or OAuth Config Editor)
      * Or ask the administrator to grant you permissions to create a project.


This table shows which combinations of features are supported by each mode.
| For Local or Remote? | Project Needed | Scopes Settable | Local CLI Needed | Project Owner  
---|---|---|---|---|---  
`localhost` | local | Y | Y | N | N  
`colab` | remote | Y | N | N | N  
`gcloud` | both | Y | Y | N | N  
`notebook` | both | Y | Y | N | Y  
### Credentials for Service Accounts and Compute Engine
`ee.Initialize()` will use Earth Engine credentials (which `ee.Authenticate()` stores in `~/.config/earthengine/credentials`) or retrieve credentials from `google.auth.default()`, but if necessary you can pass a `credentials=` argument to use credentials from elsewhere, bypassing these defaults.
If you are authenticating Python code that will run unattended, you may want to authenticate with a **service account** rather than a user account. See [these docs](https://developers.google.com/earth-engine/guides/service_account#use-a-service-account-with-a-private-key) for using service accounts with Earth Engine. Other methods include `authenticate_service_account` in the Colab auth module and the methods described in the [Cloud guide to authenticating as a service account](https://cloud.google.com/docs/authentication/production).
If your code is running on a **Compute Engine VM** , a [default service account](https://cloud.google.com/iam/docs/service-accounts#default) is created for the environment, which `ee.Initialize()` will use by default. You may need to [register the service account to use Earth Engine](https://developers.google.com/earth-engine/guides/service_account#register-the-service-account-to-use-earth-engine) if the Cloud Project through which the VM was started is not registered for use with Earth Engine (commercial or non-commercial).
### Details on modes
**auth_mode=colab**. `ee.Authenticate()` will create or obtain the default credentials supported by Colab, by running `colab.auth.authenticate_user()` if necessary. The credentials always use the `cloud-platform` scope and can also be used to call other Cloud APIs.
**auth_mode=gcloud**. This delegates authentication to the [gcloud](https://cloud.google.com/sdk/docs/install) tool and is the same as running `gcloud auth application-default login` with the default Earth Engine scopes (earthengine, cloud-platform, and drive) or the scopes in the `scopes` argument. `gcloud` mode works in both local and remote cases.
Step-by-step instructions for gcloud mode (local and remote cases)
**The following steps describe how to authenticate from a command line on a local machine.**
  1. Verify that **gcloud** is installed on the local machine. 
     * In a terminal, run `gcloud help`. If **gcloud** is not installed, follow [these instructions](https://cloud.google.com/sdk/docs/install) to install **gcloud**.
  2. Local Machine Terminal 
     * In a terminal, run `earthengine authenticate`.
     * The command output will indicate that **gcloud** is being used to fetch credentials.
     * A browser window will open to an account selection page. If the browser does not open automatically, click the URL.
  3. Browser: Account Selection 
     * Select the account you want to use for authentication.
  4. Browser: Consent Screen 
     * Indicate if you are willing to grant the requested scopes and click "Allow".
  5. Browser: Confirmation Screen 
     * The browser will show a page confirming that you are authenticated, and the `earthengine authenticate` command in your terminal window will report "Successfully saved authorization token."
     * In remote cases, the web page will give you a code to paste back into the Python environment.
  6. Proceed with initialization.


**auth_mode=localhost**. This is a gcloud-like flow for cases where gcloud is not installed. It performs the same steps as gcloud, but only works for the local case. You can provide an optional internet port number, eg `localhost:8086`, or use `localhost:0` to autoselect a port. The default port is 8085.
**auth_mode=notebook**. This is a general-purpose mode designed to work in remote situations where local command lines are not available. It sends you to the Notebook Authenticator page where you'll need to choose or create an "authentication project" - see details and the troubleshooting guide below. The project passed to `ee.Initialize()` does not have to match this - you can keep the same project for authentication while working in different projects in different notebooks. It's recommended to pass a project explicitly to `ee.Initialize()`, but the authentication project will be used by default.
Step-by-step instructions for notebook mode
**The following steps describe how to authenticate from within a notebook.**
  1. Browser: Notebook 
    1. In a notebook code cell, run the following code to start an authentication flow using the "notebook" mode. ```
importee
ee.Authenticate()
```
Click the link in the cell output to open a Notebook Authenticator page in a new tab. 
  2. Browser: Notebook Authenticator 
    1. Verify that the correct user account is listed.
    2. Select a Google Cloud Project to use for Authentication. If you need to create a new project, we recommend the naming convention "ee-xyz" where xyz is your usual Earth Engine username. (If you cannot select or create a Cloud Project, see the [troubleshooting section](https://developers.google.com/earth-engine/guides/auth#troubleshooting) below.) 
You must be assigned sufficient IAM permissions for authentication, such as either Owner or Editor on the project, or an additional "OAuth Config Editor" predefined role on top of the [other IAM roles assigned](https://developers.google.com/earth-engine/cloud/roles_permissions). If someone else on your team has already created an authentication config on this project, you will get an extra warning. You should only continue if the creator is a trusted collaborator. 
    3. Click Generate Token.
  3. Browser: Account Selection 
     * You will be shown an account selection page. Click the user account that you want to grant access from the notebook.
  4. Browser: Warning page 
     * A warning page is presented, indicating that Google did not create the app (i.e. the code in the notebook). Click Continue to acknowledge.
  5. Browser: Consent Screen 
     * Indicate if you are willing to grant the requested scopes and click **Continue**.
  6. Browser: Authorization Code Screen 
     * Copy the authorization verification code
  7. Browser: Notebook 
     * Switch back to the notebook tab, and paste the verification code into the notebook cell output.
     * The cell output should indicate _"Successfully saved authorization token."_
  8. Proceed with initialization.


Notebook mode has a rarely-used `quiet` parameter: if set, it runs "noninteractively" and doesn't prompt and wait for you to enter the auth code. Instead, it gives a command to run to save the code.
#### Authentication projects
You will need to be an Owner, Editor or OAuth Config Editor on the authentication project used in notebook mode. In many cases, particularly in smaller teams, the authentication project that you use on the Notebook Authenticator page can be the same as the primary project that you use for other work.
Due to [security concerns](https://developers.google.com/workspace/guides/configure-oauth-consent), the "OAuth client configuration" on the authentication project is a once-off setup. If you or other users have set up an OAuth client on the project for other reasons, it cannot be removed and you will see an error saying "incompatible OAuth2 client configuration." You will need to use a different project for authentication, or use the colab, localhost or gcloud modes above.
## Troubleshooting
### What if I cannot create a Cloud Project?
Some organisations control who can create Cloud Projects. If you receive an error on the Notebook Authenticator page when trying to create a project, there are a few things to try:
  1. Try to [create a project](https://console.cloud.google.com/projectcreate) directly to confirm whether or not you have the necessary permissions.
  2. Speak to the administrator of your organisation to find out what processes are available to have a project created.
  3. Create a project from a non-organizational account, and add the account you use for work as an Owner of the project. Note: some organizations have security policies which prevent access to OAuth clients from external projects.


### Error: "Earth Engine API has not been used in project XXX before or it is disabled"
Firstly, ensure that you have configured a project in `ee.Initialize()` or on the command line (the default projects provided by Cloud and Colab will not have Earth Engine enabled). Secondly, ensure that the Earth Engine API is [ enabled](https://developers.google.com/earth-engine/cloud/earthengine_cloud_project_setup#enable-the-earth-engine-api) on your project.
### Error: "Project has an incompatible OAuth2 Client configuration"
Cloud projects can only have one OAuth2 Client configuration. You can check if a Cloud project has an OAuth2 Client configuration set by checking the OAuth 2.0 Client IDs on the Credentials page. You need to either select another Cloud project that has a compatible configuration already set up by the Notebook Authenticator, or select or create a Cloud project with no OAuth2 clients. The authenticator will configure this project automatically. Unfortunately, the OAuth system doesn't allow users to delete configurations, so one must use a different project. This project does not have to be the same project that's used for other Earth Engine work. Note that this error does not occur in Colab mode.
### Error: "gcloud failed. Please check for any errors above and install gcloud if needed."
This error may occur if gcloud is not installed or not on your PATH. It may also occur if you call `ee.Authenticate(auth_mode='gcloud')` from within a notebook code cell. Use `ee.Authenticate()` instead, which will default to using notebook mode authentication. If you cannot create a project, see the solution above.
### What if I do not have access to a local machine to install gcloud?
If you are working in a web-only environment without access to a local terminal, and you still need to use a remote terminal, you can still initialize the command line tool by triggering the notebook mode by running the `earthengine authenticate --auth_mode=notebook` command.
### Error 400: redirect_uri_mismatch
You may obtain this error if authenticating on a remote machine without access to a web browser. Try adding `--quiet` if running `earthengine authenticate` from the command line or `ee.Authenticate(quiet=True)` if using the Python client. This will require you to authenticate with `gcloud` from a machine that has access to a web browser.
### Error: "Your application is authenticating by using local Application Default Credentials. The earthengine.googleapis.com API requires a quota project, which is not set by default."
This error may occur when Earth Engine cannot determine your project ID. If the Google Cloud [troubleshooting options](https://cloud.google.com/docs/authentication/adc-troubleshooting/user-creds) don't work, try running `earthengine set_project YOUR_PROJECT_ID` or `gcloud auth application-default set-quota-project YOUR_PROJECT_ID`.
## Technical notes
For the technically curious: the need for these different credential creation mechanisms comes from the need to pass credentials to a known and trusted environment. Here's a quick discussion of the different cases above.
  * There used to be a `paste` mode which gave you a token to paste anywhere, and this was deemed too risky and is no longer available.
  * `colab`: `auth.authenticate_user()` will prompt you to share credentials with the "Colab" auth client, the notebook environment itself. These are then available through `google.auth.default()` and used by `ee.Initialize()`.
  * `localhost`: credentials are passed from the browser to a port on your local machine. In this situation, end-to-end security depends on the fact that your local machine has not been compromised. The auth client you'll see is the "Earth Engine Authenticator".
  * `gcloud`: This uses the `--launch-browser` flow described in the [gcloud reference](https://cloud.google.com/sdk/gcloud/reference/auth/login), and `--no-launch-browser` if on a remote machine. The auth client used is "Google Auth Library."
  * `notebook`: We create a new auth client specifically for your work - you'll see your email address on the consent page. This client is set in "development" mode, which is a special case which allows the older paste mode tokens. We need to use your own project for this, because such clients cannot be shared with large numbers of users.


Was this helpful?
