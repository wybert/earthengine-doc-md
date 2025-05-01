 
#  Earth Engine Code Editor 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [JavaScript editor](https://developers.google.com/earth-engine/guides/playground#javascript_editor)
  * [API reference (Docs tab)](https://developers.google.com/earth-engine/guides/playground#api_reference_docs_tab)
  * [Script Manager (Scripts tab)](https://developers.google.com/earth-engine/guides/playground#script_manager_scripts_tab)
  * [Script modules](https://developers.google.com/earth-engine/guides/playground#script_modules)
  * [Asset Manager (Assets tab)](https://developers.google.com/earth-engine/guides/playground#asset_manager_assets_tab)
  * [Script links](https://developers.google.com/earth-engine/guides/playground#script_links)
    * [Get link](https://developers.google.com/earth-engine/guides/playground#get_link)
    * [Script link management](https://developers.google.com/earth-engine/guides/playground#script_link_management)
    * [Script link URL parameters](https://developers.google.com/earth-engine/guides/playground#script_link_url_parameters)
  * [Search tool](https://developers.google.com/earth-engine/guides/playground#search_tool)
  * [Imports](https://developers.google.com/earth-engine/guides/playground#imports)
  * [Map](https://developers.google.com/earth-engine/guides/playground#map)
  * [Layer Manager](https://developers.google.com/earth-engine/guides/playground#layer_manager)
  * [Inspector tab](https://developers.google.com/earth-engine/guides/playground#inspector_tab)
  * [Console Tab](https://developers.google.com/earth-engine/guides/playground#console_tab)
  * [Tasks tab](https://developers.google.com/earth-engine/guides/playground#tasks_tab)
  * [Profiler](https://developers.google.com/earth-engine/guides/playground#profiler)
  * [Geometry tools](https://developers.google.com/earth-engine/guides/playground#geometry_tools)
  * [Help!](https://developers.google.com/earth-engine/guides/playground#help)


The Earth Engine (EE) Code Editor at [code.earthengine.google.com](https://code.earthengine.google.com) is a web-based IDE for the Earth Engine JavaScript API. Code Editor features are designed to make developing complex geospatial workflows fast and easy. The Code Editor has the following elements (illustrated in Figure 1):
  * JavaScript code editor
  * Map display for visualizing geospatial datasets
  * API reference documentation (Docs tab)
  * [Git](http://git-scm.com/)-based Script Manager (Scripts tab)
  * Console output (Console tab)
  * Task Manager (Tasks tab) to handle long-running queries
  * Interactive map query (Inspector tab)
  * Search of the data archive or saved scripts
  * Geometry drawing tools


![Components of the Code Editor](https://developers.google.com/static/earth-engine/images/Code_editor_diagram.png)
**Figure 1.** _Diagram of components of the Earth Engine Code Editor at[code.earthengine.google.com](https://code.earthengine.google.com)._
The Code Editor has a variety of features to help you take advantage of the Earth Engine API. View example scripts or save your own scripts on the **Scripts** tab. Query objects placed on the map with the **Inspector** tab. [Display and chart numeric results](https://developers.google.com/earth-engine/guides/charts) using the Google Visualization API. Share a unique URL to your script with collaborators and friends with the **Get Link** button. Scripts you develop in the Code Editor are sent to Google for processing and the generated map tiles and/or messages are sent back for display in the **Map** and/or **Console** tab. All you need to run the Code Editor is a web browser (use [Google Chrome](https://www.google.com/chrome/) for best results) and an internet connection. The following sections describe elements of the Earth Engine Code Editor in more detail.
## JavaScript editor
The JavaScript editor will:
  * Format and highlight code as you type
  * Underline code with problems, offer fixes and other hints for correct syntax
  * Autocomplete pairs of quotes, brackets and parentheses
  * Offer code completion hints for Earth Engine functions


Above the code editor are buttons for running the script, saving the script, resetting the output map and console, and getting a link to the script. When the **Get Link** button is pressed, a unique link will appear in the browser's address bar. This link represents the code in the editor at the time the button was pressed.
**Note:** The editor supports most features of ECMAScript 5 (ES5), a standardized specification of the JavaScript language. Language features introduced in ECMAScript 6 (ES6) and above are not supported at this time.
## API reference (Docs tab)
On the left side of the Code Editor is the **Docs** tab, which contains the complete JavaScript API documentation. The documentation can be searched and browsed from the **Docs** tab.
## Script Manager (Scripts tab)
The **Scripts** tab is next to the API Docs in the left panel of the Code Editor. The Script Manager stores private, shared and example scripts in [Git](http://git-scm.com/) repositories hosted by Google. The repositories are arranged by access level, with your private scripts stored in a repository you own in the **Owner** folder: `users/username/default`. You (and only you) have access to the repositories in the **Owner** folder unless you share them with someone else. The repositories in the **Writer** folder are repositories for which write access has been granted to you by their owner. You can add new scripts to, modify existing scripts in, or change access to (you may not remove their owner) the repositories in the **Writer** folder. The repositories in the **Reader** folder are repositories for which read access has been granted to you by their owner. The **Examples** folder is a special repository managed by Google which contains code samples. The **Archive** folder contains legacy repositories to which you have access but have not yet been migrated by their owner from an older version of the Script Manager. Search through your scripts using the filter bar at the top of the **Scripts** tab.
![Script Manager](https://developers.google.com/static/earth-engine/images/Playground_scripts.png)
**Figure 2.** _The Script Manager._
Click the ![](https://developers.google.com/static/earth-engine/images/Script_manager_new_button.png) button to create a new repository in the **Owner** folder or to create folders and files within a repository. You can rename scripts with the edit icon and delete them with the delete icon. You can move scripts and organize them into folders using drag and drop (Figure 2). If you drag a script to another repository, it gets copied.
All scripts and repositories maintain full version history. Click on the history icon next to a script or repository to compare or revert it to an older version. To delete a repository, click the delete icon. To configure access to a repository, click the settings icon next to the repository name. Note that if you share a repository, the person with whom you're sharing will need to accept the repository by clicking the link shown in the settings dialog. Previously accepted repositories can be hidden by clicking the block icon following the repo name in the Script Manager.
Repositories can be accessed using [Git](http://git-scm.com/), so you can manage and edit your scripts outside the Code Editor, or sync them with an external system like GitHub. (Learn more about Git from [this tutorial](https://try.github.io/)). Click on the settings icon next to the repository name for instructions on cloning the repository. Note that you can browse the repositories to which you have access by going to [earthengine.googlesource.com](https://earthengine.googlesource.com). For some Git operations, you may need to create authentication credentials by going to the "Generate Password" link at the top of the [earthengine.googlesource.com](https://earthengine.googlesource.com) page.
## Script modules
It's good practice to write modular, reusable code that can be shared between scripts without extensive copying and pasting. To enable modular development, Earth Engine provides the ability to share code between scripts. For example, suppose you write a [function](https://developers.google.com/earth-engine/guides/tutorial_js_01#functions) that performs a useful set of operations. Rather than copy the code of the function into a new script, it's easier for the new script to load the function directly. To make a function or object available to other scripts, you add it to a special object called `exports`. To use the code in another script, use the `require` function to load the exports from another script. For example, suppose you define the following module in a file named `FooModule.js` which is in a folder named `Modules`:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/playground#code-editor-javascript-sample) More
```
/**
 * The Foo module is a demonstration of script modules.
 * It contains a foo function that returns a greeting string.
 * It also contains a bar object representing the current date.
 * @module Modules/FooModule
 */
/**
 * Returns a greeting string.
 * @param {ee.String} arg The name to which the greeting should be addressed
 * @return {ee.String} The complete greeting.
 */
exports.foo=function(arg){
return'Hello, '+arg+'! And a good day to you!';
};
/**
 * An ee.Date object containing the time at which the object was created.
 */
exports.bar=ee.Date(Date.now());
```

Note the use of the `exports` keyword in the form of `exports.objectToExport`. You can make use of this module in another script by using the `require` function. For example:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/playground#code-editor-javascript-sample) More
```
varFoo=require('users/username/default:Modules/FooModule.js');
print(Foo.doc);
print(Foo.foo('world'));
print('Time now:',Foo.bar);
```

The `require` function expects a string that describes the absolute path to the location of the module. Specifically, the argument of `require()` is of the form `'pathToRepository:pathToModuleScript'`. You can only load modules from repositories that you own and/or have read access to. If you want others to be able to use your module, the repository must be shared with the other users you want to have access. You may wish to document your module to help others understand how to use it; we [recommend using JSDoc style](https://google.github.io/styleguide/jsguide.html#jsdoc) with the [`@module` tag](https://jsdoc.app/howto-commonjs-modules.html).
You can use the URL parameter `?scriptPath={repo}:{script}` to share a reference to a file in your repo, e.g. `https://code.earthengine.google.com/?scriptPath=users/username/utils:utils`. Upon visiting the URL, the referenced file and its repo will be added to either the Reader or Writer directory on the [**Scripts** tab](https://developers.google.com/earth-engine/guides/playground#script_manager_scripts_tab), depending on your permission level for the shared repo.
## Asset Manager (Assets tab)
The Asset Manager is in the **Assets** tab in the left panel. Use the Asset Manager (Figure 3) to upload and manage your own image assets in Earth Engine. See the [Asset Manager page](https://developers.google.com/earth-engine/guides/asset_manager) for details.
![The Asset Manager](https://developers.google.com/static/earth-engine/images/Asset_manager_assets_anon.png)
**Figure 3.** _The Asset Manager._
## Script links
Code Editor scripts can be shared via an encoded URL. The following sections describe various ways to generate a script URL, available options, and methods for managing script URLs.
**Caution:** If your shared script includes private asset imports, be sure to [share them](https://developers.google.com/earth-engine/guides/asset_manager#sharing-assets) with intended users or publicly. Unshared asset imports can easily cause your script to break.
### Get link
The "Get Link" button at the top of the Code Editor (Figure 4) provides an interface for generating script URLs and setting script behavior options. Note the distinctions between snapshot and saved script URLs described below.
![The ](https://developers.google.com/static/earth-engine/images/Playground_get_link_button.png)
**Figure 4.** _The "Get Link" button._
#### Snapshot script links
Code in the Editor can be shared via an encoded snapshot URL that gets created upon clicking the "Get Link" button at the top of the Code Editor. When the URL is visited by someone with an Earth Engine account, the browser will navigate to the Code Editor and replicate the environment as it was when the link was created, including code, imports, map layers, and map position. Clicking the "Get Link" button will automatically copy the script link to the clipboard. Additionally, a dialog box will appear providing options to control the execution of the shared script, along with buttons to copy and visit the generated link. The control options include preventing the script from automatically running, and hiding the code pane when someone opens the shared link. The draggable dialog box can be dismissed via the "Esc" key or a click elsewhere on the page.
#### Saved script links
Saved scripts have an option to share a link that will always load the most recent saved version and is only accessible by you and others with current access to the repository containing the script. To use this feature, load a saved script from the Script Manager tab, click the dropdown arrow to the right of the "Get Link" button and select "Copy Script Path". A dialog box will appear presenting the shareable script URL. Note that the script URL has also been set in the browser's address bar. For guidance on sharing your repository with others, please see the [Script Manager section](https://developers.google.com/earth-engine/guides/playground#script_manager_scripts_tab).
### Script link management
The dropdown button to the right of the "Get Link" button has an option to "Manage Links". Clicking this option loads a new browser tab with an interface for you to recall, remove, and download previously generated script links. Selecting a script and pressing the download button will download a zipped folder ("code_editor_links.zip") to your system containing a .txt file representation for each selected script.
### Script link URL parameters
The `ui.url` module allows programmatic manipulation of the script URL's fragment identifier via `get` and `set` methods. This means that Code Editor scripts and Earth Engine Apps can read and store values in the page's URL. Notice the end of the following two URLs, the first sets the `debug` variable as `false` and the second sets it as `true`; visit both links and notice that the debug checkbox in the console is not checked in the first, and is checked in the second, changing the behavior of each script.
```
https://code.earthengine.google.com/5695887aad76979388a723a85339fbf2#debug=false;

```
```
https://code.earthengine.google.com/5695887aad76979388a723a85339fbf2#debug=true;

```

This feature can be used to set map zoom and center, as well as other behaviors you might want to customize when sending links to particular people or groups.
## Search tool
To find datasets to use in your scripts, you can use the search tool for the data archive. The search tool is the text box at the top of the Code Editor that says 'Search places and datasets...' Type the name of a data product, sensor, or other keyword into the search bar and click the search button to see a list of matching places, raster and table datasets. Click on any raster or table result to see the description for that dataset in the archive. To import the dataset directly into your script, click the **import** link or the ![](https://developers.google.com/static/earth-engine/images/Playground_button_import.png) button from the dataset description.
## Imports
The results of importing datasets to your script are organized in an imports section at the top of your script, hidden until you import something. Once you have created some imports, you should see something similar to Figure 5. To copy imports to another script, or convert the imports to JavaScript, click the subject icon next to the **Imports** header and copy the generated code into your script. You can delete the import with the delete icon.
![Code Editor imports section](https://developers.google.com/static/earth-engine/images/Playground_imports_crop.png)
**Figure 5.** _The imports section at the top of the Code Editor._
## Map
The Map object in the API refers to the map display in the Code Editor. For example, `Map.getBounds()` will return the geographic region visible in the Code Editor. Check the `Map` functions in the API to see other customizations for this display.
## Layer Manager
Use the Layer Manager in the upper right corner of the map to adjust the display of layers you added to the map. Specifically, you can toggle the visibility of a layer or adjust its transparency with the slider. Click the settings icon to adjust visualization parameters for individual layers. The visualization tool that appears (Figure 6) allows you to interactively configure layer display parameters. Click the button on the right of the tool (which performs a **Custom** stretch to the supplied min and max range by default) to linearly stretch the display to either percentiles or standard deviations of image values in the display window. Statistics are computed from all the pixels in the Map window at the current zoom level. Use the sliders to adjust gamma and/or transparency. Click the **Palette** radio button and specify a custom palette by adding colors (add), removing colors (remove) or manually entering a comma separated list of hex strings (edit) Click **Apply** to apply the visualization parameters to the current display. Click **Import** to load a visualization parameters object as a new variable in the imports section of your script.
![The layer visualization tool.](https://developers.google.com/static/earth-engine/images/Playground_layer_vis.png)
**Figure 6.** _The layer visualization tool._
**Note:** To the right of the Layer Manager are toggle buttons for different map backgrounds. Customize the background using `Map.setStyle()`.
## Inspector tab
The **Inspector** tab next to the Task Manager lets you interactively query the map. When the **Inspector** tab is activated, the cursor becomes a crosshair which will display the location and layer values under the cursor when you click on the map. For example, Figure 7 shows the results of clicking on the map within the **Inspector** tab. The cursor location and zoom level are displayed along with pixel values and a list of objects on the map. The objects list is interactive. To see more information, expand the objects in the **Inspector** tab.
![Inspector tab](https://developers.google.com/static/earth-engine/images/Playground_inspector_cropped.png)
**Figure 7.** _The Inspector tab shows information about the cursor location and the layer values under the cursor._
## Console Tab
When you `print()` something from your script, such as text, objects or charts, the result will be displayed in the **Console**. The console is interactive, so you can expand printed objects to get more details about them.
## Tasks tab
Earth Engine Tasks are operations that are capable of running much longer than the standard API request timeout. These long-running tasks are the only mechanism for creating persistent artifacts in Earth Engine and adjacent systems (Google Cloud Storage, Google Drive, etc.), and they fall into two categories: `Import` and `Export`.
Import tasks can be used to [upload images](https://developers.google.com/earth-engine/guides/image_upload) or [upload tables](https://developers.google.com/earth-engine/guides/table_upload) into Earth Engine from a variety of filetypes (`.csv`, `.tif`, etc.). Export tasks can be used to execute and write results from the EE computation system (see the [guide for exporting data](https://developers.google.com/earth-engine/guides/exporting) ).
For exports, each call to an `Export` function in the Code Editor will populate an entry in the **Unsubmitted tasks** section of the **Tasks** tab. To submit an export task to the server, click the **Run** button next to the task. A configuration dialog will appear that allows you to specify a variety of parameters for the task. If the task is fully specified at creation time (that is, the call to `Export` has all necessary parameters), hold `ctrl` or `⌘` while clicking **Run** to submit the task without showing the dialog.
For imports, file upload happens locally before the task is submitted to the server. Import tasks in the upload phase will show their progress in the **Unsubmitted tasks** section and automatically submit to the server once the file upload is complete.
Unsubmitted tasks only appear on the page which created them, and they are lost when the page is closed. Once a task is submitted to the server, clicking on its row in the UI will provide additional information and options about the task status, including the option to request cancellation.
To view and cancel multiple tasks in a full-page view (including on mobile clients), use the [Tasks page in the Cloud Console](https://console.cloud.google.com/earth-engine/tasks).
## Profiler
The profiler displays information about the resources (CPU time, memory) consumed by specific algorithms and other parts of a computation. This helps to diagnose why a script is running slowly or failing due to memory limits. To use the profiler, click the **Run with profiler** option in the dropdown on the Run button. As a shortcut, hold down Alt (or Option on Mac) and click Run, or press Ctrl+Alt+Enter. This activates a **Profiler** tab on the right side of the code editor. As the script runs, the **Profiler** tab will display a table of resource usage from the script. Clicking the **Run** button (without profiling) will make the **Profiler** tab disappear and disable the profiler.
See the [computation overview](https://developers.google.com/earth-engine/guides/computation_overview#profiler) page for a breakdown of the profiler's output.
## Geometry tools
You can also import geometries to your script by drawing them on screen. To create geometries, use the geometry drawing tools in the upper left corner of the map display (Figure 8). For drawing points, use the placemark icon ![](https://developers.google.com/static/earth-engine/images/Playground_button_placemark.png), for drawing lines, use the line icon ![](https://developers.google.com/static/earth-engine/images/Playground_button_line.png), for drawing polygons, use the polygon icon ![](https://developers.google.com/static/earth-engine/images/Playground_button_polygon.png), for drawing rectangles use the rectangle icon ![](https://developers.google.com/static/earth-engine/images/Playground_button_rectangle.png). (Note that rectangles are planar geometries, so they cannot be placed on a layer with geodesic geometries like lines and polygons.)
Using any of the drawing tools will automatically create a new geometry layer and add an import for that layer to the Imports section. To add geometries to a new layer, hover on the Geometry Imports in the map display and click the **+new layer** link. You can also toggle visibility of the geometries from the Geometry Imports section. Note that drawn geometries are geodesic by default, except for rectangles, which are planar only. Use the [Geometry constructor](https://developers.google.com/earth-engine/apidocs/ee-geometry) to convert them to planar geometries. Learn more about geometries in Earth Engine on the [Geometry page](https://developers.google.com/earth-engine/guides/geometries).
![](https://developers.google.com/static/earth-engine/images/Playground_geometries_cropped.png)
**Figure 8.** _The geometry drawing tools are in the upper left corner of the map display._
To configure the way geometries are imported to your script, click the settings icon next to the layer in the **Geometry Imports** section on the map or in the **Imports** section of the code editor. The geometry layer settings tool will be displayed in a dialog box which should look something like Figure 9. Note that you can import the drawn shapes as geometries, features or feature collections. The geometry import settings also allow you to change the color with which the layer is displayed, add properties to the layer (if it is imported as a `Feature` or `FeatureCollection`) or rename the layer.
![The geometry configuration
tool](https://developers.google.com/static/earth-engine/images/Playground_geometry_properties_cropped.png)
**Figure 9.** _The geometry configuration tool._
Finally, to prevent geometries in a layer from being edited, you can lock the layer by pressing the lock_open icon next to the layer. This will prevent adding, deleting, or editing any geometries on the layer. To unlock the layer again, press the lock icon.
## Help!
Click the  help button in the upper right of the Code Editor to see links to this Developer's Guide, other help forums, a guided tour of the Code Editor and a list of keyboard shortcuts that help with coding, running code, and displaying data on the **Map**. Click the feedback button to file a bug report, request a new feature, suggest a dataset, or otherwise send feedback when no response is needed.
