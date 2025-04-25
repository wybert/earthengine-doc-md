 
#  ee.Classifier.setOutputMode 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Sets a classifier's output format. 
Refer to https://developers.google.com/earth-engine/guides/classification for a list of supported modes for each classifier.
Usage| Returns  
---|---  
`Classifier.setOutputMode(mode)`| Classifier  
Argument| Type| Details  
---|---|---  
this: `classifier`| Classifier| An input classifier.  
`mode`| String| The output mode. One of: 
  * CLASSIFICATION (default): The output is the class number.
  * REGRESSION: The output is the result of standard regression.
  * PROBABILITY: The output is the probability that the classification is correct.
  * MULTIPROBABILITY: The output is an array of probabilities that each class is correct ordered by classes seen.
  * RAW: The output is an array of the internal representation of the classification process. For example, the raw votes in multi-decision tree models.
  * RAW_REGRESSION: The output is an array of the internal representation of the regression process. For example, the raw predictions of multiple regression trees.

  
Was this helpful?
