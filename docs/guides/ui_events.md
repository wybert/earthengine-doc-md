 
#  Events 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Unlistening](https://developers.google.com/earth-engine/guides/ui_events#unlistening)
  * [Asynchronous Events](https://developers.google.com/earth-engine/guides/ui_events#asynchronous-events)


Events are fired by user interaction with a widget or a programmatic change to a widget. To do something when the event occurs, register a callback function on the widget with either `onClick()` (for `ui.Map` or `ui.Button`) or `onChange()` (everything else). You can also specify a callback in the constructor. The parameters to event callbacks vary depending on the widget and event type. For example, a `ui.Textbox` passes the currently entered string value to its ‘click’ event callback functions. Check the API reference in the **Docs** tab for the type of parameter passed to the callback functions of each widget.
The following example demonstrates multiple events originating from a single user action of specifying an image to display. When the user selects an image, another select widget is updated with the bands of the image and displays the first band in the map:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/ui_events#code-editor-javascript-sample) More
```
// Load some images.
vardem=ee.Image('NASA/NASADEM_HGT/001');
varveg=ee.Image('NOAA/VIIRS/001/VNP13A1/2022_06_02')
.select(['EVI','EVI2','NDVI']);
// Make a drop-down menu of bands.
varbandSelect=ui.Select({
placeholder:'Select a band...',
onChange:function(value){
varlayer=ui.Map.Layer(imageSelect.getValue().select(value));
// Use set() instead of add() so the previous layer (if any) is overwritten.
Map.layers().set(0,layer);
}
});
// Make a drop down menu of images.
varimageSelect=ui.Select({
items:[
{label:'NASADEM',value:dem},
{label:'VIIRS Veg',value:veg}
],
placeholder:'Select an image...',
onChange:function(value){
// Asynchronously get the list of band names.
value.bandNames().evaluate(function(bands){
// Display the bands of the selected image.
bandSelect.items().reset(bands);
// Set the first band to the selected band.
bandSelect.setValue(bandSelect.items().get(0));
});
}
});
print(imageSelect);
print(bandSelect);
```

Note that when the user selects an image, the list of the image's band names is loaded into the `bandSelect` widget, the first band is set to the current value, and the `onChange` function of `bandSelect` is fired automatically. Also note the use of `evaluate()` to asynchronously get the value of the `ComputedObject` returned by `bandNames()`. Learn more in the [Asynchronous Events section](https://developers.google.com/earth-engine/guides/ui_events#asynchronous-events).
## Unlistening
The `unlisten()` method provides the ability to remove callback functions registered on a widget. This is useful to prevent triggering events that should only occur once, or under certain circumstances. The return value of `onClick()` or `onChange()` is an ID that can be passed to `unlisten()` in order to make the widget stop calling the function. To unregister all events or events of a specific type, call `unlisten()` with no arguments or an event type (e.g. `'click'` or `'change'`) argument, respectively. The following example demonstrates `unlisten()` to facilitate opening and closing of a panel: 
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/ui_events#code-editor-javascript-sample) More
```
// Create a panel, initially hidden.
varpanel=ui.Panel({
style:{
width:'400px',
shown:false
},
widgets:[
ui.Label('Click on the map to collapse the settings panel.')
]
});
// Create a button to unhide the panel.
varbutton=ui.Button({
label:'Open settings',
onClick:function(){
// Hide the button.
button.style().set('shown',false);
// Display the panel.
panel.style().set('shown',true);
// Temporarily make a map click hide the panel
// and show the button.
varlistenerId=Map.onClick(function(){
panel.style().set('shown',false);
button.style().set('shown',true);
// Once the panel is hidden, the map should not
// try to close it by listening for clicks.
Map.unlisten(listenerId);
});
}
});
// Add the button to the map and the panel to root.
Map.add(button);
ui.root.insert(0,panel);
```

Observe that `unlisten()` is used to stop `Map` from listening for click events to close the panel when the panel is already closed.
## Asynchronous Events
If you use an Earth Engine result (such the numerical output from a reduction) in a widget, you will need to get the value from the server. (See the [this page](https://developers.google.com/earth-engine/client_server) for details about client vs. server in Earth Engine). To keep from hanging the entire UI while that value is computed, you can use the `evaluate()` function to get the value asynchronously. The `evaluate()` function begins a request for a value, and when the value is ready calls a callback function to do something with the result. For example, consider an application to get the mean value of an NDVI time series at a point:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/ui_events#code-editor-javascript-sample) More
```
// Load and display an NDVI image.
varndvi=ee.ImageCollection('LANDSAT/COMPOSITES/C02/T1_L2_8DAY_NDVI')
.filterDate('2014-01-01','2015-01-01');
varvis={min:0,max:1,palette:['99c199','006400']};
Map.addLayer(ndvi.median(),vis,'NDVI');
// Configure the map.
Map.setCenter(-94.84497,39.01918,8);
Map.style().set('cursor','crosshair');
// Create a panel and add it to the map.
varinspector=ui.Panel([ui.Label('Click to get mean NDVI')]);
Map.add(inspector);
Map.onClick(function(coords){
// Show the loading label.
inspector.widgets().set(0,ui.Label({
value:'Loading...',
style:{color:'gray'}
}));
// Determine the mean NDVI, a long-running server operation.
varpoint=ee.Geometry.Point(coords.lon,coords.lat);
varmeanNdvi=ndvi.reduce('mean');
varsample=meanNdvi.sample(point,30);
varcomputedValue=sample.first().get('NDVI_mean');
// Request the value from the server.
computedValue.evaluate(function(result){
// When the server returns the value, show it.
inspector.widgets().set(0,ui.Label({
value:'Mean NDVI: '+result.toFixed(2),
}));
});
});
```

When the user clicks a point on this map, a `reduceRegion()` call is triggered on the server. This operation might take a while. To prevent the application from blocking while Earth Engine is computing, this example registers a callback function to the result, specifically `computedValue.evaluate()`. When the computation is finished, the result is displayed. In the meantime, a message is displayed to indicate that the computation is in progress.
Was this helpful?
