 
#  Functional Programming Concepts 
Stay organized with collections  Save and categorize content based on your preferences. 
## Introduction to functional programming
Earth Engine uses a parallel processing system to carry out computation across a large number of machines. To enable such processing, Earth Engine takes advantage of standard techniques commonly used by functional languages, such as referential transparency and lazy evaluation, for significant optimization and efficiency gains.
The main concept that sets functional programming apart from procedural programming is _the absence of side effects_. What it means is that the functions that you write doesn’t rely on or update data that is outside of the function. As you will see in the examples below, it is possible to re-structure your problem so that it can be solved using functions without side-effects - which are much better suited to be executed in parallel.
### For Loops
The use of for-loops is discouraged in Earth Engine. The same results can be achieved using a `map()` operation where you specify a function that can be independently applied to each element. This allows the system to distribute the processing to different machines.
The example below illustrates how you would take a list of numbers and create another list with the squares of each number using `map()`: 
### Code Editor (JavaScript)
```
// This generates a list of numbers from 1 to 10.
varmyList=ee.List.sequence(1,10);
// The map() operation takes a function that works on each element independently
// and returns a value. You define a function that can be applied to the input.
varcomputeSquares=function(number){
// We define the operation using the EE API.
returnee.Number(number).pow(2);
};
// Apply your function to each item in the list by using the map() function.
varsquares=myList.map(computeSquares);
print(squares);// [1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### If/Else Conditions
Another common problem faced by new users who are used to procedural programming paradigm is the proper use of if/else conditional operators in Earth Engine. While, the API does provide a `ee.Algorithms.If()` algorithm, the use of it is strongly discouraged in favor of a more functional approach using `map()` and filters. Earth Engine uses [ deferred execution](https://developers.google.com/earth-engine/guides/deferred_execution), which means that the evaluation of an expression is delayed until its realized value is actually required. In some cases, this type of execution model will evaluate both the true and false alternatives of an `ee.Algorithms.If()` statement. This can lead to extra computation and memory usage, depending on the expressions and the resources required to execute them. 
Say you want to solve a variant of the above example, where the task is to compute squares of only odd numbers. A functional approach to solving this without if/else conditions, is demonstrated below:
### Code Editor (JavaScript)
```
// The following function determines if a number is even or odd. The mod(2)
// function returns 0 if the number is even and 1 if it is odd (the remainder
// after dividing by 2). The input is multiplied by this remainder so even
// numbers get set to 0 and odd numbers are left unchanged.
vargetOddNumbers=function(number){
number=ee.Number(number);// Cast the input to a Number so we can use mod.
varremainder=number.mod(2);
returnnumber.multiply(remainder);
};
varnewList=myList.map(getOddNumbers);
// Remove the 0 values.
varoddNumbers=newList.removeAll([0]);
varsquares=oddNumbers.map(computeSquares);
print(squares);// [1, 9, 25, 49, 81]
```

This paradigm is especially applicable when working with collections. If you wanted to apply a different algorithm to the collection based on some conditions, the preferred way is to first filter the collection based on the condition, and then `map()` a different function to each of the subsets. This allows the system to parallelize the operation. For example: 
### Code Editor (JavaScript)
```
// Import Landsat 8 TOA collection and filter to 2018 images.
varcollection=ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA')
.filterDate('2018-01-01','2019-01-01');
// Divide the collection into 2 subsets and apply a different algorithm on them.
varsubset1=collection.filter(ee.Filter.lt('SUN_ELEVATION',40));
varsubset2=collection.filter(ee.Filter.gte('SUN_ELEVATION',40));
// Multiply all images in subset1 collection by 2;
// do nothing to subset2 collection.
varprocessed1=subset1.map(function(image){
returnimage.multiply(2);
});
varprocessed2=subset2;
// Merge the collections to get a single collection.
varfinal=processed1.merge(processed2);
print('Original collection size',collection.size());
print('Processed collection size',final.size());
```

### Cumulative Iteration
You may need to do sequential operation, where the result of each iteration is used by the subsequent iteration. Earth Engine provides a `iterate()` method for such tasks. Remember that `iterate()` is executed in a sequential manner and hence will be slow for large operations. Use it only when you are not able to use `map()` and filters to achieve the desired output.
A good demonstration of `iterate()` is for creation of [Fibonacci number](https://en.wikipedia.org/wiki/Fibonacci_number) sequence. Here, each number in the series is the sum of previous 2 numbers. The `iterate()` function takes 2 arguments, a function (algorithm) and a starting value. The function itself gets passed on 2 values, the current value in the iteration, and the result of the previous iteration. The following example demonstrates how to implement a fibonacci sequence in Earth Engine.
### Code Editor (JavaScript)
```
varalgorithm=function(current,previous){
previous=ee.List(previous);
varn1=ee.Number(previous.get(-1));
varn2=ee.Number(previous.get(-2));
returnprevious.add(n1.add(n2));
};
// Compute 10 iterations.
varnumIteration=ee.List.repeat(1,10);
varstart=[0,1];
varsequence=numIteration.iterate(algorithm,start);
print(sequence);// [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```

Now that you have a good understanding of javascript concepts, you can see the [API Tutorial](https://developers.google.com/earth-engine/tutorials/tutorial_api_01) for an introduction to the geospatial functionality of the Earth Engine API.
