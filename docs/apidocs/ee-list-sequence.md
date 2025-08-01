 
#  ee.List.sequence
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-list-sequence#examples)


Generate a sequence of numbers from start to end (inclusive) in increments of step, or in count equally-spaced increments. If end is not specified it is computed from start + step * count, so at least one of end or count must be specified.
Usage | Returns  
---|---  
`ee.List.sequence(start, _end_, _step_, _count_)`|  List  
Argument | Type | Details  
---|---|---  
`start` | Number | The starting number.  
`end` | Number, default: null | The ending number.  
`step` | Number, default: 1 | The increment.  
`count` | Integer, default: null | The number of increments.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-list-sequence#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-list-sequence#colab-python-sample) More
```
print(ee.List.sequence(0,5));// [0,1,2,3,4,5]
print(ee.List.sequence(0,10,2));// [0,2,4,6,8,10]
print(ee.List.sequence(0,null,2,6));// [0,2,4,6,8,10]
print(ee.List.sequence(0,null,-2,6));// [0,-2,-4,-6,-8,-10]

// Step ignored when present along with count.
print(ee.List.sequence(0,10,2,999));// 999 elements
print(ee.List.sequence(0,10,2,3));// [0,5,10]

// Using a dictionary for arguments.
print(ee.List.sequence({start:10,count:3}));// [10,11,12]
print(ee.List.sequence({start:3,step:2,end:6}));// [3,5]
// [-1000000000,0,1000000000]
print(ee.List.sequence({start:-1e9,end:1e9,count:3}));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print(ee.List.sequence(0, 5).getInfo())  # [0, 1, 2, 3, 4, 5]
print(ee.List.sequence(0, 10, 2).getInfo())  # [0, 2, 4, 6, 8, 10]
print(ee.List.sequence(0, None, 2, 6).getInfo())  # [0, 2, 4, 6, 8, 10]
print(ee.List.sequence(0, None, -2, 6).getInfo())  # [0, -2, -4, -6, -8, -10]

# Step ignored when present along with count.
print(ee.List.sequence(0, 10, 2, 999).getInfo())  # 999 elements
print(ee.List.sequence(0, 10, 2, 3).getInfo())  # [0, 5, 10]

# Using a dictionary for arguments.
print(ee.List.sequence(start=10, count=3).getInfo())  # [10, 11, 12]
print(ee.List.sequence(start=3, step=2, end=6).getInfo())  # [3, 5]
# [-1000000000, 0, 1000000000]
print(ee.List.sequence(start=-1e9, end=1e9, count=3).getInfo())
```

