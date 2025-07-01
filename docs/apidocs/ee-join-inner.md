 
#  ee.Join.inner
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Returns a join that pairs elements from the primary collection with matching elements from the secondary collection. Each result has a 'primary' property that contains the element from the primary collection, and a 'secondary' property containing the matching element from the secondary collection. If measureKey is specified, the join measure is also attached to the object as a property. 
Usage| Returns  
---|---  
`ee.Join.inner( _primaryKey_, _secondaryKey_, _measureKey_)`| Join  
Argument| Type| Details  
---|---|---  
`primaryKey`| String, default: "primary"| The property name used to save the primary match.  
`secondaryKey`| String, default: "secondary"| The property name used to save the secondary match.  
`measureKey`| String, default: null| An optional property name used to save the measure of the join condition.  
