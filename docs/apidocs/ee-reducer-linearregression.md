 
#  ee.Reducer.linearRegression 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Creates a reducer that computes a linear least squares regression with numX independent variables and numY dependent variables. 
Each input tuple will have values for the independent variables followed by the dependent variables.
The first output is a coefficients array with dimensions (numX, numY); each column contains the coefficients for the corresponding dependent variable. The second output is a vector of the root mean square of the residuals of each dependent variable. Both outputs are null if the system is underdetermined, e.g., the number of inputs is less than or equal to numX.
Usage| Returns  
---|---  
`ee.Reducer.linearRegression(numX,  _numY_)`| Reducer  
Argument| Type| Details  
---|---|---  
`numX`| Integer| The number of input dimensions.  
`numY`| Integer, default: 1| The number of output dimensions.  
