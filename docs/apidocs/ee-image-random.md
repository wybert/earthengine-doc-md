 
#  ee.Image.random 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Generates a random number at each pixel location. When using the 'uniform' distribution, outputs are in the range of [0, 1). Using the 'normal' distribution, the outputs have μ=0, σ=1, but no explicit limits. 
Usage| Returns  
---|---  
`ee.Image.random( _seed_, _distribution_)`| Image  
Argument| Type| Details  
---|---|---  
`seed`| Long, default: 0| Seed for the random number generator.  
`distribution`| String, default: "uniform"| The distribution type of random numbers to produce. One of 'uniform' or 'normal'.  
