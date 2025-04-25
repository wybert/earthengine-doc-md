 
#  ee.ImageCollection.reduceColumns 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Apply a reducer to each element of a collection, using the given selectors to determine the inputs. 
Returns a dictionary of results, keyed with the output names.
Usage| Returns  
---|---  
`ImageCollection.reduceColumns(reducer, selectors,  _weightSelectors_)`| Dictionary  
Argument| Type| Details  
---|---|---  
this: `collection`| FeatureCollection| The collection to aggregate over.  
`reducer`| Reducer| The reducer to apply.  
`selectors`| List| A selector for each input of the reducer.  
`weightSelectors`| List, default: null| A selector for each weighted input of the reducer.  
Was this helpful?
