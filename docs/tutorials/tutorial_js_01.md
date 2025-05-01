 
#  Introduction to JavaScript for Earth Engine 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
This tutorial covers just enough [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/About_JavaScript) to get you started writing Earth Engine scripts. For more thorough JavaScript tutorials, see [these Mozilla developer resources](https://developer.mozilla.org/en-US/docs/Web/JavaScript). For an introduction to programming, with examples in JavaScript, see [Eloquent JavaScript](http://eloquentjavascript.net/). For suggestions on JavaScript coding style, see the [Google JavaScript Style Guide](http://google.github.io/styleguide/javascriptguide.xml). In this tutorial, you're going to write JavaScript in the Earth Engine [Code Editor](https://code.earthengine.google.com/). Before getting started, use [the Code Editor guide](https://developers.google.com/earth-engine/guides/playground) to get familiar with the Code Editor environment.
## Hello World!
Time to write your first JavaScript for Earth Engine! In your Chrome browser, go to [code.earthengine.google.com](https://code.earthengine.google.com/) and copy the following into the [Code Editor](https://developers.google.com/earth-engine/guides/playground):
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/tutorials/tutorial_js_01#code-editor-javascript-sample) More
```
print('Hello World!');
```

Click **Run** and observe that 'Hello world!' is printed to the [Console tab](https://developers.google.com/earth-engine/guides/playground#console-tab). The line above is a JavaScript statement. In JavaScript, statements end in a semicolon. Earth Engine programs are made up of a set of statements like this one. You can prevent code from running without deleting it by commenting it. One of the ways to comment out code is by putting two forward slashes `//` before the code that you don't want to run. For example:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/tutorials/tutorial_js_01#code-editor-javascript-sample) More
```
// print('Hello World!');
```

It's good practice to put lots of comments in your code, to describe what you're trying to do. It's also good to delete commented code that doesn't do anything anymore. Both these practices will improve code readability.
## Basic JavaScript data types
### Strings
Using variables to store objects and primitives helps code readability. For example, a variable that stores a string object is defined by single `'` or double `"` quotes (but don't mix them), with [single quotes preferred](https://google.github.io/styleguide/javascriptguide.xml#Strings). Make a new string and store it in a variable called `greetString`: 
More
### Code Editor (JavaScript)
```
// Use single (or double) quotes to make a string.
vargreetString='Ahoy there!';
// Use parentheses to pass arguments to functions.
print(greetString);
```

### Numbers
Note that variables are defined with the keyword `var`. Variables can also store numbers:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/tutorials/tutorial_js_01#code-editor-javascript-sample) More
```
// Store a number in a variable.
varnumber=42;
print('The answer is:',number);
```

In this example, observe that when `print()` is given two arguments separated by commas, each argument is printed on a different line.
### Lists
Define lists with square brackets `[]`. A list of numbers, for example:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/tutorials/tutorial_js_01#code-editor-javascript-sample) More
```
// Use square brackets [] to make a list.
varlistOfNumbers=[0,1,1,2,3,5];
print('List of numbers:',listOfNumbers);
```

Lists can also store strings or other objects. For example:
More
### Code Editor (JavaScript)
```
// Make a list of strings.
varlistOfStrings=['a','b','c','d'];
print('List of strings:',listOfStrings);
```

### Objects
Objects in JavaScript are dictionaries of `key: value` pairs. Make an object (or dictionary) using curly brackets `{}`, for example:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/tutorials/tutorial_js_01#code-editor-javascript-sample) More
```
// Use curly brackets {} to make a dictionary of key:value pairs.
varobject={
foo:'bar',
baz:13,
stuff:['this','that','the other thing']
};
print('Dictionary:',object);
// Access dictionary items using square brackets.
print('Print foo:',object['foo']);
// Access dictionary items using dot notation.
print('Print stuff:',object.stuff);
```

Note that you can get a value from a dictionary by supplying the key. This example shows you how to do that for JavaScript objects. Later you'll learn how to do it for dictionaries that are on the Earth Engine server.
## Functions
Functions are another way to improve code readability and reusability by grouping sets of operations. Define a function with the `function` keyword. Function names start with a letter and have a pair of parentheses at the end. Functions often take _parameters_ which tell the function what to do. These parameters go inside the parentheses `()`. The set of statements making up the function go inside curly brackets. The `return` keyword indicates what the function output is. There are several ways to declare a function, but here we'll use something like this:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/tutorials/tutorial_js_01#code-editor-javascript-sample) More
```
varmyFunction=function(parameter1,parameter2,parameter3){
statement;
statement;
statement;
returnstatement;
};
```

Let's consider the lines one by one. The first line creates a new function and assigns it to the variable `myFunction`. This variable could have been named anything. It defines how to call the function later. The terms in the parentheses after the function name (i.e. parameter1, parameter2, parameter3) are the parameter names and could have been named anything as well, though it's good practice to give them unique names that are different from the code outside the function. Whatever you name them, these are the names that function will use to refer to the values that are passed into the function when it is called. The value of a parameter once it's been passed into a function is called an _argument_. Although functions can use variables declared outside the function (_global_ variables), function arguments are not visible outside the function. Functions can take as many parameters as you need, even zero. Here's a simple example of a function that just returns its argument:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/tutorials/tutorial_js_01#code-editor-javascript-sample) More
```
// The reflect function takes a single parameter: element.
varreflect=function(element){
// Return the argument.
returnelement;
};
print('A good day to you!',reflect('Back at you!'));
```

This is an example of a user-defined function. There are also lots of built-in Earth Engine functions. Explore the Code Editor [Docs tab](https://developers.google.com/earth-engine/guides/playground#api-reference-docs-tab) to learn about these built-in functions. Here's a very simple example of an Earth Engine function:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/tutorials/tutorial_js_01#code-editor-javascript-sample) More
```
varaString=ee.Algorithms.String(42);
```

In the next section, learn more about [Earth Engine Objects and Methods](https://developers.google.com/earth-engine/tutorials/tutorial_js_02).
