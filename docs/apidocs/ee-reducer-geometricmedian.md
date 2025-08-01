 
#  ee.Reducer.geometricMedian
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Creates a reducer that computes the geometric median across a set of inputs.
Usage | Returns  
---|---  
`ee.Reducer.geometricMedian(numX, _eta_, _initialStepSize_)`|  Reducer  
Argument | Type | Details  
---|---|---  
`numX` | Integer | The number of input dimensions.  
`eta` | Float, default: 0.001 | The minimum improvement in the solution used as a stopping criteria for the solver.  
`initialStepSize` | Float, default: 10 | The initial step size used in the solver.  
