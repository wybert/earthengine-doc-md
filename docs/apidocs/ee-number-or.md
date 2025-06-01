 
#  ee.Number.or 
Stay organized with collections  Save and categorize content based on your preferences. 
Returns 1 if and only if either input value is non-zero. Usage| Returns  
---|---  
`Number.or(right)`| Number  
Argument| Type| Details  
---|---|---  
this: `left`| Number| The left-hand value.  
`right`| Number| The right-hand value.  
## Examples
### Code Editor (JavaScript)
```
print('Either 0 or 5 non-zero?',ee.Number(0).or(ee.Number(5)));// 1
print('Either 0 or 0 non-zero?',ee.Number(0).or(ee.Number(0)));// 0
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
print('Either 0 or 5 non-zero?', ee.Number(0).Or(ee.Number(5)).getInfo()) # 1
print('Either 0 or 0 non-zero?', ee.Number(0).Or(ee.Number(0)).getInfo()) # 0
```

