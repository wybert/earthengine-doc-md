 
#  Earth Engine User Interface API 
Stay organized with collections  Save and categorize content based on your preferences. 
Earth Engine provides access to client-side user interface (UI) widgets through the `ui` package. Use the `ui` package to construct graphical interfaces for your Earth Engine scripts. These interfaces can include simple input widgets like buttons and checkboxes, more complex widgets like charts and maps, panels to control the layout of the UI, and event handlers for interactions between UI widgets. Explore the full functionality of the `ui` API in the **Docs** tab on the left side of the Code Editor. The following example uses the `ui` package to illustrate basic functions for making a widget, defining behavior for when the user clicks the widget, and displaying the widget.
## Hello, world!
This example represents a simple UI of a button displayed in the console. Clicking the button results in 'Hello, world!' getting printed to the console:
### Code Editor (JavaScript)
```
// Make a button widget.
varbutton=ui.Button('Click me!');
// Set a callback function to run when the
// button is clicked.
button.onClick(function(){
print('Hello, world!');
});
// Display the button in the console.
print(button);
```

Observe that first, the button is created with a single argument: its label. Next, the button's `onClick()` function is called. The argument to `onClick()` is another function that will get run whenever the button is clicked. This mechanism of a function to be called (a "callback" function) when an event happens is called an "event handler" and is used widely in the UI library. In this example, when the button is clicked, the function prints 'Hello, world!' to the console.
## Mutability
Note that unlike objects in the `ee.*` namespace, objects within the `ui.*` namespace are mutable. So you don’t need to reassign the object to a variable every time you call an instance function on the object. Simply calling the function will mutate (change) the widget. Appending the following code to the previous example results in registering another callback for the button's click event:
### Code Editor (JavaScript)
```
// Set another callback function on the button.
button.onClick(function(){
print('Oh, yeah!');
});
```

Copy this code to the end of the previous example and click **Run**. Now when you click the button, both messages are printed to the console.
Use the UI pages to learn more about building UIs for your Earth Engine scripts. The [Widgets page](https://developers.google.com/earth-engine/guides/ui_widgets) provides a visual tour and describes basic functionality of the widgets in the `ui` package. The [Panels and Layouts page](https://developers.google.com/earth-engine/guides/ui_panels) describes top-level containers and layouts you can use to organize and arrange widgets. The [Events page](https://developers.google.com/earth-engine/guides/ui_events) has details on configuring the behavior and interaction of widgets in your UI.
