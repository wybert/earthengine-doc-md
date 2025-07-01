 
#  ee.Number.erfcInv
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-erfcinv#examples)


Computes the inverse complementary error function of the input. 
Usage| Returns  
---|---  
`Number.erfcInv()`| Number  
Argument| Type| Details  
---|---|---  
this: `input`| Number| The input value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-erfcinv#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-erfcinv#colab-python-sample) More
```
print('Inverse complementary error function of 0',
ee.Number(0).erfcInv());// Infinity
print('Inverse complementary error function of 0.001',
ee.Number(0.001).erfcInv());// 2.326753765
print('Inverse complementary error function of 1',
ee.Number(1).erfcInv());// 0
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print('Inverse complementary error function of 0:',
   ee.Number(0).erfcInv().getInfo()) # Infinity
print('Inverse complementary error function of 0.001:',
   ee.Number(0.001).erfcInv().getInfo()) # 2.326753765
print('Inverse complementary error function of 1:',
   ee.Number(1).erfcInv().getInfo()) # 0
```

Was this helpful?
