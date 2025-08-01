 
#  ee.Number.expression
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-expression#examples)


Computes a numeric expression.
Usage | Returns  
---|---  
`ee.Number.expression(expression, _vars_)`|  Number  
Argument | Type | Details  
---|---|---  
`expression` | String | A mathematical expression string to be evaluated. In addition to the standard arithmetic, boolean and relational operators, expressions also support any function in Number, the '.' operator to extract child elements from the 'vars' dictionary, and mathematical constants Math.PI and Math.E.  
`vars` | Dictionary, default: null | A dictionary of named values that can be used in the expression.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-expression#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-expression#colab-python-sample) More
```
// A dictionary of variables to use in expression.
varvariables={x:5,y:10};

// Arithmetic operators.
print('x + y',
ee.Number.expression('x + y',variables));
print('x - y',
ee.Number.expression('x - y',variables));
print('x * y',
ee.Number.expression('x * y',variables));
print('x / y',
ee.Number.expression('x / y',variables));
print('x ** y',
ee.Number.expression('x ** y',variables));
print('x % y',
ee.Number.expression('x % y',variables));

// Logical operators.
print('x || y',
ee.Number.expression('x || y',variables));
print('x && y',
ee.Number.expression('x && y',variables));
print('!(x)',
ee.Number.expression('!(x)',variables));

// Relational operators.
print('x > y',
ee.Number.expression('x > y',variables));
print('x >= y',
ee.Number.expression('x >= y',variables));
print('x < y',
ee.Number.expression('x < y',variables));
print('x <= y',
ee.Number.expression('x <= y',variables));
print('x == y',
ee.Number.expression('x == y',variables));
print('x != y',
ee.Number.expression('x != y',variables));

// Conditional (ternary) operator.
print('(x < y) ? 100 : 1000)',
ee.Number.expression('(x < y) ? 100 : 1000',variables));

// Constants in the expression.
print('100 * (x + y)',
ee.Number.expression('100 * (x + y)',variables));

// JavaScript Math constants.
print('Math.PI',
ee.Number.expression('Math.PI',null));
print('Math.E',
ee.Number.expression('Math.E',null));

// Dot notation to call on child elements.
print('Use dot notation to call on child elements',
ee.Number.expression('vals.x * vals.y',{vals:variables}));

// ee.Number functions.
print('Use ee.Number add: add(x, y)',
ee.Number.expression('add(x, y)',variables));
print('Use ee.Number add and subtract: subtract(add(x, y), 5)',
ee.Number.expression('subtract(add(x, y), 5)',variables));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# A dictionary of variables to use in expression.
variables = {'x': 5, 'y': 10}

# Arithmetic operators.
print('x + y:',
      ee.Number.expression('x + y', variables).getInfo())
print('x - y:',
      ee.Number.expression('x - y', variables).getInfo())
print('x * y:',
      ee.Number.expression('x * y', variables).getInfo())
print('x / y:',
      ee.Number.expression('x / y', variables).getInfo())
print('x ** y:',
      ee.Number.expression('x ** y', variables).getInfo())
print('x % y:',
      ee.Number.expression('x % y', variables).getInfo())

# Logical operators.
print('x || y:',
      ee.Number.expression('x || y', variables).getInfo())
print('x && y:',
      ee.Number.expression('x && y', variables).getInfo())
print('!(x):',
      ee.Number.expression('!(x)', variables).getInfo())

# Relational operators.
print('x > y:',
      ee.Number.expression('x > y', variables).getInfo())
print('x >= y:',
      ee.Number.expression('x >= y', variables).getInfo())
print('x < y:',
      ee.Number.expression('x < y', variables).getInfo())
print('x <= y:',
      ee.Number.expression('x <= y', variables).getInfo())
print('x == y:',
      ee.Number.expression('x == y', variables).getInfo())
print('x != y:',
      ee.Number.expression('x != y', variables).getInfo())

# Conditional JavaScript (ternary) operator.
print('(x < y) ? 100 : 1000):',
      ee.Number.expression('(x < y) ? 100 : 1000', variables).getInfo())

# Constants in the expression.
print('100 * (x + y):',
      ee.Number.expression('100 * (x + y)', variables).getInfo())

# JavaScript Math constants.
print('Math.PI:',
      ee.Number.expression('Math.PI', None).getInfo())
print('Math.E:',
      ee.Number.expression('Math.E', None).getInfo())

# Dot notation to call on child elements.
print('Use dot notation to call on child elements:',
      ee.Number.expression('vals.x * vals.y', {'vals': variables}).getInfo())

# ee.Number functions.
print('Use ee.Number add. add(x, y):',
      ee.Number.expression('add(x, y)', variables).getInfo())
print('Use ee.Number add and subtract. subtract(add(x, y), 5):',
      ee.Number.expression('subtract(add(x, y), 5)', variables).getInfo())
```

Was this helpful?
