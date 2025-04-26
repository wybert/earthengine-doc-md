 
#  ee.ImageCollection.randomColumn 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Adds a column of deterministic pseudorandom numbers to a collection. The outputs are double-precision floating point numbers. When using the 'uniform' distribution (default), outputs are in the range of [0, 1). Using the 'normal' distribution, outputs have μ=0, σ=1, but have no explicit limits. 
Usage| Returns  
---|---  
`ImageCollection.randomColumn( _columnName_, _seed_, _distribution_, _rowKeys_)`| FeatureCollection  
Argument| Type| Details  
---|---|---  
this: `collection`| FeatureCollection| The input collection to which to add a random column.  
`columnName`| String, default: "random"| The name of the column to add.  
`seed`| Long, default: 0| A seed used when generating the random numbers.  
`distribution`| String, default: "uniform"| The distribution type of random numbers to produce; one of 'uniform' or 'normal'.  
`rowKeys`| List, optional| A list of properties that should uniquely and repeatably identify an element of the collection, used to generate the random number. Defaults to [system:index].  
