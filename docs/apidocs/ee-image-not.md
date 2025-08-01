 
#  ee.Image.not
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-not#examples)


Returns 0 if the input is non-zero, and 1 otherwise.
Usage | Returns  
---|---  
`Image.not()` | Image  
Argument | Type | Details  
---|---|---  
this: `value` | Image | The image to which the operation is applied.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image-not#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image-not#colab-python-sample) More
```
/**
 * Demonstrates the ee.Image.Not method.
 *
 * This example uses positive integers; non-integer and negative
 * values are allowed.
 */

varnotZeros=ee.Image(3);// Define an image where all pixels are not zero.
varzeros=notZeros.not();// Pixels are not zeros, return zeros.
varones=zeros.not();// Pixels are zeros, return ones.

print('zeros:',zeros);
print('ones:',ones);

// Display images to the map; explore values using the Inspector.
varvisParams={min:0,max:1};
Map.addLayer(notZeros,visParams,'notZeros');
Map.addLayer(zeros,visParams,'zeros');
Map.addLayer(ones,visParams,'ones');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
"""Demonstrates the ee.Image.Not method.

This example uses positive integers; non-integer and negative
values are allowed.
"""

importpprint
importee
ee.Authenticate()
ee.Initialize()

not_zeros = ee.Image(3)  # Define an image where all pixels are not zero.
zeros = not_zeros.Not()  # Pixels are not zeros, return zeros.
ones = zeros.Not()  # Pixels are zeros, return ones.

print('zeros:')
pprint.pprint(zeros.getInfo())
print('\nones:')
pprint.pprint(ones.getInfo())

# Sample images at a location and print the results.
loc = ee.Geometry.Point(0, 0)  # Location to sample image values.
print('not_zeros:', not_zeros.sample(loc, 1).first().get('constant').getInfo())
print('zeros:', zeros.sample(loc, 1).first().get('constant').getInfo())
print('ones:', ones.sample(loc, 1).first().get('constant').getInfo())
```

Was this helpful?
