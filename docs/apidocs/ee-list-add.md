 
#  ee.List.add
Stay organized with collections  Save and categorize content based on your preferences. 
Appends the element to the end of list. Usage | Returns  
---|---  
`List.add(element)` | List  
Argument | Type | Details  
---|---|---  
this: `list` | List |   
`element` | Object |   
## Examples
### Code Editor (JavaScript)
```
print(ee.List([]).add('b'));// ["b"]
print(ee.List(['a']).add('b'));// ["a","b"]
print(ee.List(['a']).add(ee.String('b')));// ["a","b"]

print(ee.List(['a']).add(1));// ["a",1]
print(ee.List(['a']).add(ee.Number(1)));// ["a",1]

print(ee.List(['a']).add(true));// ["a",true]

print(ee.List(['a']).add([]));// ["a",[]]
print(ee.List(['a']).add(ee.List([])));// ["a",[]]
print(ee.List(['a']).add(['b']));// ["a",["b"]]
print(ee.List(['a']).add(ee.List(['b'])));// ["a",["b"]]

print(ee.List(['a']).add(ee.Dictionary()));// ["a",{}]
print(ee.List(['a']).add(ee.Dictionary({b:'c'})));// ["a",{"b":"c"}]

// 0: a
// 1: Image (1 band)
print(ee.List(['a']).add(ee.Image.constant(1)));

// ["a",{"type":"ImageCollection","bands":[]}]
print(ee.List(['a']).add(ee.ImageCollection([])));
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
print(ee.List([]).add('b').getInfo())                # ['b']
print(ee.List(['a']).add('b').getInfo())             # ['a', 'b']
print(ee.List(['a']).add(ee.String('b')).getInfo())  # ['a', 'b']

print(ee.List(['a']).add(1).getInfo())             # ['a', 1]
print(ee.List(['a']).add(ee.Number(1)).getInfo())  # ['a', 1]

print(ee.List(['a']).add(True).getInfo())  # ['a', True]

print(ee.List(['a']).add([]).getInfo())              # ['a', []]
print(ee.List(['a']).add(ee.List([])).getInfo())     # ['a', []]
print(ee.List(['a']).add(['b']).getInfo())           # ['a', ['b']]
print(ee.List(['a']).add(ee.List(['b'])).getInfo())  # ['a', ['b']]

print(ee.List(['a']).add(ee.Dictionary()).getInfo())  # ['a', {}]

# ['a', {'b': 'c'}]
print(ee.List(['a']).add(ee.Dictionary({'b': 'c'})).getInfo())

# 0: a
# 1: Image (1 band)
print(ee.List(['a']).add(ee.Image.constant(1)).getInfo())

# ["a", {"type":"ImageCollection", "bands":[]}]
print(ee.List(['a']).add(ee.ImageCollection([])).getInfo())
```

