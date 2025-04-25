 
#  ee.ImageCollection.combine 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Makes a new collection that is a copy of the images in primary, adding all the bands from the image in secondary with a matching ID. If there are no matching IDs, the resulting collection will be empty. This is equivalent to an inner join on ID with merging of the bands of the result. 
Note that this algorithm assumes that for a matching pair of inputs, both have the same footprint and metadata.
Usage| Returns  
---|---  
`ImageCollection.combine(secondary,  _overwrite_)`| ImageCollection  
Argument| Type| Details  
---|---|---  
this: `primary`| ImageCollection| The primary collection to join.  
`secondary`| ImageCollection| The secondary collection to join.  
`overwrite`| Boolean, default: false| If true, bands with the same name will get overwritten. If false, bands with the same name will be renamed.  
Was this helpful?
