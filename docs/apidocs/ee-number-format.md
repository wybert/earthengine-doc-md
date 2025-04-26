 
#  ee.Number.format 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Convert a number to a string using printf-style formatting. 
Usage| Returns  
---|---  
`Number.format( _pattern_)`| String  
Argument| Type| Details  
---|---|---  
this: `number`| Number| The number to convert to a string.  
`pattern`| String, default: "%s"| A printf-style format string. For example, '%.2f' produces numbers formatted like '3.14', and '%05d' produces numbers formatted like '00042'. The format string must satisfy the following criteria: 
  1. Zero or more prefix characters.
  2. Exactly one '%'.
  3. Zero or more modifier characters in the set [#-+ 0,(.\d].
  4. Exactly one conversion character in the set [sdoxXeEfgGaA].
  5. Zero or more suffix characters.

For more about format strings, see https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Formatter.html  
## Examples
### Code Editor (JavaScript)
```
print('Zero-fill to length of 3',
ee.Number(1).format('%03d'));// 001
print('Include 1 decimal place in 1.2347',
ee.Number(1.23476).format('%.1f'));// 1.2
print('Include 3 decimal places in 1.2347',
ee.Number(1.23476).format('%.3f'));// 1.235 (rounds up)
print('Scientific notation with 3 decimal places shown',
ee.Number(123476).format('%.3e'));// 1.235e+05 (rounds up)
print('Integer with 2 decimal places of precision',
ee.Number(123476).format('%.2f'));// 123476.00
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
print('Zero-fill to length of 3:',
   ee.Number(1).format('%03d').getInfo()) # 001
print('Include 1 decimal place in 1.2347:',
   ee.Number(1.23476).format('%.1f').getInfo()) # 1.2
print('Include 3 decimal places in 1.2347:',
   ee.Number(1.23476).format('%.3f').getInfo()) # 1.235 (rounds up)
print('Scientific notation with 3 decimal places shown:',
   ee.Number(123476).format('%.3e').getInfo()) # 1.235e+05 (rounds up)
print('Integer with 2 decimal places of precision:',
   ee.Number(123476).format('%.2f').getInfo()) # 123476.00
```

