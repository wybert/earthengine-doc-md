 
#  ee.Feature.select 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Selects properties from a feature by name or RE2-compatible regex and optionally renames them. 
Usage| Returns  
---|---  
`Feature.select(propertySelectors,  _newProperties_, _retainGeometry_)`| Element  
Argument| Type| Details  
---|---|---  
this: `input`| Element| The feature to select properties from.  
`propertySelectors`| List| A list of names or regexes specifying the properties to select.  
`newProperties`| List, default: null| Optional new names for the output properties. Must match the number of properties selected.  
`retainGeometry`| Boolean, default: true| When false, the result will have a NULL geometry.  
