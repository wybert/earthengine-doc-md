 
#  ee.Image.linkCollection
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Links the source image to a matching image from an image collection. 
Any specified bands or metadata will be added to the source image from the image found in the collection, and if the bands or metadata are already present they will be overwritten. If a matching image is not found, any new or updated bands will be fully masked and any new or updated metadata will be null. The output footprint will be the same as the source image footprint.
A match is determined if the source image and an image in the collection have a specific equivalent metadata property. If more than one collection image would match, the collection image selected is arbitrary. By default, images are matched on their 'system:index' metadata property.
This linking function is a convenience method for adding bands to a target image based on a specified shared metadata property and is intended to support linking collections that apply different processing/product generation to the same source imagery. For more expressive linking known as 'joining', see https://developers.google.com/earth-engine/guides/joins_intro.
Usage| Returns  
---|---  
`Image.linkCollection(imageCollection,  _linkedBands_, _linkedProperties_, _matchPropertyName_)`| Image  
Argument| Type| Details  
---|---|---  
this: `input`| Image| The source image a matching image in the collection will be linked to.  
`imageCollection`| ImageCollection| The image collection searched to extract an image matching the source.  
`linkedBands`| Object, default: null| A band name or list of band names to add or update from the matching image.  
`linkedProperties`| Object, default: null| A metadata property or list of properties to add or update from the matching image.  
`matchPropertyName`| String, default: "system:index"| The metadata property name to use as a match criteria.  
Was this helpful?
