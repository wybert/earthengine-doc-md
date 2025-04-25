 
#  ee.Reducer.toList 
Stay organized with collections  Save and categorize content based on your preferences. 
Creates a reducer that collects its inputs into a list, optionally grouped into tuples. Usage| Returns  
---|---  
`ee.Reducer.toList( _tupleSize_, _numOptional_)`| Reducer  
Argument| Type| Details  
---|---|---  
`tupleSize`| Integer, default: null| The size of each output tuple, or null for no grouping. Also determines the number of inputs (null tupleSize has 1 input).  
`numOptional`| Integer, default: 0| The last numOptional inputs will be considered optional; the other inputs must be non-null or the input tuple will be dropped.  
