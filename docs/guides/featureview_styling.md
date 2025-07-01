 
#  FeatureView Styling
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Style object](https://developers.google.com/earth-engine/guides/featureview_styling#style_object)
    * [Broad rules](https://developers.google.com/earth-engine/guides/featureview_styling#broad_rules)
    * [Specific rules](https://developers.google.com/earth-engine/guides/featureview_styling#specific_rules)
  * [Setting style](https://developers.google.com/earth-engine/guides/featureview_styling#setting_style)
    * [FeatureViewLayer declaration](https://developers.google.com/earth-engine/guides/featureview_styling#featureviewlayer_declaration)
    * [Existing FeatureViewLayer](https://developers.google.com/earth-engine/guides/featureview_styling#existing_featureviewlayer)
  * [Symbology](https://developers.google.com/earth-engine/guides/featureview_styling#symbology)
    * [Constant](https://developers.google.com/earth-engine/guides/featureview_styling#constant)
    * [Categorical](https://developers.google.com/earth-engine/guides/featureview_styling#categorical)
    * [Interpolated](https://developers.google.com/earth-engine/guides/featureview_styling#interpolated)
  * [All style properties](https://developers.google.com/earth-engine/guides/featureview_styling#all_style_properties)


The style of features in a `FeatureView` asset are specified using rules defined in a JavaScript object. Style can be set during initial definition of a `FeatureViewLayer` or anytime after. The styling system allows you to set broad style rules that apply to large groups of features, as well as more specific rules for particular features. Feature style can be defined by constant values or data driven, based on feature characteristics.
## Style object
The basic structure of a style object is shown below. There are two types of rules: broad rules and specific rules. Broad rules affect all features in a `FeatureView` asset, while specific rules affect a subset of features.
```
{
// Broad style rules.
opacity:…,
polygonFillColor:…,
// Specific style rules.
rules:[
{…},
{…}
]
};

```

### Broad rules
To apply style properties to all features (or those of a specific geometry type), specify the style properties at the top level in the style object.
```
{
opacity:0.5,
pointShape:'triangle',
lineWidth:10,
polygonFillColor:'green'
};

```

### Specific rules
To apply style properties to a subset of features, use the `rules` field. The `rules` field accepts a list of JavaScript objects, each with a `filter` that selects features according to conditions defined by an `ee.Filter` object, followed by a series of style properties. In the example below, there is a rule that sets `polygonStrokeWidth` and `polygonFillColor` only if the "REP_AREA" property is less than 100. Specific rules override the style properties of broad rules, and rules near the end of the `rules` list override those near the beginning (specific rules are evaluated first to last).
```
{
rules:[
{
filter:ee.Filter.lt('REP_AREA',100),
polygonStrokeWidth:0.5,
polygonFillColor:'blue'
},
{…}// Optionally include additional rules.
]
};

```

## Setting style
Feature style can be set when a `FeatureViewLayer` is declared or anytime after.
### `FeatureViewLayer` declaration
To set the visualization parameters when declaring a `FeatureViewLayer`, use the `visParams` parameter.
```
varvisParams={
opacity:0.5,
lineWidth:10,
polygonFillColor:'purple'
};
varlayer=ui.Map.FeatureViewLayer({
assetId:'WCMC/WDPA/current/polygons_FeatureView',
visParams:visParams
});
Map.add(layer);

```

### Existing `FeatureViewLayer`
To set the visualization parameters for an existing `FeatureViewLayer`, use the `setVisParams` function. It replaces any previously specified style rules; unspecified properties are set to their default.
```
varlayer=ui.Map.FeatureViewLayer('WCMC/WDPA/current/polygons_FeatureView');
Map.add(layer);
layer.setVisParams({
opacity:0.5,
lineWidth:10,
polygonFillColor:'purple'
});

```

## Symbology
For each style property, you can specify either a constant style rule or a data-driven style rule. The data-driven option uses feature property values to determine symbolization, which can either be categorical or interpolated. For a full list of the style properties, see the [style properties table](https://developers.google.com/earth-engine/guides/featureview_styling#all_style_properties).
### Constant
A constant style rule consists of a style property to set and its value. The following example sets the polygon fill color to blue.
```
varvisParams={
polygonFillColor:'blue'
};

```

### Categorical
A categorical style rule consists of a style property to set and a JavaScript object with three properties:
  * **`property`**— a feature property name whose value will affect the style.
  * **`categories`**— a list of lists that map feature property values to style property symbologies. Each category includes a property value followed by a symbology value to apply. The property value that defines a category must be a string.
  * **`defaultValue`**— a default symbology to apply to features whose property value is not defined in`categories`. If it is null/undefined, default style settings will be applied.


For example, the following object sets the `color` style property based on the "MARINE" feature property. Features in "MARINE" category "0" are set as purple, "1" as green, "2" as blue, and any other category as white.
```
varvisParams={
color:{
property:'MARINE',
categories:[
['0','purple'],
['1','green'],
['2','blue']
],
defaultValue:'white'
}
};

```

### Interpolated
An interpolated style rule consists of a style property to set and a JavaScript object with up to five properties:
  * **`property`**— a feature property name whose value will affect the style.
  * **`mode`**— the interpolation mode, either`'linear'` or `'interval'`.
  * **`palette`**— a list of colors, opacities, or widths to interpolate input property values between. The format depends on the`mode` , see the [Linear](https://developers.google.com/earth-engine/guides/featureview_styling#linear) and [Interval](https://developers.google.com/earth-engine/guides/featureview_styling#interval) sections for more details.


_Applies only to`'linear'` mode_
  * **`min`**— the property value to map to the first element in the`palette` list.
  * **`max`**— the property value to map to the last element in the`palette` list.


#### Linear
Linear interpolation mode sets a feature style property by mapping input values in the range `min` to `max` linearly between a list of symbology values defined in the `palette` property. The input values are clamped to the range set by `min` and `max`.
For example, the following object sets the `color` style property based on the "REP_AREA" feature property. The `palette` property is a list of colors indicating that input values between `min` and `max` should grade linearly from yellow to red to blue. A value between 1 and 500 is interpolated between yellow and red, and a value between 500 and 1000 is interpolated between red and blue.
```
varvisParams={
color:{
property:'REP_AREA',
mode:'linear',
palette:['yellow','red','blue'],
min:1,
max:1000
}
};

```

#### Interval
Interval interpolation mode sets a feature style property by mapping input values to class breaks and then applying a class-specific symbology. Input values from the selected feature property are assigned to the nearest class break value by rounding down. The `palette` property is formatted as a list of lists, where each inner list contains a class break value followed by a style property value. Features whose property value are less than the minimum class break value maintain their default style property setting.
In the following example, feature fill opacity is set according to graduated classes of the "REP_AREA" property. Class definition and style symbology are provided in the `palette` property as a list of lists. It indicates that there should be 4 classes with breaks at value 0, 80, 2000, and 5000, with respective feature opacities of 0.5, 0.35, 0.22, and 0.15. In other words, features with "REP_AREA" values in the interval 0≤x<80 will have a fill opacity of 0.5, values in the interval 80≤x<2000 will have fill opacity of 0.35, and so on.
```
varvisParams={
fillOpacity:{
property:'REP_AREA',
mode:'interval',
palette:[
[0,0.5],
[80,0.35],
[2000,0.22],
[5000,0.15]
]
}
};

```

## All style properties
Below are all of the style properties you can specify in the style object. Setting style properties for specific geometry types overrides the corresponding style properties set for "All geometries" (for example, setting `polygonFillColor` overrides the value set in `fillColor`).
Property | Type | Description | Supports Interpolated Rule  
---|---|---|---  
_All geometries_  
`isVisible` | `Boolean` | Sets whether the feature is visible. | No  
`color` | `String` | Sets fill/stroke color for all geometry types. Must be a hex value or a CSS3 color. | Yes  
`opacity` | `Double` | Sets fill/stroke opacity for all geometry types. Must be a double between 0 and 1. | Yes  
`width` | `Double` | Sets stroke width for all geometry types. | Yes  
`fillColor` | `String` | Sets fill color for all geometry types. Must be a hex value or a CSS3 color. | Yes  
_Point geometries_  
`pointShape` | `String` | Sets the shape of point geometries. Supports the same shapes as `ee.FeatureCollection.style` (circle, square, diamond, cross, plus, pentagram, hexagram, triangle, triangle_up, triangle_down, triangle_left, triangle_right, pentagon, hexagon, star5, star6). | No  
`pointSize` | `Double` | Sets the width of point geometries (in px). | Yes  
`pointFillColor` | `String` | Sets fill color for point geometries. Must be a hex value or a CSS3 color. | Yes  
`pointFillOpacity` | `Double` | Sets fill opacity for point geometries. Must be a double between 0 and 1. | Yes  
_Line geometries_  
`lineType` | `String` | Sets the line type. Supports the same types as `ee.FeatureCollection.style` (solid, dashed, dotted). | No  
`lineWidth` | `Double` | Sets the line width (in px). | Yes  
`lineColor` | `String` | Sets color for line geometries. Must be a hex value or a CSS3 color. | Yes  
`lineOpacity` | `Double` | Sets opacity for line geometries. Must be a double between 0 and 1. | Yes  
_Polygon geometries_  
`polygonStrokeWidth` | `Double` | Sets the stroke width of polygons (in px). | Yes  
`polygonStrokeType` | `String` | Sets the line type for polygons. Supports the same types as `ee.FeatureCollection.style` (solid, dashed, dotted). | No  
`polygonStrokeColor` | `String` | Sets stroke color for polygon geometries. Must be a hex value or a CSS3 color. | Yes  
`polygonStrokeOpacity` | `Double` | Sets stroke opacity for polygon geometries. Must be a double between 0 and 1. | Yes  
`polygonFillColor` | `String` | Sets fill color for polygon geometries. Must be a hex value or a CSS3 color. | Yes  
`polygonFillOpacity` | `Double` | Sets fill opacity for polygon geometries. Must be a double between 0 and 1. | Yes  
