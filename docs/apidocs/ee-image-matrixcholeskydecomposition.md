 
#  ee.Image.matrixCholeskyDecomposition 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Calculates the Cholesky decomposition of a matrix. The Cholesky decomposition is a decomposition into the form L * L' where L is a lower triangular matrix. The input must be a symmetric positive-definite matrix. Returns an image with 1 band named 'L'. Usage| Returns  
---|---  
`Image.matrixCholeskyDecomposition()`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| Image of 2-D matrices to be decomposed.  
