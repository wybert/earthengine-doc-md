 
#  ee.Image.regexpRename 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Renames the bands of an image by applying a regular expression replacement to the current band names. Any bands not matched by the regex will be copied over without renaming. 
Usage| Returns  
---|---  
`Image.regexpRename(regex, replacement,  _all_)`| Image  
Argument| Type| Details  
---|---|---  
this: `input`| Image| The image containing the bands to rename.  
`regex`| String| A regular expression to match in each band name.  
`replacement`| String| The text with which to replace each match. Supports $n syntax for captured values.  
`all`| Boolean, default: true| If true, all matches in a given string will be replaced. Otherwise, only the first match in each string will be replaced.  
Was this helpful?
