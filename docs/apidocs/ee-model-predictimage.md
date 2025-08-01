 
#  ee.Model.predictImage
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Make predictions from pixel tiles of an image. The predictions are merged as bands with the input image.
The model will receive 0s in place of masked pixels. The masks of predicted output bands are the minimum of the masks of the inputs.
Usage | Returns  
---|---  
`Model.predictImage(image)` | Image  
Argument | Type | Details  
---|---|---  
this: `model` | Model |   
`image` | Image | The input image.  
Was this helpful?
