 
#  ListAssetsResponse 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Response message for EarthEngineService.ListAssets.
JSON representation  
---  
```
{
 "assets": [
  {
   object (EarthEngineAsset[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset))
  }
 ],
 "nextPageToken": string
}
```
  
Fields  
---  
`assets[]` |  `object (`EarthEngineAsset[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset)`)` The list of assets.  
`nextPageToken` |  `string` A token to retrieve the next page of results. Pass this value in the `ListAssetsRequest.page_token[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets/listAssets#body.QUERY_PARAMETERS.page_token)` field in the subsequent call to the `ListAssets` method to retrieve the next page of results.  
