 
#  ee.List.cat 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-list-cat#examples)


Concatenates the contents of other onto list. 
Usage| Returns  
---|---  
`List.cat(other)`| List  
Argument| Type| Details  
---|---|---  
this: `list`| List  
`other`| List  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-list-cat#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-list-cat#colab-python-sample) More
```
print(ee.List(['dog']).cat(['squirrel']));// ["dog","squirrel"]
print(ee.List(['moose']).cat(['&','squirrel']));// ["moose","&","squirrel"]
print(ee.List([['a','b']]).cat(ee.List([['1',1]])));// [["a","b"],["1",1]]
print(ee.List([]).cat(ee.List([])));// []
print(ee.List([1]).cat(ee.List([])));// [1]
print(ee.List([]).cat(ee.List([2])));// [2]
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print(ee.List(['dog']).cat(['squirrel']).getInfo()) # ['dog', 'squirrel']
# ['moose', '&', 'squirrel']
print(ee.List(['moose']).cat(['&', 'squirrel']).getInfo())
# [['a', 'b'], ['1', 1]]
print(ee.List([['a', 'b']]).cat(ee.List([['1', 1]])).getInfo())
print(ee.List([]).cat(ee.List([])).getInfo()) # []
print(ee.List([1]).cat(ee.List([])).getInfo()) # [1]
print(ee.List([]).cat(ee.List([2])).getInfo()) # [2]
```

