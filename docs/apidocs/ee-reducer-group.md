 
#  ee.Reducer.group
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Groups reducer records by the value of a given input and reduces each group with the given reducer.
Usage | Returns  
---|---  
`Reducer.group(_groupField_, _groupName_)`|  Reducer  
Argument | Type | Details  
---|---|---  
this: `reducer` | Reducer | The reducer to apply to each group, without the group field.  
`groupField` | Integer, default: 0 | The field that contains record groups.  
`groupName` | String, default: "group" | The dictionary key that contains the group. Defaults to 'group'.  
Was this helpful?
