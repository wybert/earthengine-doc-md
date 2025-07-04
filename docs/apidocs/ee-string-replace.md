 
#  ee.String.replace
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-string-replace#examples)


Returns a new string with some or all matches of a pattern replaced. 
Usage| Returns  
---|---  
`String.replace(regex, replacement,  _flags_)`| String  
Argument| Type| Details  
---|---|---  
this: `input`| String| The string in which to search.  
`regex`| String| The regular expression to match.  
`replacement`| String| The string that replaces the matched substring.  
`flags`| String, default: ""| A string specifying a combination of regular expression flags, specifically one or more of: 'g' (global match) or 'i' (ignore case)  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-string-replace#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-string-replace#colab-python-sample) More
```
print(ee.String('abc-abc').replace('abc','X'));// X-abc
print(ee.String('abc-abc').replace('abc','X','g'));// X-X
print(ee.String('abc-abc').replace('abc','','g'));// -
print(ee.String('aBc-Abc').replace('abc','Z','i'));// Z-Abc
print(ee.String('aBc-Abc').replace('abc','Z','ig'));// Z-Z
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print(ee.String('abc-abc').replace('abc', 'X').getInfo()) # X-abc
print(ee.String('abc-abc').replace('abc', 'X', 'g').getInfo()) # X-X
print(ee.String('abc-abc').replace('abc', '', 'g').getInfo()) # -
print(ee.String('aBc-Abc').replace('abc', 'Z', 'i').getInfo()) # Z-Abc
print(ee.String('aBc-Abc').replace('abc', 'Z', 'ig').getInfo()) # Z-Z
```

Was this helpful?
