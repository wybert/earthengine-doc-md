 
#  ee.List.splice
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-list-splice#examples)


Starting at the start index, removes count elements from list and insert the contents of other at that location. If start is negative, it counts backwards from the end of the list. 
Usage| Returns  
---|---  
`List.splice(start, count,  _other_)`| List  
Argument| Type| Details  
---|---|---  
this: `list`| List|   
`start`| Integer|   
`count`| Integer|   
`other`| List, default: null|   
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-list-splice#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-list-splice#colab-python-sample) More
```
// An ee.List object.
varlist=ee.List([0,1,2,3,4]);
print('Original list',list);
// If "other" argument is null, elements at positions specified by "start" and
// "count" are deleted. Here, the 3rd element is removed.
print('Remove 1 element',list.splice({start:2,count:1,other:null}));
// If "start" is negative, the position is from the end of the list.
print('Remove 2nd from last element',list.splice(-2,1));
// Deletes 3 elements starting at position 1.
print('Remove multiple sequential elements',list.splice(1,3));
// Insert elements from the "other" list without deleting existing elements
// by specifying the insert "start" position and setting "count" to 0.
print('Insert new elements',list.splice(2,0,['X','Y','Z']));
// Replace existing elements with those from the "other" list by specifying the
// "start" position to replace and the "count" of proceeding elements. If
// length of "other" list is greater than "count", the remaining "other"
// elements are inserted, they do not replace existing elements.
print('Replace elements',list.splice(2,3,['X','Y','Z']));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# An ee.List object.
ee_list = ee.List([0, 1, 2, 3, 4])
print('Original list:', ee_list.getInfo())
# If "other" argument is None, elements at positions specified by "start" and
# "count" are deleted. Here, the 3rd element is removed.
print('Remove 1 element:',
   ee_list.splice(start=2, count=1, other=None).getInfo())
# If "start" is negative, the position is from the end of the list.
print('Remove 2nd from last element:', ee_list.splice(-2, 1).getInfo())
# Deletes 3 elements starting at position 1.
print('Remove multiple sequential elements:', ee_list.splice(1, 3).getInfo())
# Insert elements from the "other" list without deleting existing elements
# by specifying the insert "start" position and setting "count" to 0.
print('Insert new elements:', ee_list.splice(2, 0, ['X', 'Y', 'Z']).getInfo())
# Replace existing elements with those from the "other" list by specifying the
# "start" position to replace and the "count" of proceeding elements. If
# length of "other" list is greater than "count", the remaining "other"
# elements are inserted, they do not replace existing elements.
print('Replace elements:', ee_list.splice(2, 3, ['X', 'Y', 'Z']).getInfo())
```

