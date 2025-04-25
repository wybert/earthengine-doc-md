 
#  ee.List.get 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-list-get#examples)


Returns the element at the specified position in list. A negative index counts backwards from the end of the list. 
Usage| Returns  
---|---  
`List.get(index)`| Object  
Argument| Type| Details  
---|---|---  
this: `list`| List  
`index`| Integer  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-list-get#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-list-get#colab-python-sample) More
```
// An ee.List object.
varlist=ee.List([5,10,15,20,25,30]);
// Fetch elements at specified 0-based positions in the list.
print('The second element',list.get(1));
print('The fourth element',list.get(3));
print('The last element',list.get(-1));
print('The second to last element',list.get(-2));
// ee.Number and integer computed objects are valid inputs.
print('Computed object index input',list.get(list.get(0)));
// The result of ee.List.get is an ambiguous object type. You need to cast the
// result to the expected type to use it in subsequent instance methods. For
// example, if you are fetching a number and wish to add it to another number,
// you must cast the .get() result as an ee.Number.
print('Add fetched number to another number',ee.Number(list.get(1)).add(2));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# An ee.List object.
ee_list = ee.List([5, 10, 15, 20, 25, 30])
# Fetch elements at specified 0-based positions in the list.
print('The second element:', ee_list.get(1).getInfo())
print('The fourth element:', ee_list.get(3).getInfo())
print('The last element:', ee_list.get(-1).getInfo())
print('The second to last element:', ee_list.get(-2).getInfo())
# ee.Number and integer computed objects are valid inputs.
print('Computed object index input:', ee_list.get(list.get(0)).getInfo())
# The result of ee.List.get is an ambiguous object type. You need to cast the
# result to the expected type to use it in subsequent instance methods. For
# example, if you are fetching a number and wish to add it to another number,
# you must cast the .get() result as an ee.Number.
print('Add fetched number to another number:',
   ee.Number(list.get(1)).add(2).getInfo())
```

