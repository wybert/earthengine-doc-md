 
#  Earth Engine audit logging
Stay organized with collections  Save and categorize content based on your preferences. 
This document describes audit logging for Cloud Earth Engine. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 
  * [Types of audit logs](https://cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://cloud.google.com/logging/docs/audit/configure-data-access)


## Service name
Cloud Earth Engine audit logs use the service name `earthengine.googleapis.com`. Filter for this service: 
```
protoPayload.serviceName="earthengine.googleapis.com"

```

## Methods by permission type
`CopyAsset` produces a `DATA_READ` audit log in the source project, and a `DATA_WRITE` audit log in the destination project. `MoveAsset` produces `DATA_READ` and `DATA_WRITE` audit logs in the source project, and a `DATA_WRITE` audit log in the destination project.
Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Cloud Earth Engine generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://cloud.google.com/logging/docs/audit#admin-activity) audit logs.
Permission type | Methods  
---|---  
`ADMIN_READ` |  `google.earthengine.v1.EarthEngine.GetIamPolicy`  
`google.earthengine.v1alpha.EarthEngine.GetIamPolicy`  
`google.earthengine.v1beta.EarthEngine.GetIamPolicy`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`google.longrunning.Operations.WaitOperation`  
`ADMIN_WRITE` |  `google.earthengine.v1.EarthEngine.SetIamPolicy`  
`google.earthengine.v1alpha.EarthEngine.SetIamPolicy`  
`google.earthengine.v1beta.EarthEngine.SetIamPolicy`  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
`DATA_READ` |  `google.earthengine.v1.EarthEngine.ComputeFeatures`  
`google.earthengine.v1.EarthEngine.ComputeImages`  
`google.earthengine.v1.EarthEngine.ComputePixels`  
`google.earthengine.v1.EarthEngine.ComputeValue`  
`google.earthengine.v1.EarthEngine.CopyAsset`  
`google.earthengine.v1.EarthEngine.CreateFeatureView`  
`google.earthengine.v1.EarthEngine.CreateFilmstripThumbnail`  
`google.earthengine.v1.EarthEngine.CreateMap`  
`google.earthengine.v1.EarthEngine.CreateTable`  
`google.earthengine.v1.EarthEngine.CreateThumbnail`  
`google.earthengine.v1.EarthEngine.CreateVideoThumbnail`  
`google.earthengine.v1.EarthEngine.ExportClassifier`  
`google.earthengine.v1.EarthEngine.ExportImage`  
`google.earthengine.v1.EarthEngine.ExportMap`  
`google.earthengine.v1.EarthEngine.ExportTable`  
`google.earthengine.v1.EarthEngine.ExportVideo`  
`google.earthengine.v1.EarthEngine.ExportVideoMap`  
`google.earthengine.v1.EarthEngine.GetAsset`  
`google.earthengine.v1.EarthEngine.GetPixels`  
`google.earthengine.v1.EarthEngine.GetProjectConfig`  
`google.earthengine.v1.EarthEngine.ImportImage`  
`google.earthengine.v1.EarthEngine.ImportTable`  
`google.earthengine.v1.EarthEngine.ListAlgorithms`  
`google.earthengine.v1.EarthEngine.ListAssets`  
`google.earthengine.v1.EarthEngine.ListFeatures`  
`google.earthengine.v1alpha.EarthEngine.ComputeFeatures`  
`google.earthengine.v1alpha.EarthEngine.ComputeImages`  
`google.earthengine.v1alpha.EarthEngine.ComputePixels`  
`google.earthengine.v1alpha.EarthEngine.ComputeValue`  
`google.earthengine.v1alpha.EarthEngine.CopyAsset`  
`google.earthengine.v1alpha.EarthEngine.CreateFeatureView`  
`google.earthengine.v1alpha.EarthEngine.CreateFilmstripThumbnail`  
`google.earthengine.v1alpha.EarthEngine.CreateMap`  
`google.earthengine.v1alpha.EarthEngine.CreateTable`  
`google.earthengine.v1alpha.EarthEngine.CreateThumbnail`  
`google.earthengine.v1alpha.EarthEngine.CreateVideoThumbnail`  
`google.earthengine.v1alpha.EarthEngine.ExportClassifier`  
`google.earthengine.v1alpha.EarthEngine.ExportImage`  
`google.earthengine.v1alpha.EarthEngine.ExportMap`  
`google.earthengine.v1alpha.EarthEngine.ExportTable`  
`google.earthengine.v1alpha.EarthEngine.ExportVideo`  
`google.earthengine.v1alpha.EarthEngine.ExportVideoMap`  
`google.earthengine.v1alpha.EarthEngine.GetAsset`  
`google.earthengine.v1alpha.EarthEngine.GetPixels`  
`google.earthengine.v1alpha.EarthEngine.GetProjectConfig`  
`google.earthengine.v1alpha.EarthEngine.ImportExternalImage`  
`google.earthengine.v1alpha.EarthEngine.ImportImage`  
`google.earthengine.v1alpha.EarthEngine.ImportTable`  
`google.earthengine.v1alpha.EarthEngine.ListAlgorithms`  
`google.earthengine.v1alpha.EarthEngine.ListAssets`  
`google.earthengine.v1alpha.EarthEngine.ListFeatures`  
`google.earthengine.v1alpha.EarthEngine.ListImages`  
`google.earthengine.v1beta.EarthEngine.ComputeFeatures`  
`google.earthengine.v1beta.EarthEngine.ComputeImages`  
`google.earthengine.v1beta.EarthEngine.ComputePixels`  
`google.earthengine.v1beta.EarthEngine.ComputeValue`  
`google.earthengine.v1beta.EarthEngine.CopyAsset`  
`google.earthengine.v1beta.EarthEngine.CreateFeatureView`  
`google.earthengine.v1beta.EarthEngine.CreateFilmstripThumbnail`  
`google.earthengine.v1beta.EarthEngine.CreateMap`  
`google.earthengine.v1beta.EarthEngine.CreateTable`  
`google.earthengine.v1beta.EarthEngine.CreateThumbnail`  
`google.earthengine.v1beta.EarthEngine.CreateVideoThumbnail`  
`google.earthengine.v1beta.EarthEngine.ExportClassifier`  
`google.earthengine.v1beta.EarthEngine.ExportImage`  
`google.earthengine.v1beta.EarthEngine.ExportMap`  
`google.earthengine.v1beta.EarthEngine.ExportTable`  
`google.earthengine.v1beta.EarthEngine.ExportVideo`  
`google.earthengine.v1beta.EarthEngine.ExportVideoMap`  
`google.earthengine.v1beta.EarthEngine.GetAsset`  
`google.earthengine.v1beta.EarthEngine.GetPixels`  
`google.earthengine.v1beta.EarthEngine.GetProjectConfig`  
`google.earthengine.v1beta.EarthEngine.ImportImage`  
`google.earthengine.v1beta.EarthEngine.ImportTable`  
`google.earthengine.v1beta.EarthEngine.ListAlgorithms`  
`google.earthengine.v1beta.EarthEngine.ListAssets`  
`google.earthengine.v1beta.EarthEngine.ListFeatures`  
`DATA_WRITE` |  `google.earthengine.v1.EarthEngine.CopyAsset`  
`google.earthengine.v1.EarthEngine.CreateAsset`  
`google.earthengine.v1.EarthEngine.DeleteAsset`  
`google.earthengine.v1.EarthEngine.ExportClassifier`  
`google.earthengine.v1.EarthEngine.ImportImage`  
`google.earthengine.v1.EarthEngine.ImportTable`  
`google.earthengine.v1.EarthEngine.MoveAsset`  
`google.earthengine.v1.EarthEngine.UpdateAsset`  
`google.earthengine.v1.EarthEngine.UpdateProjectConfig`  
`google.earthengine.v1alpha.EarthEngine.CopyAsset`  
`google.earthengine.v1alpha.EarthEngine.CreateAsset`  
`google.earthengine.v1alpha.EarthEngine.DeleteAsset`  
`google.earthengine.v1alpha.EarthEngine.ExportClassifier`  
`google.earthengine.v1alpha.EarthEngine.ExportTable`  
`google.earthengine.v1alpha.EarthEngine.ImportExternalImage`  
`google.earthengine.v1alpha.EarthEngine.ImportImage`  
`google.earthengine.v1alpha.EarthEngine.ImportTable`  
`google.earthengine.v1alpha.EarthEngine.MoveAsset`  
`google.earthengine.v1alpha.EarthEngine.UpdateAsset`  
`google.earthengine.v1alpha.EarthEngine.UpdateProjectConfig`  
`google.earthengine.v1beta.EarthEngine.CopyAsset`  
`google.earthengine.v1beta.EarthEngine.CreateAsset`  
`google.earthengine.v1beta.EarthEngine.DeleteAsset`  
`google.earthengine.v1beta.EarthEngine.ExportClassifier`  
`google.earthengine.v1beta.EarthEngine.ExportImage`  
`google.earthengine.v1beta.EarthEngine.ImportImage`  
`google.earthengine.v1beta.EarthEngine.ImportTable`  
`google.earthengine.v1beta.EarthEngine.MoveAsset`  
`google.earthengine.v1beta.EarthEngine.UpdateAsset`  
`google.earthengine.v1beta.EarthEngine.UpdateProjectConfig`  
## API interface audit logs
For information about how and which permissions are evaluated for each method, see the Cloud Identity and Access Management documentation for Cloud Earth Engine.
### `google.earthengine.v1.EarthEngine`
The following audit logs are associated with methods belonging to `google.earthengine.v1.EarthEngine`.
#### `ComputeFeatures`
  * **Method** : `google.earthengine.v1.EarthEngine.ComputeFeatures`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.computations.create - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1.EarthEngine.ComputeFeatures"   `  



#### `ComputeImages`
  * **Method** : `google.earthengine.v1.EarthEngine.ComputeImages`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.computations.create - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1.EarthEngine.ComputeImages"   `  



#### `ComputePixels`
  * **Method** : `google.earthengine.v1.EarthEngine.ComputePixels`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.computations.create - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1.EarthEngine.ComputePixels"   `  



#### `ComputeValue`
  * **Method** : `google.earthengine.v1.EarthEngine.ComputeValue`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.computations.create - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1.EarthEngine.ComputeValue"   `  



#### `CopyAsset`
  * **Method** : `google.earthengine.v1.EarthEngine.CopyAsset`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.create - DATA_WRITE`
    * `earthengine.assets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1.EarthEngine.CopyAsset"   `  


**Note:** Produces a `DATA_READ` audit log in the source project, and a `DATA_WRITE` audit log in the destination project.
#### `CreateAsset`
  * **Method** : `google.earthengine.v1.EarthEngine.CreateAsset`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1.EarthEngine.CreateAsset"   `  



#### `CreateFeatureView`
  * **Method** : `google.earthengine.v1.EarthEngine.CreateFeatureView`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.maps.create - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1.EarthEngine.CreateFeatureView"   `  



#### `CreateFilmstripThumbnail`
  * **Method** : `google.earthengine.v1.EarthEngine.CreateFilmstripThumbnail`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.filmstripthumbnails.create - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1.EarthEngine.CreateFilmstripThumbnail"   `  



#### `CreateMap`
  * **Method** : `google.earthengine.v1.EarthEngine.CreateMap`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.maps.create - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1.EarthEngine.CreateMap"   `  



#### `CreateTable`
  * **Method** : `google.earthengine.v1.EarthEngine.CreateTable`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.tables.create - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1.EarthEngine.CreateTable"   `  



#### `CreateThumbnail`
  * **Method** : `google.earthengine.v1.EarthEngine.CreateThumbnail`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.thumbnails.create - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1.EarthEngine.CreateThumbnail"   `  



#### `CreateVideoThumbnail`
  * **Method** : `google.earthengine.v1.EarthEngine.CreateVideoThumbnail`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.videothumbnails.create - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1.EarthEngine.CreateVideoThumbnail"   `  



#### `DeleteAsset`
  * **Method** : `google.earthengine.v1.EarthEngine.DeleteAsset`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1.EarthEngine.DeleteAsset"   `  



#### `ExportClassifier`
  * **Method** : `google.earthengine.v1.EarthEngine.ExportClassifier`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.create - DATA_WRITE`
    * `earthengine.exports.create - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1.EarthEngine.ExportClassifier"   `  



#### `ExportImage`
  * **Method** : `google.earthengine.v1.EarthEngine.ExportImage`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.create - DATA_WRITE`
    * `earthengine.exports.create - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1.EarthEngine.ExportImage"   `  



#### `ExportMap`
  * **Method** : `google.earthengine.v1.EarthEngine.ExportMap`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.exports.create - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1.EarthEngine.ExportMap"   `  



#### `ExportTable`
  * **Method** : `google.earthengine.v1.EarthEngine.ExportTable`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.exports.create - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1.EarthEngine.ExportTable"   `  



#### `ExportVideo`
  * **Method** : `google.earthengine.v1.EarthEngine.ExportVideo`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.exports.create - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1.EarthEngine.ExportVideo"   `  



#### `ExportVideoMap`
  * **Method** : `google.earthengine.v1.EarthEngine.ExportVideoMap`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.exports.create - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1.EarthEngine.ExportVideoMap"   `  



#### `GetAsset`
  * **Method** : `google.earthengine.v1.EarthEngine.GetAsset`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1.EarthEngine.GetAsset"   `  



#### `GetIamPolicy`
  * **Method** : `google.earthengine.v1.EarthEngine.GetIamPolicy`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1.EarthEngine.GetIamPolicy"   `  



#### `GetPixels`
  * **Method** : `google.earthengine.v1.EarthEngine.GetPixels`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1.EarthEngine.GetPixels"   `  



#### `GetProjectConfig`
  * **Method** : `google.earthengine.v1.EarthEngine.GetProjectConfig`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.config.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1.EarthEngine.GetProjectConfig"   `  



#### `ImportImage`
  * **Method** : `google.earthengine.v1.EarthEngine.ImportImage`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.create - DATA_WRITE`
    * `earthengine.imports.create - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1.EarthEngine.ImportImage"   `  



#### `ImportTable`
  * **Method** : `google.earthengine.v1.EarthEngine.ImportTable`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.create - DATA_WRITE`
    * `earthengine.imports.create - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1.EarthEngine.ImportTable"   `  



#### `ListAlgorithms`
  * **Method** : `google.earthengine.v1.EarthEngine.ListAlgorithms`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.computations.create - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1.EarthEngine.ListAlgorithms"   `  



#### `ListAssets`
  * **Method** : `google.earthengine.v1.EarthEngine.ListAssets`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1.EarthEngine.ListAssets"   `  



#### `ListFeatures`
  * **Method** : `google.earthengine.v1.EarthEngine.ListFeatures`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1.EarthEngine.ListFeatures"   `  



#### `MoveAsset`
  * **Method** : `google.earthengine.v1.EarthEngine.MoveAsset`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.create - DATA_WRITE`
    * `earthengine.assets.delete - DATA_WRITE`
    * `earthengine.assets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1.EarthEngine.MoveAsset"   `  


**Note:** Produces `DATA_READ` and `DATA_WRITE` audit logs in the source project, and a `DATA_WRITE` audit log in the destination project.
#### `SetIamPolicy`
  * **Method** : `google.earthengine.v1.EarthEngine.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `earthengine.assets.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1.EarthEngine.SetIamPolicy"   `  



#### `UpdateAsset`
  * **Method** : `google.earthengine.v1.EarthEngine.UpdateAsset`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1.EarthEngine.UpdateAsset"   `  



#### `UpdateProjectConfig`
  * **Method** : `google.earthengine.v1.EarthEngine.UpdateProjectConfig`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.config.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1.EarthEngine.UpdateProjectConfig"   `  



### `google.earthengine.v1alpha.EarthEngine`
The following audit logs are associated with methods belonging to `google.earthengine.v1alpha.EarthEngine`.
#### `ComputeFeatures`
  * **Method** : `google.earthengine.v1alpha.EarthEngine.ComputeFeatures`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.computations.create - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1alpha.EarthEngine.ComputeFeatures"   `  



#### `ComputeImages`
  * **Method** : `google.earthengine.v1alpha.EarthEngine.ComputeImages`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.computations.create - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1alpha.EarthEngine.ComputeImages"   `  



#### `ComputePixels`
  * **Method** : `google.earthengine.v1alpha.EarthEngine.ComputePixels`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.computations.create - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1alpha.EarthEngine.ComputePixels"   `  



#### `ComputeValue`
  * **Method** : `google.earthengine.v1alpha.EarthEngine.ComputeValue`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.computations.create - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1alpha.EarthEngine.ComputeValue"   `  



#### `CopyAsset`
  * **Method** : `google.earthengine.v1alpha.EarthEngine.CopyAsset`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.create - DATA_WRITE`
    * `earthengine.assets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1alpha.EarthEngine.CopyAsset"   `  


**Note:** Produces a `DATA_READ` audit log in the source project, and a `DATA_WRITE` audit log in the destination project.
#### `CreateAsset`
  * **Method** : `google.earthengine.v1alpha.EarthEngine.CreateAsset`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1alpha.EarthEngine.CreateAsset"   `  



#### `CreateFeatureView`
  * **Method** : `google.earthengine.v1alpha.EarthEngine.CreateFeatureView`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.maps.create - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1alpha.EarthEngine.CreateFeatureView"   `  



#### `CreateFilmstripThumbnail`
  * **Method** : `google.earthengine.v1alpha.EarthEngine.CreateFilmstripThumbnail`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.filmstripthumbnails.create - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1alpha.EarthEngine.CreateFilmstripThumbnail"   `  



#### `CreateMap`
  * **Method** : `google.earthengine.v1alpha.EarthEngine.CreateMap`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.maps.create - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1alpha.EarthEngine.CreateMap"   `  



#### `CreateTable`
  * **Method** : `google.earthengine.v1alpha.EarthEngine.CreateTable`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.tables.create - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1alpha.EarthEngine.CreateTable"   `  



#### `CreateThumbnail`
  * **Method** : `google.earthengine.v1alpha.EarthEngine.CreateThumbnail`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.thumbnails.create - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1alpha.EarthEngine.CreateThumbnail"   `  



#### `CreateVideoThumbnail`
  * **Method** : `google.earthengine.v1alpha.EarthEngine.CreateVideoThumbnail`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.videothumbnails.create - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1alpha.EarthEngine.CreateVideoThumbnail"   `  



#### `DeleteAsset`
  * **Method** : `google.earthengine.v1alpha.EarthEngine.DeleteAsset`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1alpha.EarthEngine.DeleteAsset"   `  



#### `ExportClassifier`
  * **Method** : `google.earthengine.v1alpha.EarthEngine.ExportClassifier`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.create - DATA_WRITE`
    * `earthengine.exports.create - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1alpha.EarthEngine.ExportClassifier"   `  



#### `ExportImage`
  * **Method** : `google.earthengine.v1alpha.EarthEngine.ExportImage`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.create - DATA_WRITE`
    * `earthengine.exports.create - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1alpha.EarthEngine.ExportImage"   `  



#### `ExportMap`
  * **Method** : `google.earthengine.v1alpha.EarthEngine.ExportMap`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.exports.create - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1alpha.EarthEngine.ExportMap"   `  



#### `ExportTable`
  * **Method** : `google.earthengine.v1alpha.EarthEngine.ExportTable`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.create - DATA_WRITE`
    * `earthengine.exports.create - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1alpha.EarthEngine.ExportTable"   `  



#### `ExportVideo`
  * **Method** : `google.earthengine.v1alpha.EarthEngine.ExportVideo`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.exports.create - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1alpha.EarthEngine.ExportVideo"   `  



#### `ExportVideoMap`
  * **Method** : `google.earthengine.v1alpha.EarthEngine.ExportVideoMap`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.exports.create - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1alpha.EarthEngine.ExportVideoMap"   `  



#### `GetAsset`
  * **Method** : `google.earthengine.v1alpha.EarthEngine.GetAsset`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1alpha.EarthEngine.GetAsset"   `  



#### `GetIamPolicy`
  * **Method** : `google.earthengine.v1alpha.EarthEngine.GetIamPolicy`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1alpha.EarthEngine.GetIamPolicy"   `  



#### `GetPixels`
  * **Method** : `google.earthengine.v1alpha.EarthEngine.GetPixels`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1alpha.EarthEngine.GetPixels"   `  



#### `GetProjectConfig`
  * **Method** : `google.earthengine.v1alpha.EarthEngine.GetProjectConfig`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.config.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1alpha.EarthEngine.GetProjectConfig"   `  



#### `ImportExternalImage`
  * **Method** : `google.earthengine.v1alpha.EarthEngine.ImportExternalImage`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.create - DATA_WRITE`
    * `earthengine.imports.create - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1alpha.EarthEngine.ImportExternalImage"   `  



#### `ImportImage`
  * **Method** : `google.earthengine.v1alpha.EarthEngine.ImportImage`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.create - DATA_WRITE`
    * `earthengine.imports.create - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1alpha.EarthEngine.ImportImage"   `  



#### `ImportTable`
  * **Method** : `google.earthengine.v1alpha.EarthEngine.ImportTable`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.create - DATA_WRITE`
    * `earthengine.imports.create - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1alpha.EarthEngine.ImportTable"   `  



#### `ListAlgorithms`
  * **Method** : `google.earthengine.v1alpha.EarthEngine.ListAlgorithms`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.computations.create - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1alpha.EarthEngine.ListAlgorithms"   `  



#### `ListAssets`
  * **Method** : `google.earthengine.v1alpha.EarthEngine.ListAssets`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.get - DATA_READ`
    * `earthengine.assets.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1alpha.EarthEngine.ListAssets"   `  



#### `ListFeatures`
  * **Method** : `google.earthengine.v1alpha.EarthEngine.ListFeatures`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1alpha.EarthEngine.ListFeatures"   `  



#### `ListImages`
  * **Method** : `google.earthengine.v1alpha.EarthEngine.ListImages`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1alpha.EarthEngine.ListImages"   `  



#### `MoveAsset`
  * **Method** : `google.earthengine.v1alpha.EarthEngine.MoveAsset`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.create - DATA_WRITE`
    * `earthengine.assets.delete - DATA_WRITE`
    * `earthengine.assets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1alpha.EarthEngine.MoveAsset"   `  


**Note:** Produces `DATA_READ` and `DATA_WRITE` audit logs in the source project, and a `DATA_WRITE` audit log in the destination project.
#### `SetIamPolicy`
  * **Method** : `google.earthengine.v1alpha.EarthEngine.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `earthengine.assets.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1alpha.EarthEngine.SetIamPolicy"   `  



#### `UpdateAsset`
  * **Method** : `google.earthengine.v1alpha.EarthEngine.UpdateAsset`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1alpha.EarthEngine.UpdateAsset"   `  



#### `UpdateProjectConfig`
  * **Method** : `google.earthengine.v1alpha.EarthEngine.UpdateProjectConfig`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.config.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1alpha.EarthEngine.UpdateProjectConfig"   `  



### `google.earthengine.v1beta.EarthEngine`
The following audit logs are associated with methods belonging to `google.earthengine.v1beta.EarthEngine`.
#### `ComputeFeatures`
  * **Method** : `google.earthengine.v1beta.EarthEngine.ComputeFeatures`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.computations.create - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1beta.EarthEngine.ComputeFeatures"   `  



#### `ComputeImages`
  * **Method** : `google.earthengine.v1beta.EarthEngine.ComputeImages`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.computations.create - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1beta.EarthEngine.ComputeImages"   `  



#### `ComputePixels`
  * **Method** : `google.earthengine.v1beta.EarthEngine.ComputePixels`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.computations.create - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1beta.EarthEngine.ComputePixels"   `  



#### `ComputeValue`
  * **Method** : `google.earthengine.v1beta.EarthEngine.ComputeValue`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.computations.create - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1beta.EarthEngine.ComputeValue"   `  



#### `CopyAsset`
  * **Method** : `google.earthengine.v1beta.EarthEngine.CopyAsset`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.create - DATA_WRITE`
    * `earthengine.assets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1beta.EarthEngine.CopyAsset"   `  


**Note:** Produces a `DATA_READ` audit log in the source project, and a `DATA_WRITE` audit log in the destination project.
#### `CreateAsset`
  * **Method** : `google.earthengine.v1beta.EarthEngine.CreateAsset`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1beta.EarthEngine.CreateAsset"   `  



#### `CreateFeatureView`
  * **Method** : `google.earthengine.v1beta.EarthEngine.CreateFeatureView`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.maps.create - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1beta.EarthEngine.CreateFeatureView"   `  



#### `CreateFilmstripThumbnail`
  * **Method** : `google.earthengine.v1beta.EarthEngine.CreateFilmstripThumbnail`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.filmstripthumbnails.create - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1beta.EarthEngine.CreateFilmstripThumbnail"   `  



#### `CreateMap`
  * **Method** : `google.earthengine.v1beta.EarthEngine.CreateMap`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.maps.create - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1beta.EarthEngine.CreateMap"   `  



#### `CreateTable`
  * **Method** : `google.earthengine.v1beta.EarthEngine.CreateTable`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.tables.create - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1beta.EarthEngine.CreateTable"   `  



#### `CreateThumbnail`
  * **Method** : `google.earthengine.v1beta.EarthEngine.CreateThumbnail`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.thumbnails.create - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1beta.EarthEngine.CreateThumbnail"   `  



#### `CreateVideoThumbnail`
  * **Method** : `google.earthengine.v1beta.EarthEngine.CreateVideoThumbnail`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.videothumbnails.create - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1beta.EarthEngine.CreateVideoThumbnail"   `  



#### `DeleteAsset`
  * **Method** : `google.earthengine.v1beta.EarthEngine.DeleteAsset`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1beta.EarthEngine.DeleteAsset"   `  



#### `ExportClassifier`
  * **Method** : `google.earthengine.v1beta.EarthEngine.ExportClassifier`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.create - DATA_WRITE`
    * `earthengine.exports.create - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1beta.EarthEngine.ExportClassifier"   `  



#### `ExportImage`
  * **Method** : `google.earthengine.v1beta.EarthEngine.ExportImage`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.create - DATA_WRITE`
    * `earthengine.exports.create - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1beta.EarthEngine.ExportImage"   `  



#### `ExportMap`
  * **Method** : `google.earthengine.v1beta.EarthEngine.ExportMap`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.exports.create - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1beta.EarthEngine.ExportMap"   `  



#### `ExportTable`
  * **Method** : `google.earthengine.v1beta.EarthEngine.ExportTable`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.create - DATA_WRITE`
    * `earthengine.exports.create - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1beta.EarthEngine.ExportTable"   `  



#### `ExportVideo`
  * **Method** : `google.earthengine.v1beta.EarthEngine.ExportVideo`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.exports.create - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1beta.EarthEngine.ExportVideo"   `  



#### `ExportVideoMap`
  * **Method** : `google.earthengine.v1beta.EarthEngine.ExportVideoMap`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.exports.create - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1beta.EarthEngine.ExportVideoMap"   `  



#### `GetAsset`
  * **Method** : `google.earthengine.v1beta.EarthEngine.GetAsset`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1beta.EarthEngine.GetAsset"   `  



#### `GetIamPolicy`
  * **Method** : `google.earthengine.v1beta.EarthEngine.GetIamPolicy`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1beta.EarthEngine.GetIamPolicy"   `  



#### `GetPixels`
  * **Method** : `google.earthengine.v1beta.EarthEngine.GetPixels`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1beta.EarthEngine.GetPixels"   `  



#### `GetProjectConfig`
  * **Method** : `google.earthengine.v1beta.EarthEngine.GetProjectConfig`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.config.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1beta.EarthEngine.GetProjectConfig"   `  



#### `ImportImage`
  * **Method** : `google.earthengine.v1beta.EarthEngine.ImportImage`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.create - DATA_WRITE`
    * `earthengine.imports.create - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1beta.EarthEngine.ImportImage"   `  



#### `ImportTable`
  * **Method** : `google.earthengine.v1beta.EarthEngine.ImportTable`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.create - DATA_WRITE`
    * `earthengine.imports.create - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1beta.EarthEngine.ImportTable"   `  



#### `ListAlgorithms`
  * **Method** : `google.earthengine.v1beta.EarthEngine.ListAlgorithms`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.computations.create - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1beta.EarthEngine.ListAlgorithms"   `  



#### `ListAssets`
  * **Method** : `google.earthengine.v1beta.EarthEngine.ListAssets`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1beta.EarthEngine.ListAssets"   `  



#### `ListFeatures`
  * **Method** : `google.earthengine.v1beta.EarthEngine.ListFeatures`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1beta.EarthEngine.ListFeatures"   `  



#### `MoveAsset`
  * **Method** : `google.earthengine.v1beta.EarthEngine.MoveAsset`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.create - DATA_WRITE`
    * `earthengine.assets.delete - DATA_WRITE`
    * `earthengine.assets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1beta.EarthEngine.MoveAsset"   `  


**Note:** Produces `DATA_READ` and `DATA_WRITE` audit logs in the source project, and a `DATA_WRITE` audit log in the destination project.
#### `SetIamPolicy`
  * **Method** : `google.earthengine.v1beta.EarthEngine.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `earthengine.assets.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1beta.EarthEngine.SetIamPolicy"   `  



#### `UpdateAsset`
  * **Method** : `google.earthengine.v1beta.EarthEngine.UpdateAsset`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.assets.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1beta.EarthEngine.UpdateAsset"   `  



#### `UpdateProjectConfig`
  * **Method** : `google.earthengine.v1beta.EarthEngine.UpdateProjectConfig`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.config.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.earthengine.v1beta.EarthEngine.UpdateProjectConfig"   `  



### `google.longrunning.Operations`
The following audit logs are associated with methods belonging to `google.longrunning.Operations`.
#### `CancelOperation`
  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `earthengine.operations.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.longrunning.Operations.CancelOperation"   `  



#### `DeleteOperation`
  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `earthengine.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.longrunning.Operations.DeleteOperation"   `  



#### `GetOperation`
  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.longrunning.Operations.GetOperation"   `  



#### `ListOperations`
  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.longrunning.Operations.ListOperations"   `  



#### `WaitOperation`
  * **Method** : `google.longrunning.Operations.WaitOperation`  

  * **Audit log type** : [Data access](https://cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `earthengine.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.longrunning.Operations.WaitOperation"   `  



