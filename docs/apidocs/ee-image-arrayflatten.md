 
#  ee.Image.arrayFlatten 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-arrayflatten#examples)


Converts a single-band image of equal-shape multidimensional pixels to an image of scalar pixels, with one band for each element of the array. 
Usage| Returns  
---|---  
`Image.arrayFlatten(coordinateLabels,  _separator_)`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| Image of multidimensional pixels to flatten.  
`coordinateLabels`| List| Name of each position along each axis. For example, 2x2 arrays with axes meaning 'day' and 'color' could have labels like [['monday', 'tuesday'], ['red', 'green']], resulting in band names'monday_red', 'monday_green', 'tuesday_red', and 'tuesday_green'.  
`separator`| String, default: "_"| Separator between array labels in each band name.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image-arrayflatten#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image-arrayflatten#colab-python-sample) More
```
// A function to print arrays for a selected pixel in the following examples.
functionsampArrImg(arrImg){
varpoint=ee.Geometry.Point([-121,42]);
returnarrImg.sample(point,500).first().get('array');
}
// A 1D array image.
vararrayImg1D=ee.Image([0,1,2]).toArray();
print('1D array image (pixel)',sampArrImg(arrayImg1D));
// [0, 1, 2]
// Define image band names for a 1D array image with 3 rows. You are labeling
// all rows and columns using a list of lists; the 1st sub list defines labels
// for array rows and the 2nd (if applicable) defines labels for array columns.
varbandNames1D=[['row0','row1','row2']];
// Flatten the 1D array image into an image with n bands equal to all
// combinations of rows and columns. Here, we have 3 rows and 0 columns,
// so the result will be a 3-band image.
varimgFrom1Darray=arrayImg1D.arrayFlatten(bandNames1D);
print('Image from 1D array',imgFrom1Darray);
// Make a 2D array image by repeating the 1D array on 2-axis.
vararrayImg2D=arrayImg1D.arrayRepeat(1,2);
print('2D array image (pixel)',sampArrImg(arrayImg2D));
// [[0, 0],
// [1, 1],
// [2, 2]]
// Define image band names for a 2D array image with 3 rows and 2 columns.
// Recall that you are labeling all rows and columns using a list of lists;
// The 1st sub list defines labels for array rows and the 2nd (if applicable)
// defines labels for array columns.
varbandNames2D=[['row0','row1','row2'],['col0','col1']];
// Flatten the 2D array image into an image with n bands equal to all
// combinations of rows and columns. Here, we have 3 rows and 2 columns,
// so the result will be a 6-band image.
varimgFrom2Darray=arrayImg2D.arrayFlatten(bandNames2D);
print('Image from 2D array',imgFrom2Darray);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# A function to print arrays for a selected pixel in the following examples.
defsamp_arr_img(arr_img):
 point = ee.Geometry.Point([-121, 42])
 return arr_img.sample(point, 500).first().get('array')
# A 1D array image.
array_img_1d = ee.Image([0, 1, 2]).toArray()
print('1D array image (pixel):', samp_arr_img(array_img_1d).getInfo())
# [0, 1, 2]
# Define image band names for a 1D array image with 3 rows. You are labeling
# all rows and columns using a list of lists; the 1st sub list defines labels
# for array rows and the 2nd (if applicable) defines labels for array columns.
band_names_1d = [['row0', 'row1', 'row2']]
# Flatten the 1D array image into an image with n bands equal to all
# combinations of rows and columns. Here, we have 3 rows and 0 columns,
# so the result will be a 3-band image.
img_from_1d_array = array_img_1d.arrayFlatten(band_names_1d)
print('Image from 1D array:', img_from_1d_array.getInfo())
# Make a 2D array image by repeating the 1D array on 2-axis.
array_img_2d = array_img_1d.arrayRepeat(1, 2)
print('2D array image (pixel):', samp_arr_img(array_img_2d).getInfo())
# [[0, 0],
# [1, 1],
# [2, 2]]
# Define image band names for a 2D array image with 3 rows and 2 columns.
# Recall that you are labeling all rows and columns using a list of lists;
# The 1st sub list defines labels for array rows and the 2nd (if applicable)
# defines labels for array columns.
band_names_2d = [['row0', 'row1', 'row2'], ['col0', 'col1']]
# Flatten the 2D array image into an image with n bands equal to all
# combinations of rows and columns. Here, we have 3 rows and 2 columns,
# so the result will be a 6-band image.
img_from_2d_array = array_img_2d.arrayFlatten(band_names_2d)
print('Image from 2D array:', img_from_2d_array.getInfo())
```

Was this helpful?
