 
#  ee.Algorithms.CrossCorrelation 
Stay organized with collections  Save and categorize content based on your preferences. 
Gives information on the quality of image registration between two (theoretically) co-registered images. The input is two images with the same number of bands. This function outputs an image composed of four bands of information. The first three are distances: the deltaX, deltaY, and the Euclidean distance for each pixel in imageA to the pixel which has the highest corresponding correlation coefficient in imageB. The fourth band is the value of the correlation coefficient for that pixel [-1 : +1]. Usage| Returns  
---|---  
`ee.Algorithms.CrossCorrelation(imageA, imageB, maxGap, windowSize,  _maxMaskedFrac_)`| Image  
Argument| Type| Details  
---|---|---  
`imageA`| Image| First image, with N bands.  
`imageB`| Image| Second image, must have the same number of bands as imageA.  
`maxGap`| Integer| The greatest distance a pixel may shift in either X or Y.  
`windowSize`| Integer| Size of the window to be compared.  
`maxMaskedFrac`| Float, default: 0| The maximum fraction of pixels within the correlation window that are allowed to be masked. This test is applied at each offset location within the search region. For each offset, the overlapping image patches are compared and a correlation score computed. A pixel within these overlapping patches is considered masked if either of the patches is masked there. If the test fails at any single location in the search region, the output pixel for which the correlation is being computed is considered invalid, and will be masked.  
