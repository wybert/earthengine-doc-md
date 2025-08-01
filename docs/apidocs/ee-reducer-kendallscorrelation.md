 
#  ee.Reducer.kendallsCorrelation
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Creates a reducer that computes the Kendall's Tau-b rank correlation. A positive tau value indicates an increasing trend; negative value indicates a decreasing trend. See https://commons.apache.org/proper/commons-math/javadocs/api-3.6.1/org/apache/commons/math3/stat/correlation/KendallsCorrelation.html for details.
Usage | Returns  
---|---  
`ee.Reducer.kendallsCorrelation(_numInputs_)`|  Reducer  
Argument | Type | Details  
---|---|---  
`numInputs` | Integer, default: 1 | The number of inputs to expect (1 or 2). If 1 is specified, automatically generates sequence numbers for the x value (meaning there can be no ties).  
