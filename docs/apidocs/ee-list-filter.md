 
#  ee.List.filter 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-list-filter#examples)


Filters a list to only the elements that match the given filter. To filter list items that aren't images or features, test a property named 'item', e.g., ee.Filter.gt('item', 3). 
Usage| Returns  
---|---  
`List.filter(filter)`| List  
Argument| Type| Details  
---|---|---  
this: `list`| List|   
`filter`| Filter|   
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-list-filter#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-list-filter#colab-python-sample) More
```
// An ee.Image list object.
varlist=ee.List([1,2,3,null,6,7]);
// Filter the list by a variety of conditions. Note that the property name
// 'item' is used to refer to list elements in ee.Filter functions.
print('List items equal to 3',
list.filter(ee.Filter.eq('item',3)));
print('List items greater than 4',
list.filter(ee.Filter.gt('item',4)));
print('List items not null',
list.filter(ee.Filter.notNull(['item'])));
print('List items in another list',
list.filter(ee.Filter.inList('item',[1,98,99])));
print('List items 3 ≤ 𝑥 ≤ 6',
list.filter(ee.Filter.and(
ee.Filter.gte('item',3),
ee.Filter.lte('item',6))));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# An ee.Image list object.
ee_list = ee.List([1, 2, 3, None, 6, 7])
# Filter the list by a variety of conditions. Note that the property name
# 'item' is used to refer to list elements in ee.Filter functions.
print('List items equal to 3:',
   ee_list.filter(ee.Filter.eq('item', 3)).getInfo())
print('List items greater than 4:',
   ee_list.filter(ee.Filter.gt('item', 4)).getInfo())
print('List items not None:',
   ee_list.filter(ee.Filter.notNull(['item'])).getInfo())
print('List items in another list:',
   ee_list.filter(ee.Filter.inList('item', [1, 98, 99])).getInfo())
print('List items 3 ≤ 𝑥 ≤ 6:',
   ee_list.filter(ee.Filter.And(
     ee.Filter.gte('item', 3),
     ee.Filter.lte('item', 6))).getInfo())
```

Was this helpful?
