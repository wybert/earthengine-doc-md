 
#  ee.String.split
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-string-split#examples)


Splits a string on a regular expression, Returning a list of strings. 
Usage| Returns  
---|---  
`String.split(regex,  _flags_)`| List  
Argument| Type| Details  
---|---|---  
this: `string`| String| The string to split.  
`regex`| String| A regular expression to split on. If regex is the empty string, then the input string is split into individual characters.  
`flags`| String, default: ""| A string specifying the regular expression flag: 'i' (ignore case).  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-string-split#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-string-split#colab-python-sample) More
```
vars=ee.String('aBAbcD');
print(s.split('Ab'));// ["aB","cD"]
// 'i' tells split to ignore case.
print(s.split('ab','i'));// ["","","cD"]
// Split on 'b' or 'c'
print(s.split('[bc]','i'));// ["a","A","","D"]
// Split on 'BA' or 'c'
print(s.split('(BA|c)'));// ["a","b","D"]
vars=ee.String('a,b,cdee f,g');
// ["a",",","b",",","c","d","e","e"," ","f",",","g"]
print(s.split(''));
print(s.split(' '));// ["a,b,cdee","f,g"]
print(s.split('[[:space:]]'));// ["a,b,cdee","f,g"]
print(s.split(','));// ["a","b","cdee f","g"]
print(s.split('ee'));// ["a,b,cd"," f,g"]
// Split on any lower case letter.
print(s.split('[a-z]'));// ["",",",",","","",""," ",","]
// ^ as the first character in [] excludes.
print(s.split('[^a-z]'));// ["a","b","cdee","f","g"]
// Splitting on characters that are special to split.
vars=ee.String('a.b*c?d');
print(s.split('\\.'));// ["a","b*c?d"]
print(s.split('[*]'));// ["a.b","c?d"]
print(s.split('[?]'));// ["a.b*c","d"]
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
s = ee.String('aBAbcD')
print(s.split('Ab').getInfo()) # ['aB', 'cD']
# 'i' tells split to ignore case.
print(s.split('ab', 'i').getInfo()) # ['', '', 'cD']
# Split on 'b' or 'c'
print(s.split('[bc]', 'i').getInfo()) # ['a', 'A', '', 'D']
# Split on 'BA' or 'c'
print(s.split('(BA|c)').getInfo()) # ['a', 'b', 'D']
s = ee.String('a,b,cdee f,g')
# ['a', ',', 'b', ',', 'c', 'd', 'e', 'e', ' ', 'f', ',', 'g']
print(s.split('').getInfo())
print(s.split(' ').getInfo()) # ['a,b,cdee', 'f,g']
print(s.split('[[:space:]]').getInfo()) # ['a,b,cdee', 'f,g']
print(s.split(',').getInfo()) # ['a', 'b', 'cdee f', 'g']
print(s.split('ee').getInfo()) # ['a,b,cd', ' f,g']
# Split on any lower case letter.
print(s.split('[a-z]').getInfo()) # ['', ',', ',', '', '', '', ' ', ',']
# ^ as the first character in [] excludes.
print(s.split('[^a-z]').getInfo()) # ['a', 'b', 'cdee', 'f', 'g']
# Splitting on characters that are special to split.
s = ee.String('a.b*c?d')
print(s.split('\\.').getInfo()) # ['a', 'b*c?d']
print(s.split('[*]').getInfo()) # ['a.b', 'c?d']
print(s.split('[?]').getInfo()) # ['a.b*c', 'd']
```

Was this helpful?
