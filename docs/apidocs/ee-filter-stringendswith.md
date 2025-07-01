 
#  ee.Filter.stringEndsWith
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Creates a unary or binary filter that passes if the left operand, a string, ends with the right operand, also a string. 
Usage| Returns  
---|---  
`ee.Filter.stringEndsWith( _leftField_, _rightValue_, _rightField_, _leftValue_)`| Filter  
Argument| Type| Details  
---|---|---  
`leftField`| String, default: null| A selector for the left operand. Should not be specified if leftValue is specified.  
`rightValue`| Object, default: null| The value of the right operand. Should not be specified if rightField is specified.  
`rightField`| String, default: null| A selector for the right operand. Should not be specified if rightValue is specified.  
`leftValue`| Object, default: null| The value of the left operand. Should not be specified if leftField is specified.  
Was this helpful?
