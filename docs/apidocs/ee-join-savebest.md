 
#  ee.Join.saveBest
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Returns a join that pairs each element from the first collection with a matching element from the second collection. The match with the best join measure is added to each result as an additional property. Join measures are produced when withinDistance or maxDifference filters are used as the join condition. 
Usage| Returns  
---|---  
`ee.Join.saveBest(matchKey, measureKey,  _outer_)`| Join  
Argument| Type| Details  
---|---|---  
`matchKey`| String| The key used to save the match.  
`measureKey`| String| The key used to save the measure of the join condition on the match.  
`outer`| Boolean, default: false| If true, primary rows without matches will be included in the result.  
Was this helpful?
