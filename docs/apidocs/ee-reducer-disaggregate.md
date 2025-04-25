 
#  ee.Reducer.disaggregate 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Separates aggregate inputs (Arrays, Lists, or Dictionaries) into individual items that are then each passed to the specified reducer. When used on dictionaries, the dictionary keys are ignored. Non-aggregated inputs (e.g., Numbers or Strings) are passed to the underlying reducer directly. 
Usage| Returns  
---|---  
`Reducer.disaggregate( _axis_)`| Reducer  
Argument| Type| Details  
---|---|---  
this: `reducer`| Reducer| The reducer for which to disaggregate inputs.  
`axis`| Integer, default: null| If specified, indicates an array axis along which to disaggregate. If not specified, arrays are completely disaggregated. Ignored for non-array types.  
