 
#  ee.Algorithms.Landsat.TOA 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Calibrates Landsat DN to TOA reflectance and brightness temperature for Landsat and similar data. For recently-acquired scenes calibration coefficients are extracted from the image metadata; for older scenes the coefficients are derived from: 
Chander, Gyanesh, Brian L. Markham, and Dennis L. Helder. "Summary of current radiometric calibration coefficients for Landsat MSS, TM, ETM+, and EO-1 ALI sensors." Remote sensing of environment 113.5 (2009): 893-903.
Usage| Returns  
---|---  
`ee.Algorithms.Landsat.TOA(input)`| Image  
Argument| Type| Details  
---|---|---  
`input`| Image| The Landsat image to process.  
Was this helpful?
