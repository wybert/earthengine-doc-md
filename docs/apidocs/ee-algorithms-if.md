 
#  ee.Algorithms.If 
Stay organized with collections  Save and categorize content based on your preferences. 
Selects one of its inputs based on a condition, similar to an if-then-else construct. Usage| Returns  
---|---  
`ee.Algorithms.If( _condition_, _trueCase_, _falseCase_)`| Object  
Argument| Type| Details  
---|---|---  
`condition`| Object, default: null| The condition that determines which result is returned. If this is not a boolean, it is interpreted as a boolean by the following rules: 
  * Numbers that are equal to 0 or a NaN are false.
  * Empty strings, lists and dictionaries are false.
  * Null is false.
  * Everything else is true.

  
`trueCase`| Object, default: null| The result to return if the condition is true.  
`falseCase`| Object, default: null| The result to return if the condition is false.  
## Examples
### Code Editor (JavaScript)
```
print(ee.Algorithms.If(false,'*true*','*false*'));// The string "*false*"
print(ee.Algorithms.If(true,'*true*','*false*'));// The string "*true*"
// Consider using remap rather than If for tasks like numbers for classes.
print(ee.Algorithms.If(ee.String('Tree').compareTo('Tree'),0,1));
print(ee.Algorithms.If(ee.String('NotTree').compareTo('Tree'),0,1));
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# The string "*false*"
print(ee.Algorithms.If(False, '*true*', '*false*').getInfo())
# The string "*true*"
print(ee.Algorithms.If(True, '*true*', '*false*').getInfo())
# Consider using remap rather than If for tasks like numbers for classes.
print(ee.Algorithms.If(ee.String('Tree').compareTo('Tree'), 0, 1).getInfo())
print(ee.Algorithms.If(ee.String('NotTree').compareTo('Tree'), 0, 1).getInfo())
```

