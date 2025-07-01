 
#  ProjectConfig
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [RegistrationState](https://developers.google.com/earth-engine/reference/rest/v1beta/ProjectConfig#registrationstate)


Information about a Cloud-based Earth Engine project. <https://developers.google.com/earth-engine/cloud/projects>.
JSON representation  
---  
```
{
 "name": string,
 "registrationState": enum (RegistrationState[](https://developers.google.com/earth-engine/reference/rest/v1beta/ProjectConfig#RegistrationState))
}
```
  
Fields  
---  
`name` |  `string` Required. The project config name, of the format "projects/*/config".  
`registrationState` |  `enum (`RegistrationState[](https://developers.google.com/earth-engine/reference/rest/v1beta/ProjectConfig#RegistrationState)`)` Output only. The project registration state.  
## RegistrationState
Registration state.
Enums  
---  
`REGISTRATION_STATE_UNSPECIFIED` | Unspecified.  
`NOT_REGISTERED` | Project is not registered.  
`REGISTERED_COMMERCIALLY` | Project is registered for commercial use.  
`REGISTERED_NOT_COMMERCIALLY` | Project is registered for non-commercial use.  
Was this helpful?
