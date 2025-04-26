 
#  ee.String.match 
Stay organized with collections  Save and categorize content based on your preferences. 
Matches a string against a regular expression. Returns a list of matching strings. Usage| Returns  
---|---  
`String.match(regex,  _flags_)`| List  
Argument| Type| Details  
---|---|---  
this: `input`| String| The string in which to search.  
`regex`| String| The regular expression to match.  
`flags`| String, default: ""| A string specifying a combination of regular expression flags, specifically one or more of: 'g' (global match) or 'i' (ignore case).  
## Examples
### Code Editor (JavaScript)
```
vars=ee.String('ABCabc123');
print(s.match(''));// ""
print(s.match('ab','g'));// ab
print(s.match('ab','i'));// AB
print(s.match('AB','ig'));// ["AB","ab"]
print(s.match('[a-z]+[0-9]+'));// "abc123"
print(s.match('\\d{2}'));// "12"
// Use [^] to match any character except a digit.
print(s.match('abc[^0-9]','i'));// ["ABCa"]
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
s = ee.String('ABCabc123')
print(s.match('').getInfo()) # ""
print(s.match('ab', 'g').getInfo()) # ab
print(s.match('ab', 'i').getInfo()) # AB
print(s.match('AB', 'ig').getInfo()) # ['AB','ab']
print(s.match('[a-z]+[0-9]+').getInfo()) # 'abc123'
print(s.match('\\d{2}').getInfo()) # '12'
# Use [^] to match any character except a digit.
print(s.match('abc[^0-9]', 'i').getInfo()) # ['ABCa']
```

