 
#  ee.List.frequency 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-list-frequency#examples)


Returns the number of elements in list equal to element. 
Usage| Returns  
---|---  
`List.frequency(element)`| Integer  
Argument| Type| Details  
---|---|---  
this: `list`| List|   
`element`| Object|   
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-list-frequency#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-list-frequency#colab-python-sample) More
```
// An ee.Image list object.
varlist=ee.List([0,1,2,2,3,4]);
print('List of integers',list);
// The ee.List.frequency function is used to determine how many times a value is
// present in a list, e.g. what is the frequency of 0, 2, and 9 in the list.
print('Frequency of value 0',list.frequency(0));
print('Frequency of value 2',list.frequency(2));
print('Frequency of value 9',list.frequency(9));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# An ee.Image list object.
ee_list = ee.List([0, 1, 2, 2, 3, 4])
print('List of integer:', ee_list.getInfo())
# The ee.List.frequency function is used to determine how many times a value is
# present in a list, e.g. what is the frequency of 0, 2, and 9 in the list.
print('Frequency of value 0:', ee_list.frequency(0).getInfo())
print('Frequency of value 2:', ee_list.frequency(2).getInfo())
print('Frequency of value 9:', ee_list.frequency(9).getInfo())
```

