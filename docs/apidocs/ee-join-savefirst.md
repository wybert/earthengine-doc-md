 
#  ee.Join.saveFirst
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Returns a join that pairs each element from the first collection with a matching element from the second collection. The first match is added to the result as an additional property.
Usage | Returns  
---|---  
`ee.Join.saveFirst(matchKey, _ordering_, _ascending_, _measureKey_, _outer_)`|  Join  
Argument | Type | Details  
---|---|---  
`matchKey` | String | The property name used to save the match.  
`ordering` | String, default: null | The property on which to sort the matches before selecting the first.  
`ascending` | Boolean, default: true | Whether the ordering is ascending.  
`measureKey` | String, default: null | An optional property name used to save the measure of the join condition on the match.  
`outer` | Boolean, default: false | If true, primary rows without matches will be included in the result.  
Was this helpful?
