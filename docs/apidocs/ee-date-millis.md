 
#  ee.Date.millis 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-date-millis#examples)


The number of milliseconds since 1970-01-01T00:00:00Z. 
Usage| Returns  
---|---  
`Date.millis()`| Long  
Argument| Type| Details  
---|---|---  
this: `date`| Date|   
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-date-millis#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-date-millis#colab-python-sample) More
```
vardate=ee.Date(Date.now());
print('Milliseconds since Unix epoch',date.millis());
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
fromdatetimeimport datetime
date = ee.Date(datetime.now())
display('Milliseconds since Unix epoch:', date.millis())
```

