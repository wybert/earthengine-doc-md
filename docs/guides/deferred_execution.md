 
#  Deferred Execution 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
The [Client vs. Server](https://developers.google.com/earth-engine/guides/client_server) doc describes how objects referenced in your script can be either client-side or server-side. The complete script contains not only the objects you want to use, but also a set of instructions that tell Earth Engine what to do with them. This doc describes how those instructions are sent to Google for processing and how the results are sent back to the client for display.
When you write a script in Earth Engine (either JavaScript or Python), that code does NOT run directly on Earth Engine servers at Google. Instead, the [client library](https://github.com/google/earthengine-api) encodes the script into a set of [JSON](http://www.json.org/) objects, sends the objects to Google and waits for a response. Each object represents a set of operations required to get a particular output, an image to display in the client, for example. Consider the following code:
### Code Editor (JavaScript)
```
varimage=ee.Image('CGIAR/SRTM90_V4');
varoperation=image.add(10);
print(operation.toString());
print(operation);
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
image = ee.Image('CGIAR/SRTM90_V4')
operation = image.add(10)
print(operation)
print(operation.getInfo())
```

The first print statement will output the JSON structure that the client library uses to describe that image to the server at Google:
```
ee.Image({
"type":"Invocation",
"arguments":{
"image1":{
"type":"Invocation",
"arguments":{
"id":"CGIAR/SRTM90_V4"
},
"functionName":"Image.load"
},
"image2":{
"type":"Invocation",
"arguments":{
"value":10
},
"functionName":"Image.constant"
}
},
"functionName":"Image.add"
})

```

The second print statement will send the request to Google and output the [POST](https://en.wikipedia.org/wiki/POST_\(HTTP\)) response from Google servers. To see the response in all its JSON glory, click the `JSON` link on the right side of the console, next to the printed object:
```
{
"type":"Image",
"bands":[
{
"id":"elevation",
"data_type":{
"type":"PixelType",
"precision":"int",
"min":-32758,
"max":32777
},
"crs":"EPSG:4326",
"crs_transform":[
0.0008333333535119891,
0,
-180,
0,
-0.0008333333535119891,
60
]
}
]
}

```

Nothing is sent to Google for processing until there is a request for it. In this example, printing the result of a `getInfo()` call on a server object triggers a request. No processing is done on the server until that result is explicitly requested. Note that `print()` in the JavaScript Code Editor is a special client-side function that wraps an asynchronous `getInfo()` call; for Python we call it directly.
Another example of requesting something is displaying it on the Code Editor or geemap map element. When this request is sent to Google, only the tiles necessary to display the result in the Code Editor or geemap map element are returned. Specifically, the position of the map and the zoom level determine which data get processed and turned into images that can be displayed on the map. If you pan or zoom, note that other tiles are computed lazily. This on-demand system allows for parallelization and efficient processing, but also means that the image displayed on the map is produced from different inputs depending on the zoom level and location of the map bounds. Learn more about how inputs to a computation are determined from the request in the [Scale](https://developers.google.com/earth-engine/guides/scale) doc.
