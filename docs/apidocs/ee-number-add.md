 
#  ee.Number.add
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Adds the first value to the second. 
Usage| Returns  
---|---  
`Number.add(right)`| Number  
Argument| Type| Details  
---|---|---  
this: `left`| Number| The left-hand value.  
`right`| Number| The right-hand value.  
## Examples
### Code Editor (JavaScript)
```
print('5 + 10',ee.Number(5).add(ee.Number(10)));// 15
print('5 + 10.2',ee.Number(5).add(ee.Number(10.2)));// 15.2
print('5 + -10.2',ee.Number(5).add(ee.Number(-10.2)));// -5.199999999
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
print('5 + 10:', ee.Number(5).add(ee.Number(10)).getInfo()) # 15
print('5 + 10.2:', ee.Number(5).add(ee.Number(10.2)).getInfo()) # 15.2
print('5 + -10.2:',
   ee.Number(5).add(ee.Number(-10.2)).getInfo()) # -5.199999999
```

