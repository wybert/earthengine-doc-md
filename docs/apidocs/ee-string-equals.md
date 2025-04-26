 
#  ee.String.equals 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-string-equals#examples)


Checks for string equality with a given object. Returns true if the target is a string and is lexicographically equal to the reference, or false otherwise. 
Usage| Returns  
---|---  
`String.equals(target)`| Boolean  
Argument| Type| Details  
---|---|---  
this: `reference`| String| The string to compare for equality.  
`target`| Object| The second object to check for equality.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-string-equals#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-string-equals#colab-python-sample) More
```
varsp=ee.String('Abies grandis');
print('"Abies grandis" equals "Abies grandis"?',sp.equals('Abies grandis'));
print('"Abies grandis" equals "abies grandis"?',sp.equals('abies grandis'));
print('"Abies grandis" equals "Thuja plicata"?',sp.equals('Thuja plicata'));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
sp = ee.String('Abies grandis')
print('"Abies grandis" equals "Abies grandis"?',
   sp.equals('Abies grandis').getInfo())
print('"Abies grandis" equals "abies grandis"?',
   sp.equals('abies grandis').getInfo())
print('"Abies grandis" equals "Thuja plicata"?',
   sp.equals('Thuja plicata').getInfo())
```

Was this helpful?
