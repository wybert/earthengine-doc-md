 
#  ee.List.reduce 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Apply a reducer to a list. If the reducer takes more than 1 input, then each element in the list is assumed to be a list of inputs. If the reducer returns a single output, it is returned directly, otherwise returns a dictionary containing the named reducer outputs. 
Usage| Returns  
---|---  
`List.reduce(reducer)`| Object  
Argument| Type| Details  
---|---|---  
this: `list`| List  
`reducer`| Reducer  
