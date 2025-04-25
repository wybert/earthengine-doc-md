 
#  ee.ConfusionMatrix.fscore 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Computes the Fβ-score for the confusion matrix. 
Usage| Returns  
---|---  
`ConfusionMatrix.fscore( _beta_)`| Array  
Argument| Type| Details  
---|---|---  
this: `confusionMatrix`| ConfusionMatrix|   
`beta`| Float, default: 1| A factor indicating how much more important recall is than precision. The standard F-score is equivalent to setting β to one.  
