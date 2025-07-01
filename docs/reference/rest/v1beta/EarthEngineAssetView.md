 
#  EarthEngineAssetView
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
A resource view for `EarthEngineAsset`.
The view determines the maximum page size for API operations, with generally higher limits for more restrictive views: - 10000 for BASIC - 1000 otherwise
Enums  
---  
`EARTH_ENGINE_ASSET_VIEW_UNSPECIFIED` | Not specified, equivalent to `FULL`.  
`FULL` | All fields are set in each `EarthEngineAsset` returned in the response. The default value.  
`BASIC` | Only the fields `type`, `name`, and `id` are set in each `EarthEngineAsset` returned in the response.  
Was this helpful?
