 
#  ee.ImageCollection.linkCollection
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
`imageCollection`.
For each source image in this collection, any specified bands or metadata will be added to the source image from the matching image found in
`imageCollection`. If bands or metadata are already present, they will be overwritten. If matching images are not found, any new or updated bands will be fully masked and any new or updated metadata will be null. The output footprint will be the same as the source image footprint.
Matches are determined if a source image and an image in `imageCollection` have a specific equivalent metadata property. If more than one collection image would match, the collection image selected is arbitrary. By default, images are matched on their 'system:index' metadata property.
This linking function is a convenience method for adding bands to target images based on a specified shared metadata property and is intended to support linking collections that apply different processing/product generation to the same source imagery. For more expressive linking known as
'joining', see https://developers.google.com/earth-engine/guides/joins_intro.
Returns the linked image collection.
Usage | Returns  
---|---  
`ImageCollection.linkCollection(imageCollection, _linkedBands_, _linkedProperties_, _matchPropertyName_)`|  ImageCollection  
Argument | Type | Details  
---|---|---  
this: `imagecollection` | ImageCollection | The ImageCollection instance.  
`imageCollection` | ImageCollection | The image collection searched to find matches from this collection.  
`linkedBands` | List<String>, optional | Optional list of band names to add or update from matching images.  
`linkedProperties` | List<String>, optional | Optional list of metadata properties to add or update from matching images.  
`matchPropertyName` | String, optional | The metadata property name to use as a match criteria. Defaults to "system:index".  
