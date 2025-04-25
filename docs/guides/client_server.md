 
#  Client vs. Server 
Stay organized with collections  Save and categorize content based on your preferences. 
Earth Engine client libraries for [Python](https://github.com/google/earthengine-api/tree/master/python) and [JavaScript](https://github.com/google/earthengine-api/tree/master/javascript) translate complex geospatial analyses to Earth Engine requests. Code that you write for a client library may contain a mixture of references to client-side objects and variables that represent server-side objects. 
**Note:** Fetching values from server-side objects requires a call to `getInfo()`. In the JavaScript Code Editor, `getInfo()` is automatically called when printing a server-side object. In the Python client library, you must explicitly call `getInfo()` when printing server-side objects. Some libraries, like [geemap](https://developers.google.com/earth-engine/guides/python_install#interactive-exploration-with-geemap) or [eerepr](https://github.com/aazuspan/eerepr), may automatically call `getInfo()` for you when displaying an object in a Jupyter-like notebook. In the following Python code samples, `getInfo()` is called explicitly to make it more clear about when client and server objects are being printed. 
It is important to distinguish Earth Engine objects from other Python or JavaScript objects or primitives that might be in your code. You can manipulate objects on the server by manipulating client-side "proxy" objects in your script. You can recognize a proxy object as anything starting with `ee`. These Earth Engine proxy objects don't contain any actual data and are just handles for objects on the server. To start, consider a client-side string object (which is NOT a proxy object):
### Code Editor (JavaScript)
```
varclientString='I am a String';
print(typeofclientString);// string
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
client_string = 'I am a String'
print(type(client_string)) # str
```

Observe from the output that the client (the web browser or notebook) has interpreted this code and run it, determining that the variable is type `string`. Now suppose you want Earth Engine to be able to do something with this string. To do that, you need to wrap up the string in a nice container and send it to Google. That container is the proxy object. Here's an example:
### Code Editor (JavaScript)
```
varserverString=ee.String('I am not a String!');
print(typeofserverString);// object
print('Is this an EE object?',
serverStringinstanceofee.ComputedObject);// true
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
server_string = ee.String('I am not a String!')
print(type(server_string)) # ee.ee_string.String
print(
  'Is this an EE object?', isinstance(server_string, ee.ee_string.String)
) # True
```

Observe from the output that the `ee.String` is an `object`, NOT a `string`. More specifically, it's an `ee.computedObject`, which means it's a proxy object for something on the server. Think of `ee.Thing` as the way to put a thing in a container for sending to Google. Your client doesn't know what's in the container, but you can find out what's in it by printing it:
### Code Editor (JavaScript)
```
print(serverString);// I am not a String
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
print(server_string.getInfo()) # I am not a String
```

To see what the container itself looks like, print the string representation of the object:
### Code Editor (JavaScript)
```
print(serverString.toString());// ee.String("I am not a String!")
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
print(server_string) # ee.String({"constantValue": "I am not a String!"})
```

If, for some reason, you need to use Python or JavaScript running in the client to manipulate whatever is in the container, then use `getInfo()` to get the contents of the container and assign it to a variable:
### Code Editor (JavaScript)
```
varsomeString=serverString.getInfo();
varstrings=someString+' Am I?';
print(strings);// I am not a String! Am I?
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
some_string = server_string.getInfo()
strings = some_string + ' Am I?'
print(strings) # I am not a String! Am I?
```
**Warning:** Use `getInfo()` with caution! If you call `getInfo()` in your code, Earth Engine will open the container and tell you what's inside, but it will block the rest of your code until that's done. Whenever possible, it's best to do everything on the server. 
## Looping
Because the client doesn't know what's in server-side `ee.Thing` objects, client-side operations such as conditionals and for-loops does not work with them. For that reason, and to avoid synchronous calls to `getInfo()`, use server functions to the extent possible. For example, consider the following two ways of creating a list:
Not recommended — client-side for-loop
### Code Editor (JavaScript)
```
varclientList=[];
for(vari=0;i < 8;i++){
clientList.push(i+1);
}
print(clientList);
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
client_list = []
for i in range(8):
 client_list.append(i + 1)
print(client_list)
```

Recommended — server-side mapping
### Code Editor (JavaScript)
```
varserverList=ee.List.sequence(0,7);
serverList=serverList.map(function(n){
returnee.Number(n).add(1);
});
print(serverList);
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
server_list = ee.List.sequence(0, 7)
server_list = server_list.map(lambda n: ee.Number(n).add(1))
print(server_list.getInfo())
```

The server-side mapping example is a little silly because you could make the same list simply with `ee.List.sequence(1, 8)`, but it illustrates some important concepts. The first concept is `map()` which simply applies the same function to everything in the list. Because this function is executed on the server, client-side functions such as `getInfo()` and `print()` won't work in a mapped function. For that reason, the `i + 1` code has to be replaced with the equivalent server-side code: `ee.Number(n).add(1)`. Importantly, `n` is an object that only exists on the server. Because the function doesn't know the type of its argument, it needs to be cast to an `ee.Number`.
(See [the section on Client and Server functions](https://developers.google.com/earth-engine/guides/client_server#client-and-server-functions) for a description of which functions run on the client.) 
It's also worth noting that occasionally client-side functionality is convenient. For example, the previous for loop could be used to build a list and wrap it with a server-side object:
### Code Editor (JavaScript)
```
vartoServerList=ee.List(clientList);
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
to_server_list = ee.List(client_list)
```

Realize that client-side processing is done in your notebook or browser, the host machine's CPU, so it can be less efficient than using Earth Engine to do the work on the server. Also, to avoid potentially surprising results, it is good practice to avoid mixing client and server functionality in your scripts. The [Conditionals](https://developers.google.com/earth-engine/guides/client_server#conditionals) section provides an example of possibly unintended consequences.
## Conditionals
Server-side objects don't necessarily work with client-side functions and vice versa. For example, consider the case of a server-side Boolean variable:
### Code Editor (JavaScript)
```
varmyList=ee.List([1,2,3]);
varserverBoolean=myList.contains(5);
print(serverBoolean);// false
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
my_list = ee.List([1, 2, 3])
server_boolean = my_list.contains(5)
print(server_boolean.getInfo()) # False
```

As shown in the following example, the variable does not behave in a client-side conditional because it is a server-side object. To correctly check a server-side boolean, use a server-side function:
Not recommended — client-side conditional
### Code Editor (JavaScript)
```
varclientConditional;
if(serverBoolean){
clientConditional=true;
}else{
clientConditional=false;
}
print('Should be false:',clientConditional);// True!
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
if server_boolean:
 client_conditional = True
else:
 client_conditional = False
print('Should be False:', client_conditional) # True!
```

Recommended — server-side conditional
### Code Editor (JavaScript)
```
varserverConditional=ee.Algorithms.If(serverBoolean,'True!','False!');
print('Should be false:',serverConditional);// False!
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
server_conditional = ee.Algorithms.If(server_boolean, 'True!', 'False!')
print('Should be False:', server_conditional.getInfo()) # False!
```
**Warning:** Use `ee.Algorithms.If()` with caution! The preferred way to accomplish conditional tests on the server is with filters. For example, see [Filtering an `ImageCollection`](https://developers.google.com/earth-engine/guides/ic_filtering) and [Filtering a `FeatureCollection`](https://developers.google.com/earth-engine/guides/feature_collection_filtering). 
## Client and Server Functions
The previous sections describe several reasons why it is inefficient or illogical to mix client and server objects and functions. Which objects and functions are client-side and which are server-side? In general, anything initialized as `ee.Thing` is a server object and any method on that object, `ee.Thing.method()`, is a server function. Objects and functions that appear in the [Python](https://docs.python.org/3/reference/index.html) or [JavaScript](https://developer.mozilla.org/docs/Web/JavaScript/Reference) reference are client-side. As noted previously, you can use client-side functionality to create an object, then wrap it by supplying the client-side object to an Earth Engine constructor, for example `ee.String()`.
