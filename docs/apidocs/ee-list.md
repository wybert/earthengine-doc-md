 
#  ee.List
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-list#examples)


Constructs a new list. 
Usage| Returns  
---|---  
`ee.List(list)`| List  
Argument| Type| Details  
---|---|---  
`list`| List| A list or a computed object.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-list#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-list#colab-python-sample) More
```
print(ee.List([]));// []
print(ee.List([null]));// [null]
print(ee.List([true]));// [true]
print(ee.List([1]));// [1]
print(ee.List([ee.Number(1)]));// [1]
print(ee.List(['a']));// ["a"]
print(ee.List([[]]));// [[]]
print(ee.List([ee.List([])]));// [[]]
print(ee.List([[],[[]],[1,[],'a']]));// [[],[[]],[1,[],"a"]]
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print(ee.List([]).getInfo()) # []
print(ee.List([None]).getInfo()) # [None]
print(ee.List([True]).getInfo()) # [True]
print(ee.List([1]).getInfo()) # [1]
print(ee.List([ee.Number(1)]).getInfo()) # [1]
print(ee.List(['a']).getInfo()) # ['a']
print(ee.List([[]]).getInfo()) # [[]]
print(ee.List([ee.List([])]).getInfo()) # [[]]
print(ee.List([[], [[]], [1, [], 'a']]).getInfo()) # [[], [[]], [1, [], 'a']]
```

Was this helpful?
