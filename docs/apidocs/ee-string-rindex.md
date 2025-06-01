 
#  ee.String.rindex 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-string-rindex#examples)


Searches a string for the last occurrence of a substring. Returns the index of the first match, or -1. 
Usage| Returns  
---|---  
`String.rindex(pattern)`| Integer  
Argument| Type| Details  
---|---|---  
this: `target`| String| The string to search.  
`pattern`| String| The string to find.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-string-rindex#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-string-rindex#colab-python-sample) More
```
print(ee.String('aBc-Abc').rindex('A'));// 4
print(ee.String('aBc-Abc').rindex('a'));// 0
print(ee.String('aBc-Abc').rindex('Bc'));// 1
print(ee.String('aBc-Abc').rindex('Z'));// -1
print(ee.String('aBc-Abc').rindex('-'));// 3
print(ee.String('aBc-Abc').rindex(''));// 7
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print(ee.String('aBc-Abc').rindex('A').getInfo()) # 4
print(ee.String('aBc-Abc').rindex('a').getInfo()) # 0
print(ee.String('aBc-Abc').rindex('Bc').getInfo()) # 1
print(ee.String('aBc-Abc').rindex('Z').getInfo()) # -1
print(ee.String('aBc-Abc').rindex('-').getInfo()) # 3
print(ee.String('aBc-Abc').rindex('').getInfo()) # 7
```

