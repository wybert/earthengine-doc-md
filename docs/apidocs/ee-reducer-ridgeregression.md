 
#  ee.Reducer.ridgeRegression 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Creates a reducer that computes a ridge regression with numX independent variables (not including constant) followed by numY dependent variables. Ridge regression is a form of Tikhonov regularization which shrinks the regression coefficients by imposing a penalty on their size. With this implementation of ridge regression there NO NEED to include a constant value for bias. 
The first output is a coefficients array with dimensions (numX + 1, numY); each column contains the coefficients for the corresponding dependent variable plus the intercept for the dependent variable in the last column. Additional outputs are a vector of the root mean square of the residuals of each dependent variable and a vector of p-values for each dependent variable. Outputs are null if the system is underdetermined, e.g., the number of inputs is less than numX + 1.
Usage| Returns  
---|---  
`ee.Reducer.ridgeRegression(numX,  _numY_, _lambda_)`| Reducer  
Argument| Type| Details  
---|---|---  
`numX`| Integer| the number of independent variables being regressed.  
`numY`| Integer, default: 1| the number of dependent variables.  
`lambda`| Float, default: 0.1| Regularization parameter.  
