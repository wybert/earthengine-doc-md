 
#  Python Installation 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Python support](https://developers.google.com/earth-engine/guides/python_install#python-support)
  * [Install options](https://developers.google.com/earth-engine/guides/python_install#install-options)
  * [Package import](https://developers.google.com/earth-engine/guides/python_install#package-import)
  * [Authentication and Initialization](https://developers.google.com/earth-engine/guides/python_install#authentication-and-initialization)
  * [Hello world!](https://developers.google.com/earth-engine/guides/python_install#hello-world)
  * [Syntax](https://developers.google.com/earth-engine/guides/python_install#syntax)
  * [Date objects](https://developers.google.com/earth-engine/guides/python_install#date-objects)
  * [Exporting data](https://developers.google.com/earth-engine/guides/python_install#exporting-data)
  * [Printing objects](https://developers.google.com/earth-engine/guides/python_install#printing-objects)
  * [UI objects](https://developers.google.com/earth-engine/guides/python_install#ui-objects)
  * [Python in the Developer Guide](https://developers.google.com/earth-engine/guides/python_install#python-in-the-developer-guide)
    * [Earth Engine setup](https://developers.google.com/earth-engine/guides/python_install#earth-engine-setup)
    * [Interactive exploration with geemap](https://developers.google.com/earth-engine/guides/python_install#interactive-exploration-with-geemap)


Keep your client library up to date by running the command for the package manager you used to install `earthengine-api`: 
  * [Conda Package Manager](https://developers.google.com/earth-engine/guides/python_install-conda#updating_the_api): `conda update -c conda-forge earthengine-api`
  * [Python Package Installer](https://developers.google.com/earth-engine/guides/python_install#pip): `pip install earthengine-api --upgrade`


## Python support
The Earth Engine Python client library is compatible with [Python versions supported by Google Cloud](https://cloud.google.com/python/docs/supported-python-versions). Support is updated annually following the Python point release schedule ([PEP 602](https://peps.python.org/pep-0602/); [Status of Python versions](https://devguide.python.org/versions/)). Using unsupported Python versions may cause authentication failures, unexpected behavior, or failure of certain operations. 
## Install options
If you are using **Google Colab** , the latest version of the Earth Engine Python client library has already been installed (via pip). Try the following notebook to get started with Earth Engine and Colab: 
[ ![Colab logo](https://developers.google.com/static/earth-engine/images/colab_logo_32px.png) Run in Google Colab ](https://colab.research.google.com/github/google/earthengine-community/blob/master/guides/linked/ee-api-colab-setup.ipynb) |  [ ![GitHub logo](https://developers.google.com/static/earth-engine/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/earthengine-community/blob/master/guides/linked/ee-api-colab-setup.ipynb)  
---|---  
If you don't use Colab, the Earth Engine client library can be manually installed and updated on your system using **conda** (recommended) or **pip** : 
[ Install with **conda** ](https://developers.google.com/earth-engine/guides/python_install-conda)
Install with **pip** expand_more [](https://developers.google.com/earth-engine/guides/pip-install)
**Install** the API to an arbitrary Python environment using [pip](https://pypi.org/project/pip/). From a terminal or command prompt:
```
pip install earthengine-api
```

Once installed, you can import, authenticate and initialize the Earth Engine API as described [here](https://developers.google.com/earth-engine/guides/python_install#package-import). 
**Update** the API:
```
pip install earthengine-api --upgrade
```

## Package import
The Python API package is called `ee`. It must be imported and initialized for each new Python session and script:
```
importee
```

## Authentication and Initialization
Prior to using the Earth Engine Python client library, you need to authenticate and use the resultant credentials to initialize the Python client. Run: 
```
ee.Authenticate()
```

This will select the best authentication mode for your environment, and prompt you to confirm access for your scripts. To initialize, you will need to provide a project that you own, or have [permissions](https://developers.google.com/earth-engine/cloud/roles_permissions) to use. This project will be used for running all Earth Engine operations: 
```
ee.Initialize(project='my-project')
```

See the [authentication guide](https://developers.google.com/earth-engine/guides/auth) for troubleshooting and to learn more about authentication modes and Cloud projects. 
## Hello world!
Here is a short script to test that you're all set for working with Earth Engine. 
```
importee
ee.Authenticate()
ee.Initialize(project='my-project')
print(ee.String('Hello from the Earth Engine servers!').getInfo())
```

## Syntax
Both the Python and JavaScript APIs access the same server-side functionality, but client-side expressions ([learn more about client vs. server](https://developers.google.com/earth-engine/guides/client_server)) can vary because of language syntax differences. The following table includes a list of the common syntax differences you'll encounter when working with the Python API relative to the JavaScript API.
Common syntax differences between JavaScript and Python Property | JavaScript | Python  
---|---|---  
Function definition |  ```
functionmyFun(arg){
returnarg;
}
varmyFun=function(arg){
returnarg;
};
```
|  ```
defmy_fun(arg):
 return arg
```
  
Anonymous function mapping |  ```
varfoo=col.map(function(arg){
returnarg;
});
```
|  ```
foo = col.map(lambda arg: arg)
```
  
Variable definition |  ```
varmyVar='var';
```
|  ```
my_var = 'var'
```
  
Logical operators |  ```
varmatch=such.and(that);
varmatch=such.or(that);
varmatch=such.not(that);
```
|  ```
match = such.And(that)
match = such.Or(that)
match = such.Not(that)
```
  
Multi-line method chain |  ```
varfoo=my.really()
.reallyLong()
.methodChain();
```
|  ```
foo = (my.really()
    .reallyLong()
    .methodChain())
```
  
Dictionary keys |  ```
vardic={'key':value};
vardic={key:value};
```
|  ```
dic = {'key': value}
```
  
Dictionary object access |  ```
varvalue=dic.key;
varvalue=dic['key'];
```
|  ```
value = dic['key']
```
  
Function argument definition |  ```
// Positional arguments.
varfoo=fun(argX,argY,argZ);
// Keyword arguments object.
varfoo=fun({y:argY});
```
|  ```
# Positional arguments.
foo = fun(arg_x, arg_y, arg_z)
# Keyword arguments dictionary.
foo = fun(**{'y': arg_y})
# Keyword arguments.
foo = fun(x=arg_x, z=arg_z)
```
  
Boolean |  ```
vart=true;
varf=false;
```
|  ```
t = True
f = False
```
  
Null values |  ```
varna=null;
```
|  ```
na = None
```
  
Comment |  ```
//
```
|  ```
#
```
  
**Notes regarding Python API syntax:**
  * Anonymous function mapping is achieved via [ `lambda`](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions) functions, which accept only a single expression. Use traditional named functions when complex mapping operations are required.
  * Function arguments provided as a keyword arguments dictionary must be specified as [**kwargs](https://book.pythontips.com/en/latest/args_and_kwargs.html); i.e., prepend two asterisks to the function input dictionary: `y = fun(**{'x': 0})` or `y = fun(**arg_dict)`.


## Date objects
Define and manipulate client-side date objects with the [ `datetime`](https://docs.python.org/2/library/datetime.html) module. Include the module in your script:
```
importdatetime
```

#### Convert `ee.Date` to client-side date:
```
ee_date = ee.Date('2020-01-01')
py_date = datetime.datetime.utcfromtimestamp(ee_date.getInfo()['value']/1000.0)
```

#### Convert client-side date to `ee.Date:`
```
py_date = datetime.datetime.utcnow()
ee_date = ee.Date(py_date)
```

## Exporting data
Exporting data with the Python API requires the use of the `ee.batch` module, which provides an interface to the [`Export`](https://developers.google.com/earth-engine/guides/exporting) functions. Pass parameter arguments as you would with the JavaScript API, minding the differences noted in the [syntax table](https://developers.google.com/earth-engine/guides/python_install#syntax) above. Export tasks must be started by calling the `start()` method on a defined task. Query a task's status by calling the `status()` method on it. The following example demonstrates exporting an `ee.Image` object.
#### Create an export task:
```
task = ee.batch.Export.image.toDrive(image=my_image, # an ee.Image object.
                   region=my_geometry, # an ee.Geometry object.
                   description='mock_export',
                   folder='gdrive_folder',
                   fileNamePrefix='mock_export',
                   scale=1000,
                   crs='EPSG:4326')
```

#### Start an export task:
```
task.start()
```

#### Check export task status:
```
task.status()
```

The result of `task.status()` is a dictionary containing information such as the state of the task and its ID. 
```
{
 'state': 'READY',
 'description': 'my_export_task',
 'creation_timestamp_ms': 1647567508236,
 'update_timestamp_ms': 1647567508236,
 'start_timestamp_ms': 0,
 'task_type': 'EXPORT_IMAGE',
 'id': '56TVJIZABUMTD5CJ5YHTMYK4',
 'name': 'projects/earthengine-legacy/operations/56TVJIZABUMTX5CJ5HHTMYK4'
}
```

You can monitor task progress using the `state` field. See the Processing Environments page for a [ list of `state` values](https://developers.google.com/earth-engine/guides/processing_environments#list-of-task-states) and more information on [task lifecycle](https://developers.google.com/earth-engine/guides/processing_environments#task-lifecycle).
**Note:** Tasks started from the Python API will also appear in the Tasks tab of the JavaScript [Code Editor](https://developers.google.com/earth-engine/guides/playground) for the same Google account.
## Printing objects
Printing an Earth Engine object in Python prints the serialized request for the object, not the object itself. Refer to the [Client vs. server](https://developers.google.com/earth-engine/guides/client_server) page to understand the reason for this. 
Call `getInfo()` on Earth Engine objects to get the desired object from the server to the client:
```
# Load a Landsat image.
img = ee.Image('LANDSAT/LT05/C02/T1_L2/LT05_034033_20000913')
# Print image object WITHOUT call to getInfo(); prints serialized request instructions.
print(img)
# Print image object WITH call to getInfo(); prints image metadata.
print(img.getInfo())
```
Note that `getInfo()` is a synchronous operation, meaning execution of expressions following the `getInfo()` call are blocked until the result is returned to the client. Additionally, requests for a lot of data or expensive computations can return an error and/or hang. In general, the best practice is to [export your results](https://developers.google.com/earth-engine/guides/exporting), and once complete, import them into a new script for further analysis.  **Caution:** Calling `getInfo()` in your script will block execution. Additionally, requests for a lot of data or expensive computations can return an error and/or hang. [Export](https://developers.google.com/earth-engine/guides/exporting) to obtain the results of expensive, large, or long running computations. 
## UI objects
The Earth Engine `ui` module is only available through the JavaScript API Code Editor. Use third party libraries for UI elements in Python. Libraries such as [geemap](https://github.com/gee-community/geemap), [Folium](https://python-visualization.github.io/folium/), and [ipyleaflet](https://github.com/jupyter-widgets/ipyleaflet) provide interactive map display, while charting can be done with [Matplotlib](https://matplotlib.org/), [Altair](https://altair-viz.github.io/), or [seaborn](https://seaborn.pydata.org/), to name a few. See examples in the [ Earth Engine in Colab setup notebook](https://colab.sandbox.google.com/github/google/earthengine-community/blob/master/guides/linked/ee-api-colab-setup.ipynb) for using geemap and Matplotlib.
## Python in the Developer Guide
Python code is included throughout the Earth Engine Developer Guide. Where available, code examples can be viewed by clicking on the "Colab (Python)" tab at the top of code blocks. Guide pages may also include buttons at the top for running the page as a Colab notebook or viewing on GitHub. Python code examples are intended to be run using [Google Colab](https://colab.google/). Interactive map and object exploration are handled by the [`geemap`](https://github.com/gee-community/geemap) library. Both the Earth Engine Python client library and `geemap` are preinstalled in Colab.
### Earth Engine setup
Running Python code requires that you import the Earth Engine library, authenticate, and initialize. The following commands are used in examples (see the [Authentication and Initialization](https://developers.google.com/earth-engine/guides/auth) page for alternatives).
```
importee
ee.Authenticate()
ee.Initialize(project='my-project')
```

### Interactive exploration with `geemap`
The [`geemap`](https://github.com/gee-community/geemap) library is used for displaying map tiles and printing rich representations of Earth Engine objects. The library depends respectively on [`ipyleaflet`](https://github.com/jupyter-widgets/ipyleaflet) and [`eerepr`](https://github.com/aazuspan/eerepr) for these features. The `geemap` library and its dependencies are preinstalled in Google Colab; import it into each session.
```
importgeemap.coreasgeemap
```

Geographic Earth Engine data classes, such as `ee.Image` and `ee.FeatureCollection`, can be viewed using the `geemap.Map` object. First, define the map object. Then, add layers to it or alter its viewport.
```
# Initialize a map object.
m = geemap.Map()
# Define an example image.
img = ee.Image.random()
# Add the image to the map.
m.add_layer(img, None, 'Random image')
# Display the map (you can call the object directly if it is the final line).
display(m)
```

Was this helpful?
