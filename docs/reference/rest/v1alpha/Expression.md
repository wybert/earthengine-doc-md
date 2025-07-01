 
#  Expression
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Specifies an arbitrary expression, of an arbitrary type. The context in which it is used determines the type of the response.
JSON representation  
---  
```
{
 "values": {
  string: {
   object (ValueNode)
  },
  ...
 },
 "result": string
}
```
  
Fields  
---  
`values` |  `map (key: string, value: object (`ValueNode`))` All intermediate values in the computation. The directed graph these form must be acyclic.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`result` |  `string` Which of the ValueNodes in "values" is the final result of the computation.  
Was this helpful?
