 
#  ee.Reducer.combine 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Creates a Reducer that runs two reducers in parallel. The combined reducer's outputs will be those of reducer1 followed by those of reducer2, where the output names of reducer2 are prefixed with the given string. 
If sharedInputs is true, the reducers must have the same number of inputs, and the combined reducer's will match them; if it is false, the inputs of the combined reducer will be those of reducer1 followed by those of reducer2.
Usage| Returns  
---|---  
`Reducer.combine(reducer2,  _outputPrefix_, _sharedInputs_)`| Reducer  
Argument| Type| Details  
---|---|---  
this: `reducer1`| Reducer| The first reducer.  
`reducer2`| Reducer| The second reducer.  
`outputPrefix`| String, default: ""| Prefix for reducer2's output names.  
`sharedInputs`| Boolean, default: false| Whether the reducers share inputs.  
