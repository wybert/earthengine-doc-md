 
#  ee.Join.saveAll
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Returns a join that pairs each element from the first collection with a group of matching elements from the second collection. The list of matches is added to each result as an additional property. If measureKey is specified, each match has the value of its join measure attached. Join measures are produced when withinDistance or maxDifference filters are used as the join condition.
Usage | Returns  
---|---  
`ee.Join.saveAll(matchesKey, _ordering_, _ascending_, _measureKey_, _outer_)`|  Join  
Argument | Type | Details  
---|---|---  
`matchesKey` | String | The property name used to save the matches list.  
`ordering` | String, default: null | The property on which to sort the matches list.  
`ascending` | Boolean, default: true | Whether the ordering is ascending.  
`measureKey` | String, default: null | An optional property name used to save the measure of the join condition on each match.  
`outer` | Boolean, default: false | If true, primary rows without matches will be included in the result.  
Was this helpful?
