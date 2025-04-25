 
#  ee.Image.matrixLUDecomposition 
Stay organized with collections  Save and categorize content based on your preferences. 
Calculates the LU matrix decomposition such that P×input=L×U, where L is lower triangular (with unit diagonal terms), U is upper triangular and P is a partial pivot permutation matrix. The input matrix must be square. Returns an image with bands named 'L', 'U' and 'P'. Usage| Returns  
---|---  
`Image.matrixLUDecomposition()`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| Image of 2-D matrices to be decomposed.  
