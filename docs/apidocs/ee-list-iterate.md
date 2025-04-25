 
#  ee.List.iterate 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-list-iterate#examples)


Iterate an algorithm over a list. The algorithm is expected to take two objects, the current list item, and the result from the previous iteration or the value of first for the first iteration. 
Usage| Returns  
---|---  
`List.iterate(function, first)`| Object  
Argument| Type| Details  
---|---|---  
this: `list`| List  
`function`| Algorithm  
`first`| Object  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-list-iterate#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-list-iterate#colab-python-sample) More
```
// This example uses the ee.List.iterate function to generate a series of
// sequentially halved values.
// Declare a list that will hold the series of sequentially halved values,
// initialize it with the starting quantity.
varquantityList=[1000];
// Define the number of iterations as a list sequence.
varnSteps=ee.List.sequence(1,10);
// Declare a function that takes the current element of the iteration list and
// the returned result of the previous iteration as inputs. In this case, the
// the function is returning an accumulating list of quantities that are reduced
// by half at each iteration.
varhalfOfPrevious=function(currentElement,previousResult){
varpreviousQuantity=ee.Number(ee.List(previousResult).get(-1));
varcurrentQuantity=previousQuantity.divide(2);
returnee.List(previousResult).add(currentQuantity);
};
// Apply the function to the nSteps list, each element is an iteration.
quantityList=ee.List(nSteps.iterate(halfOfPrevious,quantityList));
// Display the results. Note that step 0 is included for the initial value.
print('Steps in the iteration of halved quantities',nSteps);
print('Series of sequentially halved quantities',quantityList);
print(ui.Chart.array.values({
array:quantityList,
axis:0,
xLabels:ee.List([0]).cat(nSteps)
}));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
importmatplotlib.pyplotasplt
# This example uses the ee.List.iterate function to generate a series of
# sequentially halved values.
# Declare a list that will hold the series of sequentially halved values,
# initialize it with the starting quantity.
quantity_list = [1000]
# Define the number of iterations as a list sequence.
n_steps = ee.List.sequence(1, 10)

# Declare a function that takes the current element of the iteration list and
# the returned result of the previous iteration as inputs. In this case, the
# the function is returning an accumulating list of quantities that are reduced
# by half at each iteration.
defhalf_of_previous(current_element, previous_result):
 previous_quantity = ee.Number(ee.List(previous_result).get(-1))
 current_quantity = previous_quantity.divide(2)
 return ee.List(previous_result).add(current_quantity)

# Apply the function to the n_steps list, each element is an iteration.
quantity_list = ee.List(n_steps.iterate(half_of_previous, quantity_list))
# Display the results.
display('Steps in the iteration of halved quantities', n_steps)
display('Series of sequentially halved quantities', quantity_list)
quantity_list_client = quantity_list.getInfo()
plt.scatter(range(len(quantity_list_client)), quantity_list_client)
plt.show()
```

Was this helpful?
