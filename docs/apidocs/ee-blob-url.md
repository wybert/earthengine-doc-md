 
#  ee.Blob.url 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Returns the Blob's Google Cloud Storage URL. The bucket metadata must be accessible (requires the `storage.buckets.get` permission which is provided by the role "Storage Legacy Bucket Reader" among others, see https://cloud.google.com/storage/docs/access-control/iam-roles) and the bucket must be located in the US multi-region, a dual-region including US-CENTRAL1, or theUS-CENTRAL1 region. 
Usage| Returns  
---|---  
`Blob.url()`| String  
Argument| Type| Details  
---|---|---  
this: `blob`| Blob|   
Was this helpful?
