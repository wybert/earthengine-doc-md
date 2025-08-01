 
#  ee.Array.pad
Stay organized with collections  Save and categorize content based on your preferences. 
Pad an array to a given length. The pad value will be repeatedly appended to the array to extend it to given length along each axis. If the array is already as large or larger than a given length, it will remain unchanged along that axis. Usage | Returns  
---|---  
`Array.pad(lengths, _pad_)`|  Array  
Argument | Type | Details  
---|---|---  
this: `array` | Array | Array to pad.  
`lengths` | List | A list of new lengths for each axis.  
`pad` | Number, default: 0 | The value with which to pad the array.  
