 
#  Customizing Base Map Styles 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [The default maps in Earth Engine](https://developers.google.com/earth-engine/tutorials/community/customizing-base-map-styles#the_default_maps_in_earth_engine)
  * [Changing the basic map style](https://developers.google.com/earth-engine/tutorials/community/customizing-base-map-styles#changing_the_basic_map_style)
  * [Changing map elements](https://developers.google.com/earth-engine/tutorials/community/customizing-base-map-styles#changing_map_elements)
  * [Cheat codes](https://developers.google.com/earth-engine/tutorials/community/customizing-base-map-styles#cheat_codes)


[ Edit on GitHub ](https://github.com/google/earthengine-community/edit/master/tutorials/customizing-base-map-styles/index.md "Contribute to this article on GitHub.")
[ Report issue ](https://github.com/google/earthengine-community/issues/new?title=Issue%20with%20tutorials/customizing-base-map-styles/index.md&body=Issue%20Description "Report an issue with this article on GitHub.")
[ Page history ](https://github.com/google/earthengine-community/commits/master/tutorials/customizing-base-map-styles/index.md "View changes to this article over time.")
Author(s): [ TC25 ](https://github.com/TC25 "View the profile for TC25 on GitHub")
Tutorials contributed by the Earth Engine developer community are not part of the official Earth Engine product documentation. 
[Open In Code Editor](https://code.earthengine.google.com/887084c4b82c71545bf009902974aac9)
In this tutorial, you'll learn how to change the options of the `Map` object to define your own styles for the underlying base map.
## The default maps in Earth Engine
Earth Engine's base maps are those in Google's Map API. The default options include:
  * roadmap, which displays the default road map view,
  * satellite, which displays Google Earth satellite images,
  * hybrid, which displays a mixture of normal and satellite views, and
  * terrain, which displays a physical map based on terrain information.


## Changing the basic map style
We can start by changing the style of the base map. One easy fix is to invert the lightness to get a darker background, like so:
```
varbaseChange=[{featureType:'all',stylers:[{invert_lightness:true}]}];
Map.setOptions('baseChange',{'baseChange':baseChange});

```

The main styler options include:
  * hue: indicates the basic color
  * lightness: indicates percentage change in brightness of an element
  * saturation: indicates percentage change in basic color of an element
  * gamma: gamma correction of an element (0.01 and 10.0)
  * invert_lightness: inverts the existing lightness
  * visibility: changes visibility options for an element (on, off, or simplified)
  * color: sets the color of an element (using RGB Hex Strings)
  * weight: sets the weight of a feature in pixels


## Changing map elements
The Google Maps API (and by extension, Earth Engine) gives you the ability to control a large number of map features and elements.
The full list of elements that you can modify can be found in the Google Maps documentation: https://developers.google.com/maps/documentation/javascript/style-reference
The full list of features (also in the Google Maps API documentation linked above) includes geometries, labels, icons, and more. All styler options work with each of these features.
For example, to remove icons and customize road map styles, one could define the styles as follows:
```
// Remove icons.
variconChange=[
{
// Change map saturation.
stylers:[{gamma:0.2}]
},
{
// Change label properties.
elementType:'labels',
stylers:[{visibility:'off',color:'#000055'}]
},
{
// Change road properties.
featureType:'road',
elementType:'geometry',
stylers:[{visibility:'off',color:'#000055'}]
},
{
// Change road labels.
featureType:'road',
elementType:'labels',
stylers:[{visibility:'off'}]
},
{
// Change icon properties.
elementType:'labels.icon',
stylers:[{visibility:'off'}]
},
{
// Change POI options.
featureType:'poi',
elementType:'all',
stylers:[{visibility:'off'}]
},
{
featureType:'administrative',
elementType:'geometry.fill',
stylers:[{visibility:'off'}]
},
{
featureType:'administrative',
elementType:'geometry.stroke',
stylers:[{visibility:'off'}]
}
];
// Enhanced road network visualization.
varroadNetwork=[
{stylers:[{saturation:-100}]},{
featureType:'road.highway',
elementType:'geometry.fill',
stylers:[{color:'#000055'},{weight:2.5}]
},
{
featureType:'road.highway',
elementType:'geometry.stroke',
stylers:[{color:'#000000'},{weight:2}]
},
{
featureType:'road.arterial',
elementType:'geometry',
stylers:[{color:'#FF0000'},{weight:1.8}]
},
{
featureType:'road.local',
elementType:'geometry',
stylers:[{color:'#00FF55'},{weight:1.5}]
}
];
Map.setOptions(
'roadNetwork',{iconChange:iconChange,roadNetwork:roadNetwork});

```

The map would then be restyled as shown here:
![Road](https://developers.google.com/static/earth-engine/tutorials/community/customizing-base-map-styles/road.png)
## Cheat codes
There is also an easy way to create custom base map styles without tweaking any options: enter [Snazzy Maps](https://snazzymaps.com), a community project for creating and sharing great styles for Google Maps. Their website provides JavaScript snippets that can be copied from their website and pasted into Earth Engine to quickly create alternate base map styles.
To apply Snazzy Maps styles, one might do the following:
```
varsnazzyBlack=[
{
featureType:'administrative',
elementType:'all',
stylers:[{visibility:'off'}]
},
{
featureType:'administrative',
elementType:'labels.text.fill',
stylers:[{color:'#444444'}]
},
{
featureType:'landscape',
elementType:'all',
stylers:[{color:'#000000'},{visibility:'on'}]
},
{featureType:'poi',elementType:'all',stylers:[{visibility:'off'}]},{
featureType:'road',
elementType:'all',
stylers:[{saturation:-100},{lightness:45}]
},
{
featureType:'road',
elementType:'geometry.fill',
stylers:[{color:'#ffffff'}]
},
{
featureType:'road',
elementType:'geometry.stroke',
stylers:[{color:'#eaeaea'}]
},
{featureType:'road',elementType:'labels',stylers:[{visibility:'off'}]},
{
featureType:'road',
elementType:'labels.text.fill',
stylers:[{color:'#dedede'}]
},
{
featureType:'road',
elementType:'labels.icon',
stylers:[{visibility:'off'}]
},
{
featureType:'road.highway',
elementType:'all',
stylers:[{visibility:'simplified'}]
},
{
featureType:'road.arterial',
elementType:'labels.icon',
stylers:[{visibility:'off'}]
},
{featureType:'transit',elementType:'all',stylers:[{visibility:'off'}]},
{
featureType:'water',
elementType:'all',
stylers:[{color:'#434343'},{visibility:'on'}]
}
];
varsnazzyColor=[
{elementType:'labels',stylers:[{visibility:'off'}]},{
featureType:'road',
elementType:'geometry.fill',
stylers:[{color:'#0F0919'}]
},
{
featureType:'water',
elementType:'geometry.fill',
stylers:[{color:'#E4F7F7'}]
},
{elementType:'geometry.stroke',stylers:[{visibility:'off'}]},{
featureType:'poi.park',
elementType:'geometry.fill',
stylers:[{color:'#002FA7'}]
},
{
featureType:'poi.attraction',
elementType:'geometry.fill',
stylers:[{color:'#E60003'}]
},
{
featureType:'landscape',
elementType:'geometry.fill',
stylers:[{color:'#FBFCF4'}]
},
{
featureType:'poi.business',
elementType:'geometry.fill',
stylers:[{color:'#FFED00'}]
},
{
featureType:'poi.government',
elementType:'geometry.fill',
stylers:[{color:'#D41C1D'}]
},
{
featureType:'poi.school',
elementType:'geometry.fill',
stylers:[{color:'#BF0000'}]
},
{
featureType:'transit.line',
elementType:'geometry.fill',
stylers:[{saturation:-100}]
}
];
Map.setOptions(
'snazzyBlack',{snazzyBlack:snazzyBlack,snazzyColor:snazzyColor});

```

The resulting map would then use the Snazzy Maps styles as shown here:
![Dark](https://developers.google.com/static/earth-engine/tutorials/community/customizing-base-map-styles/snazzy-black.png)
Finally, to get visual feedback while creating custom styles for the base map, one can also use [mapstyle](https://mapstyle.withgoogle.com/). Create a map, copy the JavaScript snippet and paste it into the Google Earth Engine JavaScript editor. The following style was created with the mapstyle wizard.
```
varmapStyle=[
{elementType:'geometry',stylers:[{color:'#ebe3cd'}]},
{elementType:'labels.text.fill',stylers:[{color:'#523735'}]},
{elementType:'labels.text.stroke',stylers:[{color:'#f5f1e6'}]},
{
featureType:'administrative',
elementType:'geometry.stroke',
stylers:[{color:'#c9b2a6'}]
},
{
featureType:'administrative.land_parcel',
elementType:'geometry.stroke',
stylers:[{color:'#dcd2be'}]
},
{
featureType:'administrative.land_parcel',
elementType:'labels.text.fill',
stylers:[{color:'#ae9e90'}]
},
{
featureType:'administrative.land_parcel',
elementType:'labels.text.stroke',
stylers:[{color:'#000040'},{visibility:'simplified'}]
},
{
featureType:'administrative.neighborhood',
elementType:'labels.text.fill',
stylers:[{color:'#408080'}]
},
{
featureType:'landscape.man_made',
elementType:'geometry.fill',
stylers:[{color:'#800040'}]
},
{
featureType:'landscape.natural',
elementType:'geometry',
stylers:[{color:'#dfd2ae'}]
},
{
featureType:'landscape.natural',
elementType:'geometry.fill',
stylers:[{color:'#737c03'}]
},
{
featureType:'landscape.natural.terrain',
elementType:'geometry.fill',
stylers:[{color:'#000040'}]
},
{
featureType:'poi',
elementType:'geometry',
stylers:[{color:'#dfd2ae'}]
},
{
featureType:'poi',
elementType:'labels.text',
stylers:[{visibility:'off'}]
},
{
featureType:'poi',
elementType:'labels.text.fill',
stylers:[{color:'#93817c'}]
},
{featureType:'poi.business',stylers:[{visibility:'off'}]},
{
featureType:'poi.park',
elementType:'geometry.fill',
stylers:[{color:'#a5b076'}]
},
{
featureType:'poi.park',
elementType:'labels.text.fill',
stylers:[{color:'#447530'}]
},
{
featureType:'road',
elementType:'geometry',
stylers:[{color:'#f5f1e6'}]
},
{
featureType:'road',
elementType:'labels.icon',
stylers:[{visibility:'off'}]
},
{
featureType:'road.arterial',
elementType:'geometry',
stylers:[{color:'#fdfcf8'}]
},
{
featureType:'road.highway',
elementType:'geometry',
stylers:[{color:'#f8c967'}]
},
{
featureType:'road.highway',
elementType:'geometry.stroke',
stylers:[{color:'#e9bc62'}]
},
{
featureType:'road.highway.controlled_access',
elementType:'geometry',
stylers:[{color:'#e98d58'}]
},
{
featureType:'road.highway.controlled_access',
elementType:'geometry.stroke',
stylers:[{color:'#db8555'}]
},
{
featureType:'road.local',
elementType:'labels.text.fill',
stylers:[{color:'#806b63'}]
},
{featureType:'transit',stylers:[{visibility:'off'}]},
{
featureType:'transit.line',
elementType:'geometry',
stylers:[{color:'#dfd2ae'}]
},
{
featureType:'transit.line',
elementType:'labels.text.fill',
stylers:[{color:'#8f7d77'}]
},
{
featureType:'transit.line',
elementType:'labels.text.stroke',
stylers:[{color:'#ebe3cd'}]
},
{
featureType:'transit.station',
elementType:'geometry',
stylers:[{color:'#dfd2ae'}]
},
{
featureType:'water',
elementType:'geometry.fill',
stylers:[{color:'#b9d3c2'}]
},
{
featureType:'water',
elementType:'labels.text.fill',
stylers:[{color:'#92998d'}]
}
];
Map.setOptions('mapStyle',{mapStyle:mapStyle});

```

The resulting base map would look like this:
![MapStyle](https://developers.google.com/static/earth-engine/tutorials/community/customizing-base-map-styles/map-style.png)
You can find all the map styling options provided in Google Maps API at: https://developers.google.com/maps/documentation/javascript/reference#MapTypeStyle
