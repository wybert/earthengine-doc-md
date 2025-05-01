 
#  ee.String.compareTo 
Stay organized with collections  Save and categorize content based on your preferences. 
Compares two strings lexicographically. Returns: the value 0 if the two strings are lexicographically equal; -1 if string1 is less than string2; and 1 if string1 is lexicographically greater than string2. Usage| Returns  
---|---  
`String.compareTo(string2)`| Integer  
Argument| Type| Details  
---|---|---  
this: `string1`| String| The string to compare.  
`string2`| String| The string to be compared.  
## Examples
### Code Editor (JavaScript)
```
print(ee.String('a').compareTo('b'));// -1
print(ee.String('a').compareTo('a'));// 0
print(ee.String('b').compareTo('a'));// 1
print(ee.String('a').compareTo(ee.String('b')));// -1
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
print(ee.String('a').compareTo('b').getInfo()) # -1
print(ee.String('a').compareTo('a').getInfo()) # 0
print(ee.String('b').compareTo('a').getInfo()) # 1
print(ee.String('a').compareTo(ee.String('b')).getInfo()) # -1
```

