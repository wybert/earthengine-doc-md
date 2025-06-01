 
#  Earth Engine Objects 
Stay organized with collections  Save and categorize content based on your preferences. 
Now that you're comfortable with JavaScript, learn how to put JavaScript objects and primitives into Earth Engine containers for sending to the server and processing at Google.
## Strings
For example, define a string, then put it into the `ee.String()` container to be sent to Earth Engine:
### Code Editor (JavaScript)
```
// Define a string, then put it into an EE container.
varaString='To the cloud!';
vareeString=ee.String(aString);
print('Where to?',eeString);
```

Think of `ee.Thing` as a container for a thing that exists on the server. In this example, the string is defined first, then put into the container. You can also define the container and its contents all at once. For example:
### Code Editor (JavaScript)
```
// Define a string that exists on the server.
varserverString=ee.String('This is on the server.');
print('String on the server:',serverString);
```

Although the first argument to `print()` is just a string on the client, the second argument is actually sent to the server to be evaluated, then sent back.
## Numbers
Use `ee.Number()` to create number objects on the server. For example, use the `Math.E` JavaScript method to create a constant value on the server:
### Code Editor (JavaScript)
```
// Define a number that exists on the server.
varserverNumber=ee.Number(Math.E);
print('e=',serverNumber);
```

The `ee.String()` and `ee.Number()` methods are _constructors_. A constructor takes its argument (and possibly other parameters), puts it in a container, and returns the container and its contents as an Earth Engine object that you can manipulate in your code. Any constructor starting with `ee` returns an Earth Engine object.
## Methods on Earth Engine objects
Note that once you've created an Earth Engine object, you have to use Earth Engine methods to process it. In this example, you can't use JavaScript's [`Math.log()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/log) to process that Earth Engine object. You have to use the equivalent method defined for an `ee.Number`:
### Code Editor (JavaScript)
```
// Use a built-in function to perform an operation on the number.
varlogE=serverNumber.log();
print('log(e)=',logE);
```

In this example, `log()` is a method for a `ee.Number` object. (Use the [**Docs** tab](https://developers.google.com/earth-engine/guides/playground#api-reference-docs-tab) at the left side of the code editor to see a list of all the methods for every Earth Engine object type, for example ee.Number > log()). Note that the methods of Earth Engine objects return other Earth Engine objects.
## Lists
To make a JavaScript list into an `ee.List` object on the server, you can put a JavaScript literal into a container as with numbers and strings. Earth Engine also provides server-side convenience methods for making sequences of numbers. For example:
### Code Editor (JavaScript)
```
// Make a sequence the hard way.
vareeList=ee.List([1,2,3,4,5]);
// Make a sequence the easy way!
varsequence=ee.List.sequence(1,5);
print('Sequence:',sequence);
```

Since the `ee.List` objects only exist on the server, use Earth Engine provided functions to interact with them. For example, to get something out of the list, use the `get()` method of the `ee.List` object:
### Code Editor (JavaScript)
```
// Use a method on an ee.List to extract a value.
varvalue=sequence.get(2);
print('Value at index 2:',value);
```

## Casting
Sometimes, Earth Engine doesn't know the type of an object that gets returned from a method. You, as the programmer, know that the `value` variable in the previous example is a number object. But if you try to use the `add()` method of an `ee.Number`, you'll get an error like:
value.add is not a function
This is common with the `get()` function, which could return all sorts of Earth Engine objects. To correct it, use the `ee.Number` constructor to _cast_ the result:
### Code Editor (JavaScript)
```
// Cast the return value of get() to a number.
print('No error:',ee.Number(value).add(3));
```

## Dictionaries
You can construct an Earth Engine `Dictionary` from a JavaScript object, as with strings, numbers and lists. At construction time, you can use JavaScript functionality to initialize the Earth Engine object. In this case an `ee.Dictionary` is constructed directly from a JavaScript literal object:
### Code Editor (JavaScript)
```
// Make a Dictionary on the server.
vardictionary=ee.Dictionary({
e:Math.E,
pi:Math.PI,
phi:(1+Math.sqrt(5))/2
});
// Get some values from the dictionary.
print('Euler:',dictionary.get('e'));
print('Pi:',dictionary.get('pi'));
print('Golden ratio:',dictionary.get('phi'));
// Get all the keys:
print('Keys: ',dictionary.keys());
```

In this example, observe that once you have an `ee.Dictionary`, you must use methods on the `ee.Dictionary` to get values (unlike the JavaScript dictionary in the previous lesson). Specifically, `get(key)` returns the value associated with `key`. Since the type of object returned by `get()` could be be anything, if you're going to do anything to the object other then print it, you need to cast it to the right type. Also note that the `keys()` method returns an `ee.List`. 
## Dates
Date objects are the way Earth Engine represents time. As in the previous examples, it is important to distinguish between a JavaScript [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) object and an Earth Engine `ee.Date` object. Construct an `ee.Date` from a string, from a JavaScript `Date`, or using static methods provided by the `ee.Date` class. (See the Date section in the [**Docs** tab](https://developers.google.com/earth-engine/guides/playground#api-reference-docs-tab) for details). This example illustrates the construction of dates from strings or a JavaScript date representing milliseconds since midnight on January 1, 1970:
### Code Editor (JavaScript)
```
// Define a date in Earth Engine.
vardate=ee.Date('2015-12-31');
print('Date:',date);
// Get the current time using the JavaScript Date.now() method.
varnow=Date.now();
print('Milliseconds since January 1, 1970',now);
// Initialize an ee.Date object.
vareeNow=ee.Date(now);
print('Now:',eeNow);
```

Dates are useful for filtering collections, specifically as arguments to the `filterDate()` method. See [this section of the Get Started page](https://developers.google.com/earth-engine/guides/getstarted#filtering-and-sorting) for more information about sorting collections.
## Digression: passing parameters by name
Arguments to Earth Engine methods can be passed in order, for example to create an `ee.Date` from year, month and day, you can pass parameters of the `fromYMD()` static method in the order year, month, day:
### Code Editor (JavaScript)
```
varaDate=ee.Date.fromYMD(2017,1,13);
print('aDate:',aDate);
```

Alternatively, you can pass the parameters by name, in any order. While it might be more code, it can improve readability and reusability. To pass parameters by name, pass in a JavaScript object in which the keys of the object are the names of the method parameters and the values are the arguments to the method. For example:
### Code Editor (JavaScript)
```
vartheDate=ee.Date.fromYMD({
day:13,
month:1,
year:2017
});
print('theDate:',theDate);
```

Note that the names of the object properties (the keys) match the names specified in the [`ee.Date.fromYMD()` docs](https://developers.google.com/earth-engine/apidocs/ee-date-fromymd). Also note that the object that is passed as an argument can be saved in a variable for reuse, as illustrated by the [JavaScript object example](https://developers.google.com/earth-engine/tutorials/tutorial_js_01#objects).
You now have enough of an introduction to JavaScript to start using Earth Engine! See the [Client vs. Server page](https://developers.google.com/earth-engine/guides/client_server) for a more detailed explanation of JavaScript vs. Earth Engine objects.
In the next section, learn more about [Functional programming concepts](https://developers.google.com/earth-engine/tutorials/tutorial_js_03) to effectively use for-loops, if/else conditions and iterations in Earth Engine.
