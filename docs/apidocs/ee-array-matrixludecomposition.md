 
#  ee.Array.matrixLUDecomposition 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Calculates the LU matrix decomposition such that P×input=L×U, where L is lower triangular (with unit diagonal terms), U is upper triangular and P is a partial pivot permutation matrix. The input matrix must be square. Returns a dictionary with entries named 'L', 'U' and 'P'. Usage| Returns  
---|---  
`Array.matrixLUDecomposition()`| Dictionary  
Argument| Type| Details  
---|---|---  
this: `array`| Array| The array to decompose.  
