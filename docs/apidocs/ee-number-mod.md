 
#  ee.Number.mod 
Stay organized with collections  Save and categorize content based on your preferences. 
Calculates the remainder of the first value divided by the second. Usage| Returns  
---|---  
`Number.mod(right)`| Number  
Argument| Type| Details  
---|---|---  
this: `left`| Number| The left-hand value.  
`right`| Number| The right-hand value.  
## Examples
### Code Editor (JavaScript)
```
// Remainder with positive dividend.
print('Remainder of 12/5',ee.Number(12).mod(ee.Number(5)));// 2
print('Remainder of 1/-2',ee.Number(1).mod(ee.Number(-2)));// 1
print('Remainder of 1/2',ee.Number(1).mod(ee.Number(2)));// 1
print('Remainder of 2/3',ee.Number(2).mod(ee.Number(3)));// 2
print('Remainder of 5.5/2',ee.Number(5.5).mod(ee.Number(2)));// 1.5
// Remainder with negative dividend.
print('Remainder of -12/5',ee.Number(-12).mod(ee.Number(5)));// -2
print('Remainder of -1/2',ee.Number(-1).mod(ee.Number(2)));// -1
print('Remainder of -4/2',ee.Number(-4).mod(ee.Number(2)));// 0
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Remainder with positive dividend.
print('Remainder of 12/5:', ee.Number(12).mod(ee.Number(5)).getInfo()) # 2
print('Remainder of 1/-2:', ee.Number(1).mod(ee.Number(-2)).getInfo()) # 1
print('Remainder of 1/2:', ee.Number(1).mod(ee.Number(2)).getInfo()) # 1
print('Remainder of 2/3:', ee.Number(2).mod(ee.Number(3)).getInfo()) # 2
print('Remainder of 5.5/2:', ee.Number(5.5).mod(ee.Number(2)).getInfo()) # 1.5
# Remainder with negative dividend.
print('Remainder of -12/5:', ee.Number(-12).mod(ee.Number(5)).getInfo()) # -2
print('Remainder of -1/2:', ee.Number(-1).mod(ee.Number(2)).getInfo()) # -1
print('Remainder of -4/2:', ee.Number(-4).mod(ee.Number(2)).getInfo()) # 0
```

