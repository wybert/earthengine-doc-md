 
#  ee.String.slice 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-string-slice#examples)


Returns a substring of the given string. If the specified range exceeds the length of the string, returns a shorter substring. 
Usage| Returns  
---|---  
`String.slice(start,  _end_)`| String  
Argument| Type| Details  
---|---|---  
this: `string`| String| The string to subset.  
`start`| Integer| The beginning index, inclusive. Negative numbers count backwards from the end of the string.  
`end`| Integer, default: null| The ending index, exclusive. Defaults to the length of the string. Negative numbers count backwards from the end of the string.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-string-slice#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-string-slice#colab-python-sample) More
```
print(ee.String('').slice(0));// ''
print(ee.String('').slice(-1));// ''
vars=ee.String('abcdefghijklmnopqrstuvwxyz');
print(s.slice(0));// abcdefghijklmnopqrstuvwxyz
print(s.slice(24));// yz
print(s.slice(-3));// xyz
print(s.slice(3,3));// ''
print(s.slice(2,3));// c
print(s.slice(-4,25));// wxy
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print(ee.String('').slice(0).getInfo()) # ''
print(ee.String('').slice(-1).getInfo()) # ''
s = ee.String('abcdefghijklmnopqrstuvwxyz')
print(s.slice(0).getInfo()) # abcdefghijklmnopqrstuvwxyz
print(s.slice(24).getInfo()) # yz
print(s.slice(-3).getInfo()) # xyz
print(s.slice(3, 3).getInfo()) # ''
print(s.slice(2, 3).getInfo()) # c
print(s.slice(-4, 25).getInfo()) # wxy
```

Was this helpful?
