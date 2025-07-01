 
#  ee.Array.reduce
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Apply a reducer to an array by collapsing all the input values along each specified axis into a single output value computed by the reducer. 
The output always has the same dimensionality as the input, and the individual axes are affected as follows:
  * The axes specified in the 'axes' parameter have their length reduced to 1 (by applying the reducer).
  * If the reducer has multiple inputs or multiple outputs, the axis specified in 'fieldAxis' will be used to provide the reducer's inputs and store the reducer's outputs.
  * All other axes are unaffected (independent reductions are performed).


Usage| Returns  
---|---  
`Array.reduce(reducer, axes,  _fieldAxis_)`| Array  
Argument| Type| Details  
---|---|---  
this: `array`| Array| The array.  
`reducer`| Reducer| The reducer to apply. Each of its outputs must be a number, not an array or other type.  
`axes`| List| The list of axes over which to reduce. The output will have a length of 1 in all these axes.  
`fieldAxis`| Integer, default: null| The axis to use as the reducer's input and output fields. Only required if the reducer has multiple inputs or multiple outputs, in which case the axis must have length equal to the number of reducer inputs, and in the result it will have length equal to the number of reducer outputs.  
Was this helpful?
